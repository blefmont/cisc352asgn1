## Alpha-Beta Pruning


## documentation
class Node():
    def _init__(self):
        pass
    ## documentation
    def is_root_node(self):
        pass
    ## documentation
    def is_leaf(self):
        pass
    ## documentation
    def is_min_node(self):
        pass
    ## documentation
    def is_max_node(self):
        pass
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
        alpha = max(alpha, alpha_beta(current_node.get_children(), alpha, beta))
        if alpha >= beta:
            cut_off_search_below(current_node)

    if current_node.is_min_node():
        beta = min(beta, alpha_beta(current_node.get_children(), alpha, beta))
        if beta <= alpha:
            cut_off_search_below(current_node)


## documentation
def input():
    pass
## documentation
def output():
    pass
## documentation
def parse_n_init():
    pass
