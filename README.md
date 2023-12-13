# Reddit FastAPI Application

## Overview
This FastAPI application provides a simple yet powerful interface for interacting with Reddit. It leverages Reddit's API to search for subreddits and posts based on user-defined keywords. This tool is particularly useful for educational and research purposes where quick and efficient extraction of Reddit data is required.

## Features
- **Subreddit Search**: Find subreddits related to specified keywords.
- **Post Retrieval**: Retrieve posts from the identified subreddits, filtering out NSFW content.

## Getting Started

### Prerequisites
- Python 3.6+
- PRAW (Python Reddit API Wrapper)
- FastAPI
- Uvicorn for running the application

### Installation
1. Clone the repository:
   ```bash
   git clone https://your-repository-url.git
   cd your-repository
```

### (Optional) Set up a virtual environment:
```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install the dependencies:
```bash
   pip install -r requirements.txt
```

### Set up your Reddit API credentials in a .env file in the project root:
```bash
   CLIENT_ID=your_reddit_client_id
   CLIENT_SECRET=your_reddit_client_secret
   USERNAME=your_reddit_username
   PASSWORD=your_reddit_password
   USER_AGENT=your_user_agent
```

### Running the Application
```bash
   uvicorn main:app --reload
```

### Usage
The application provides two primary endpoints:

- GET /find-subreddits/: Accepts a list of keywords and returns subreddits related to those keywords.
- GET /find-posts/: Accepts a list of subreddits and keywords and returns posts corresponding to them.