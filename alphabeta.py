## Alpha-Beta Pruning

counter = []

## documentation
class Node():
    def __init__(self, maxOrMin, isRoot = False):
        if (maxOrMin == "MAX"):
            self.isMax = True
        elif (maxOrMin == "MIN"):
            self.isMax = False
        else: raise ValueError('maxOrMin must be "MAX" or "MIN"')
        self.isLeaf = False
        self.isRoot = isRoot
        self.value = None
        self.children = []

    ## documentation
    def is_root_node(self):
        return self.isRoot
    ## documentation
    def is_leaf(self):
        return self.isLeaf
    ## documentation
    def is_min_node(self):
        return (not self.isMax)
    ## documentation
    def is_max_node(self):
        return self.isMax
    ## documentation
    def add_child(self, node):
        if (type(node) != type(self)):
            print("Child must be a node")
        elif (self.isLeaf):
            print("Leaves can not have children")
        else:
            self.children.append(node)
    ## documentation
    def makeLeaf(self, value):
        self.isLeaf = True
        self.value = value

    ## documentation
    def get_children(self):
        return self.children
## documentation
def cut_off_search_below(current_node):
    pass

## documentation
def alpha_beta(current_node, alpha, beta):
    global counter
    
    if current_node.is_root_node():
        alpha = -999999999
        beta = 999999999
        
    if current_node.is_leaf():
        print(current_node.value)
        return current_node.value
    
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


## documentation
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
    nodeRef[nodesList[0][0]] = Node(nodesList[0][1], True)
    rootNode = nodeRef[nodesList[0][0]]

    # init other nodes
    for i in range(1, len(nodesList)):
        nodesList[i] = nodesList[i].split(',')
        nodeRef[nodesList[i][0]] = Node(nodesList[i][1])
        
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
            nodeRef[nodesData[i][0]].makeLeaf(int(nodesData[i][1]))
    return rootNode
        
def main():
    global counter
    root = parse_n_init()
    print("Score:", alpha_beta(root, None, None))
    print("Leafs Examined:", counter)
    
