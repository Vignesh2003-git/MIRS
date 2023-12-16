from flask import Flask, request, render_template
import requests
from util import read_credentials_file

cred_json = read_credentials_file("Credentials.json")

app = Flask(__name__)


def perform_search(query, api_key, cx):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": cred_json['Google_Search']['google_Search_key'],
        "cx": cred_json['Google_Search']['google_Search_cx'],
        "q": query,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    search_results = data.get("items", [])
    formatted_results = f"You searched for: {query}\n\nHere are the search results:\n"

    for item in search_results:
        title = item["title"]
        link = item["link"]
        formatted_results += f"<a href='{link}'>{title}</a><br>"

    return formatted_results


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form["query"]
        search_result = perform_search(
            query, "AIzaSyA1sMAt7m0ft40zgJRS81ggY1qKM5MX1s0", "d18cf906a50574eb7"
        )
        return render_template("search.html", query=query, result=search_result)


if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)
