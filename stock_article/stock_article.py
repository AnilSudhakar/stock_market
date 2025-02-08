import yfinance as yf

class StockArticle:

    def __init__(self):
        pass

    def fetch_quotes(self, symbol, max_results=10):
        return yf.Search(symbol, max_results=max_results).quotes

    def fetch_news(self, symbol, news_count=10):
        return yf.Search(symbol, news_count=news_count).news

    def fetch_research(self, symbol, include_research=True):
        return yf.Search(symbol, include_research=include_research).research
