from util import read_credentials_file
import requests

class SearchMan:
    def __init__(self):
        self.cred_json = read_credentials_file("Credentials.json")

    def QueryInternetForWebLinks(self,query:str):
        base_url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": self.cred_json['Google_Search']['google_Search_key'],
            "cx": self.cred_json['Google_Search']['google_Search_cx'],
            "q": query,
        }
        response = requests.get(base_url, params=params)
        data = response.json()
        search_results = data.get("items", [])
        return search_results

    def QueryInternetForYoutubeLinks(self,query:str):
        pass

    

# obj = SearchMan()

# result = obj.QueryInternetForWebLinks("Saint Padre Pio")

# print (result)