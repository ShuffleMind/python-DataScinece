from bs4 import BeautifulSoup
import requests
import pandas as pd


def getPlayerStats(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))[0]
    return df


# myUrl = 'https://www.fantasypros.com/nba/stats/overall.php'

