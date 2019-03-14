## Alpha-Beta Pruning


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
        pass
    ## documentation
    def is_leaf(self):
        pass
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
        pass
## documentation
def cut_off_search_below(current_node):
    pass

## documentation
def alpha_beta(current_node, alpha, beta):
    if current_node.is_root_node():
        alpha = -999999999
        beta = 999999999
        
    if current_node.is_leaf():
        return current_node.static_evaluation
    
    if current_node.is_max_node():
        for a in current_node.get_children():
            alpha = max(alpha, alpha_beta(a, alpha, beta))
            if alpha >= beta:
                break

    if current_node.is_min_node():
        for b in current_node.get_children():
            beta = min(beta, alpha_beta(b, alpha, beta))
            if beta <= alpha:
                break


## documentation
def inputData(fileName):
    with open(fileName) as f:
        content = f.read()
    return content

## documentation
def outputData():
    pass
## documentation
def parse_n_init():
    nodeRef = dict()
    content = inputData("alphabeta.txt")
    nodesListString, nodesDataString = content.split(' ')
    
    nodesList = nodesListString[2:-2].split('),(')
    nodesList[0] = nodesList[0].split(',')
    nodeRef[nodesList[0][0]] = Node(nodesList[0][1], True)
    for i in range(1, len(nodesList)):
        nodesList[i] = nodesList[i].split(',')
        nodeRef[nodesList[i][0]] = Node(nodesList[i][1])

    nodesData = nodesDataString[2:-2].split('),)')

    for i in range(len(nodesData)):
        nodesData[i] = nodesData[i].split(',')
        if (nodesData[i][1].isalpha()):
            nodeRef[nodesData[i][0]].addChild(nodeRef[nodesData[i][1]])
        elif (nodesData[i][1].isnumeric()):
            nodeRef[nodesData[i][0]].makeLeaf(int(nodeRef[nodesData[i][1]]))
    print(nodeRef)
        
