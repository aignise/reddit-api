from fastapi import FastAPI, HTTPException
from typing import List

from . import extract
from . import actions

app = FastAPI()

## FastAPI test
@app.get("/")
def home():
    return "Reddit API is live."

## FastAPI routes
@app.get("/find-subreddits/")
def get_subreddits(keywords: List[str]):
    return extract.find_subreddits(keywords)

@app.get("/find-posts/")
def get_posts(subreddits: List[str], keywords: List[str]):
    return extract.find_posts(subreddits, keywords)