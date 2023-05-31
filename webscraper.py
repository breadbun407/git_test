import requests
from bs4 import BeautifulSoup as bs

with open('links.txt', 'r') as file:
    link_names = file.read().splitlines()



    # Making a GET request
    URL = 'https://dota2.fandom.com/' + link_names
    response = requests.get(URL)
    if response.status_code == 200:
     # Parsing the HTML
        soup = bs(response.content, 'html.parser')

        lines = soup.find_all('p')
        scraped_data = []
        scraped_data.append(lines)
        for line in scraped_data:
            title = line["title"]
            paragraph = line["paragraph"]

            # Generate a filename based on the title
            filename = f"{title}.md"

            # Open a file in write mode
            with open(filename, 'w') as file:
                # Write the paragraph to the file in Markdown format
                file.write(f"# {title}\n\n")
                file.write(f"{paragraph}\n")
