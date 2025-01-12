import psycopg2


# Creamos la conexión con la DDBB
def create_connection():
    conn = psycopg2.connect(
        dbname="reddit_db",
        user="reddit_user",
        password="reddit_password",
        host="localhost",
        port=5432
    )
    return conn


# Creamos la tabla de Datos
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subreddit_scores (
            subreddit TEXT PRIMARY KEY,
            post_score INTEGER,
            comment_score INTEGER,
            total_score INTEGER
        );
    ''')
    conn.commit()


# Función para insertar los resultados en la DDBB
def insert_results(conn, results):
    cursor = conn.cursor()
    for subreddit, scores in results.items():
        cursor.execute('''
            INSERT INTO subreddit_scores (subreddit, post_score, comment_score, total_score)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (subreddit) DO UPDATE
            SET post_score = EXCLUDED.post_score,
                comment_score = EXCLUDED.comment_score,
                total_score = EXCLUDED.total_score;
        ''', (subreddit, scores['post_score'], scores['comment_score'], scores['total_score']))
    conn.commit()


# Recupera los datos almacenados del PostgresSQL
def fetch_results(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subreddit_scores;")
    rows = cursor.fetchall()
    return rows
