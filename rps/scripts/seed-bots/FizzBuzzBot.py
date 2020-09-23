import random

# Bot that plays FizzBuzz. Only three options, so returns the same for nothing and FizzBuzz results.

def chooseMove(myMoves, opponentMoves):
    
    gameRound = len(myMoves)+1
    isThree = gameRound%3
    isFive = gameRound%5
    
    if gameRound%3 > 0 and gameRound%5 >0:
        #FizzBuzz
        return 'S'
    elif gameRound%3 > 0:
        #Fizz
        return 'R'
    elif gameRound%5 > 0:
        #Buzz
        return 'P'
    else:
        #Boring.
        return 'S'