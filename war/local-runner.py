import os
import importlib
import json

from models.gameState import GameState
from models.gameState import PlayerGameState
from models.roundState import RoundState
from models.roundState import PlayerRoundState

SCRIPT_USER = 'my-first-bot'
SCRIPT_OPP = 'opponent-bot'
ROUND_BY_ROUND_LOG = False
ROUNDS_PER_GAME = 10

STARTING_CARDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class WarRunner:
    
    def __init__(self):
        
        self.initialised = True
        self.results = {
            'p1' : 0,
            'p2' : 0,
            'draw' : 0,
            'gameSuccess' : True
        }

        self.script_dir = 'scripts'
        self.script_p1 = SCRIPT_USER
        self.script_p2 = SCRIPT_OPP

        try:
            self.playerOne = importlib.import_module('{}.{}'.format(self.script_dir, self.script_p1))
            self.playerTwo = importlib.import_module('{}.{}'.format(self.script_dir, self.script_p2))
        except Exception as e:
            self.results['gameSuccess'] = False
            self.results['error'] = str(e)
            self.initialised = False
    
    def runGame(self):
        
        gameState = GameState()

        try:
            for i in range(ROUNDS_PER_GAME):

                # Run a single round - passing in the results of the previousRounds
                roundResults = self.runRound(gameState)

                p1Wins = roundResults.p1Wins
                p2Wins = roundResults.p2Wins
                draws = roundResults.draws
                
                # Calculate who won the round and add to the results
                if p1Wins > p2Wins and p1Wins > draws :
                    self.results['p1'] +=1
                elif p2Wins > p1Wins and p2Wins > draws :
                    self.results['p2'] +=1
                else :
                    self.results['draw'] +=1

                # Update the gameState
                gameState.p1History.append(roundResults.p1PlayedCards)
                gameState.p2History.append(roundResults.p2PlayedCards)

        except Exception as e:
            self.results['gameSuccess'] = False
            self.results['error'] = str(e)

    def runRound(self, gameState):

        # Create a new RoundState for this round
        roundState = RoundState(STARTING_CARDS)

        # Generate the player specific instances of the GameState (so they can ignore p1 and p2)
        p1GameState = gameState.generateStateP1()
        p2GameState = gameState.generateStateP2()

        numMoves = len(STARTING_CARDS)
        for i in range(numMoves):

            # Player 1
            # Ask the player to pick their card and pop it off their hand
            p1RoundState = roundState.generateStateP1()
            p1Move = self.playerOne.chooseCard(roundState.p1CardsInHand, p1RoundState, p1GameState)
            p1Card = roundState.p1CardsInHand.pop(p1Move)
            roundState.p1PlayedCards.append(p1Card)

            # Player 2
            p2RoundState = roundState.generateStateP2()
            p2Move = self.playerTwo.chooseCard(roundState.p2CardsInHand, p2RoundState, p2GameState)
            p2Card = roundState.p2CardsInHand.pop(p2Move)
            roundState.p2PlayedCards.append(p2Card)

            # Get the result of the move & update the roundState
            if p1Card > p2Card :
                roundState.p1Wins += 1
            elif p2Card > p1Card :
                roundState.p2Wins += 1
            else :
                roundState.draws += 1

        if ROUND_BY_ROUND_LOG:
            print("ROUND RESULTS: ", roundState)

        return roundState

    def printResults(self):

        if (self.results['gameSuccess']):
            print("Game successfully run! Results:")
            print("Games won (out of {}): {}".format(ROUNDS_PER_GAME, self.results['p1']))
            print("Games lost (out of {}): {}".format(ROUNDS_PER_GAME, self.results['p2']))
            print("Games drawn (out of {}): {}".format(ROUNDS_PER_GAME, self.results['draw']))
            print("INFO: For more detailed information, you can set ROUND_BY_ROUND_LOG to be TRUE to see all the played cards per round")
            print("Your script is ready to be uploaded!")
        else:
            print("Game failed! Your script will not complete validation.")
            print("Error: {}".format(self.results['error']))

# Create a new instance of the GameRunner
print("RUNNING WAR RUNNER")
runner = WarRunner()

if runner.initialised:
    runner.runGame()

runner.printResults()
