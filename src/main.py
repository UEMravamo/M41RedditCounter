from src.reddit_api import get_trending_subreddits, get_top_posts
from src.data_processing import create_dataframe, analyze_top_posts

def main():
    # Obtener subreddits en tendencia
    trending = get_trending_subreddits(limit=3)
    print("Subreddits en tendencia:")
    for subreddit in trending:
        print(f"- {subreddit}")

    # Obtener publicaciones principales de cada subreddit
    for subreddit in trending:
        top_posts = get_top_posts(subreddit, post_limit=5)
        df = create_dataframe(top_posts)
        print(f"\nPublicaciones principales de {subreddit}:")
        print(df)

        # Análisis básico de los datos (Pendiente)
        print(f"\nAnálisis de las publicaciones de {subreddit}:")
        print(analyze_top_posts(df))

if __name__ == "__main__":
    main()

