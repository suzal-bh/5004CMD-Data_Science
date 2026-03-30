import time
import pandas as pd
import dask.dataframe as dd

def compare_processing():
    df = pd.read_csv("data/Trips_by_Distance.csv")
    df.columns = df.columns.str.strip()
    df['Date'] = pd.to_datetime(df['Date'])
    start_serial = time.time()
    serial_result = df.groupby('Date')['Population Not Staying at Home'].mean()
    serial_time = time.time() - start_serial

    dd_df = dd.read_csv(
        "data/Trips_by_Distance.csv",
        assume_missing=True,
        dtype={
            "County Name": "object",
            "State Postal Code": "object"
        }
    )
    dd_df['Date'] = dd.to_datetime(dd_df['Date'])
    start_parallel = time.time()
    parallel_result = dd_df.groupby('Date')['Population Not Staying at Home'].mean().compute()
    parallel_time = time.time() - start_parallel

    return serial_time, parallel_time