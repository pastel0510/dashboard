#!/usr/bin/env python3
import sys, re

html = sys.stdin.read()

# Find article
idx = html.find('<article')
if idx == -1:
    print('Article not found')
    exit(1)

article_html = html[idx:]

# Find all <li> tags in Weekly Highlights section (before Newswire)
newswire_idx = article_html.find('id="newswire"')
highlights_section = article_html[:newswire_idx] if newswire_idx > 0 else article_html

lis = re.findall(r'<li>(.*?)</li>', highlights_section, re.DOTALL)

# Known project keywords to identify actual projects
project_keywords = ['github.com', 'drone', 'log', 'app', 'platform', 'tool', 'suite', 'server', 'client', 'library']

projects = []
seen_urls = set()

for li in lis:
    # Get all links in this li
    links = re.findall(r'<a[^>]+href="(https://[^"]+)"[^>]*>(.*?)</a>', li, re.DOTALL)
    
    for url, text in links:
        # Skip unwanted links
        if any(x in url for x in ['reddit.com', 'airdata.com', 'selfh.st/apps', 'calebleak.com', 
                                   'mashable.com', 'extremetech.com', 'tomshardware.com', 'time.com',
                                   'zdnet.com', 'omgubuntu.co.uk', 'marginalia.nu', 'nytimes.com',
                                   'youtube.com', 'samsung.com', 'news.samsung.com', 'hetzner.com']):
            continue
        
        clean_text = re.sub(r'<[^>]+>', '', text).strip()
        clean_text = re.sub(r'\s+', ' ', clean_text)
        clean_url = url.replace('?ref=selfh.st', '').replace('&ref=selfh.st', '').replace('?ref=selfh-st', '').replace('&utm_source=selfhstnewsletter', '')
        
        # Skip if already seen
        if clean_url in seen_urls:
            continue
        
        # Look for strong/bold text which usually indicates project name
        strong_match = re.search(r'<strong>([^<]+)</strong>', li)
        if strong_match:
            project_name = strong_match.group(1).strip()
        else:
            project_name = clean_text
        
        # Clean up project name
        project_name = re.sub(r'\s*,?\s*(received|exposed|announced|said|developed|released|dropped)\s+.*$', '', project_name, flags=re.I)
        project_name = project_name.strip(' ,')
        
        if project_name and len(project_name) < 60:
            seen_urls.add(clean_url)
            projects.append((project_name, clean_url))

# Also look for Content Spotlight
spotlight_match = re.search(r'<h2 id="content-spotlight"[^>]*>.*?</h2>(.*?)(?:<h2|<div id="|$)', article_html, re.DOTALL)
if spotlight_match:
    spotlight_content = spotlight_match.group(1)
    # Find the project name (usually bold)
    spotlight_name = re.search(r'<strong>([^<]+)</strong>', spotlight_content)
    if spotlight_name:
        proj_name = spotlight_name.group(1).strip()
        # Find GitHub link
        gh_link = re.search(r'href="(https://github\.com/[^"]+)"', spotlight_content)
        if gh_link:
            projects.append((proj_name, gh_link.group(1).replace('?ref=selfh.st', '')))

print(f'Found {len(projects)} projects:')
print()
for i, (name, url) in enumerate(projects[:10], 1):
    print(f'{i}. {name}')
    print(f'   {url}')
    print()

# Save to file format for dashboard
print('\\n--- DASHBOARD FORMAT ---\\n')
for name, url in projects[:5]:
    print(f'<li><a href="{url}">{name}</a></li>')
