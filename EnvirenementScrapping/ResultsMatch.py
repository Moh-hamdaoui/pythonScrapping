import requests
from bs4 import BeautifulSoup
import json

def getMatchsResults(url, output_file):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        match_results_block = soup.find_all('section', class_='gameModules')
        i = 0
        DataMatches = []
        for e in match_results_block:
            Squade = e.find_all('div', class_=['ScoreCell__TeamName', 'ScoreCell__Score'])
            for i in range (0, len(Squade)-3, 4) :
                match_data = {
                    "equipe1": Squade[i].text,
                    "score1": Squade[i+1].text,
                    "equipe2": Squade[i+2].text,
                    "score2": Squade[i+3].text
                    }
                DataMatches.append(match_data)
                print(DataMatches)
        with open(output_file, 'w') as json_file:
            json.dump(DataMatches, json_file, indent=2)
        print(f"Les résultats des matches ont été stockés dans {output_file}")
    else:
        print(f"Erreur de requête. Code de statut : {response.status_code}")


URL = 'https://www.espn.co.uk/football/scoreboard/_/date/'

date_input = input("Veuillez entrer la date (au format AAAAMMJJ) : ")

URL += date_input

getMatchsResults(URL, './matches_results.json')