import praw
from typing import List

import config

reddit = config.reddit

def createPost(email):
    profile = reddit.subreddit(f'u_{reddit.user.me().name}')  # This will target your own profile
    profile.submit(title='What online business can you start that will make $100 in 3 days or less?', selftext=description)
    post.mod.nsfw = False  # This will remove the NSFW tag

    #subreddit = reddit.subreddit('name_of_subreddit_here')  # replace with the name of the subreddit where you want to post
    #subreddit.submit(title='What online business can you start that will make $100 in 3 days or less?', selftext=description)#,url="https://example.com"

def commentPost(email, thread_id, response):
    submission = reddit.submission(id=thread_id)
    return submission.reply(response)

