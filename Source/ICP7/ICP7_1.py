import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Google"
html = requests.get(url).text #this get method requests to retrieve data from specified url

webscrap = BeautifulSoup(html,"html.parser") #beautifulsoup is constructor which retrives content based on the method passsed

for script in webscrap(["script", "style"]):
    script.extract()

txt = webscrap.body.get_text()

f = open("E:\python\input.txt","w+")
f.write(str(txt.encode("utf-8")))

