from nqueens import *

def printBoard(csp):
    for i in range(csp.n):
        for j in range(csp.n):
            if (csp.queens[i].y != j):
                print("_", end = '\t')
            else:  print(csp.queens[i].x, end = '\t')
        print("")
