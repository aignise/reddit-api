from api import extract

kw = ["autogen"]

subs = extract.find_subreddits(kw)
posts = extract.find_posts(subs,kw)

print(posts)