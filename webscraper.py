import requests
from bs4 import BeautifulSoup as bs

with open('links.txt', 'r') as file:
    link_names_list = file.read().splitlines()

    base_url = 'https://dota2.fandom.com'  # Replace with the base URL of the website

    complete_urls = []
    for urls in link_names_list:
        complete_url = base_url + urls
        complete_urls.append(complete_url)

    # Making a GET request
    for url in complete_urls:
        response = requests.get(url)
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
