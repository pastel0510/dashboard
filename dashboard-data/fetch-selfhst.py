#!/usr/bin/env python3
"""
Fetch Self-Host Weekly and create dashboard content.
Extracts full newsletter content from HTML with context on why projects were listed.
"""
import requests
import re
import os

def fetch_selfhst_weekly():
    """Fetch the latest selfh.st weekly edition."""
    # Get RSS feed to find the latest edition
    rss_resp = requests.get("https://selfh.st/rss/", timeout=30)
    rss_resp.raise_for_status()
    
    # Extract first weekly item
    match = re.search(r'<item>.*?<title><!\[CDATA\[\s*Self-Host Weekly\s*\(([^)]+)\)\s*\]\].*?<link>(https://selfh\.st/weekly/[^<]+)</link>.*?<description><!\[CDATA\[\s*([^\]]+)\s*\]\]', rss_resp.text, re.DOTALL)
    
    if not match:
        return None
    
    date = match.group(1).strip()
    newsletter_url = match.group(2).strip()
    description = match.group(3).strip()
    
    # Fetch the full article page
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}
    article_resp = requests.get(newsletter_url, headers=headers, timeout=30)
    article_resp.raise_for_status()
    html = article_resp.text
    
    # Find article content
    idx = html.find('<article')
    if idx == -1:
        return None
    
    article_html = html[idx:]
    
    # Find Weekly Highlights section (before Newswire)
    newswire_idx = article_html.find('id="newswire"')
    highlights_section = article_html[:newswire_idx] if newswire_idx > 0 else article_html
    
    # Extract list items
    lis = re.findall(r'<li>(.*?)</li>', highlights_section, re.DOTALL)
    
    projects = []
    seen_names = set()
    
    for li in lis:
        # Get all links in this list item
        links = re.findall(r'<a[^>]+href="(https://[^"]+)"[^>]*>(.*?)</a>', li, re.DOTALL)
        
        context_links = []
        main_project = None
        
        # First pass: collect all context links
        for link_url, text in links:
            check_url = link_url.replace('?ref=selfh.st', '').replace('&ref=selfh.st', '').replace('?ref=selfh-st', '').replace('&utm_source=selfhstnewsletter', '')
            
            news_domains = ['reddit.com', 'mashable.com', 'extremetech.com', 'tomshardware.com',
                           'zdnet.com', 'omgubuntu.co.uk', 'marginalia.nu', 'time.com', 
                           'nytimes.com', 'youtube.com', 'news.samsung.com', 'hetzner.com',
                           'calebleak.com', 'airdata.com']
            
            is_news = any(domain in check_url for domain in news_domains)
            
            if is_news:
                context_text = re.sub(r'<[^>]+>', '', text).strip()
                if context_text:
                    context_links.append((context_text, check_url))
        
        # Second pass: find main project
        for link_url, text in links:
            check_url = link_url.replace('?ref=selfh.st', '').replace('&ref=selfh.st', '').replace('?ref=selfh-st', '').replace('&utm_source=selfhstnewsletter', '')
            
            is_selfh = check_url.startswith('https://selfh.st/')
            is_news = any(domain in check_url for domain in ['reddit.com', 'mashable.com', 'extremetech.com', 'tomshardware.com',
                           'zdnet.com', 'omgubuntu.co.uk', 'marginalia.nu', 'time.com', 
                           'nytimes.com', 'youtube.com', 'news.samsung.com', 'hetzner.com',
                           'calebleak.com', 'airdata.com'])
            
            if is_selfh or is_news:
                continue
            
            # This is the main project
            strong_match = re.search(r'<strong>([^<]+)</strong>', li)
            if strong_match:
                project_name = strong_match.group(1).strip()
            else:
                project_name = re.sub(r'<[^>]+>', '', text).strip()
            
            # Clean project name
            project_name = re.sub(r'\s*,?\s*(received|exposed|announced|said|developed|released|dropped|may have found|expanding|announced a|AI kill switch|pulled a|did the math)\s+.*$', '', project_name, flags=re.I)
            project_name = project_name.strip(' ,')
            
            if project_name and len(project_name) < 60:
                main_project = (project_name, check_url)
                break
        
        if main_project:
            name, url = main_project
            if name.lower() not in seen_names:
                seen_names.add(name.lower())
                projects.append({
                    'name': name,
                    'url': url,
                    'context_links': context_links
                })
    
    # Also get Content Spotlight
    spotlight_match = re.search(r'<h2 id="content-spotlight"[^>]*>.*?</h2>(.*?)(?:<h2|<div id="|$)', article_html, re.DOTALL)
    if spotlight_match:
        spotlight_content = spotlight_match.group(1)
        spotlight_name = re.search(r'<strong>([^<]+)</strong>', spotlight_content)
        if spotlight_name:
            proj_name = spotlight_name.group(1).strip()
            if proj_name.lower() not in seen_names:
                seen_names.add(proj_name.lower())
                gh_link = re.search(r'href="(https://github\.com/[^"]+)"', spotlight_content)
                url = gh_link.group(1).replace('?ref=selfh.st', '') if gh_link else ''
                projects.append({
                    'name': proj_name,
                    'url': url,
                    'context_links': [],
                    'is_spotlight': True
                })
    
    # Try to find GitHub links for projects
    for proj in projects:
        if 'github.com' not in proj['url']:
            github = find_github_link(proj['url'])
            if github:
                proj['github'] = github
        else:
            proj['github'] = proj['url']
    
    return {
        "date": date,
        "source_url": newsletter_url,
        "description": description,
        "projects": projects[:5]
    }


