import random

# Bot that plays whatever would beat its own previous move.

def chooseMove(myMoves, opponentMoves):
    
    if not myMoves:
        choice = random.choice(["R","P","S"])
        return choice
    else:
        prevchoice = myMoves[-1]
        if prevchoice == "R":
            return "P"
        elif prevchoice == "P":
            return "S"
        elif prevchoice == "S":
            return "R"
        else:
            choice = random.choice(["R","P","S"])
            return choice