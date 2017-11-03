from bs4 import BeautifulSoup
import requests
import pandas as pd
def getPlayerStats(url,years):
    #funcao para recuperar dados danba na web
    getUrl = url + str("year=") + str(years)
    response = requests.get(getUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))[0]
    team = []
    player = []
    #loop para adicionar o campo team
    for j in df['Player']:
        j = j.split('(')
        player.append(j[0])
        team.append(j[1])
    team = pd.Series(team).str.replace(')', '')
    df['Player'] = player
    df['Team'] = team
    df['Year']= years
    return df

def getHist(dfIn,time):
    #funcao para fazer a carga dos dados historicos
    for getData in range(len(time)):
        temp = getPlayerStats(myUrl,time[getData]) 
        dfIn = dfIn.append(temp, ignore_index=True) 
    return dfIn
    
# myUrl = 'https://www.fantasypros.com/nba/stats/overall.php'

