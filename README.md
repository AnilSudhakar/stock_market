# Stock Market Analysis Project

This project is designed to fetch, parse, and analyze stock market data, including news articles and trading data of congress members.

## Project Structure

- `stock_article/`: Contains the `StockArticle` class for fetching stock-related news and quotes.
- `utility/`: Contains utility modules for parsing HTML, saving files, creating data frames, and fetching congress members' data.
  - `html_parser.py`: Parses HTML content.
  - `file_saver.py`: Saves data to files.
  - `data_frame_creator.py`: Creates pandas DataFrames.
  - `congress_members.py`: Fetches data about congress members.
- `stock_articles_parse.ipynb`: Jupyter notebook for parsing stock articles and saving the data.

## Running the Jupyter Notebook

Open `stock_articles_parse.ipynb` in Jupyter Notebook to run the complete workflow for fetching and parsing stock articles and saving the data.
