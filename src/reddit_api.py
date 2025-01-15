import praw
from config import CONFIG
import concurrent.futures

# Instancia global de Reddit
reddit = praw.Reddit(
    client_id=CONFIG["client_id"],
    client_secret=CONFIG["client_secret"],
    user_agent=CONFIG["user_agent"],
    check_for_updates=False
)


# Función Inicial para obtener Subreddits en tendencia
def get_trending_subreddits(limit=5):
    try:
        return [subreddit.display_name for subreddit in reddit.subreddits.default(limit=limit)]
    except Exception as e:
        print(f"❌ Error al obtener subreddits en tendencia: {e}")
        return []


# Función para obtener los 10 posts más top
def get_top_posts(subreddit_name, post_limit=10, comment_limit=5):
    subreddit = reddit.subreddit(subreddit_name)
    top_posts = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_post = {executor.submit(get_comments, post.id, comment_limit): post for post in subreddit.top(limit=post_limit)}
        for future in concurrent.futures.as_completed(future_to_post):
            post = future_to_post[future]
            comments = future.result()
            comment_score = sum([comment["score"] for comment in comments])
            top_posts.append({"title": post.title, "score": post.score, "comment_score": comment_score})
    return top_posts


# Función para obtener los 5 mejores con más puntos
def get_comments(post_id, comment_limit=5):
    try:
        submission = reddit.submission(id=post_id)
        submission.comment_sort = "best"
        submission.comments.replace_more(limit=0)
        comments = [{"body": comment.body, "score": comment.score} for comment in submission.comments[:comment_limit]]
        return comments
    except Exception as e:
        print(f"⚠️ Error al obtener comentarios de la publicación {post_id}: {e}")
        return []

