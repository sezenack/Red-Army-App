import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Team Stats Skaters
url1 = 'http://collegehockeyinc.com/stats/filters19.php?target=REN'
response1 = requests.get(url1)
soup1 = BeautifulSoup(response1.text, 'html.parser')
table1 = soup1.findAll('td')
infostrings1 = []
i = 0
header = ""
while i < 26:
    header += table1[i].get_text() + "\n"
    i += 1
infostrings1.append(header)
for t in range(26, 844, 30):
    a = 0
    string = ""
    while a < 30 and a + t < len(table1):
        string += table1[t + a].get_text() + "\n"
        a += 1
    infostrings1.append(string)

# Team Stats Goaltenders
url2 = 'http://collegehockeyinc.com/stats/filters19.php?target=REN&conf=on&nonconf=on&playoff=on&ncaa=on&site=all&wins=on&losses=on&ties=on&otgames=all&start=35&end=224&sun=on&mon=on&tue=on&wed=on&thu=on&fri=on&sat=on&limitx=none&limitn=1&limitt=indiv&p1=on&p2=on&p3=on&ot=on&full=on&even=on&pp=on&sh=on&lead=on&tied=on&trail=on&time1=on&time2=on&time3=on&time4=on&time5=on&time6=on&time7=on&time8=on&for=on&def=on&goal=on&fr=on&so=on&jr=on&sr=on&drafted=on&eligible=on&free=on&stats=goalie&sort=g'
response2 = requests.get(url2)
soup2 = BeautifulSoup(response2.text, 'html.parser')
table2 = soup2.findAll('td')
infostrings2 = []
i = 0
header = ""
while i < 17:
    header += table2[i].get_text() + "\n"
    i += 1
infostrings2.append(header)
for t in range(17, 20 * 3 + 17, 20):
    a = 0
    string = ""
    while a < 20 and a + t < len(table2):
        txt = table2[t + a].get_text()
        if '%' in txt:
            txt = txt[0:(txt.index('%') + 1)]
        string += txt + "\n"
        a += 1
    infostrings2.append(string)
    
# ECAC Player Stats (Main Skater Stats and Main Goaltender Stats)
url3 = 'https://www.ecachockey.com/men/2018-19/leaders'
response3 = requests.get(url3)
soup3 = BeautifulSoup(response3.text, 'html.parser')
table3 = soup3.findAll('tr')
table3 = table3[2:8] + table3[9:15] + table3[16:22] + table3[23:29] + table3[31:37] + table3[38:44]
infostrings3 = []
for t in table3:
    infostrings3.append(t.get_text())
    
# ECAC Skater Points per Game Stats
url4 = 'http://collegehockeyinc.com/stats/filters19.php?target=EC&conf=on&nonconf=on&playoff=on&ncaa=on&site=all&start=35&end=224&wins=on&losses=on&ties=on&otgames=all&sun=on&mon=on&tue=on&wed=on&thu=on&fri=on&sat=on&limitx=none&limitn=1&limitt=indiv&p1=on&p2=on&p3=on&ot=on&full=on&even=on&pp=on&sh=on&lead=on&tied=on&trail=on&time1=on&time2=on&time3=on&time4=on&time5=on&time6=on&time7=on&time8=on&for=on&def=on&goal=on&fr=on&so=on&jr=on&sr=on&drafted=on&eligible=on&free=on&stats=scoring&sort=p_gm'
response4 = requests.get(url4)
soup4 = BeautifulSoup(response4.text, 'html.parser')
table4 = soup4.findAll('td')
infostrings4 = []
for t in range(27, len(table4), 31):
    a = 0
    string = ""
    while a < 5 and a + t < len(table4):
        string += table4[t + a].get_text() + "\n"
        a += 1
    string += table4[t + 12].get_text() + "\n"
    infostrings4.append(string)
    
# ECAC Skater Shooting % Stats
url5 = 'http://collegehockeyinc.com/stats/filters19.php?target=EC&conf=on&nonconf=on&playoff=on&ncaa=on&site=all&start=35&end=224&wins=on&losses=on&ties=on&otgames=all&sun=on&mon=on&tue=on&wed=on&thu=on&fri=on&sat=on&limitx=none&limitn=1&limitt=indiv&p1=on&p2=on&p3=on&ot=on&full=on&even=on&pp=on&sh=on&lead=on&tied=on&trail=on&time1=on&time2=on&time3=on&time4=on&time5=on&time6=on&time7=on&time8=on&for=on&def=on&goal=on&fr=on&so=on&jr=on&sr=on&drafted=on&eligible=on&free=on&stats=scoring&sort=shpct'
response5 = requests.get(url5)
soup5 = BeautifulSoup(response5.text, 'html.parser')
table5 = soup5.findAll('td')
infostrings5 = []
for t in range(27, len(table5), 31):
    a = 0
    string = ""
    while a < 5 and a + t < len(table5):
        string += table5[t + a].get_text() + "\n"
        a += 1
    string += table5[t + 24].get_text() + "\n"
    infostrings5.append(string)

