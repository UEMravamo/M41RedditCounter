# RedditCounter

Imagina que trabajas para una agencia de publicidad. Para personalizar aún más los anuncios, se te pide que diseñes y desarrolles una solución que rastree y clasifique los temas en tendencia en Reddit.

Tus compañeros propusieron los siguientes criterios de clasificación:

- **Puntuación del subreddit**:

$$\text{s} = \sum_{i=1}^{n} \text{postRS}$$

Donde \(n\) es el número de publicaciones en un subreddit dado.

- **Puntuación de la publicación**:  

 $$\text{p} = \sum_{i=1}^{n} \text{cp}$$
 
 Donde \(n\) es el número de comentarios de la publicación y \(cp\) son los puntos para ese comentario.

Durante el desarrollo, debes enfocarte en los **50 subreddits principales**. Para cada uno de ellos, extrae las **10 publicaciones principales** y considera solo los **5 comentarios con más puntos** (sin incluir subcomentarios). Estos parámetros deben ser configurables en producción.

Tu solución debe generar un informe que puede guardarse en un archivo o en una base de datos (SQLite, PostgreSQL, etc.).

## Consejos

1. Familiarízate con Reddit:
   - Página de inicio
   - [Preguntas frecuentes](https://www.reddit.com/help/faq)
2. Familiarízate con la [API REST de Reddit](https://www.reddit.com/dev/api):
   - Ejemplos de endpoints:
     - `/api/trending_subreddits`
     - `/comments/article`

## Requisitos

1. Usa Python 3.7.
2. Escribe código conforme a PEP8.
3. Escribe algunas pruebas (considera usar pytest o uniitest).
4. Documenta tu solución en un archivo.

### Puntos extra (opcional)

2. ¿Cómo manejarías los reinicios y reintentos de tareas fallidas?
3. ¿Cómo puedes contenerizar la canalización?


