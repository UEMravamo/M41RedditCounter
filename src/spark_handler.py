from multiprocessing import Pool


# Mapper que recibe los datos de un subreddit y calcula la puntuación total de publicaciones y comentarios
def mapper(subreddit_data):
    subreddit, posts = subreddit_data
    post_scores = sum(post["score"] for post in posts)
    comment_scores = sum(post["comment_score"] for post in posts)
    return subreddit, {"post_score": post_scores, "comment_score": comment_scores,
                       "total_score": post_scores + comment_scores}


# Reducer que combina los resultados parciales
def reducer(mapped_data):
    combined = {}
    for subreddit, scores in mapped_data:
        combined[subreddit] = scores
    return combined


# Realiza el análisis MapReduce completo
def mapreduce_analyze(data):
    # Crear chunks de subreddits para procesar en paralelo
    with Pool() as pool:
        mapped_data = pool.map(mapper, data.items())
    # Reducir los resultados
    final_results = reducer(mapped_data)
    return final_results
