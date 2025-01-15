import pandas as pd
# Archivo pendiente de realizar
def create_dataframe(posts):
    return pd.DataFrame(posts)

def analyze_top_posts(dataframe):
    return dataframe.describe()
