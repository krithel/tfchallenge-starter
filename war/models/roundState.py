import json

# RoundState
# Defines the state of a single Round of War and generates player specific views of it
class RoundState:

    def __init__(self, startingCards):

        self.p1Wins = 0
        self.p2Wins = 0
        self.draws = 0

        self.startingHand = startingCards.copy()

        # Each player starts with a full hand of cards
        self.p1CardsInHand = self.startingHand.copy()
        self.p2CardsInHand = self.startingHand.copy()

        self.p1PlayedCards = []
        self.p2PlayedCards = []

    def __str__(self):
        return json.dumps(self.__dict__)

    def generateStateP1(self):

        p1State = PlayerRoundState(self.startingHand)
        p1State.myPlayedCards = self.p1PlayedCards
        p1State.oppPlayedCards = self.p2PlayedCards

        return p1State

    def generateStateP2(self):

        p2State = PlayerRoundState(self.startingHand)
        p2State.myPlayedCards = self.p2PlayedCards
        p2State.oppPlayedCards = self.p1PlayedCards

        return p2State

# PlayerRoundState
# Defines a player specific view of the current round of War
class PlayerRoundState:

    def __init__(self, startingCards):
        self.startingHand = startingCards.copy()
        self.myPlayedCards = []
        self.oppPlayedCards = []

    def __str__(self):
        return json.dumps(self.__dict__)