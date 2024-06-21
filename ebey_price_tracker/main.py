import requests
from bs4 import BeautifulSoup
url = "https://www.ebay.com/itm/276217871434?var=578595881617"
res = requests.get(url)
# print(res.text)
soup = BeautifulSoup(res.text,'lxml')
unedited = soup.select('.x-price-primary > .ux-textspans')[0].text[4:]
actual_price = float(unedited)
my_price = 1000
if actual_price < my_price:
    print("The price is below your budget, go grab them")
    