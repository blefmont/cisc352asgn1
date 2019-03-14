## Alpha-Beta Pruning


## documentation
class Node():
    def _init__(self, isMaxNode, isRootNode, isLeafNode, value = None):
        self.isMax = isMaxNode
        self.isMin = not isMaxNode
        self.isLeaf = isLeafNode
        self.isRoot = isRootNode
        self.value = value
        if (isLeafNode and value == None):
            raise ValueError("If is a leaf node, value must be provided")
        self.children = []
    ## documentation
    def is_root_node(self):
        return self.isRoot
    ## documentation
    def is_leaf(self):
        return self.isLeaf
    ## documentation
    def is_min_node(self):
        return self.isMin
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
    def get_children(self):
        return children
    
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
def input(filename):
    with open(fileName) as f:
        content = f.read()
    return content
## documentation
def output():
    pass
## documentation
def parse_n_init():
    pass
