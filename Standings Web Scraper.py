import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import mysql.connector
'''
cnx = mysql.connector.connect(user='', password='', host='', database='')
cursor = cnx.cursor()
tables = {}

tables['ecacstandings'] = (
    "CREATE TABLE `ecacstandings` ("
    "  `rank` tinyint NOT NULL AUTO_INCREMENT,"
    "  `team_name` varchar(12) NOT NULL,"
    "  `points` tinyint NOT NULL,"
    "  `conf_gp` tinyint NOT NULL,"
    "  `conf_record` varchar(8) NOT NULL,"
    "  `conf_win_pct` decimal NOT NULL,"
    "  `conf_gf` tinyint NOT NULL,"
    "  `conf_ga` tinyint NOT NULL,"
    "  `tot_gp` tinyint NOT NULL,"
    "  `tot_record` varchar(8) NOT NULL,"
    "  `tot_win_pct` decimal NOT NULL,"
    "  `tot_gf` tinyint NOT NULL,"
    "  `tot_ga` tinyint NOT NULL,"
    "  `l10` varchar(6) NOT NULL,"
    "  `strk` varchar(6) NOT NULL,"
    "  PRIMARY KEY (`rank`)"
    ") ENGINE=InnoDB")
add_teamecac = ("INSERT INTO ecacstandings "
            "(team_name, points, conf_gp, conf_record, conf_win_pct, conf_gf, conf_ga, tot_gp, tot_record, tot_win_pct, tot_gf, tot_ga, l10, strk) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
'''
# ECAC Standings
url1 = 'https://www.ecachockey.com/men/2018-19/standings'
response1 = requests.get(url1)
soup1 = BeautifulSoup(response1.text, 'html.parser')
table1 = soup1.findAll('tr')
table1 = table1[2:14]
info1 = []
for t in table1:
    teaminfo = (t.get_text()).split('\n')
    teaminfo.remove('')
    teaminfo.remove('')
    teaminfo.remove('')
    teaminfo[0] = teaminfo[0].strip()
    teaminfo[1] = teaminfo[1].strip()
    index = teaminfo[0].index(' ')
    teaminfo[0] = teaminfo[0][index + 1:len(teaminfo[0])]
    info1.append(teaminfo)
    # cursor.execute(add_teamecac, (teaminfo[0], teaminfo[1], teaminfo[2], teaminfo[3], teaminfo[4], teaminfo[5], teaminfo[6], teaminfo[7], teaminfo[8], teaminfo[9], teaminfo[10], teaminfo[11], teaminfo[12], teaminfo[13]))
'''
tables['pairwise'] = (
    "CREATE TABLE `pairwise` ("
    "  `rank` tinyint NOT NULL AUTO_INCREMENT,"
    "  `team_name` varchar(22) NOT NULL,"
    "  `pcw` tinyint NOT NULL,"
    "  `rpi` decimal NOT NULL,"
    "  `rpi_rank` tinyint NOT NULL,"
    "  `qwb` decimal NOT NULL,"
    "  `record` varchar(8) NOT NULL,"
    "  `win_pct` decimal NOT NULL,"
    "  PRIMARY KEY (`rank`)"
    ") ENGINE=InnoDB")
add_teampairwise = ("INSERT INTO pairwise "
            "(team_name, pcw, rpi, rpi_rank, qwb, record, win_pct) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)")
'''
# Pairwise Rankings
url2 = 'https://www.collegehockeynews.com/ratings/pairwise/2019'
response2 = requests.get(url2)
soup2 = BeautifulSoup(response2.text, 'html.parser')
table2 = soup2.findAll('tr')
table2 = table2[1:61]
info2 = []
for t in table2:
    teaminfo = (t.get_text()).split('\n')
    teaminfo.remove('')
    teaminfo.remove('')
    teaminfo = teaminfo[1:8]
    info2.append(teaminfo)
    # cursor.execute(add_teampairwise, (teaminfo[0], teaminfo[1], teaminfo[2], teaminfo[3], teaminfo[4], teaminfo[5], teaminfo[6]))
'''
tables['uscho'] = (
    "CREATE TABLE `uscho` ("
    "  `rank` tinyint NOT NULL AUTO_INCREMENT,"
    "  `team_name` varchar(22) NOT NULL,"
    "  `record` varchar(8) NOT NULL,"
    "  `points` tinyint NOT NULL,"
    "  `prev_rank` tinyint NOT NULL,"
    "  PRIMARY KEY (`rank`)"
    ") ENGINE=InnoDB")
add_teamuscho = ("INSERT INTO uscho "
            "(team_name, record, points, prev_rank) "
            "VALUES (%s, %s, %s, %s)")
'''
# USCHO Poll Rankings
url3 = 'https://www.ncaa.com/rankings/icehockey-men/d1/uschocom'
response3 = requests.get(url3)
soup3 = BeautifulSoup(response3.text, 'html.parser')
table3 = soup3.findAll('tr')
table3 = table3[1:25]
info3 = []
for t in table3:
    teaminfo = (t.get_text()).split('\n')
    teaminfo.remove('')
    teaminfo.remove('')
    teaminfo[1] = teaminfo[1].strip()
    teaminfo = teaminfo[1:len(teaminfo)]
    info3.append(teaminfo)
    # cursor.execute(add_teamuscho, (teaminfo[0], teaminfo[1], teaminfo[2], teaminfo[3]))
'''
tables['usatoday'] = (
    "CREATE TABLE `usatoday` ("
    "  `rank` tinyint NOT NULL AUTO_INCREMENT,"
    "  `team_name` varchar(22) NOT NULL,"
    "  `points` tinyint NOT NULL,"
    "  `prev_rank` tinyint NOT NULL,"
    "  `record` varchar(8) NOT NULL,"
    "  PRIMARY KEY (`rank`)"
    ") ENGINE=InnoDB")
add_teamusatoday = ("INSERT INTO usatoday "
            "(team_name, points, prev_rank, record) "
            "VALUES (%s, %s, %s, %s)")
'''
# USA Today Poll Rankings
url4 = 'https://www.ncaa.com/rankings/icehockey-men/d1/usa-today/usa-hockey-magazine'
response4 = requests.get(url4)
soup4 = BeautifulSoup(response4.text, 'html.parser')
table4 = soup4.findAll('tr')
table4 = table4[1:16]
info4 = []
for t in table4:
    teaminfo = (t.get_text()).split('\n')
    teaminfo.remove('')
    teaminfo.remove('')
    teaminfo = teaminfo[1:len(teaminfo)]
    info4.append(teaminfo)
    # cursor.execute(add_teamusatoday, (teaminfo[0], teaminfo[1], teaminfo[2], teaminfo[3]))