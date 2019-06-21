import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# ECAC Standings
url1 = 'https://www.ecachockey.com/men/2018-19/standings'
response1 = requests.get(url1)
soup1 = BeautifulSoup(response1.text, 'html.parser')
table1 = soup1.findAll('tr')
table1 = table1[1:14]
infostrings1 = []
for t in table1:
    infostrings1.append(t.get_text())
    
# Pairwise Rankings
url2 = 'https://www.collegehockeynews.com/ratings/pairwise/2019'
response2 = requests.get(url2)
soup2 = BeautifulSoup(response2.text, 'html.parser')
table2 = soup2.findAll('tr')
table2 = table2[0:61]
infostrings2 = []
for t in table2:
    infostrings2.append(t.get_text())
    
# USCHO Poll Rankings
url3 = 'https://www.ncaa.com/rankings/icehockey-men/d1/uschocom'
response3 = requests.get(url3)
soup3 = BeautifulSoup(response3.text, 'html.parser')
table3 = soup3.findAll('tr')
table3 = table3[0:25]
infostrings3 = []
for t in table3:
    infostrings3.append(t.get_text())
    
# USA Today Poll Rankings
url4 = 'https://www.ncaa.com/rankings/icehockey-men/d1/usa-today/usa-hockey-magazine'
response4 = requests.get(url4)
soup4 = BeautifulSoup(response4.text, 'html.parser')
table4 = soup4.findAll('tr')
table4 = table4[0:16]
infostrings4 = []
for t in table4:
    infostrings4.append(t.get_text())