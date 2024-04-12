from util import read_credentials_file

import textwrap

import google.generativeai as genai
import markdown as md
from IPython.display import Markdown


def to_HTML(text):
  text = text.replace('•', '  *')
  my_data = Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
  return md.markdown(my_data.data)



class AiMan:
    def __init__(self):
        self.cred_json = read_credentials_file("Credentials.json")
        API_KEY = self.cred_json['Google_Gemini']['google_Gemini_key']       
        genai.configure(api_key=API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')

    def ProcessContentData(self,Content:str):
        
        return self.Produce_Text(Content)
        # write the code to communicate with Google generative Ai and get the response
        # Produce_AudioURL(Content)
        # Produce_ImageURL(Content)
        # Produce_YoutubeVideoURL(Content)


    def Produce_Text(self,Content:str):
        response = self.model.generate_content(Content)
        myData = to_HTML(response.text)
        
        return myData

    def Produce_ImageURL(self,Content:str):
        pass

    def Produce_AudioURL(self,Content:str):
        pass

    def Produce_YoutubeVideoURL(self,Content:str):
        pass

if(__name__ == "__main__"):
    Ai = AiMan()
    Ai.ProcessContentData("How smart is a human?")
    Ai.ProcessContentData("What is the meaning of life?")
    Ai.ProcessContentData("What is the future of AI?")
    Ai.ProcessContentData("What is the meaning of love?")
    Ai.ProcessContentData("What is the meaning of death?")
    Ai.ProcessContentData("What is the meaning of the universe?")