# Import required libraries
import requests
from bs4 import BeautifulSoup

# Make an HTTP fetch request to url to return content
html_response = requests.get('http://books.toscrape.com/')
html_content = BeautifulSoup(html_response.content, 'html.parser')

# Use the bs4 object property 'find_all' to search returned
# html content for common html class 'product_pod'. This class
# is common among all books listed on the site so should return
# a list of all books
book_list = html_content.find_all(class_='product_pod')

# Iterate through 'book_list' and print each book to console
for book in book_list:
    book_title = book.find('h3').find('a').attrs['title']
    print(book_title)

