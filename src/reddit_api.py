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
