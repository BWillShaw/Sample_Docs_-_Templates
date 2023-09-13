import requests
from bs4 import BeautifulSoup
import json

# Fetch the webpage content
url = 'https://www.amazon.co.uk/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Pretty-print the HTML
print(soup.prettify())

# Convert some part of the HTML to a dictionary, for instance, the links in the page
links = []
for link in soup.find_all('a'):
    links.append({
        'text': link.text,
        'url': link.get('href')
    })

# Convert the dictionary to JSON and print it
links_json = json.dumps(links, indent=4)
print(links_json)
