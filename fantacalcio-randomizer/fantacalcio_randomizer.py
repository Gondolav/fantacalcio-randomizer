import os.path
import random
import xlrd


def extract_players(sheet):
    return [Player(name.value, team.value) for (name, team) in zip(sheet.col(2)[2:], sheet.col(3)[2:])]


class Player:
    """TODO"""

    def __init__(self, name, team):
        names = name.split()
        last_name = names[0]
        self.name = last_name[0] + last_name[1:].lower()
        if (len(names) > 1):
            first_name = names[1]
            self.name += " " + first_name[0] + first_name[1:].lower()
        self.team = team

    def __repr__(self):
        return f"{self.name} ({self.team})"


class FantaTeam:
    """TODO"""

    def __init__(self, name, goalkeepers, defenders, midfielders, forwards):
        self.name = name
        self.goalkeepers = random.sample(goalkeepers, k=3)
        self.defenders = random.sample(defenders, k=8)
        self.midfielders = random.sample(midfielders, k=8)
        self.forwards = random.sample(forwards, k=6)

    def __repr__(self):
        slash_n = '\n'
        return f"Nome squadra: {self.name}\n\nPortieri:\n{slash_n.join(repr(g) for g in self.goalkeepers)}\n\nDifensori:\n{slash_n.join(repr(d) for d in self.defenders)}\n\nCentrocampisti:\n{slash_n.join(repr(m) for m in self.midfielders)}\n\nAttaccanti:\n{slash_n.join(repr(f) for f in self.forwards)}"


def draw_teams(filename, n_teams, teams_names):
    workbook = xlrd.open_workbook(filename)

    goalkeepers_sheet = workbook.sheet_by_name('Portieri')
    defenders_sheet = workbook.sheet_by_name('Difensori')
    midfielders_sheet = workbook.sheet_by_name('Centrocampisti')
    forwards_sheet = workbook.sheet_by_name('Attaccanti')

    goalkeepers = extract_players(goalkeepers_sheet)
    defenders = extract_players(defenders_sheet)
    midfielders = extract_players(midfielders_sheet)
    forwards = extract_players(forwards_sheet)

    for i in range(n_teams):
        with open(os.path.join(os.path.split(os.path.dirname(__file__))[0], "Squadra_" + teams_names[i] + ".txt"), "w+") as file:
            team = FantaTeam(teams_names[i], goalkeepers,
                             defenders, midfielders, forwards)
            file.write(str(team))

        goalkeepers = [i for i in goalkeepers if i not in team.goalkeepers]
        defenders = [i for i in defenders if i not in team.defenders]
        midfielders = [i for i in midfielders if i not in team.midfielders]
        forwards = [i for i in forwards if i not in team.forwards]
