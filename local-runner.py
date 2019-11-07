import os
import importlib
import json

BASE_USER_SCRIPT = 'my-first-bot'
BASE_OPPONENT_SCRIPT = 'opponent-bot'

ROUNDS = 1000

# Map winning to losing moves
moveMap = {
    'R': 'S',
    'P': 'R',
    'S': 'P'
}

class GameRunner:
    
    def __init__(self):
        self.initialised = True
        self.results = {
            'p1' : 0,
            'p2' : 0,
            'draw' : 0,
            'gameSuccess' : True
        }

        self.script_dir = "scripts"

        try:
            self.playerOne = importlib.import_module('{}.{}'.format(self.script_dir, BASE_USER_SCRIPT))
            self.playerTwo = importlib.import_module('{}.{}'.format(self.script_dir, BASE_OPPONENT_SCRIPT))
        except Exception as e:
            self.results['gameSuccess'] = False
            self.results['error'] = str(e)
            self.initialised = False
            # print("ERROR:", e)
    
    def runRound(self):
        p1History = []
        p2History = []
        try:
            for i in range(ROUNDS):
            
                p1Move = self.playerOne.chooseMove(p1History, p2History)
                p2Move = self.playerTwo.chooseMove(p2History, p1History)

                p1History.append(p1Move)
                p2History.append(p2Move)

                if moveMap[p1Move] == p2Move:   # If p1 has defeated p2
                    self.results['p1'] += 1
                elif moveMap[p2Move] == p1Move: # If p2 has defeated p1
                    self.results['p2'] += 1
                elif p1Move == p2Move:          # If there is a tie
                    self.results['draw'] += 1
                else:
                    # raise "Invalid state on winner check" # Either p1 or p2 made an invalid move (such as Spock)
                    self.results['gameSuccess'] = False
        except Exception as e:
            self.results['gameSuccess'] = False
            self.results['error'] = str(e)
            # print("ERROR:", e)
        
        # print('results:', self.results)
        
    def printResults(self):
        if (self.results['gameSuccess']):
            print("Game successfully run! Results:")
            print("Games won (out of 1000): {}".format(self.results['p1']))
            print("Games lost (out of 1000): {}".format(self.results['p2']))
            print("Games drawn (out of 1000): {}".format(self.results['draw']))
            print("Your script is ready to be uploaded!")
        else:
            print("Game failed. Your script will not complete validation.")
            print("Error: {}".format(self.results['error']))

runner = GameRunner()
if runner.initialised:
    runner.runRound()    #this works now.
runner.printResults()
