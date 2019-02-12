from nqueens import *

def pb(csp):
    for i in range(csp.n):
        for j in range(csp.n):
            if (csp.queens[j].y != i):
                print("_", end = '\t')
            else:  print(csp.queens[j].x, end = '\t')
        print("")
def pc(csp):
    print("Conflicts:")
    for i in csp.queens:
        print("Queen " + str(i.x) + ": " + str(i.conflicts))
        
c = Board(8)
c.randomizeQueens()
pb(c)
c.checkSolution()
pc(c)
