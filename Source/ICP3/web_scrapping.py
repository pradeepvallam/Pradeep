#import necessary libraries for web scrapping
import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/Deep_learning"
html = requests.get(url) #this get method requests to retrieve data from specified url
webscrap = BeautifulSoup(html.content,"html.parser") #beautifulsoup is constructor which retrives content based on the method passsed
print(webscrap.title) #prints the title of the page
print(webscrap.find_all("a")) #prints all the links in page
for link in webscrap.find_all("a"): #iterates for each link a
    print(link.get("href")) #for each iteration returns a link using href attribute
