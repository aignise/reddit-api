from fastapi import FastAPI, HTTPException
from typing import List

from . import extract
from . import actions

## FastAPI routes
@app.get("/find-subreddits/")
async def get_subreddits(keywords: List[str]):
    return extract.find_subreddits(keywords)

@app.get("/find-posts/")
async def get_posts(subreddits: List[str], keywords: List[str]):
    return extract.find_posts(subreddits, keywords)