import praw
from typing import List

import config

reddit = config.reddit

## Function to find subreddits
def find_subreddits(keywords: List[str]) -> List[str]:
    subreddits = []
    for keyword in keywords:
        results = reddit.subreddit("all").search(keyword, limit=3)
        for result in results:
            subreddits.append(result.subreddit.display_name)
    return subreddits

# Function to find posts
def find_posts(subreddits: List[str], keywords: List[str]) -> dict:
    posts = {}
    for subreddit in subreddits:
        for keyword in keywords:
            results = reddit.subreddit(subreddit).search(keyword, limit=1)
            for result in results:
                if not result.over_18:
                    posts[result.title] = f"https://www.reddit.com{result.permalink}"
    return posts

