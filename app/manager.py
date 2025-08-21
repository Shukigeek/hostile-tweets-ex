import pandas as pd
from fetcher import FetchData


class Manager:
    def __init__(self):
        self.mongo_data = FetchData()
    def mongo_to_df(self):
        df = pd.DataFrame(list(self.mongo_data.fetch()))
        return df
d = Manager()
print(d.mongo_to_df().head(5))