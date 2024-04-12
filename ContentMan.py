import SearchMan 

class ContentMan:
    def __init__(self):
        self.GeneratedView = ""

    def GenerateWebPagebasedOnContent(self,TextContent,imageURLs,videURLs):
        pass

    def create_html_file(self,search_results, output_file=r'templates\search_results.html'):


        
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

        html_content += """
        </body>
        </html>
        """

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(html_content)


        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(html_content)

        return html_content





    