import pytest
from src.reddit_api import get_trending_subreddits, get_top_posts


# Test para obtener los subreddits en tendencia
def test_get_trending_subreddits():
    trending = get_trending_subreddits(limit=3)
    assert isinstance(trending, list)
    assert len(trending) == 3


# Test para obtener los post más puntuados
def test_get_top_posts():
    posts = get_top_posts("python", post_limit=5)
    assert isinstance(posts, list)
    assert len(posts) == 5
    assert all("title" in post and "score" in post for post in posts)
