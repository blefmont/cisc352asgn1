"""
CISC352 Assignment 1
Group 2
Febuary 15th 2019
Authors:
Michael Olson    20008033
Brandon Christof 20014247
"""
import random
  
## This is the chess board. The chess board should manage
##      the queens, and keep track of positons and conflicts
class Board():
    def __init__(self, n):
        self.n = n
        ## 2D matrix of 0 if no queen and instance in queen's position
        ## List of queen instances.
        self.queens = []
        
        ## List of queens that currently have at least one conflict
        self.conflicts = []
        self.rowConflicts = [0] * n
        self.leftDiag = [0] * ((2 * n) - 1)
        self.rightDiag = [0] * ((2 * n) - 1)

    ## If self.queens is empty, create queens
    ## randomize the postions, with one queen per row
    
    def setQueens(self):

        col = list(range(self.n))
        notSet = []
        
        for i in range(self.n):
            ql = len(self.queens)
            test = col.pop(0)
            columnConflict = self.rowConflicts[test] + self.rightDiag[ql + test] + self.leftDiag[self.n + test - ql - 1]
            if columnConflict == 0:
                self.queens.append(test)
                self.rowConflicts[test] += 1
                self.leftDiag[self.n + test - ql - 1] += 1
                self.rightDiag[test + ql] += 1
            else:
                notSet.append(test)
                
        ns = len(notSet)
        
        if ns > 0:
            idx = len(self.queens)
            for k in range(ns):
                self.queens.append(notSet[k])
                self.rowConflicts[notSet[k]] += 1
                self.leftDiag[self.n + notSet[k] - idx - 1] += 1
                self.rightDiag[notSet[k] + idx] += 1
                idx+=1


    def getConflicts(self):
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

## Main min conflicts algoritm, see assignment for algorithm.
##      return solution, or None if no solution is found.
def minConflicts(csp, maxSteps):
    for i in range(maxSteps):
        m = csp.getConflicts()
        if (m == -1):
            return csp.queens

        findLeastconflicts(csp, m)

    return None   

## Should convert an instance of Board to a list of queen positions
## ex. return [2,0,1,4]
def convertBoard(board):
    positions = []
    for q in board.queens:
        positions.append(i.y)
    return positions
    
def findLeastconflicts(csp, idx):

    yPos = csp.queens[idx]
    
    csp.rowConflicts[yPos] -=1
    csp.leftDiag[csp.n + yPos - idx - 1] -=1
    csp.rightDiag[yPos + idx] -=1
    
    numConflicts = csp.n
    bestPos = []
    
    for i in range(csp.n):
        c = csp.rowConflicts[i] + csp.rightDiag[i + idx] + csp.leftDiag[csp.n + i - idx - 1]
        if c == 0:
            csp.queens[idx] = i
            csp.rowConflicts[i] +=1
            csp.leftDiag[csp.n + i - idx - 1] +=1
            csp.rightDiag[i + idx] +=1
            return i
        if c < numConflicts:
            numConflicts = c
            bestPos = [i]
        elif c == numConflicts:
            bestPos.append(i)

    pos = random.choice(bestPos)

    csp.queens[idx] = pos 
    csp.rowConflicts[pos] +=1
    csp.leftDiag[csp.n + pos - idx - 1] +=1
    csp.rightDiag[pos + idx] +=1


## Should read in "nqueens.txt" and return list of problems to solve
def inputFile(fileName):
    with open(fileName) as f:
        content = f.readlines()
    return [int(x.strip()) for x in content] 

## Outputs found solutions to "nqueens_out.txt"
def outputFile(fileName, solutions):
    with open(fileName, 'w') as f:
        for item in solutions:
            f.write("%s\n" % item)
        

def runAlgorithm(n):
    solution = None
    while(solution == None):
        csp = Board(n)
        csp.setQueens()
        solution = minConflicts(csp, 75)
    return solution

## problems is the list of n size solutions we must find
problems = []
## solutions is a list of lists, where each element is
##      a matrix of positons as shown in assignment
solutions = []

problems = inputFile("nqueens.txt")
input("Start:")
for i in problems:
    solutions.append(runAlgorithm(i))
print("Done")
outputFile("nqueens_output.txt", solutions)

