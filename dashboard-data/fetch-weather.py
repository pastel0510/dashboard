#!/usr/bin/env python3
"""
Fetch weather from Supersää (Ilta-Sanomat) for Finnish cities.
Shows both Ilmatieteen laitos and Foreca forecasts.
"""
import requests
import re
import json
import os
from datetime import datetime
from zoneinfo import ZoneInfo

# Supersää URLs for cities
CITIES = [
    {"name": "Helsinki", "url": "https://www.is.fi/supersaa/suomi/helsinki/helsinki%20keskusta/-10019448/"},
    {"name": "Tampere", "url": "https://www.is.fi/supersaa/suomi/tampere/634963/"},
    {"name": "Turku", "url": "https://www.is.fi/supersaa/suomi/turku/633679/"},
    {"name": "Oulu", "url": "https://www.is.fi/supersaa/suomi/oulu/643492/"},
    {"name": "Rovaniemi", "url": "https://www.is.fi/supersaa/suomi/rovaniemi/638936/"},
]


def fetch_supersaa(url):
    """Fetch Supersää page."""
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "fi-FI,fi;q=0.9,en;q=0.8",
    }
    try:
        resp = requests.get(url, headers=headers, timeout=30)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None


def parse_nextjs_data(html):
    """Parse the __NEXT_DATA__ JSON from the HTML."""
    match = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.DOTALL)
    if not match:
        return None
    
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}")
        return None


def parse_supersaa(html, city_name):
    """Parse weather data from Supersää HTML using Next.js data."""
    if not html:
        return None
    
    # Parse Next.js data
    next_data = parse_nextjs_data(html)
    if not next_data:
        print(f"  No Next.js data found for {city_name}")
        return None
    
    try:
        page_props = next_data['props']['pageProps']
        
        # Get hourly and daily forecasts
        hourly = page_props.get('hourlyForecasts', [])
        daily = page_props.get('dailyForecasts', [])
        
        if not hourly or not daily:
            print(f"  Missing forecast data for {city_name}")
            return None
        
        # Get current hour (find the closest to now)
        current_hour = None
        current_hour_idx = 0
        now = datetime.now()
        for i, h in enumerate(hourly):
            hour_time = datetime.fromisoformat(h['time'].replace('+', ' +').replace(' +0', '+0').replace(' +1', '+1').replace(' +2', '+2').replace(' +3', '+3'))
            if hour_time.hour == now.hour:
                current_hour = h
                current_hour_idx = i
                break
        
        if not current_hour:
            current_hour = hourly[0]  # Fallback to first hour
            current_hour_idx = 0
        
        # Get current data
        fmi_current = current_hour.get('fmi', {})
        foreca_current = current_hour.get('foreca', {})
        
        fmi_temp = fmi_current.get('temperature', '?')
        fmi_feels = fmi_current.get('feelsLikeTemp', '?')
        foreca_temp = foreca_current.get('temperature', '?')
        foreca_feels = foreca_current.get('feelsLikeTemp', '?')
        
        # Current time in Helsinki timezone
        helsinki_now = datetime.now(ZoneInfo('Europe/Helsinki'))
        current_time = helsinki_now.strftime('%H.%M')
        
        # Build hourly forecast list (next 12 hours, every 3 hours)
        hourly_list = []
        for offset in [3, 6, 9, 12]:  # 3-hour intervals
            idx = current_hour_idx + offset
            if idx < len(hourly):
                h = hourly[idx]
                hour_time_str = h['time']
                dt = datetime.fromisoformat(hour_time_str.replace('+', ' +').replace(' +0', '+0').replace(' +1', '+1').replace(' +2', '+2').replace(' +3', '+3'))
                time_label = dt.strftime('%H:%M')
                
                fmi_data = h.get('fmi', {})
                foreca_data = h.get('foreca', {})
                fmi_t = fmi_data.get('temperature', '?')
                foreca_t = foreca_data.get('temperature', '?')
                
                hourly_list.append((time_label, str(fmi_t), str(foreca_t)))
        
        # Build daily forecast list
        daily_list = []
        for day in daily[:8]:
            day_time = day.get('time', '')
            fmi_data = day.get('fmi', {})
            foreca_data = day.get('foreca', {})
            
            fmi_max = fmi_data.get('maxTemp', '?')
            foreca_max = foreca_data.get('maxTemp', '?')
            
            # Format date
            if day_time:
                dt = datetime.fromisoformat(day_time.replace('+', ' +').replace(' +0', '+0').replace(' +1', '+1').replace(' +2', '+2').replace(' +3', '+3'))
                date_formatted = dt.strftime('%d.%m.')
                day_names = {0: 'ma', 1: 'ti', 2: 'ke', 3: 'to', 4: 'pe', 5: 'la', 6: 'su'}
                day_code = day_names.get(dt.weekday(), '?')
                daily_list.append((day_code + date_formatted, str(fmi_max), str(foreca_max)))
        
        return {
            "time": current_time,
            "fmi_temp": str(fmi_temp),
            "fmi_feels": str(fmi_feels),
            "foreca_temp": str(foreca_temp),
            "foreca_feels": str(foreca_feels),
            "hourly": hourly_list,
            "daily": daily_list
        }
    except Exception as e:
        print(f"Error parsing data for {city_name}: {e}")
        import traceback
        traceback.print_exc()
        return None


