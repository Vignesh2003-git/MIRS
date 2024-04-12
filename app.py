from flask import Flask, request, render_template
import requests
from util import read_credentials_file
import ContentMan as CM
import SearchMan as SM
cred_json = read_credentials_file("Credentials.json")

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form["query"]


        x = CM.ContentMan()

        obj = SM.SearchMan()

        

        result = obj.QueryInternetForWebLinks(query)

        QueryReq = "Summarize the following Web sniptets, and finally tell about all like a browser virtual assistant ["

        for i in result:
            QueryReq+=i["snippet"]+", "

        QueryReq+="]"



        
    
        x.GenerateWebPagebasedOnContent(QueryReq)
        
        x.create_html_file(result)
        
        
        return render_template("search_results.html")
    


if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)
