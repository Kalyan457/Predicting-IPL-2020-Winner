import requests
import urllib
from bs4 import BeautifulSoup

#Code to scrap batsmen data
f = open('batsmen.csv','w')
URL = 'https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
playersDiv = soup.findAll(class_='cb-col cb-col-100 cb-padding-left0')
players = playersDiv[2].findAll(class_='cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')

for player in players:
    playerUrl = 'https://www.cricbuzz.com' + player.find(class_='text-hvr-underline text-bold cb-font-16')['href']
    playerRating = player.find(class_='cb-col cb-col-17 cb-rank-tbl pull-right').string
    page2 = requests.get(playerUrl)
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    results2 = soup2.findAll('table', class_='table cb-col-100 cb-plyr-thead')
    if len(results2) == 0:
        continue
    results2 = results2[0].tbody.findAll('tr')
    if len(results2) == 0:
        continue
    for results2sub in results2:
        if results2sub.findAll('td')[0].find('strong').string == 'T20I':
            a = results2sub.findAll('td')
            f.write(playerRating+ "," +a[1].string+ "," +a[2].string+ "," +a[4].string+ "," +a[6].string+ "," +a[8].string+ "," +a[9].string+ "," +a[10].string+ "," +a[11].string+ "," +a[12].string+ "," +a[13].string + "\n")
            break
f.close()

#Code to scrap bowling data
f = open('bowler.csv','w')
URL = 'https://www.cricbuzz.com/cricket-stats/icc-rankings/men/bowling'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
playersDiv = soup.findAll(class_='cb-col cb-col-100 cb-padding-left0')
players = playersDiv[2].findAll(class_='cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')

for player in players:
    playerUrl = 'https://www.cricbuzz.com' + player.find(class_='text-hvr-underline text-bold cb-font-16')['href']
    playerRating = player.find(class_='cb-col cb-col-17 cb-rank-tbl pull-right').string
    page2 = requests.get(playerUrl)
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    results2 = soup2.findAll('table', class_='table cb-col-100 cb-plyr-thead')
    if len(results2) == 0:
        continue
    results2 = results2[1].tbody.findAll('tr')
    if len(results2) == 0:
        continue
    for results2sub in results2:
        if results2sub.findAll('td')[0].find('strong').string == 'T20I':
            a = results2sub.findAll('td')
            f.write(playerRating+ "," +a[1].string+ "," +a[2].string+ "," +a[5].string+ "," +a[8].string+ "," +a[9].string+ "," +a[10].string+ "," +a[11].string+ "," +a[12].string+ "\n")
            break
f.close()

#Code to scrap allrounder data
f = open('allrounder.csv','w')
URL = 'https://www.cricbuzz.com/cricket-stats/icc-rankings/men/all-rounder'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
playersDiv = soup.findAll(class_='cb-col cb-col-100 cb-padding-left0')
players = playersDiv[2].findAll(class_='cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')

for player in players:
    playerUrl = 'https://www.cricbuzz.com' + player.find(class_='text-hvr-underline text-bold cb-font-16')['href']
    playerRating = player.find(class_='cb-col cb-col-17 cb-rank-tbl pull-right').string
    page2 = requests.get(playerUrl)
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    results2 = soup2.findAll('table', class_='table cb-col-100 cb-plyr-thead')
    if len(results2) == 0:
        continue
    bat = results2[0].tbody.findAll('tr')
    if len(bat) == 0:
        continue
    bowl = results2[1].tbody.findAll('tr')
    if len(bowl) == 0:
        continue
    data = ''
    for ite in bat:
        if ite.findAll('td')[0].find('strong').string == 'T20I':
            a = ite.findAll('td')
            data = playerRating+ "," +a[1].string+ "," +a[2].string+ "," +a[4].string+ "," +a[6].string+ "," +a[8].string+ "," +a[9].string+ "," +a[10].string+ "," +a[11].string+ "," +a[12].string+ "," +a[13].string
            break
    for ite in bowl:
        if ite.findAll('td')[0].find('strong').string == 'T20I':
            a = ite.findAll('td')
            data = data + "," +a[2].string+ "," +a[5].string+ "," +a[8].string+ "," +a[9].string+ "," +a[10].string+ "," +a[11].string+ "," +a[12].string+ "\n"
            break
    f.write(data)
f.close()