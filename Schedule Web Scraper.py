import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Schedule
url1 = 'https://rpiathletics.com/schedule.aspx?path=hockey&'
response1 = requests.get(url1, headers={'User-Agent': 'Custom'})
soup1 = BeautifulSoup(response1.text, 'html.parser')
table1 = soup1.findAll('span')
#table1 = table1[0:37]
infostrings1 = []
for t in table1:
    infostrings1.append(t.get_text())
