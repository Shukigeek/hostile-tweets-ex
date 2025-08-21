from platform import processor

import pandas as pd
from fetcher import FetchData
from processor import Processor

class Manager:
    def __init__(self):
        self.mongo_data = FetchData()
    def mongo_to_df(self):
        df = pd.DataFrame(self.mongo_data.fetch())
        return df
    def process_data(self):
        process = Processor(self.mongo_to_df())
        res = process.rarest_word().sentiment().weapon_detected().rename_columns()
        return res.df
    def df_to_json(self):
        records = self.process_data().to_dict(orient="records")

        return records

d = Manager()
print(d.df_to_json())