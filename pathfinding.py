#Main class for CISC 352 Assignment 2
#Connor Way, 10192779
#Niyousha Saeidi, 20009546
#Jiaao Chen, 20004410
#Michael Olson, 20008033

import sys
import queue as q
import math

#grid class to hold array containing the char characters which make up the maze
class gridA2:
    wall = 'X'
    start = 'S'
    goal = 'G'
    pathChar = 'P'
    startX = 0
    startY = 0
    goalX = 0
    goalY = 0
    def __init__(self, originalArray):
        self.originalArray = originalArray
        self.greedyArray = originalArray
        self.astarArray = originalArray
        for x in range(len(originalArray)):
            for y in  range(len(originalArray[x])):
                if originalArray[x][y] == 'S':
                    self.startX = x
                    self.startY = y
                if originalArray[x][y] == 'G':
                    self.goalX = x
                    self.goalY = y
    def neighbours2D(self, x, y):
        nList = []
        if self.originalArray[x-1][y] != 'X':
            nList.append([x-1,y])
        if self.originalArray[x+1][y] != 'X':
            nList.append([x+1,y])
        if self.originalArray[x][y-1] != 'X':
            nList.append([x,y-1])
        if self.originalArray[x][y+1] != 'X':
            nList.append([x,y+1])
        return nList
    
    def neighbours3D(self, x, y):
        nList = []
        if self.originalArray[x-1][y] != 'X':
            nList.append([x-1,y])
        if self.originalArray[x-1][y-1] != 'X':
            nList.append([x-1,y-1])
        if self.originalArray[x][y-1] != 'X':
            nList.append([x,y-1])
        if self.originalArray[x+1][y-1] != 'X':
            nList.append([x+1,y-1])
        if self.originalArray[x+1][y] != 'X':
            nList.append([x+1,y])
        if self.originalArray[x+1][y+1] != 'X':
            nList.append([x+1,y+1])
        if self.originalArray[x][y+1] != 'X':
            nList.append([x,y+1])
        if self.originalArray[x-1][y+1] != 'X':
            nList.append([x-1,y+1])
        return nList

def heuristicM(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def heuristicC(a, b):
    return max(abs(b[0]-a[0]),abs(b[1]-a[1]))
#from a given input file, makes an array of gridA2 objects for each grid in the file       
#looped to do part a) and then part b) respectively
for part in ['a','b']:
    if part == 'a':
        inputFile = "pathfinding_a.txt"
        outputFile = "pathfinding_a_output.txt"
    else:
        inputFile = "pathfinding_b.txt"
        outputFile = "pathfinding_b_output.txt"
    minWidth = 8
    minDepth = 8
    inputArray = []
    for x in range(0,minDepth):
        inputArray.append([])
    i = 0
    j = 0
    gridList = []
    with open(inputFile) as f:
        for line in f:
            if line == '\n':
                gridList.append(gridA2(inputArray))
                inputArray.clear()
                for x in range(0,minDepth):
                    inputArray.append([])
            line = line.rstrip()
            if i >= minDepth:
                inputArray.append([])
            for x in line:
                if x != '\n':
                    inputArray[i].append(x)
            i = i+1
    gridList.append(gridA2(inputArray))
    f.close()
    print("done input for part "+ part)
          
    #for each grid from the input file performs the operations for Greedy and A*
    #outputs new grids to a target output file

    for g in gridList:
        print("started greedy search on grid")
        with open(outputFile, 'w') as f:

            ###################
            ## GREEDY SEARCH ##
            ###################
            frontier = q.PriorityQueue()
            frontier.put((0, [g.startX,g.startY]))
            came_from = dict()
            ### came from is a dictionary. Since you can't hash a list, we conver
            ###     to string
            came_from[str([g.startX,g.startY])] = None
            while not frontier.empty():
                current = frontier.get()[1]
                print("current: " + str(current))
                if current == [g.goalX,g.goalY]:
                    print("got to goal")
                    break
                if part == 'a':
                    for neighbor in g.neighbours2D(current[0],current[1]):
                        if str(neighbor) not in came_from.keys():
                            priority = heuristicM([g.goalX,g.goalY], neighbor)
                            frontier.put((priority, neighbor))
                            came_from[str(neighbor)] = current
                else:
                    for neighbor in g.neighbours3D(current[0],current[1]):
                        if str(neighbor) not in came_from.keys():
                            priority = heuristicC([g.goalX,g.goalY], neighbor)
                            frontier.put((priority, neighbor))
                            came_from[str(neighbor)] = current

            
            ###### Retrack greedy search path
            current = [g.goalX, g.goalY]
            pathList = [current]
            i = 1
            while current != [g.startX,g.startY]:
                current = came_from[str(current)]
                pathList.append(current)
                i = i+1
            pathList.reverse()
            
            #marks the path found with the char 'P'
            for i in range(len(g.greedyArray)):
                for j in range(len(g.greedyArray[i])):
                    if ([i,j] in pathList and not g.greedyArray[i][j] in ['S','G']):
                        g.greedyArray[i][j] = 'P'
                        
            #prints puzzle with path to output file           
            f.write("Greedy\n")
            for i in g.greedyArray:
                for j in i:
                    f.write(j)
                f.write('\n')

            ###################
            ##   A* SEARCH   ##
            ###################
            start = [g.startX,g.startY]
            goal = [g.goalX,g.goalY]
            frontier = q.PriorityQueue()
            frontier.put((0, start))
            came_from = dict()
            cost_so_far = dict()
            came_from[str(start)] = None
            cost_so_far[str(start)] = 0

            while not frontier.empty():
                current = frontier.get()[1]
                print("Current: " + str(current))

                if current == goal:
                    break

                if part == 'a':
                    
                    for neighbor in g.neighbours2D(current[0], current[1]):
                        new_cost = cost_so_far[str(current)] + g.cost(str(current), neighbor)
                        if (str(neighbor) not in cost_so_far.keys()) or new_cost < cost_so_far[str(neighbor)]:
                            cost_so_far[str(neighbor)] = new_cost
                            priority = new_cost + heuristicM(goal, neighbor)
                            frontier.put((priority, neighbor))
                            came_from[str(neighbor)] = current
                            
                elif part == 'b':
                    
                   for neighbor in g.neighbours3D(current[0], current[1]):
                        new_cost = cost_so_far[str(current)] + g.cost(str(current), neighbor)
                        if (str(neighbor) not in cost_so_far.keys()) or new_cost < cost_so_far[str(neighbor)]:
                            cost_so_far[str(neighbor)] = new_cost
                            priority = new_cost + heuristicC(goal, neighbor)
                            frontier.put((priority, neighbor))
                            came_from[str(neighbor)] = current
                        
            ###### Retrack A* search path
            current = [g.goalX, g.goalY]
            pathList = [current]
            i = 1
            while current != [g.startX,g.startY]:
                current = came_from[str(current)]
                pathList.append(current)
                i = i+1
            pathList.reverse()
            
            #marks the path found with the char 'P'
            for i in range(len(g.astarArray)):
                for j in range(len(g.astarArray[i])):
                    if ([i,j] in pathList and not g.astarArray[i][j] in ['S','G']):
                        g.astarArray[i][j] = 'P'
                
            #prints puzzle with path to output file
            f.write("A*\n")
            for i in g.astarArray:
                for j in i:
                    f.write(j)
                f.write('\n')
            f.close()
            

