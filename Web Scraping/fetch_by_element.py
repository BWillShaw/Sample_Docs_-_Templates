import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# URL to scrape
url_to_scrape = "https://www.theguardian.com/uk"

# Fetch webpage
response = requests.get(url_to_scrape)
soup = BeautifulSoup(response.content, "html.parser")

# Prettify and print a portion of the HTML content for better readability
print(soup.prettify()[:300])


# Function to categorize URLs as parent or child
def categorize_url(url):
    parsed = urlparse(url)
    if parsed.path in ["", "/"]:
        return "parent"
    else:
        return "child"


# Get URLs and categorize them
all_urls = [a["href"] for a in soup.find_all("a", href=True)]
parent_urls = []
child_urls = []

for url in all_urls:
    if categorize_url(url) == "parent":
        parent_urls.append(url)
    else:
        child_urls.append(url)

# Print categorized URLs in a readable manner
print("Parent URLs:")
for url in parent_urls:
    print(f"  - {url}")

print("\nChild URLs:")
for url in child_urls:
    print(f"  - {url}")

# Get all elements containing images
image_elements = soup.find_all("img")

# Get and print elements containing images
print("\nElements with Images:")
image_elements = soup.find_all("img")
for element in image_elements:
    if "src" in element.attrs:
        print(f"Image URL: {element['src']}")
