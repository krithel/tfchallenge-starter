from models.roundState import PlayerRoundState
from models.gameState import PlayerGameState

# Bot that plays it's WAR cards in ascending order, but rotates which card it starts at each round
# e.g. First round 1,2,3,4 ; Second round 2,3,4,1 ; Third round 3,4,2,1

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

    lastPlayedCard = None

    if (len(currentRoundState.myPlayedCards) == 0):
        # We've not played any cards this round yet, so check our historic games instead
        numPreviousRounds = len(historicGameState.myHistory)

        # Check we've played previous rounds
        if numPreviousRounds != 0:

            # Get the last round played, and the first card we played that round
            lastRoundPlayedCards = historicGameState.myHistory[-1]
            firstCardLastRound = lastRoundPlayedCards[0]

            # Get the index of that card in the startingHand
            indexOfFirstCard = currentRoundState.startingHand.index(firstCardLastRound)

            # Increment that index, and check that it's still valid
            newIndex = indexOfFirstCard + 1
            if newIndex >= len(currentRoundState.startingHand):
                newIndex = 0

            return newIndex

        else:
            # We've never played a card, so return the first one in the hand
            return 0

    else:

        # Otherwise, get the last card we played this round
        lastPlayedCard = currentRoundState.myPlayedCards[-1]

        # Get the next card in the sequence, using the startingHand as our reference
        lastPlayedCardIndex = currentRoundState.startingHand.index(lastPlayedCard)
        nextCardInSequenceIndex = lastPlayedCardIndex + 1

        if nextCardInSequenceIndex >= len(currentRoundState.startingHand):
            nextCardInSequenceIndex = 0

        nextCardInSequence = currentRoundState.startingHand[nextCardInSequenceIndex]

        # Get the index of the next card in our available cards and return it
        return availableCards.index(nextCardInSequence)