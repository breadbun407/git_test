import requests
from bs4 import BeautifulSoup as bs

with open('links.txt', 'w') as file:
    URL = 'https://dota2.fandom.com/wiki/Lore'

    response = requests.get(URL)
    if response.status_code == 200:
        soup = bs(response.content, 'html.parser')

    # Find all <a> tags within a specific tag (e.g., <div> with class="content")
        specific_tag = soup.find('table', class_='notanavbox')
        links = specific_tag.find_all('a')

        # Extract the href attribute from each <a> tag to get the links
        for link in links:
            href = link.get('href')
            file.write(href + '\n')
            