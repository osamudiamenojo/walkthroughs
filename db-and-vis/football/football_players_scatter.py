
import matplotlib.pyplot as pyplot
from football_players_exploration import *

def iteratePlayers():
    caps = []
    goals = []
    exploration = FootballPlayersExploration('football_players_exploration.db')
    rows = exploration.session.query(Player).all()
    for row in rows:
        caps.append(row.caps)
        goals.append(row.goals)
    
    return caps, goals
    
def go():
    caps, goals = iteratePlayers()
    pyplot.scatter(caps, goals)
    pyplot.show()
    
if __name__ == '__main__':
    go()

