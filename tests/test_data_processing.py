from src.data_processing import create_dataframe, analyze_top_posts


# Pruebas de creación del Dataframe
def test_create_dataframe():
    posts = [{"title": f"Post {i}", "score": i * 10} for i in range(2500)]
    assert len(posts) == 2500, "No se están generando suficientes datos de prueba"
    df = create_dataframe(posts)
    assert df.npartitions == 8, f"Número de particiones incorrecto: {df.npartitions}"
    assert len(df.compute()) == 2500, "El DataFrame no tiene las filas esperadas"


# Pruebas de creación completa del Dataframe
def test_create_dataframe_full():
    posts = []
    for _ in range(50):
        for i in range(10):
            for j in range(5):
                post_data = {
                    "title": f"Post {i} - Comentario {j}",
                    "score": i * 100,
                    "comment_score": j * 10
                }
                posts.append(post_data)
    df = create_dataframe(posts)
    assert df.npartitions == 8, f"Número de particiones incorrecto: {df.npartitions}"
    assert len(df.compute()) == 2500, "El DataFrame no tiene las 2500 filas esperadas"
