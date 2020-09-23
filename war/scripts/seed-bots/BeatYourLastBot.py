from models.roundState import PlayerRoundState
from models.gameState import PlayerGameState

# Bot that plays it's WAR cards by picking the last card you played and playing a card to beat it
# e.g. Opponent has played a 2; This will play 3

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

    # Get the last card my opponent played (if they've played a card) and find a card to beat it
    if len(currentRoundState.oppPlayedCards) > 0:
        oppLastCard = currentRoundState.oppPlayedCards[-1]

        # By default; we'll play our lowest card - this is incase we know we can't win
        indexToPlay = 0

        # Loop through all of our available cards
        for card in availableCards:

            if card < oppLastCard:
                # Our card can't beat the opponents; continue looking
                continue
            elif card == oppLastCard:
                # Our card can draw with the opponent; which is better than playing our lowest - store but keep looking
                indexToPlay = availableCards.index(card)
                continue
            elif card > oppLastCard:
                # We've found a card that will beat the opponent; don't look at any higher cards
                indexToPlay = availableCards.index(card)
                break

        return indexToPlay

    else:
        # Otherwise they haven't played one, so go big or go home!
        return len(availableCards)-1
