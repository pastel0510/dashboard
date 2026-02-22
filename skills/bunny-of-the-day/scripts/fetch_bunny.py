#!/usr/bin/env python3
"""
Fetch the top-voted bunny/rabbit picture from r/bunnies and r/rabbits
in the last 24 hours and send to Telegram.
Uses PRAW (Python Reddit API Wrapper) for proper API access.
"""

import json
import time
import os
from datetime import datetime, timezone

try:
    import praw
    from prawcore.exceptions import ResponseException, RequestException
    HAS_PRAW = True
except ImportError:
    HAS_PRAW = False
    print("PRAW not installed. Run: pip install praw")

TELEGRAM_CHAT_ID = "55163462"
SUBREDDITS = ["rabbits", "bunnies"]  # rabbits first for preference

def get_reddit_instance():
    """Create a read-only Reddit instance using PRAW."""
    # Use Reddit's public client credentials for read-only access
    # These are Reddit's official mobile app credentials (public knowledge)
    reddit = praw.Reddit(
        client_id="ohXpoqrZYub1kg",  # Reddit's public client ID
        client_secret="",  # Empty for public clients
        user_agent="BunnyOfTheDay/1.0",
        check_for_async=False
    )
    return reddit

def get_top_bunny_praw():
    """Find the top-voted bunny image from last 24 hours using PRAW."""
    if not HAS_PRAW:
        return None
    
    try:
        reddit = get_reddit_instance()
        all_posts = []
        
        for subreddit_name in SUBREDDITS:
            print(f"\nFetching r/{subreddit_name}...")
            subreddit = reddit.subreddit(subreddit_name)
            
            # Get top posts from last 24 hours
            try:
                for post in subreddit.top(time_filter="day", limit=100):
                    # Check if it's an image post
                    if post.url and (
                        post.url.endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')) or
                        'i.redd.it' in post.url
                    ):
                        all_posts.append({
                            "title": post.title,
                            "url": post.url,
                            "ups": post.score,
                            "subreddit": str(post.subreddit),
                            "permalink": f"https://reddit.com{post.permalink}",
                            "created": post.created_utc
                        })
            except ResponseException as e:
                print(f"Response error for r/{subreddit_name}: {e}")
                continue
            except RequestException as e:
                print(f"Request error for r/{subreddit_name}: {e}")
                continue
            except Exception as e:
                print(f"Error fetching r/{subreddit_name}: {e}")
                continue
            
            print(f"  Found {len([p for p in all_posts if p['subreddit'] == subreddit_name])} images")
        
        if not all_posts:
            return None
        
        # Sort by upvotes (descending), with preference for r/rabbits on ties
        # Use a secondary sort to prefer r/rabbits when scores are equal
        all_posts.sort(key=lambda x: (x["ups"], x["subreddit"].lower() == "rabbits"), reverse=True)
        
        # If top two are close (within 10%), prefer r/rabbits
        if len(all_posts) >= 2:
            top = all_posts[0]
            second = all_posts[1]
            # If second place is from rabbits and within 10% of top score, prefer it
            if (second["subreddit"].lower() == "rabbits" and 
                top["subreddit"].lower() != "rabbits" and
                second["ups"] >= top["ups"] * 0.9):
                all_posts[0] = second
                all_posts[1] = top
                print(f"  Preferring r/rabbits post (within 10% of top score)")
        
        print(f"\nTotal: {len(all_posts)} bunny images")
        print(f"Top 3 by votes:")
        for i, p in enumerate(all_posts[:3]):
            print(f"  {i+1}. {p['ups']:,} upvotes - r/{p['subreddit']} - {p['title'][:50]}...")
        
        return all_posts[0]
    
    except Exception as e:
        print(f"PRAW error: {e}")
        return None

def main():
    print(f"🐰 Bunny of the Day - {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 50)
    
    if not HAS_PRAW:
        print("❌ PRAW not installed!")
        return 1
    
    top = get_top_bunny_praw()
    
    if not top:
        print("\n❌ No bunny images found in the last 24 hours!")
        return 1
    
    print(f"\n🏆 TOP BUNNY:")
    print(f"   Title: {top['title']}")
    print(f"   Subreddit: r/{top['subreddit']}")
    print(f"   Upvotes: {top['ups']:,}")
    print(f"   URL: {top['url']}")
    
    # Output JSON for the agent
    result = {
        "image_url": top["url"],
        "title": top["title"],
        "subreddit": top["subreddit"],
        "ups": top["ups"],
        "permalink": top["permalink"]
    }
    
    print("\n---BUNNY_JSON---")
    print(json.dumps(result))
    
    return 0

if __name__ == "__main__":
    exit(main())
