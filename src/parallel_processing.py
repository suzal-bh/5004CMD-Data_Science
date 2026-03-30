import time
from dask.distributed import Client
import dask.dataframe as dd

def run_parallel():
    client = Client(n_workers=4)
    dd_distance = dd.read_csv("data/Trips_by_Distance.csv")
    dd_distance['Date'] = dd.to_datetime(dd_distance['Date'])
    start = time.time()
    result = dd_distance.groupby('Date')['Population Not Staying at Home'].mean().compute()
    elapsed = time.time() - start
    client.close()

    return result, elapsed