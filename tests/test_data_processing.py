import pandas as pd
from src.data_processing import create_dataframe, analyze_top_posts

def test_create_dataframe():
    posts = [{"title": "Post 1", "score": 100}, {"title": "Post 2", "score": 200}]
    df = create_dataframe(posts)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2

def test_analyze_top_posts():
    posts = [{"title": "Post 1", "score": 100}, {"title": "Post 2", "score": 200}]
    df = create_dataframe(posts)
    analysis = analyze_top_posts(df)
    assert isinstance(analysis, pd.DataFrame)
