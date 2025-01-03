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


# Función secundaria para obtener los 10 posts más top
def get_top_posts(subreddit_name, post_limit=10, comment_limit=5):
    reddit = praw.Reddit(
        client_id=CONFIG["client_id"],
        client_secret=CONFIG["client_secret"],
        user_agent=CONFIG["user_agent"]
    )
    subreddit = reddit.subreddit(subreddit_name)
    top_posts = []
    for post in subreddit.top(limit=post_limit):
        comments = get_comments(post.id, comment_limit)
        comment_score = sum([comment["score"] for comment in comments])  # Suma de puntajes de los comentarios
        top_posts.append({"title": post.title, "score": post.score, "comment_score": comment_score})
    return top_posts


# Obtenemos los 5 mejores comentarios de la publicación
def get_comments(post_id, comment_limit=5):
    reddit = praw.Reddit(
        client_id=CONFIG["client_id"],
        client_secret=CONFIG["client_secret"],
        user_agent=CONFIG["user_agent"]
    )
    submission = reddit.submission(id=post_id)
    submission.comment_sort = "best"
    submission.comments.replace_more(limit=0)
    comments = [{"body": comment.body, "score": comment.score} for comment in submission.comments[:comment_limit]]
    return comments
