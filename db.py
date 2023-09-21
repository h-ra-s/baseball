import csv

FILENAME = "players.csv"

def write_players(lineup): #the name of the list
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(lineup)
        
def read_players():
    lineup = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            lineup.append(row)
    return lineup
