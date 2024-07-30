from bs4 import BeautifulSoup
import requests

URL = "https://www.mlb.com/player/aaron-judge-592450"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

yearlystats = soup.find('div','player-stats-yearbyyear')
hr = int(yearlystats.find('td', class_='col-2 row-0').find('a').text)

print(hr)
