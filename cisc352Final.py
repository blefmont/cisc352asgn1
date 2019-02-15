'''
    CISC 352 Assignment 1
    Date Created:  2019-02-07
    Last Modified: 2019-02-15
    Group 2
    Authors:
        Brandon Christof 20014247
        Michael Olson    20008033
'''
import random
import math
import time
from math import trunc

## Changes conflicts for each list
def changeState(csp, x, y, v):
    csp.rowConflicts[x] += v
    csp.leftDiag[csp.n + x - y - 1] += v
    csp.rightDiag[x + y] += v
  
## Manages the queens positions and conflicts
class Board():
    def __init__(self, n):

        # Size of chessboard
        self.n = n
        
        # List of queen positions
        self.queens = []
        
        # Conflicts for all right diagonals, left diagonals and rows
        self.rowConflicts = [0] * n
        self.leftDiag = [0] * ((2 * n) - 1)
        self.rightDiag = [0] * ((2 * n) - 1)


    ## Places queens on chessboard at best position using Greedy Search
    def setQueens(self, differentOrder):

        # Creates a list of [0, 1, 2... n]
        col = list(range(self.n))

        # Keeps track of queen positions not set
        notSet = []

        # If last order didn't work within step count, try this order
        if differentOrder:
            f = col.pop(0)
            col.append(f)

        # Loop to place queens, all at positions with 0 conflicts
        for i in range(self.n):
            ql = len(self.queens)
            test = col[i]
            columnConflict = self.rowConflicts[test] + self.rightDiag[ql + test] + self.leftDiag[self.n + test - ql - 1]
            if columnConflict == 0:
                self.queens.append(test)
                changeState(self, test, ql, 1)
            else:
                notSet.append(test)
                
        ns = len(notSet)
        idx = len(self.queens)

        # Places queens at the rest of the positions if needed
        if ns > 0:
            idx = len(self.queens)
            for k in range(ns):
                self.queens.append(notSet[k])
                changeState(self, notSet[k], idx, 1)
                idx+=1

    ## Returns the row with the most conflicts. If there are no conflicts, returns -1.
    ##      If there is a tie, randomly chooses
    def getMostConflicted(self):
        
        most = 1
        positions = []
        
        for i in range(self.n):
            c = self.rowConflicts[self.queens[i]] + self.rightDiag[i + self.queens[i]] + self.leftDiag[self.n + self.queens[i] - i - 1] - 3
            if c > most:
                most = c
                positions = [i]
            elif c == most:
                positions.append(i)

        if len(positions) == 0:
            return -1
        return random.choice(positions)

## Finds queen with most conflicts, and places it in best position
##      until solved or until it reaches too many attempts
def minConflicts(csp, maxSteps):
    for i in range(maxSteps):
        m = csp.getMostConflicted()
        if (m == -1):
            return csp.queens
        findLeastconflicts(csp, m)
    return -1

## Takes the queen with the most conflicts and places it at least
##      conflicted position. If there is a tie, randomly chooses
def findLeastconflicts(csp, idx):

    yPos = csp.queens[idx]
    changeState(csp, yPos, idx, -1)
    numConflicts = csp.n
    bestPos = []
    
    for i in range(csp.n):
        c = csp.rowConflicts[i] + csp.rightDiag[i + idx] + csp.leftDiag[csp.n + i - idx - 1]
        if c == 0:
            csp.queens[idx] = i
            changeState(csp, i, idx, 1)
            return i
        if c < numConflicts:
            numConflicts = c
            bestPos = [i]
        elif c == numConflicts:
            bestPos.append(i)

    pos = random.choice(bestPos)

    csp.queens[idx] = pos
    changeState(csp, pos, idx, 1)


## Reads in "nqueens.txt" and returns list of problems to solve
def inputFile(fileName):
    with open(fileName) as f:
        content = f.readlines()
    return [int(x.strip()) for x in content] 

## Outputs found solutions to "nqueens_out.txt"
def outputFile(fileName, solutions):
    with open(fileName, 'w') as f:
        for item in solutions:
            f.write("%s\n" % item)
    f.close()
        

## Makes sure n value isn't too big.
## Creates a new board and attempts to solve in less than 60 moves.
## If algorithm is unable to, tries again with a different start order.
## Returns queens list when solved
def runAlgorithm(n):
    
    csp = Board(n)
    csp.setQueens(True)
    trials = 65
    
    while minConflicts(csp, trials) == -1:
        csp = Board(n)
        csp.setQueens(False)
        trials = n
    return csp.queens

problems = []       # List of n sized problems
solutions = []      # Contains solutions for each problem

problems = inputFile("nqueens.txt")
input("Press Enter to start:")

time0 = time.time() #Starts timer

# Runs through each problem given
for i in problems:
    solutions.append(runAlgorithm(i))

# Stops timer when solved and prints time
time1 = time.time()
tot_time = time1 - time0
time_string = str(trunc(tot_time*100)/100)

print("\n   Time: " + time_string + " seconds\n")
outputFile("nqueens_output.txt", solutions)
