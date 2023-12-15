import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad requests
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_text_from_html(html):
    if html is None:
        return None

    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text(separator='\n', strip=True)
    return text

def get_html_contents_of_urls(url_list):
    html_contents = []
    for url in url_list:
        html = get_html_content(url)
        text_content = extract_text_from_html(html)
        html_contents.append(text_content)
    return html_contents

# Example usage:
urls = ["https://en.wikipedia.org/wiki/Main_Page", "https://www.javatpoint.com/"]
result = get_html_contents_of_urls(urls)


for content in result:
    try:
        print("+ = "*100)
        print(content)
    except UnicodeEncodeError:
        print("UnicodeEncodeError: Unable to print content.")
