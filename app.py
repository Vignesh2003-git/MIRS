from flask import Flask, request, render_template
import requests
from util import read_credentials_file
import ContentMan as CM
import SearchMan as SM
cred_json = read_credentials_file("Credentials.json")

app = Flask(__name__)

cm = CM.ContentMan()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form["query"]

        cm.GenerateWebPagebasedOnContent(query)
        return render_template("search_results.html")
    


if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)
