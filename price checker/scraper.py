import requests
from bs4 import BeautifulSoup

class WebCrawler:
#public:
    @staticmethod
    def getLowestPriceFromCeneo(self):
        self.__setNewSoup(WebCrawler, "https://www.ceneo.pl/42355584")
        results = [str(i.text) for i in self.__soup.find_all("span", class_= "price", limit = 5)]
        prices = []
        for i in results:
            i = i.replace(",", ".")
            prices.append(eval(i))
        return min(prices)

    @staticmethod
    def getLowestPriceFromAllegro(self):
        #self.__setNewSoup(WebCrawler, "") #stuff from Allegro
        return 54.99 #example

    @staticmethod
    def getLowestPriceFromOtherWebSites(self): #stuff from other sites
        #self.__setNewSoup(WebCrawler, "")
        return 39.99 #example

#private:
    def __setNewSoup(self, newLink : str):
        self.__link = newLink
        self.__page = requests.get(self.__link, headers = self.__headers)
        self.__soup = BeautifulSoup(self.__page.content, "html.parser")

    __headers =  { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0" }
    __link = ""
    __page = None
    __soup = None


print("Actual lowest price on Ceneo: " + str(WebCrawler.getLowestPriceFromCeneo(WebCrawler)) + " pln")
print("\nActual lowest price on Allegro: " + str(WebCrawler.getLowestPriceFromAllegro(WebCrawler)) + " pln")
print("\nActual lowest price on other sites: " + str(WebCrawler.getLowestPriceFromOtherWebSites(WebCrawler)) + " pln")
input()