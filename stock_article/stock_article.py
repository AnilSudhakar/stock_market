import yfinance as yf
import time

class StockArticle:

    def __init__(self):
        pass

    def fetch_quotes(self, symbol, max_results=10):
        return self._retry(lambda: yf.Search(symbol, max_results=max_results).quotes)

    def fetch_news(self, symbol, news_count=10):
        return self._retry(lambda: yf.Search(symbol, news_count=news_count).news)

    def fetch_research(self, symbol, include_research=True):
        return self._retry(lambda: yf.Search(symbol, include_research=include_research).research)

    def _retry(self, func, retries=3, delay=5):
        for i in range(retries):
            try:
                return func()
            except Exception as e:
                print(f'Failed to fetch data. Retrying in {delay} seconds...')
                if i < retries - 1:
                    time.sleep(delay)
                else:
                    raise

if __name__ == "__main__":
    stock_article = StockArticle()
    quotes = stock_article.fetch_quotes("AAPL")
    print(quotes)
    news = stock_article.fetch_news("AAPL")
    print(news)
    research = stock_article.fetch_research("AAPL")
    print(research)
