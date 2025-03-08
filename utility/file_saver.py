import os

class FileSaver:

    def __init__(self, output_folder=None):
        if output_folder:
            self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)

    def save_to_file(self, symbol, content, file_name):
        file_name = file_name.replace(' ', '_').lower()

        folder_path = os.path.join(self.output_folder, symbol)
        os.makedirs(folder_path, exist_ok=True)

        file_path = os.path.join(folder_path, file_name)
        print(f'Saving to file: {file_path}')
        with open(file_path, 'w') as file:
            for line in content:
                self.write_to_file(line + '\n', file)
    
    def write_to_file(self, content, file):
        file.write(content)

    def save_to_excel(self, dataFrame, file_name):
        file_name = os.path.join(self.output_folder, file_name)
        print(f'Saving to Excel file: {file_name}')
        dataFrame.to_excel(file_name + ".xlsx", index=False)

if __name__ == "__main__":
    output_folder = "/home/anil/MyProjects/stock_market/outputs"
    saver = FileSaver(output_folder)
    content = ["AAPL", "GOOGL", "MSFT"]
    file_name = "stocks.txt"
    saver.save_to_file("stocks", content, file_name)
    data = [
        {"symbol": "AAPL", "price": 150.0},
        {"symbol": "GOOGL", "price": 2500.0},
        {"symbol": "MSFT", "price": 300.0}
    ]
    columns = ["symbol", "price"]
    df = saver.create_data_frame(data, columns)
    saver.save_to_excel(df, "stocks")
