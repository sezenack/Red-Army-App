import requests
import urllib.request
import time
from bs4 import BeautifulSoup
'''
cnx = mysql.connector.connect(user='', password='', host='', database='')
cursor = cnx.cursor()
tables = {}

tables['teamstats'] = (
    "CREATE TABLE `teamstats` ("
    "  `team_name` varchar(22) NOT NULL,"
    "  `gpg` decimal NOT NULL,"
    "  `gapg` decimal NOT NULL,"
    "  `shpg` decimal NOT NULL,"
    "  `shapg` decimal NOT NULL,"
    "  `shoot_pct` decimal NOT NULL,"
    "  `sv_pct` decimal NOT NULL,"
    "  `pp_pct` decimal NOT NULL,"
    "  `pk_pct` decimal NOT NULL,"
    "  `fo_pct` decimal NOT NULL,"
    "  `age` decimal NOT NULL,"
    "  `ht` varchar(10) NOT NULL,"
    "  `wt` decimal NOT NULL,"
    "  PRIMARY KEY (`team_name`)"
    ") ENGINE=InnoDB")
add_team = ("INSERT INTO teamstats "
            "(team_name, gpg, gapg, shpg, shapg, shoot_pct, sv_pct, pp_pct, pk_pct, fo_pct, age, ht, wt) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
'''
# Team Stats
url1 = 'https://www.collegehockeynews.com/stats/'
response1 = requests.get(url1)
soup1 = BeautifulSoup(response1.text, 'html.parser')
table1 = soup1.findAll('tr')
table1 = table1[2:62]
info1 = []
for t in table1:
    teaminfo = (t.get_text()).split('\n')
    teaminfo.remove('')
    teaminfo.remove('')
    teaminfo.pop(0)
    teaminfo[1] = int(teaminfo[1])
    teaminfo[2] = int(teaminfo[2])
    teaminfo[3] = int(teaminfo[3])
    teaminfo[4] = int(teaminfo[4])
    teaminfo[6] = int(teaminfo[6])
    teaminfo.pop(10)
    teaminfo.pop(10)
    info1.append(teaminfo)
    # cursor.execute(add_team, (teaminfo[0], teaminfo[2] / teaminfo[1], teaminfo[3] / teaminfo[1], teaminfo[4] / teaminfo[1], teaminfo[6] / teaminfo[1], teaminfo[5], teaminfo[7], teaminfo[8], teaminfo[9], teaminfo[10], teaminfo[11], teaminfo[12], teaminfo[13]))