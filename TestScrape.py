import os
import re
import requests
from bs4 import BeautifulSoup as bs

def sanitize_file_name(name):
    sanitized_name = re.sub(r'[<>:"/\\|?*%]', '_', name)
    return sanitized_name

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

        # Extract the title from the HTML
        title = soup.find('h1').get_text(strip=True)

        # Find the relevant <p> tags or adjust as per the target HTML structure
        paragraphs = soup.find_all('p')

        # Save the scraped paragraphs to individual files
        directory = 'Dota2Lore'
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Generate a new file for each title
        filename = f"{title}.md"
        sanitized_filename = sanitize_file_name(filename)
        file_path = os.path.join(directory, sanitized_filename)

        with open(file_path, 'w') as file:
            for idx, paragraph in enumerate(paragraphs):
                # Remove references in the form of [1], [2], etc.
                text = re.sub(r'\[\d+\]', '', paragraph.get_text())

                # Add a space after a bold tag if the text is directly wrapped by <b> tags
                if '<b>' + text + '</b>' == paragraph.prettify():
                    text = ' ' + text + ' '

                # Trim leading and trailing whitespace
                text = text.strip()

                # Write the paragraph to the file
                file.write(text + '\n')
