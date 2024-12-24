from src.reddit_api import get_trending_subreddits

# Funciones de prueba
def test_get_trending_subreddits():
    trending = get_trending_subreddits(limit=1)
    assert isinstance(trending, list)
    assert len(trending) > 0