# ECAC Skater Faceoff % Stats
url6 = 'http://collegehockeyinc.com/stats/filters19.php?target=EC&conf=on&nonconf=on&playoff=on&ncaa=on&site=all&start=35&end=224&wins=on&losses=on&ties=on&otgames=all&sun=on&mon=on&tue=on&wed=on&thu=on&fri=on&sat=on&limitx=none&limitn=1&limitt=indiv&p1=on&p2=on&p3=on&ot=on&full=on&even=on&pp=on&sh=on&lead=on&tied=on&trail=on&time1=on&time2=on&time3=on&time4=on&time5=on&time6=on&time7=on&time8=on&for=on&def=on&goal=on&fr=on&so=on&jr=on&sr=on&drafted=on&eligible=on&free=on&stats=scoring&sort=fpct'
response6 = requests.get(url6)
soup6 = BeautifulSoup(response6.text, 'html.parser')
table6 = soup6.findAll('td')
infostrings6 = []
for t in range(27, 31 * 69 + 27, 31):
    a = 0
    string = ""
    while a < 5 and a + t < len(table6):
        string += table6[t + a].get_text() + "\n"
        a += 1
    string += table6[t + 27].get_text() + "\n"
    infostrings6.append(string)

# ECAC Skater Blocked Shots Stats
url7 = 'http://collegehockeyinc.com/stats/filters19.php?target=EC&conf=on&nonconf=on&playoff=on&ncaa=on&site=all&start=35&end=224&wins=on&losses=on&ties=on&otgames=all&sun=on&mon=on&tue=on&wed=on&thu=on&fri=on&sat=on&limitx=none&limitn=1&limitt=indiv&p1=on&p2=on&p3=on&ot=on&full=on&even=on&pp=on&sh=on&lead=on&tied=on&trail=on&time1=on&time2=on&time3=on&time4=on&time5=on&time6=on&time7=on&time8=on&for=on&def=on&goal=on&fr=on&so=on&jr=on&sr=on&drafted=on&eligible=on&free=on&stats=scoring&sort=blk'
response7 = requests.get(url7)
soup7 = BeautifulSoup(response7.text, 'html.parser')
table7 = soup7.findAll('td')
infostrings7 = []
for t in range(28, 100 * 32 + 28, 32):
    a = 0
    string = ""
    while a < 5 and a + t < len(table7):
        string += table7[t + a].get_text() + "\n"
        a += 1
    string += table7[t + 28].get_text() + "\n"
    infostrings7.append(string)

# National Skater Main Stats
url8 = 'http://collegehockeyinc.com/stats/filters19.php'
response8 = requests.get(url8)
soup8 = BeautifulSoup(response8.text, 'html.parser')
table8 = soup8.findAll('td')
infostrings8 = []
for t in range(27, len(table8), 31):
    a = 0
    string = ""
    while a < 10 and a + t < len(table8):
        if a == 5 or a == 6:
            a += 1
            continue
        string += table8[t + a].get_text() + "\n"
        a += 1
    string += table8[t + 12].get_text() + "\n"
    infostrings8.append(string)

# National Skater Plus/Minus Stats
url9 = 'http://collegehockeyinc.com/stats/filters19.php?target=ALL&conf=on&nonconf=on&playoff=on&ncaa=on&site=all&start=1&end=224&wins=on&losses=on&ties=on&otgames=&sun=on&mon=on&tue=on&wed=on&thu=on&fri=on&sat=on&limitx=&limitn=&limitt=&p1=on&p2=on&p3=on&ot=on&full=on&even=on&pp=on&sh=on&lead=on&tied=on&trail=on&time1=on&time2=on&time3=on&time4=on&time5=on&time6=on&time7=on&time8=on&for=on&def=on&goal=on&fr=on&so=on&jr=on&sr=on&drafted=on&eligible=on&free=on&stats=scoring&sort=pm'
response9 = requests.get(url9)
soup9 = BeautifulSoup(response9.text, 'html.parser')
table9 = soup9.findAll('td')
infostrings9 = []
for t in range(27, len(table9), 31):
    a = 0
    string = ""
    while a < 5 and a + t < len(table9):
        string += table9[t + a].get_text() + "\n"
        a += 1
    string += table9[t + 21].get_text() + "\n"
    infostrings9.append(string)

