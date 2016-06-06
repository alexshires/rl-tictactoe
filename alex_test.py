from tictactoe import Agent, play, Human
from tictactoe import PLAYER_X, PLAYER_O, DRAW
import csv
import ipdb


def man_vs_machine():
    print "Playing against the computer"
    number_of_games = 10
    f = open('test_results.csv', 'wb')
    writer = csv.writer(f)    
    series = ['P1-Win','P2-Win','Draw']
    p2 = Agent(1, lossval = -1)
    p2.verbose = True
    p1 = Human(1)
    writer.writerow(series)
    for i in range(number_of_games):
        probs = [0,0,0]
        winner = play(p1,p2)
        p2.episode_over(winner)
        p2.episode_over(winner)
        if winner == PLAYER_X:
            probs[0] += 1
        if winner == PLAYER_O:
            probs[1] += 1
        if winner == DRAW:
            probs[2] += 1
        writer.writerow(probs)
        #write out results
    f.close()

def machine_vs_machine():
    print "Playing random against the computer"
    number_of_games = 10000
    f = open('comp_results.csv', 'wb')
    writer = csv.writer(f)    
    series = ['P1-Win','P2-Win','Draw']
    p2 = Agent(1, lossval = -1)
    p2.verbose = False
    p1 = Agent(2, learning=False)
    writer.writerow(series)
    for i in range(number_of_games):
        probs = [0,0,0]
        winner = play(p1,p2)
        p2.episode_over(winner)
        p2.episode_over(winner)
        if winner == PLAYER_X:
            probs[0] += 1
        if winner == PLAYER_O:
            probs[1] += 1
        if winner == DRAW:
            probs[2] += 1
        writer.writerow(probs)
        #write out results
    f.close()

if __name__=='__main__':
    machine_vs_machine()
