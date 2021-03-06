# This is a sample opponent. It can be replaced with any opponent you want.

from models.roundState import PlayerRoundState
from models.gameState import PlayerGameState

# Bot that plays it's WAR cards in ascending order
# e.g. 1, 2, 3, 4...

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
    
    # Always return the first card in the array (index 0) - this will always be the lowest card you have left
    return 0