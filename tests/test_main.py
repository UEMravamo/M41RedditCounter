from src.reddit_api import get_trending_subreddits, get_top_posts
from src.spark_handler import spark_analyze


def test_main_flow():
    trending = get_trending_subreddits(limit=2)
    assert len(trending) > 0, "No se obtuvieron subreddits"

    subreddit_data = {}
    for subreddit in trending:
        posts = get_top_posts(subreddit, post_limit=3, comment_limit=2)
        assert len(posts) > 0, f"No se obtuvieron publicaciones para {subreddit}"
        subreddit_data[subreddit] = posts

    results = spark_analyze(subreddit_data)
    assert "post_score" in results[trending[0]], "Falta la puntuación de las publicaciones"
