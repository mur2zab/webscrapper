import requests
from bs4 import BeautifulSoup

search_query = input("Search: ")
url = "https://www.youtube.com/results?search_query="+search_query+"&sp=EgIQAg%253D%253D"

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html,'html.parser')
# print(html)
initialDiv = soup.find_all('div',attrs={'class':'yt-lockup-content'});
initialDiv = initialDiv[1:] #Removing the first element Since it is an Advertisement
channelsList = [];

for eachDiv in initialDiv:
    title = eachDiv.find('a').text
    views_in_string = eachDiv.find('ul',attrs={'class': "yt-lockup-meta-info"}).text
    views_in_number = views_in_string.split(' ')[0]
    views_in_number = int(views_in_number.replace(',','')) # replacing , since the result contains numbers in string such as 1,234
    channelsList.append((title,views_in_number));

channelsList = sorted(channelsList,key=lambda x:x[1],reverse=True) # sort and reverse the list of tuples

for channel in channelsList:
    print("Channel name: "+channel[0]+"\n Videos: "+str(channel[1]))