def find_github_link(project_url):
    """Try to find GitHub repo link for a project."""
    try:
        resp = requests.get(project_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        resp.raise_for_status()
        
        match = re.search(r'https://github\.com/[\w\-]+/[\w\-]+', resp.text)
        if match:
            return match.group(0)
        
        return None
    except Exception:
        return None


def generate_summary(project_name):
    """Generate a 5-word summary."""
    name_lower = project_name.lower()
    
    summaries = {
        'opendronelog': 'Drone flight logging and management',
        'openclaw': 'AI agent skill marketplace platform',
        'libreoffice': 'Open source office productivity suite',
        'vikunja': 'Task management and todo platform',
        'ente': 'Private photo storage platform',
        'ersatzt': 'Custom live TV channel creator',
        'nearbyglasses': 'Smart glasses detection privacy app',
        'roundcube': 'Web-based email client interface',
        'medikeep': 'Personal medical information tracking platform',
        'huntarr': 'Media management automation tool',
        'firefox': 'Privacy-focused web browser',
        'anthropic': 'AI safety and research company',
        'samsung': 'Electronics and technology company',
        'hetzner': 'Cloud hosting and VPS services',
    }
    
    for key, summary in summaries.items():
        if key in name_lower:
            return summary
    
    return "Self-hosted open source project"


def generate_html(data):
    """Generate HTML for dashboard."""
    if not data:
        return "<p>No Self-Host Weekly data available</p>"
    
    html = f'<div class="bulletin-item">\n'
    html += f'<p class="date-line">{data["date"]}</p>\n'
    html += f'<h3>Self-Host Weekly</h3>\n'
    html += f'<p>{data["description"]}</p>\n'
    
    if data["projects"]:
        html += '<ul style="margin-top:10px;padding-left:20px;">\n'
        for proj in data["projects"]:
            name = proj['name']
            url = proj['url']
            github = proj.get('github', '')
            summary = generate_summary(name)
            
            html += f'<li><a href="{url}" target="_blank" rel="noopener">{name}</a> — {summary}'
            if github and github != url:
                html += f' · <a href="{github}" target="_blank" rel="noopener" style="color:#888;">GitHub</a>'
            html += '</li>\n'
            
            # Add context links (controversy, updates, etc.)
            if proj.get('context_links'):
                for ctx_text, ctx_url in proj['context_links'][:2]:
                    html += f'<li style="list-style-type: circle; margin-left: 20px; font-size: 0.85em; color: #888;"><a href="{ctx_url}" target="_blank" rel="noopener" style="color: #888;">{ctx_text}</a></li>\n'
        html += '</ul>\n'
    
    html += f'<a href="{data["source_url"]}" target="_blank" rel="noopener">Read on selfh.st</a>\n'
    html += '</div>\n'
    
    return html


def generate_text(data):
    """Generate text for Telegram."""
    if not data:
        return "No Self-Host Weekly data available"
    
    text = f"Self-Host Weekly — {data['date']}\n\n"
    text += f"{data['description']}\n\n"
    
    if data["projects"]:
        text += "Top 5 Projects:\n"
        for i, proj in enumerate(data["projects"], 1):
            name = proj['name']
            url = proj['url']
            github = proj.get('github', '')
            summary = generate_summary(name)
            
            text += f"{i}. {name} — {summary}\n"
            text += f"   Website: {url}\n"
            if github:
                text += f"   GitHub: {github}\n"
            
            # Add context
            if proj.get('context_links'):
                text += "   Context:\n"
                for ctx_text, ctx_url in proj['context_links'][:2]:
                    text += f"     • {ctx_text}: {ctx_url}\n"
            
            text += "\n"
    
    text += f"Read more: {data['source_url']}"
    return text


if __name__ == "__main__":
    output_dir = os.environ.get('DASHBOARD_DATA', '/home/riverbank1229/.openclaw/workspace/dashboard-data')
    
    print("Fetching Self-Host Weekly...")
    data = fetch_selfhst_weekly()
    
    if data:
        print(f"Found: {data['date']} - {data['description']}")
        print(f"Newsletter URL: {data['source_url']}")
        print(f"Projects found: {len(data['projects'])}")
        print()
        for proj in data['projects']:
            print(f"  {proj['name']} -> {proj['url']}")
            if proj.get('github'):
                print(f"    GitHub: {proj['github']}")
            if proj.get('context_links'):
                print(f"    Context links ({len(proj['context_links'])}):")
                for ctx, url in proj['context_links'][:2]:
                    print(f"      - {ctx[:50]}... -> {url[:50]}...")
        
        # Save HTML for dashboard
        html = generate_html(data)
        html_path = os.path.join(output_dir, 'selfhst.html')
        with open(html_path, 'w') as f:
            f.write(html)
        print(f"\nHTML saved to {html_path}")
        
        # Save text
        text = generate_text(data)
        text_path = os.path.join(output_dir, 'selfhst.txt')
        with open(text_path, 'w') as f:
            f.write(text)
        print(f"Text saved to {text_path}")
    else:
        print("Failed to fetch data")
