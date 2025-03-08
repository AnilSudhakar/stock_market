import requests
from bs4 import BeautifulSoup
import re

class HTMLParser:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    def __init__(self):
        self.url = ''
        self.soup = None

    def parse_html(self, url):
        print(f'Parsing HTML from: {url}')
        self.url = url
        response = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(response.content, 'html.parser')

    def get_data_by_tag(self, tag_name):
        elements = self.soup.find_all(tag_name)
        return elements

    def get_title(self):
        title = self.soup.title.text
        return title

    def get_paragraphs(self):
        paragraphs = self.get_data_by_tag('p')
        text_list = [para.text for para in paragraphs]
        return text_list

    def extract_data(self, tagName, filterName):
        trade_data = []
        trade_data_script = None
        scripts = self.get_data_by_tag(tagName)
        for script in scripts:
            if script.string and filterName in script.string:
                trade_data_script = script.string
                break
        if trade_data_script:
            match = re.search(rf"{filterName} = (\[.*?\]);", trade_data_script, re.DOTALL)
            if match:
                trade_data_json = match.group(1)
                trade_data_json = trade_data_json.replace('null', 'None').replace('NaN', 'float("nan")')
                trade_data = eval(trade_data_json)
                return trade_data
        return None

if __name__ == "__main__":
    url = "https://www.quiverquant.com/congresstrading/politician/Nancy%20Pelosi-P000197"
    parser = HTMLParser()
    parser.parse_html(url)
    print(parser.get_title())
    print(parser.get_paragraphs())
    trade_data = parser.extract_data('script', 'let tradeData')
