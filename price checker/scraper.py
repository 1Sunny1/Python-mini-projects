import requests
from bs4 import BeautifulSoup

def getLowestPriceFromCeneo():
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0" }
    link = "https://www.ceneo.pl/42355584"
    page = requests.get(link, headers = headers)
    soup = BeautifulSoup(page.content, "html.parser")

    results = [str(i.text) for i in soup.find_all("span", class_= "price", limit = 5)]
    prices = []
    for i in results:
        i = i.replace(",", ".")
        prices.append(eval(i))

    return min(prices)


print("Actual lowest price: " + str(getLowestPriceFromCeneo()) + " pln")
input()

