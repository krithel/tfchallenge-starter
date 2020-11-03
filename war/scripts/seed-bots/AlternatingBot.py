from models.roundState import PlayerRoundState
from models.gameState import PlayerGameState

# Bot that plays it's WAR cards in an alternating High/Low order
# e.g. 1, 4, 2, 3...

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

    if (len(currentRoundState.myPlayedCards) == 0):
        # Always play your lowest card first
        return 0
    else:
        # Get the value of our last played card - this is the last element in the myPlayedCards list
        lastPlayedCard = currentRoundState.myPlayedCards[-1]

        # Get the index of the last played card from our starting Hand - that way we know if we played a HIGH card or a LOW card
        indexOfLastCard = currentRoundState.startingHand.index(lastPlayedCard)
        middleIndex = len(currentRoundState.startingHand)/2

        #if last card played was higher than the middle index, it was a high card, so the next card we play is a low one
        if (indexOfLastCard > middleIndex):
            return 0
        #...else it was a low card, so the next card we play is a high one
        else:
            return len(availableCards)-1
