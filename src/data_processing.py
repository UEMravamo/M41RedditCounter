import pandas as pd
import dask.dataframe as dd


# Convierte una lista de publicaciones en un Dask DataFrame
def create_dataframe(posts):
    assert len(posts) > 0, "No se están pasando publicaciones al DataFrame"
    print(f"🔍 Número de filas antes de crear el DataFrame: {len(posts)}")
    df = pd.DataFrame(posts)
    return dd.from_pandas(df, npartitions=8)


# Realiza un análisis estadístico del Dask DataFrame solo sobre columnas numéricas
def analyze_top_posts(dataframe):
    numeric_columns = dataframe.select_dtypes(include=["number"])

    mean = numeric_columns.mean().compute()
    std = numeric_columns.std().compute()
    min_val = numeric_columns.min().compute()
    max_val = numeric_columns.max().compute()
    variance = numeric_columns.var().compute()
    median = numeric_columns.quantile(0.5).compute()  # Mediana como percentil 50%

    analysis = {
        "mean": mean.to_dict(),
        "std": std.to_dict(),
        "min": min_val.to_dict(),
        "max": max_val.to_dict(),
        "variance": variance.to_dict(),
        "median": median.to_dict(),
    }

    return analysis


# Calcula las puntuaciones del Subreddit
def calculate_subreddit_score(posts):
    total_score = sum(post["score"] for post in posts)
    total_comment_score = sum(post["comment_score"] for post in posts)
    return {
        "total_post_score": total_score,
        "total_comment_score": total_comment_score,
        "overall_score": total_score + total_comment_score
    }
