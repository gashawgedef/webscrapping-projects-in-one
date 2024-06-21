from nturl2path import url2pathname
import requests
from bs4 import BeautifulSoup
url = "https://bifacon.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')
titles=(soup.title).getText()
print(titles)
text_value= soup.find_all('div', class_="card-body")
for i in range(len(text_value)):
    print(text_value[i].get_text())
print(text_value)