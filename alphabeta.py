'''
Alpha-Beta Pruning
Authors: Michael Olson    20008033
       : Brandon Christof 20014247

    This program implements a minimax search algorithm that will determine
    a score for any given state of a game. The search method uses Alpha-Beta
    pruning to cut off any redudant searches to give a faster and
    more efficient solution.

'''

## Global counter variable, counts the leaf nodes examined
counter = 0

## Node object, these are tree objects that have no value,
##      can have children and can be root node
class Node():
    ## Constructor. Must be either MAX or MIN, can be a root and key is for debugging
    def __init__(self, maxOrMin, isRoot = False, key = ""):
        
        if (maxOrMin == "MAX"):
            self.isMax = True
        elif (maxOrMin == "MIN"):
            self.isMax = False
        else: raise ValueError('maxOrMin must be "MAX" or "MIN"')
        
        self.isRoot = isRoot
        self.key = key
        self.children = []

    ## All tree objects must be able to say if they are root
    def is_root_node(self):
        return self.isRoot

    ## Max & Min accessors
    def is_min_node(self):
        return (not self.isMax)
    def is_max_node(self):
        return self.isMax
    
    ## Ability to add children
    def add_child(self, node):
        self.children.append(node)
    ## Returns a list of the objects that are it's children. Can be Nodes or Leafs
    def get_children(self):
        return self.children
    
## Leaf object, does not have max or min, children and can't be root
class Leaf():
    ## Constructor. Value is static evaluation, key is for debugging
    def __init__(self, value):
        self.value = value
        self.key = str(value)
    ## Since Leaf is a tree object, must be able to say if it is root, but no leaves can be root
    def is_root_node(self):
        return False


## A recursive function that will search and return the highest/lowest
## score possible starting at a given root node.
## If at any point the value returned should be higher or lower than
## what their parent node is going to compare with, the sub search is
## immediately broken and returned. Since the child's lower/upper bound
## is greater than/less than their parents, it wouldn't matter what other
## choices their parent had.
def alpha_beta(current_node, alpha, beta):
    global counter
    ## Check for root node, use 999999999 as infinity
    if current_node.is_root_node():
        alpha = -999999999
        beta = 999999999

    ## Check if the tree object is of type Leaf
    if type(current_node) == Leaf:
        counter += 1
        return current_node.value

    ## Use for loop for all children and use break as cut off search below
    if current_node.is_max_node():
        for a in current_node.get_children():
            alpha = max(alpha, alpha_beta(a, alpha, beta))
            if alpha >= beta:
                break
        return alpha

    if current_node.is_min_node():
        for b in current_node.get_children():
            beta = min(beta, alpha_beta(b, alpha, beta))
            if beta <= alpha:
                break
        return beta


## Deals with the file and returns content
def inputData(fileName):
    with open(fileName) as f:
        content = f.readlines()
    return content

## Creates a new file with results
def outputData(results):
    with open("alphabeta_out.txt", 'w') as f:
        for line in results:
            f.write(line)
    f.close()

## Parse and init should get the line that defines the graph, and then
##      it create all the nodes and link them together.
##  returns the root node
def parse_n_init(graphstring):
    nodeRef = dict()
    # Sparates the two sections
    nodesListString, nodesDataString = graphstring.split(' ')

    # Clean the first string partially, and separate into items
    nodesList = nodesListString[2:-2].split('),(')
    # Init Root node
    nodesList[0] = nodesList[0].split(',')
    nodeRef[nodesList[0][0]] = Node(nodesList[0][1], True, key = nodesList[0][0])
    rootNode = nodeRef[nodesList[0][0]]

    # init other nodes
    for i in range(1, len(nodesList)):
        nodesList[i] = nodesList[i].split(',')
        nodeRef[nodesList[i][0]] = Node(nodesList[i][1], key = nodesList[i][0])
        
    # Clean data String
    nodesData = nodesDataString[2:-2].split('),(')

    # Create children and values
    for i in range(len(nodesData)):
        nodesData[i] = nodesData[i].split(',')
        # if is a letter than add child
        if (nodesData[i][1].isalpha()):
            nodeRef[nodesData[i][0]].add_child(nodeRef[nodesData[i][1]])
        # otherwise make it a leaf and give it a value
        elif (nodesData[i][1].isnumeric()):
             nodeRef[nodesData[i][0]].add_child(Leaf(int(nodesData[i][1])))
    return rootNode

## Main function, ties all other functions together.
def main():
    global counter
    ## read input data
    content = inputData("alphabeta.txt")
    results = []
    ## For every graph, parse string and run alpha_beta then collect results
    for i in range(len(content)):
        counter = 0
        root = parse_n_init(content[i])
        score = alpha_beta(root, None, None)
        resultString = "Graph " + str(i+1) + ": Score: " + str(score) + "; Leaf Nodes Examined: " + str(counter) + '\n'
        results.append(resultString)
        
    outputData(results)

main()
