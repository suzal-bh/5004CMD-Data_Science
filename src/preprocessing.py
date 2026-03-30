import pandas as pd

def preprocess(df_distance, df_full):
    df_distance['Date'] = pd.to_datetime(df_distance['Date'])
    df_full['Date'] = pd.to_datetime(df_full['Date'])
    df_full = df_full[df_full['Level'] == "National"]
    df_distance = df_distance[df_distance['Level'] == "National"] 

    return df_distance, df_full