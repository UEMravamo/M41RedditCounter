import praw
from src.config import CONFIG

# Función Inicial para obtener Subreddits en tendencia
def get_trending_subreddits(limit=5):
    reddit = praw.Reddit(
        client_id=CONFIG["client_id"],
        client_secret=CONFIG["client_secret"],
        user_agent=CONFIG["user_agent"]
    )
    return [subreddit.display_name for subreddit in reddit.subreddits.default(limit=limit)]

# Función secundaria para obtener los 5 posts más top
def get_top_posts(subreddit_name, post_limit=5):

    reddit = praw.Reddit(
        client_id=CONFIG["client_id"],
        client_secret=CONFIG["client_secret"],
        user_agent=CONFIG["user_agent"]
    )
    subreddit = reddit.subreddit(subreddit_name)
    return [{"title": post.title, "score": post.score} for post in subreddit.top(limit=post_limit)]