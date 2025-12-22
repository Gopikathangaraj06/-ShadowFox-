import requests
from bs4 import BeautifulSoup

print("Scraper started")

url = "http://quotes.toscrape.com/"
response = requests.get(url)

print("Status code:", response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("span", class_="text")

    print("\nQuotes:\n")
    for quote in quotes[:5]:
        print(quote.text)
else:
    print("Failed to load website")
