# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

#This function, given a frontier, a child to add, the child's parent,
#a heuristic (optionally), and a problem will add a node to a specific
#type of frontier. 
def add_node(frontier, child, node, heuristic, problem):
    front_type = type(frontier)     #grab the type of the frontier

    #Note: the ucs_heuristic() is used for UCS here.
    if front_type == util.PriorityQueue:
        #astar search or UCS
        g = child[2] + node[2]                   #path cost from root to x
        f = g + heuristic(child[0], problem)     #path cost root->state->goal
        new_node = (child[0], node[1] + [child[1]], g) #create a new node
        frontier.update(new_node, f)  
    else:
        #BFS or DFS
        new_node = (child[0], node[1] + [child[1]]) #create a new node
        frontier.push(new_node) 

#This generic search algorithm, given the problem state space and 
#a frontier (Priority Queue/Queue/Stack) will search the problem
#for a goal state, iteratively. 
def generic_search(problem, frontier, heuristic=None):
    visited = []        #cycle detection

    while True:
        if frontier.isEmpty(): return None      #if frontier empty, no solution

        node = frontier.pop()                   #choose the next node
        if problem.isGoalState(node[0]):        #goal test
            return node[1]

        if node[0] not in visited:              #cycle check
            visited.append(node[0])                 
            for child in problem.getSuccessors(node[0]):    #for each successor
                add_node(frontier, child, node, heuristic, problem)   #add to frontier


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    frontier = util.Stack()                 #create the frontier; DFS => FILO
    node = (problem.getStartState(), [])    #create a (location, path) node
    frontier.push(node)

    #find & return the path with generic_search()
    return generic_search(problem, frontier)


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    frontier = util.Queue()                 #create the frontier; BFS => FIFO
    node = (problem.getStartState(), [])    #create a (location, path) node
    frontier.push(node)

    #find & return the path with generic_search()
    return generic_search(problem, frontier)

#This heuristic will return 0, no matter the state or problem, since
#it will only be used in a UCS problem; by definition, UCS is Astar with
#f(n) = g(n) + h(n) where h(n) = 0 for all n.
def ucs_heuristic(state, problem):
    return 0

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    frontier = util.PriorityQueue()           #create the frontier; UCS=>PrioQue
    node = (problem.getStartState(), [], 0)   #create a (location, path, g) node
    frontier.push(node, node[2])

    #find & return the path with generic_search()
    return generic_search(problem, frontier, ucs_heuristic)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    """Search the node of least total cost first."""
    frontier = util.PriorityQueue()           #create the frontier; UCS=>PrioQue
    f = 0 + heuristic(problem.getStartState(), problem) #calculate f = g + h
    node = (problem.getStartState(), [], 0)   #create a (location, path, g) node
    frontier.push(node, f)

    #find & return the path with generic_search()
    return generic_search(problem, frontier, heuristic)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
