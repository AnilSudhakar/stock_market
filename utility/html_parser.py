import requests
from bs4 import BeautifulSoup

class HTMLParser:
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    def __init__(self):
        self.url = ''
        self.soup = None
    
    def parse_html(self, url):
        print(f'Parsing HTML from: {url}')
        self.url = url
        response = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(response.content, 'html.parser')

    def get_title(self):
        title = self.soup.title.text
        return title

    def get_paragraphs(self):
        paragraphs = self.soup.find_all('p')
        text_list = []
        for para in paragraphs:
            text_list.append(para.text)
        return text_list
