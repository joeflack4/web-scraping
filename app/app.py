"""App"""
import requests
from bs4 import BeautifulSoup

url = 'http://www.slate.com/topics/s/slate_book_review.html'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

if __name__ == '__main__':
    print(response, soup)