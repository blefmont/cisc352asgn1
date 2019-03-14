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
def input():
    pass
## documentation
def output():
    pass
## documentation
def parse_n_init():
    pass
