
import matplotlib.pyplot as plt
from football_players_exploration import *

def iteratePlayers(position='FW'):
    caps = []
    goals = []
    exploration = FootballPlayersExploration('football_players_exploration.db')
    rows = exploration.session.query(Player).filter(Player.position==position).all()
    for row in rows:
        caps.append(row.caps)
        goals.append(row.goals)
    
    return caps, goals
    
def go():
    caps, goals = iteratePlayers()
    plt.scatter(caps, goals)
    plt.show()
    
if __name__ == '__main__':
    go()

