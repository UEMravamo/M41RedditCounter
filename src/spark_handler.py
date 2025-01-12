from pyspark import SparkConf, SparkContext


# Análisis de datos con Spark
def spark_analyze(data):
    conf = SparkConf().setAppName("RedditAnalyzer").setMaster("local[*]")
    sc = SparkContext.getOrCreate(conf)

    # Crear RDD y aplicar las transformaciones
    rdd = sc.parallelize(data.items())
    mapped_rdd = rdd.flatMap(lambda x: [(x[0], (post["score"], post["comment_score"])) for post in x[1]])
    reduced_rdd = mapped_rdd.reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1]))

    results = reduced_rdd.collect()
    sc.stop()

    return {
        subreddit: {
            "post_score": scores[0],
            "comment_score": scores[1],
            "total_score": scores[0] + scores[1]
        } for subreddit, scores in results
    }
