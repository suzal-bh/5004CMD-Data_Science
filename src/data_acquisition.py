import pandas as pd
import dask.dataframe as dd

def load_data():
    df_distance = pd.read_csv("data/Trips_by_Distance.csv")
    df_full = pd.read_csv("data/Trips_Full Data.csv")
    dd_distance = dd.read_csv("data/Trips_by_Distance.csv")
    dd_full = dd.read_csv("data/Trips_Full Data.csv")

    return df_distance, df_full, dd_distance, dd_full