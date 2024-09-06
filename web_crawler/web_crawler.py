import requests
from bs4 import BeautifulSoup

def crawl_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))

url = input("Enter the URL: ")
crawl_website(url)