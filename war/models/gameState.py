import json

# GameState
# Defines the state of the whole game of War - used to capture the historic moves
class GameState:

    def __init__(self):
        
        self.p1History = []
        self.p2History = []

    def __str__(self):
        return json.dumps(self.__dict__)

    def generateStateP1(self):

        p1State = PlayerGameState()
        p1State.myHistory = self.p1History
        p1State.oppHistory = self.p2History

        return p1State

    def generateStateP2(self):

        p2State = PlayerGameState()
        p2State.myHistory = self.p2History
        p2State.oppHistory = self.p1History

        return p2State

# PlayerGameState
# Defines a player specific view of the current game of War
class PlayerGameState:

    def __init__(self):
        self.myHistory = []
        self.oppHistory = []

    def __str__(self):
        return json.dumps(self.__dict__)