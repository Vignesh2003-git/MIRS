import SearchMan 
import AiMan as A

class ContentMan:
    def __init__(self):
        self.Ai = A.AiMan()
        self.GeneratedView = ""
        self.AiGeneratedSummary = ""
        self.youtubeLinks =[]
        self.imagesLinks = []

    def GenerateWebPagebasedOnContent(self,TextContent):

        self.AiGeneratedSummary = self.Ai.ProcessContentData(TextContent)


    def create_html_file(self, search_results, output_file=r'templates\search_results.html'):

        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>MIRS Results</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    margin: 20px;
                    background-color: #f8f9fa;
                    display: flex; /* Make the body a flex container */
                }
                .search-results {
                    flex: 1; /* Take up remaining space */
                    margin-right: 20px; /* Add space between search results and summary */
                }
                .summary {
                    
                    flex: 1; /* Take up remaining space */
                    background-color: #ffffff; /* Background color for the summary section */
                    border-radius: 8px; /* Rounded corners */
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Box shadow for a subtle effect */
                    padding: 15px; /* Padding to add space inside the summary section */
                }
                h1 {
                    text-align: center;
                    color: #007BFF;
                }
                .result {
                    background-color: #fff;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    margin-bottom: 20px;
                    padding: 15px;
                }
                .title {
                    font-size: 1.5em;
                    font-weight: bold;
                    color: #007BFF;
                    margin-bottom: 10px;
                }
                .url {
                    color: #4CAF50;
                    margin-bottom: 5px;
                }
                .snippet {
                    color: #6C757D;
                    margin-bottom: 15px;
                }
                .image {
                    max-width: 100%;
                    height: auto;
                    margin-top: 10px;
                    border-radius: 8px;
                }
            </style>
        </head>
        <body>
            <div class="search-results">
                <h1>MIRS Search Results</h1>
        """

        for result in search_results:
            html_content += f"""
            <div class="result">
                <div class="title"><a href="{result['link']}" target="_blank">{result['title']}</a></div>
                <div class="url">{result['formattedUrl']}</div>
                <div class="snippet">{result['snippet']}</div>
        """

            if 'pagemap' in result and 'cse_thumbnail' in result['pagemap']:
                thumbnail = result['pagemap']['cse_thumbnail'][0]['src']
                html_content += f'<img class="image" src="{thumbnail}" alt="Result Thumbnail">'
            
            html_content += """
            </div>
            """

        html_content += f"""
            </div>
            <div class="summary">
                <!-- Summary container -->
                <h2>MIRS Summary</h2>
                <!-- Summary title -->
                {self.AiGeneratedSummary}
            </div>
        </body>
        </html>
        """

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(html_content)

        return html_content





    