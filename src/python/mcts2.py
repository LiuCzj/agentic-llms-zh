def monte_carlo_tree_search(root):
    while resources_left(time, computational power):
        leaf = select(root) # leaf = unvisited node 
        simulation_result = rollout(leaf)
        backpropagate(leaf, simulation_result)
    return best_child(root) # or: child with highest visit count

def select(node):
    while fully_expanded(node):
        node = best_child(node)    # traverse down path of best UCT nodes
    return expand(node.children) or node # no children/node is terminal 

def rollout(node):
    while non_terminal(node):
        node = rollout_policy(node)
    return result(node) 

def rollout_policy(node):
    return pick_random(node.children)

def backpropagate(node, result):
    if is_root(node) return 
    node.stats = update_stats(node, result) 
    backpropagate(node.parent)
   
def best_child(node, c_param=1.0):
    choices_weights = [
        (c.q / c.n) + c_param * np.sqrt((np.log(node.n) / c.n))    # UCT
        for c in node.children
    ]
    return node.children[np.argmax(choices_weights)]
