"""
CISC352 Assignment 1
Group 2
Febuary 15th 2019
Authors:
Michael Olson    20008033

"""
import random

## An instance of this class is one queen. Attributes that a
##  queen has are positon (x,y) and number of conflits
class Queen():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.conflits = 0
    ## Use the board to check if the queen conflits
    ##      with any others. Update number and either
    ##      add or remove self to board.conflits
    def checkConflits(self, board):
        pass

        
    
## This is the chess board. The chess board should manage
##      the queens, and keep track of positons and conflits
class Board():
    def __init__(self, n):
        self.n = n
        ## 2D matrix of 0 if no queen and instance in queen's position
        self.board = [[]]
        ## List of queen instances.
        self.queens = []
        ## List of queens that currently have at least one conflict
        self.conflits = []
        print("Board init not fully implemented")
    ## Go through and initialize self.board to size n with all 0.
    def createBoard(self, n):
        pass
    ## If self.queens is empty, create queens
    ## randomize the postions, with one queen per row
    def randomizeQueens(self):
        pass
    ## Go through the list of queens, checking
    ##      how many conflits there are. Should
    ##      also update self.conflits
    def checkSolution(self):
        pass

## Main min conflits algoritm, see assignment for algorithm.
##      return solution, or None if no solution is found.
def minConflicts(csp, maxSteps):
    print("minConflits not yet implemented")

## Should read in "nqueens.txt" and fill problems[].
def inputFile(fileName, problems):
    print("inputFile not yet implemented")

## Outputs found solutions to "nqueens_out.txt"
def outputFile(fileName, solutions):
    print("outputFile not yet implemented")

def runAlgorithm(n):
    csp = Board(n)
    solution = None
    while(solution == None):
        solution = minConflicts(csp, 75)

## problems is the list of n size solutions we must find
problems = []
## solutions is a list of lists, where each element is
##      a matrix of positons as shown in assignment
solutions = []

inputFile("nqueens.txt", problems)

for i in problems:
    solutions.append(runAlgorithm(n))
    
outputFile("nqueens_output.txt", solutions)

