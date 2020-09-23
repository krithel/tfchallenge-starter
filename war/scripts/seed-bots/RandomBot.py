from models.roundState import PlayerRoundState
from models.gameState import PlayerGameState
import random

# Bot that plays it's WAR cards randomly order
# e.g. 4, 1, 3, 2...

# chooseCard - chooses the bot's next card to play
#   returns - INDEX of the availableCards to play (0 to len(availableCards)-1)
#   availableCards - array of cards currently in your hand to play, in ascending order e.g. [1,2,3,4,5]
#   currentRoundState - PlayerRoundState object containing:
#       startingHand - array of all the cards that comprise a starting hand
#       myPlayedCards - array of cards previously played, in played order
#       oppPlayedCards - array of cards previously played by opponent, in played order
#   historicGameState - PlayerGameState object containing:
#        myHistory - array previous rounds, containing the cards played in that round in order
#        oppHistory - - array previous rounds, containing the cards played in that round in order
def chooseCard(availableCards, currentRoundState: PlayerRoundState, historicGameState: PlayerGameState):
    
    # Choose a random index between 0 and length -1 from availableCards    
    myMove = random.randint(0, len(availableCards)-1)

    return myMove