def generate_weather_html():
    """Generate HTML weather section for all cities."""
    html_parts = []
    
    for city in CITIES:
        print(f"Fetching {city['name']}...")
        html_content = fetch_supersaa(city['url'])
        if not html_content:
            html_parts.append(f'<div class="city-weather"><h3>{city["name"]}</h3><p>Weather data unavailable</p></div>')
            continue
        
        data = parse_supersaa(html_content, city['name'])
        
        if not data:
            html_parts.append(f'<div class="city-weather"><h3>{city["name"]}</h3><p>Parse error</p></div>')
            continue
        
        print(f"  Got: IL {data['fmi_temp']}° (feels {data['fmi_feels']}°), Foreca {data['foreca_temp']}° (feels {data['foreca_feels']}°), {len(data['hourly'])} hourly, {len(data['daily'])} daily forecasts")
        
        # Build hourly forecast HTML (12h every 3h)
        hourly_html = '<div class="hourly-forecast">'
        hourly_html += '<div class="forecast-subheader">Next 12 hours:</div>'
        for h in data['hourly']:
            time_label, fmi_t, foreca_t = h
            hourly_html += f'<div class="forecast-hour"><a href="{city["url"]}" target="_blank" class="h-time">{time_label}</a><span class="h-temp fmi">{fmi_t}°</span><span class="h-temp foreca">{foreca_t}°</span></div>'
        hourly_html += '</div>'
        
        # Build daily forecast HTML
        forecast_html = '<div class="forecast">'
        day_names = {'la': 'Lau', 'su': 'Sun', 'ma': 'Mon', 'ti': 'Tue', 'ke': 'Wed', 'to': 'Thu', 'pe': 'Fri'}
        
        for day in data['daily'][:5]:  # Show 5 days
            day_code = day[0][:2]
            date = day[0][2:]
            day_name = day_names.get(day_code, day_code)
            fmi_high = day[1]
            foreca_high = day[2]
            
            forecast_html += f'<div class="forecast-day"><span class="f-date">{day_name} {date}</span><span class="f-temp fmi">{fmi_high}°</span><span class="f-temp foreca">{foreca_high}°</span></div>'
        
        forecast_html += '</div>'
        
        city_html = f'''<div class="city-weather">
            <h3><a href="{city['url']}" target="_blank" style="color:#00d9ff;text-decoration:none;">{city["name"]}</a> <span class="time">@ {data['time']}</span></h3>
            <div class="current">
                <div class="temp-row">
                    <div class="provider fmi">
                        <span class="provider-name">Ilmatieteen laitos</span>
                        <span class="temp">{data['fmi_temp']}°C</span>
                        <span class="feels">Tuntuu {data['fmi_feels']}°</span>
                    </div>
                    <div class="provider foreca">
                        <span class="provider-name">Foreca</span>
                        <span class="temp">{data['foreca_temp']}°C</span>
                        <span class="feels">Tuntuu {data['foreca_feels']}°</span>
                    </div>
                </div>
            </div>
            {hourly_html}
            <div class="forecast-header" style="margin-top:12px;">
                <span></span>
                <span class="provider-label fmi">Ilmatieteen laitos</span>
                <span class="provider-label foreca">Foreca</span>
            </div>
            {forecast_html}
        </div>'''
        
        html_parts.append(city_html)
    
    return '\n'.join(html_parts)


if __name__ == "__main__":
    output_dir = os.environ.get('DASHBOARD_DATA', '/home/riverbank1229/.openclaw/workspace/dashboard-data')
    weather_html = generate_weather_html()
    
    output_path = os.path.join(output_dir, 'weather.html')
    with open(output_path, 'w') as f:
        f.write(weather_html)
    
    print(f"Weather data saved to {output_path}")
