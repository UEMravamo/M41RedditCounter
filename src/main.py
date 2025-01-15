import os
import time
from reddit_api import get_trending_subreddits, get_top_posts
from spark_handler import spark_analyze
from db_handler import create_connection, create_table, insert_results, fetch_results


def main():
    subreddit_limit = int(os.getenv("SUBREDDIT_LIMIT", 10))
    post_limit = int(os.getenv("POST_LIMIT", 5))
    comment_limit = int(os.getenv("COMMENT_LIMIT", 3))

    print("\n▶️ Iniciando análisis de Reddit...")
    start_total = time.time()

    try:
        trending = get_trending_subreddits(limit=subreddit_limit)
        if not trending:
            print("❌ No se encontraron subreddits en tendencia.")
            return

        subreddit_data = {}
        for subreddit in trending:
            top_posts = get_top_posts(subreddit, post_limit=post_limit, comment_limit=comment_limit)
            if not top_posts:
                print(f"⚠️ No se obtuvieron publicaciones para {subreddit}.")
                continue
            subreddit_data[subreddit] = top_posts

        print("\n🛠️ Realizando análisis con Spark...")
        results = spark_analyze(subreddit_data)

        print("\n🔍 Resultados del análisis:")
        for subreddit, scores in results.items():
            print(f"Subreddit: {subreddit}")
            print(f"  ⭐ Puntuación de publicaciones: {scores['post_score']}")
            print(f"  💬 Puntuación de comentarios: {scores['comment_score']}")
            print(f"  🏆 Puntuación total: {scores['total_score']}")

        conn = create_connection()
        create_table(conn)
        insert_results(conn, results)
        saved_results = fetch_results(conn)

        print("\n📋 Resultados guardados en la base de datos:")
        for row in saved_results:
            print(f"Subreddit: {row[0]}, Publicaciones: {row[1]}, Comentarios: {row[2]}, Total: {row[3]}")

        conn.close()

    except Exception as e:
        print(f"❌ Error durante el análisis: {e}")
    finally:
        end_total = time.time()
        print(f"\n✅ Tiempo total: {end_total - start_total:.2f} segundos")


if __name__ == "__main__":
    main()

