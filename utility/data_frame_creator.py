import pandas as pd

class DataFrameCreator:
    def create_data_frame(self, data, columns):
        df = pd.DataFrame(data, columns=columns)
        return df
