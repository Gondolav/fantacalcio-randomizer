import random
import xlrd
from pprint import pprint

workbook = xlrd.open_workbook('Quotazioni_Fantacalcio.xlsx')

goalkeepers_sheet = workbook.sheet_by_name('Portieri')
defenders_sheet = workbook.sheet_by_name('Difensori')
midfielders_sheet = workbook.sheet_by_name('Centrocampisti')
forwards_sheet = workbook.sheet_by_name('Attaccanti')

def extract_players(sheet):
    names = [value.value for value in sheet.col(2)[2:]]
    teams = [value.value for value in sheet.col(3)[2:]]

    return list(zip(names, teams))

class FantaTeam:
    """TODO"""

    def __init__(self, name, goalkeepers, defenders, midfielders, forwards):
        self.name = name
        self.goalkeepers = random.sample(goalkeepers, k=3)
        self.defenders = random.sample(defenders, k=8)
        self.midfielders = random.sample(midfielders, k=8)
        self.forwards = random.sample(forwards, k=6)

    def __repr__(self):
        return "Nome squadra: {self.name}\n\nPortieri:\n{self.goalkeepers}\n\nDifensori:\n{self.defenders}\n\nCentrocampisti:\n{self.midfielders}\n\nAttaccanti:\n{self.forwards}".format(self=self)

def draw_teams(n_teams, teams_names):
    goalkeepers = extract_players(goalkeepers_sheet)
    defenders = extract_players(defenders_sheet)
    midfielders = extract_players(midfielders_sheet)
    forwards = extract_players(forwards_sheet)

    teams = []

    for i in range(n_teams):
        file = open("Squadra" + str(i+1) + ".txt", "w+")
        team = FantaTeam(teams_names[i], goalkeepers, defenders, midfielders, forwards)
        teams.append(team)
        file.write(str(team))
        file.close()
        goalkeepers = [i for i in goalkeepers if i not in team.goalkeepers]
        defenders = [i for i in defenders if i not in team.defenders]
        midfielders = [i for i in midfielders if i not in team.midfielders]
        forwards = [i for i in forwards if i not in team.forwards]


draw_teams(4, ["Squadra 1", "Squadra 2", "Squadra 3", "Squadra 4"])
