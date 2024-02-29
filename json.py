import json


matches_results = [
    {"equipe1": "Équipe A", "score1": 2, "equipe2": "Équipe B", "score2": 1},
    {"equipe1": "Équipe C", "score1": 0, "equipe2": "Équipe D", "score2": 3},
    {"equipe1": "Équipe E", "score1": 1, "equipe2": "Équipe F", "score2": 1},
    
]

# Écriture des données dans un fichier JSON
with open('matches_results.json', 'w') as json_file:
    json.dump(matches_results, json_file, indent=2)

print("Le fichier JSON a été créé avec succès.")
