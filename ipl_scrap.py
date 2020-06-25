dic = {
    'CSK' : 'https://www.cricbuzz.com/cricket-series/squads/3130/players/6100',
    'DC' :'https://www.cricbuzz.com/cricket-series/squads/3130/players/6109',
    'KX1P' : 'https://www.cricbuzz.com/cricket-series/squads/3130/players/6118',
    'KKR' : 'https://www.cricbuzz.com/cricket-series/squads/3130/players/6127',
    'MI' : 'https://www.cricbuzz.com/cricket-series/squads/3130/players/6136',
    'RR' : 'https://www.cricbuzz.com/cricket-series/squads/3130/players/6145',
    'RCB' : 'https://www.cricbuzz.com/cricket-series/squads/3130/players/6154',
    'SRH' : 'https://www.cricbuzz.com/cricket-series/squads/3130/players/6163'
}

import requests
import urllib
from bs4 import BeautifulSoup
import json
f = open('ipl.csv','w')
for team,b in dic.items():
    page = requests.get(b)
    soup = BeautifulSoup(page.content, 'html.parser')
    players = soup.findAll(class_='cb-col cb-col-50')
    for player in players:
        playerName = player.find(class_='cb-col cb-col-73').find(class_='cb-font-16 text-hvr-underline').string
        playerType = player.find(class_='cb-col cb-col-73').find(class_='cb-text-gray').string
        playerUrl = 'https://www.cricbuzz.com' + player['href']
        page2 = requests.get(playerUrl)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        results2 = soup2.findAll('table', class_='table cb-col-100 cb-plyr-thead')
        if len(results2) == 0:
            continue
        if playerType == 'Batsman':
            results2 = results2[0].tbody.findAll('tr')
            if len(results2) == 0:
                continue
            for results2sub in results2:
                if results2sub.findAll('td')[0].find('strong').string == 'IPL':
                    a = results2sub.findAll('td')
                    f.write(team + "," + playerName +","+ "batsmen" +"," +a[1].string+ "," +a[2].string+ "," +a[4].string+ "," +a[6].string+ "," +a[8].string+ "," +a[9].string+ "," +a[10].string+ "," +a[11].string+ "," +a[12].string+ "," +a[13].string + "\n")
                    break
        elif playerType == 'Bowler':
            results2 = results2[1].tbody.findAll('tr')
            if len(results2) == 0:
                continue
            for results2sub in results2:
                if results2sub.findAll('td')[0].find('strong').string == 'IPL':
                    a = results2sub.findAll('td')
                    f.write( team+ "," + playerName +","+ "bowler" +"," +a[1].string+ "," +a[2].string+ "," +a[5].string+ "," +a[8].string+ "," +a[9].string+ "," +a[10].string+ "," +a[11].string+ "," +a[12].string+ "\n")
                    break
        elif playerType == 'WK-Batsman':
            results2 = results2[0].tbody.findAll('tr')
            if len(results2) == 0:
                continue
            for results2sub in results2:
                if results2sub.findAll('td')[0].find('strong').string == 'IPL':
                    a = results2sub.findAll('td')
                    f.write(team + "," + playerName +","+ "wicketkeeper" +"," +a[1].string+ "," +a[2].string+ "," +a[4].string+ "," +a[6].string+ "," +a[8].string+ "," +a[9].string+ "," +a[10].string+ "," +a[11].string+ "," +a[12].string+ "," +a[13].string + "\n")
                    break
        else:
            bat = results2[0].tbody.findAll('tr')
            if len(bat) == 0:
                continue
            bowl = results2[1].tbody.findAll('tr')
            if len(bowl) == 0:
                continue
            data = ''
            for ite in bat:
                if ite.findAll('td')[0].find('strong').string == 'IPL':
                    a = ite.findAll('td')
                    data = team + "," + playerName +","+ "allrounder" +"," +a[1].string+ "," +a[2].string+ "," +a[4].string+ "," +a[6].string+ "," +a[8].string+ "," +a[9].string+ "," +a[10].string+ "," +a[11].string+ "," +a[12].string+ "," +a[13].string 
                    break
            for ite in bowl:
                if ite.findAll('td')[0].find('strong').string == 'IPL':
                    a = ite.findAll('td')
                    data = data + "," +a[2].string+ "," +a[5].string+ "," +a[8].string+ "," +a[9].string+ "," +a[10].string+ "," +a[11].string+ "," +a[12].string+ "\n"
                    break
            f.write(data)
f.close()