from bs4 import BeautifulSoup
import requests

URL = "https://www.mlb.com/player/aaron-judge-592450"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

yearlystats = soup.find('div','player-stats-yearbyyear')
hr = int(yearlystats.find('td', class_='col-2 row-0').find('a').text)

soup = BeautifulSoup(requests.get("https://www.mlb.com/yankees/stats/team").content, 'html.parser')

table = soup.find('div', class_='stats-body-table team')
rows = table.find('tbody', class_='notranslate').find_all('tr')

gms = 1

for row in rows:
    if row.find('a', {'aria-label': 'New York Yankees'}):
        gms = int(row.find_all('td')[1].text)

print("Aaron Judge is on pace to hit", hr * 162 / gms, "home runs over a 162 game season")