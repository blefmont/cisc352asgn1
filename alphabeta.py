## Alpha-Beta Pruning

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


## documentation
def alpha_beta(current_node, alpha, beta):
    global counter
    print("alpha_beta: Current node is " + current_node.key)
    if current_node.is_root_node():
        alpha = -999999999
        beta = 999999999
        
    if type(current_node) == Leaf:
        counter.append(current_node.value)
        return current_node.value
    
    if current_node.is_max_node():
        for a in current_node.get_children():
            print("Checking child: "+ a.key)
            alpha = max(alpha, alpha_beta(a, alpha, beta))
            if alpha >= beta:
                break
        return alpha

    if current_node.is_min_node():
        for b in current_node.get_children():
            print("Checking child: "+ b.key)
            beta = min(beta, alpha_beta(b, alpha, beta))
            if beta <= alpha:
                break
        return beta


## Deals with the file and returns content
def inputData(fileName):
    with open(fileName) as f:
        content = f.read()
    return content

## documentation
def outputData():
    pass

## Parse and init should grab the data from the input file, and then
##      it create all the nodes and link them together.
##  returns the root node
def parse_n_init():
    # Gets string data from file
    nodeRef = dict()
    content = inputData("alphabeta.txt")
    # Sparates the two sections
    nodesListString, nodesDataString = content.split(' ')

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

##   
def main():
    global counter
    root = parse_n_init()
    score = alpha_beta(root, None, None))
    outputData(

main()
