import requests
import urllib
from bs4 import BeautifulSoup
import json

def is_json(myjson):
    try:
        response.json()
        json.loads(response.text)
    except ValueError as e:
        return False
    if response.json() == None:
        return False
    return True

countryDic = {
    'IND' : 'india',
    'QAT' : 'qatar',
    'ENG' : 'england',
    'IRE' : 'ireland',
    'NZ' : 'New Zealand',
    'SL' : 'sri lanka',
    'AFG' : 'Afghanistan',
    'NEP' : 'nepal',
    'CAN' : 'canada',
    'AUS' : 'australia',
    'OMA' : 'oman',
    'ZIM' : 'zimbabwe',
    'SCO' : 'scotland',
    'NAM' : 'namibia',
    'WI' : 'west indies',
    'UAE' : 'United Arab Emirates',
    'SA' : 'south africa',
    'KEN' : 'kenya',
    'BAN' : 'bangladesh',
    'HK' : 'hong kong',
    'SIN' : 'singapore',
    'PNG' : 'Papua New Guinea',
    'NED' : 'Netherlands',
    'PAK' : 'pakistan',
    'BRM' : 'Bermuda'
}

#Code to scrap batsmen data
f = open('batsmen.csv','w')
URL = 'https://www.icc-cricket.com/rankings/mens/player-rankings/t20i/batting'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.findChildren(class_='table-body')
for result in results:
    val1 = result.findChildren(class_='table-body__cell rankings-table__name name')
    val2 = result.findChildren(class_='table-body__cell rating')
    val3 = result.findChildren(class_='table-body__logo-text')
    param = {'q': val1[0].find('a').string}
    URL1 = 'https://www.cricbuzz.com/api/search/results?' + urllib.parse.urlencode(param)
    response = requests.get(URL1)
    if is_json(response) == False:
        continue
    if 'playerList' in response.json():
        pass
    else:
        continue
    for player in response.json()['playerList']:
        if player['country'].lower() == countryDic[val3[0].string].lower():
            URL2 = 'https://www.cricbuzz.com/profiles/' + str(player["id"]) + '/' + player["title"].replace(" ", "-").lower()
            page2 = requests.get(URL2)
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
                    f.write(val2[0].string+ "," +a[1].string+ "," +a[2].string+ "," +a[4].string+ "," +a[6].string+ "," +a[8].string+ "," +a[9].string+ "," +a[10].string+ "," +a[11].string+ "," +a[12].string+ "," +a[13].string + "\n")
            break
f.close()




#Code to scrap bolwer data
f = open('bowler.csv','w')
URL = 'https://www.icc-cricket.com/rankings/mens/player-rankings/t20i/bowling'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.findChildren(class_='table-body')
for result in results:
    val1 = result.findChildren(class_='table-body__cell rankings-table__name name')
    val2 = result.findChildren(class_='table-body__cell rating')
    val3 = result.findChildren(class_='table-body__logo-text')
    param = {'q': val1[0].find('a').string}
    URL1 = 'https://www.cricbuzz.com/api/search/results?' + urllib.parse.urlencode(param)
    response = requests.get(URL1)
    if is_json(response) == False:
        continue
    if 'playerList' in response.json():
        pass
    else:
        continue
    for player in response.json()['playerList']:
        if player['country'].lower() == countryDic[val3[0].string].lower():
            URL2 = 'https://www.cricbuzz.com/profiles/' + str(player["id"]) + '/' + player["title"].replace(" ", "-").lower()
            page2 = requests.get(URL2)
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
                    f.write(val2[0].string+ "," +a[1].string+ "," +a[2].string+ "," +a[5].string+ "," +a[8].string+ "," +a[9].string+ "," +a[10].string+ "," +a[11].string+ "," +a[12].string+ "\n")
            break
f.close()




#Code to scrap allrounder data
f = open('allrounder.csv','w')
URL = 'https://www.icc-cricket.com/rankings/mens/player-rankings/t20i/all-rounder'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.findChildren(class_='table-body')
for result in results:
    val1 = result.findChildren(class_='table-body__cell rankings-table__name name')
    val2 = result.findChildren(class_='table-body__cell rating')
    val3 = result.findChildren(class_='table-body__logo-text')
    param = {'q': val1[0].find('a').string}
    URL1 = 'https://www.cricbuzz.com/api/search/results?' + urllib.parse.urlencode(param)
    response = requests.get(URL1)
    if is_json(response) == False:
        continue
    if 'playerList' in response.json():
        pass
    else:
        continue
    for player in response.json()['playerList']:
        if player['country'].lower() == countryDic[val3[0].string].lower():
            URL2 = 'https://www.cricbuzz.com/profiles/' + str(player["id"]) + '/' + player["title"].replace(" ", "-").lower()
            page2 = requests.get(URL2)
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
                    data = val2[0].string+ "," +a[1].string+ "," +a[2].string+ "," +a[4].string+ "," +a[6].string+ "," +a[8].string+ "," +a[9].string+ "," +a[10].string+ "," +a[11].string+ "," +a[12].string+ "," +a[13].string
                    break
            for ite in bowl:
                if ite.findAll('td')[0].find('strong').string == 'T20I':
                    a = ite.findAll('td')
                    data = data + "," +a[2].string+ "," +a[5].string+ "," +a[8].string+ "," +a[9].string+ "," +a[10].string+ "," +a[11].string+ "," +a[12].string+ "\n"
                    break
            f.write(data)
            break
f.close()