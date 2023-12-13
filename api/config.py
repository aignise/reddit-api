import praw
from dotenv import load_dotenv
import os

## Load environment variables
load_dotenv()

## Initialize Reddit instance
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD"),
    user_agent=os.getenv("USER_AGENT")
)

"""

def verify_credentials(email):
    reddit_instance = initialize_reddit(email)
    if not reddit_instance:
        return False

    try:
        # Try fetching the authenticated user's name
        user_name = reddit_instance.user.me().name
        print(f"Authenticated as {user_name}")
        return True
    except prawcore.exceptions.ResponseException as e:
        # Handle exception if credentials are incorrect
        print(f"Authentication failed! Error: {e}")
        return False

"""