import requests
from bs4 import BeautifulSoup

url = "https://scikit-learn.org/stable/modules/clustering.html#clustering"
html = requests.get(url) #this get method requests to retrieve data from specified url

webscrap = BeautifulSoup(html.content,"html.parser") #beautifulsoup is constructor which retrives content based on the method passsed

fetched_out = webscrap.find_all("div",{"id" : "overview-of-clustering-methods"})#here we used the div tag to extract the required information
print(fetched_out)