from src.reddit_api import get_trending_subreddits

def main():
    trending = get_trending_subreddits(limit=5)
    print("Subreddits en tendencia:")
    for subreddit in trending:
        print(f"- {subreddit}")

if __name__ == "__main__":
    main()
