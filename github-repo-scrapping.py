import requests
from bs4 import BeautifulSoup

userName = input("Enter the username whose repo list you want to see:")
url = "https://github.com/"+userName
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html,'html.parser')
listofSpan = soup.find_all('span',attrs={'class':'repo js-pinnable-item'})

for span in listofSpan:
    print(span.text)
