import pandas as pd

class DataFrameCreator:
    def create_data_frame(self, data, columns):
        df = pd.DataFrame(data, columns=columns)
        return df

if __name__ == "__main__":
    data = [
        {"symbol": "AAPL", "price": 150.0},
        {"symbol": "GOOGL", "price": 2500.0},
        {"symbol": "MSFT", "price": 300.0}
    ]
    columns = ["symbol", "price"]
    creator = DataFrameCreator()
    df = creator.create_data_frame(data, columns)
    print(df)
