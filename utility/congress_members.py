import requests
import yaml

class CongressMembersFetcher:
    def __init__(self, url):
        self.url = url
        self.members = []

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.members = yaml.safe_load(response.text)
        else:
            response.raise_for_status()


    def get_bioguide_id(self, official_full):
        for member in self.members:
            if member.get('name', {}).get('official_full') == official_full:
                return member.get('id', {}).get('bioguide', "Bioguide ID not found")
        
        return "Politician not found"

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/unitedstates/congress-legislators/main/legislators-current.yaml"
    output_file = "/home/anil/MyProjects/stock_market/utility/congress_members.yaml"
    fetcher = CongressMembersFetcher(url)
    fetcher.fetch_data()

    print(fetcher.get_bioguide_id("Maria Cantwell"))
