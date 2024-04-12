from util import read_credentials_file
import requests

class SearchMan:
    def __init__(self):
        self.cred_json = read_credentials_file("Credentials.json")
        self.SearResultData = None
        self.query = None

    def QueryInternetForWebLinks(self,query:str):
        base_url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": self.cred_json['Google_Search']['google_Search_key'],
            "cx": self.cred_json['Google_Search']['google_Search_cx'],
            "q": query,
        }
        self.query = query
        # Make the API request
        response = requests.get(base_url, params=params)
        self.SearResultData = response.json()


        search_results = self.SearResultData.get("items", [])
        
        return self.SearResultData

    def QueryInternetForYoutubeLinks(self,query:str):

        search_query = query

        # Set the search URL and parameters
        search_url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            "part": "snippet",
            "maxResults": 5,
            "q": search_query,
            "key": self.cred_json['Google_Search']['google_Search_key'],
        }

        # Make the API request
        response = requests.get(search_url, params=params)

        # Parse the JSON response
        results = response.json()

        # Extract the video IDs from the search results
        video_ids = []
        for item in results["items"]:
            if(item["id"]["kind"] == "youtube#video"):
                video_ids.append(item["id"]["videoId"])

        # Return the list of video IDs
        return video_ids

    def GeneratePromptForGemini(self,result):
        QueryReq = "Summarize the following Web sniptets into a singularity ,Be a virtual Assitant and tell your ideas ,you are now called as MIRS ["
        QueryReq += f"User Query : {self.query}\n"
        c = 1
        for i in result.get("items", []):
            try:
                QueryReq+=f"{c} = "+i["title"]+", "+i["link"]+", "+i["snippet"]+"\n "
                c+=1
            except:
                QueryReq+=f"{c} = "+i["title"]+", "+i["link"]+" \n " 
                c+=1

        QueryReq+="]"

        return QueryReq
    
    def QueryInternetForImages(self,query:str):
        base_url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": self.cred_json['Google_Search']['google_Search_key'],
            "cx": self.cred_json['Google_Search']['google_Search_cx'],
            "q": query,
            "searchType": "image",
        }
        self.query = query
        # Make the API request
        response = requests.get(base_url, params=params)
        self.SearResultData = response.json()

        self.search_results = self.SearResultData.get("items", [])
        links = []
        c = 1
        for i in self.search_results:
            try:
                links.append(i["link"])
                
            except:
                pass
            
            c+=1

        
        print(links)
        return links
    

if(__name__ == "__main__"):
    SM = SearchMan()

    # result = obj.QueryInternetForWebLinks("Saint Padre Pio")

    # print (result)
    result = SM.QueryInternetForYoutubeLinks("Saint Padre Pio")
    print (result)

    result = SM.QueryInternetForImages("Saint Padre Pio")
    print (result)

    SM.GeneratePromptForGemini(result)
