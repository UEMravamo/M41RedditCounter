import time
from src.reddit_api import get_trending_subreddits, get_top_posts
from src.data_processing import create_dataframe, analyze_top_posts, calculate_subreddit_score


def main():

    start_total = time.time()

    trending = get_trending_subreddits(limit=5)
    print("Subreddits en tendencia:")
    for subreddit in trending:
        print(f"- {subreddit}")

    for subreddit in trending:

        start_subreddit = time.time()

        top_posts = get_top_posts(subreddit, post_limit=10, comment_limit=5)
        df = create_dataframe(top_posts)

        print(f"\nPublicaciones principales de {subreddit}:")
        for index, post in df.compute().iterrows():
            print(f"📢 Post #{index + 1}")
            print(f"Título: {post['title']}")
            print(f"Puntuación: {post['score']}")
            print(f"Puntos de Comentarios: {post['comment_score']}\n{'-' * 40}")

        # Análisis de los datos
        print(f"\nAnálisis estadístico de las publicaciones de {subreddit}:")
        analysis = analyze_top_posts(df)
        for metric, values in analysis.items():
            print(f"\n{metric.upper()}:")
            for key, value in values.items():
                print(f"  {key}: {value}")

        # Tiempo de fin y cálculo del tiempo de ejecución por subreddit
        end_subreddit = time.time()
        elapsed_subreddit = end_subreddit - start_subreddit
        print(f"⏱️ Tiempo de ejecución para {subreddit}: {elapsed_subreddit:.2f} segundos\n{'-' * 40}")

    # Tiempo total
    end_total = time.time()
    elapsed_total = end_total - start_total
    print(f"Tiempo total de ejecución: {elapsed_total:.2f} segundos")


if __name__ == "__main__":
    main()
