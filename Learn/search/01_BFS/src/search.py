from .bfs_algo import Node, StackFrontier, QueueFrontier

def bfs(initial, goal_test, successors):
    """
    Breadth-First Search algorithm.
    
    Args:
        initial: Initial state
        goal_test: Function to test if a state is the goal
        successors: Function that returns a list of (action, state) pairs for a given state
    
    Returns:
        Tuple of (solution_path, explored_count) or None if no solution found
    """
    frontier = QueueFrontier()
    frontier.add(Node(initial))
    explored = set()
    explored_count = 0
    
    while not frontier.empty():
        node = frontier.remove()
        explored_count += 1
        
        if goal_test(node.state):
            actions = []
            cells = []
            
            # Follow parent nodes to reconstruct path
            while node.parent is not None:
                actions.append(node.action)
                cells.append(node.state)
                node = node.parent
            
            actions.reverse()
            cells.reverse()
            return (actions, cells, explored_count)
        
        explored.add(node.state)
        
        for action, state in successors(node.state):
            if not frontier.contains_state(state) and state not in explored:
                child = Node(state=state, parent=node, action=action)
                frontier.add(child)
    
    return None

def dfs(initial, goal_test, successors):
    """
    Depth-First Search algorithm.
    
    Args:
        initial: Initial state
        goal_test: Function to test if a state is the goal
        successors: Function that returns a list of (action, state) pairs for a given state
    
    Returns:
        Tuple of (solution_path, explored_count) or None if no solution found
    """
    frontier = StackFrontier()
    frontier.add(Node(initial))
    explored = set()
    explored_count = 0
    
    while not frontier.empty():
        node = frontier.remove()
        explored_count += 1
        
        if goal_test(node.state):
            actions = []
            cells = []
            
            # Follow parent nodes to reconstruct path
            while node.parent is not None:
                actions.append(node.action)
                cells.append(node.state)
                node = node.parent
            
            actions.reverse()
            cells.reverse()
            return (actions, cells, explored_count)
        
        explored.add(node.state)
        
        for action, state in successors(node.state):
            if not frontier.contains_state(state) and state not in explored:
                child = Node(state=state, parent=node, action=action)
                frontier.add(child)
    
    return None
