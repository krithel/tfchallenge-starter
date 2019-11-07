import random

# Bot that reads the opponent's last move and plays the counter to it.

def chooseMove(myMoves, opponentMoves):
    
    if not opponentMoves:
        choice = random.choice(["R","P","S"])
        return choice
    else:
        oppchoice = opponentMoves[-1]
        if oppchoice == "R":
            return "P"
        elif oppchoice == "P":
            return "S"
        elif oppchoice == "S":
            return "R"
        else:
            choice = random.choice(["R","P","S"])
            return choice