# National Skater Shooting % Stats
url10 = 'http://collegehockeyinc.com/stats/filters19.php?target=ALL&conf=on&nonconf=on&playoff=on&ncaa=on&site=all&start=1&end=224&wins=on&losses=on&ties=on&otgames=&sun=on&mon=on&tue=on&wed=on&thu=on&fri=on&sat=on&limitx=&limitn=&limitt=&p1=on&p2=on&p3=on&ot=on&full=on&even=on&pp=on&sh=on&lead=on&tied=on&trail=on&time1=on&time2=on&time3=on&time4=on&time5=on&time6=on&time7=on&time8=on&for=on&def=on&goal=on&fr=on&so=on&jr=on&sr=on&drafted=on&eligible=on&free=on&stats=scoring&sort=shpct'
response10 = requests.get(url10)
soup10 = BeautifulSoup(response10.text, 'html.parser')
table10 = soup10.findAll('td')
infostrings10 = []
for t in range(27, len(table10), 31):
    a = 0
    string = ""
    while a < 5 and a + t < len(table10):
        string += table10[t + a].get_text() + "\n"
        a += 1
    string += table10[t + 24].get_text() + "\n"
    infostrings10.append(string)

# National Skater Faceoff % Stats
url11 = 'http://collegehockeyinc.com/stats/filters19.php?target=ALL&conf=on&nonconf=on&playoff=on&ncaa=on&site=all&start=1&end=224&wins=on&losses=on&ties=on&otgames=&sun=on&mon=on&tue=on&wed=on&thu=on&fri=on&sat=on&limitx=&limitn=&limitt=&p1=on&p2=on&p3=on&ot=on&full=on&even=on&pp=on&sh=on&lead=on&tied=on&trail=on&time1=on&time2=on&time3=on&time4=on&time5=on&time6=on&time7=on&time8=on&for=on&def=on&goal=on&fr=on&so=on&jr=on&sr=on&drafted=on&eligible=on&free=on&stats=scoring&sort=fpct'
response11 = requests.get(url11)
soup11 = BeautifulSoup(response11.text, 'html.parser')
table11 = soup11.findAll('td')
infostrings11 = []
for t in range(27, len(table11), 31):
    a = 0
    string = ""
    while a < 5 and a + t < len(table11):
        string += table11[t + a].get_text() + "\n"
        a += 1
    string += table11[t + 27].get_text() + "\n"
    infostrings11.append(string)

# National Skater Blocked Shots Stats
url12 = 'http://collegehockeyinc.com/stats/filters19.php?target=ALL&conf=on&nonconf=on&playoff=on&ncaa=on&site=all&start=1&end=224&wins=on&losses=on&ties=on&otgames=&sun=on&mon=on&tue=on&wed=on&thu=on&fri=on&sat=on&limitx=&limitn=&limitt=&p1=on&p2=on&p3=on&ot=on&full=on&even=on&pp=on&sh=on&lead=on&tied=on&trail=on&time1=on&time2=on&time3=on&time4=on&time5=on&time6=on&time7=on&time8=on&for=on&def=on&goal=on&fr=on&so=on&jr=on&sr=on&drafted=on&eligible=on&free=on&stats=scoring&sort=blk'
response12 = requests.get(url12)
soup12 = BeautifulSoup(response12.text, 'html.parser')
table12 = soup12.findAll('td')
infostrings12 = []
for t in range(28, len(table12), 32):
    a = 0
    string = ""
    while a < 5 and a + t < len(table12):
        string += table12[t + a].get_text() + "\n"
        a += 1
    string += table12[t + 28].get_text() + "\n"
    infostrings12.append(string)

# National Main Goaltender Stats
url13 = 'http://collegehockeyinc.com/stats/filters19.php?stats=goalie'
response13 = requests.get(url13)
soup13 = BeautifulSoup(response13.text, 'html.parser')
table13 = soup13.findAll('td')
infostrings13 = []
for t in range(17, 70 * 20 + 17, 20):
    a = 0
    string = ""
    while a < 4 and a + t < len(table13):
        string += table13[t + a].get_text() + "\n"
        a += 1
    string += table13[t + 13].get_text() + "\n"
    string += table13[t + 14].get_text() + "\n"
    infostrings13.append(string)