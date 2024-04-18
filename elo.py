import numpy as np
import matplotlib.pyplot as plt

def reset_stats():
    winMatrix = np.zeros((numPlayers, numPlayers))
    gamesMatrix = np.zeros((numPlayers, numPlayers))
    elo = np.ones(numPlayers) * 1500

def match(p1, p2):
    return np.argmax([np.random.normal(playerStrength[p1], width), np.random.normal(playerStrength[p2], width)])

def simulate_matches(numMatches):
    for i in range(numMatches):
        chosenPlayers = np.random.choice(numPlayers, size=2, replace=False)
        winnerIdx = match(*chosenPlayers)
        loserIdx = (winnerIdx + 1) % 2
        winner = chosenPlayers[winnerIdx]
        loser = chosenPlayers[loserIdx]
        #print(chosenPlayers, winner, loser)
        gamesMatrix[chosenPlayers[0], chosenPlayers[1]] += 1
        gamesMatrix[chosenPlayers[1], chosenPlayers[0]] += 1
        winMatrix[winner, loser] += 1
        #print('Elo before: ', elo)
        update_elo(winner, loser)
        #print('Elo after: ', elo)

def update_elo(p1, p2):
    # p1 is assumed the winner
    q1 = 10**(elo[p1]/400)
    q2 = 10**(elo[p2]/400)
    e1 = q1/(q1+q2)
    e2 = q2/(q1+q2)
    s1 = 1
    s2 = 0
    elo[p1] += elo_rate * (s1 - e1)
    elo[p2] += elo_rate * (s2 - e2)

def create_elo_plot():
    fig, ax = plt.subplots()
    ax.scatter(players, elo)
    ax.set_title('Elo Rating of Various Strength Normal Distributions in a Game of Dice')
    ax.set_xlabel('Player Strength')
    ax.set_ylabel('Elo Rating')
    fig.show()

def create_wins_plot():
    fig, ax = plt.subplots()
    ax.imshow(winMatrix, cmap='viridis')
    ax.set_title('Win Matrix of Various Strength Normal Distributions in a Game of Dice')
    ax.set_xlabel('Player')
    ax.set_ylabel('Player')
    fig.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # initiate parameters
    playerStrength = np.arange(-10, 11)
    numPlayers = len(playerStrength)
    players = np.arange(numPlayers)
    width = 3
    winMatrix = np.zeros((numPlayers, numPlayers))
    gamesMatrix = np.zeros((numPlayers, numPlayers))
    elo = np.ones(numPlayers) * 1500
    elo_rate = 16

    # run simulations
    simulate_matches(10000)
    print(elo)
    create_wins_plot()
    create_elo_plot()

