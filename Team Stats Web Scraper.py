import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Team Stats
url1 = 'https://www.collegehockeynews.com/stats/'
response1 = requests.get(url1)
soup1 = BeautifulSoup(response1.text, 'html.parser')
table1 = soup1.findAll('tr')
table1 = table1[1:62]
infostrings1 = []
for t in table1:
    infostrings1.append(t.get_text())