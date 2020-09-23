import random

#Bot that sticks with one move until it loses, then randomly shifts to another move.

def chooseMove(myMoves, opponentMoves):
    
    if not myMoves:
        #Start with a random barrier
        choice = random.choice(["R","P","S"])
        return choice
    else:
        oppchoice = opponentMoves[-1]
        mychoice = myMoves[-1]
        
        if oppchoice == "R" and mychoice == "S":
            return random.choice(["R","P"])
        elif oppchoice == "P" and mychoice == "R":
            return random.choice(["P","S"])
        elif oppchoice == "S" and mychoice == "P":
            return random.choice(["R","S"])
        else:
            return mychoice