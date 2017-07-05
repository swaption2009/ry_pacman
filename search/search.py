# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
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
     Returns the start state for the search problem
     """
     util.raiseNotDefined()

  def isGoalState(self, state):
     """
       state: Search state

     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state

     For a given state, this should return a list of triples,
     (successor, action, stepCost), where 'successor' is a
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take

     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()


def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]


def graph_search(problem, fringe, add_to_fringe_fn):
    """Search through the successors of a problem to find a goal.
    The argument fringe should be an empty queue.
    If two paths reach a state, only use the best one. [Fig. 3.18]"""

    visited = set()
    start = (problem.getStartState(), 0, []) # (node, cost, path)
    #fringe.push((problem.getStartState(), []))
    add_to_fringe_fn(fringe, start, 0)

    while not fringe.isEmpty():
        (node, cost, path) = fringe.pop()
        if problem.isGoalState(node):
            return path
        if not node in visited:
            visited.add(node)

            # INDENT HERE
            successors = problem.getSuccessors(node)
            for child_node, child_action, child_cost in successors:
                if child_node[0] not in visited:
                    #fringe.push((state, path + [action]))
                    new_cost = cost + child_cost
                    new_path = path + [child_action]
                    new_state = (child_node, new_cost, new_path)
                    add_to_fringe_fn(fringe, new_state, new_cost)

def add_to_fringe_fn(fringe, state, cost):
    fringe.push(state)


def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]

  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:

  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  #print "Start:", problem.getStartState()
  #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  #print "Start's successors:", problem.getSuccessors(problem.getStartState())
  return graph_search(problem, util.Stack(), add_to_fringe_fn)



def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
  return graph_search(problem, util.Queue(), add_to_fringe_fn)

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  visited = set()
  que = util.PriorityQueue()
  que.push((problem.getStartState(), []), 0)

  while que:
    (node, path) = que.pop()
    if problem.isGoalState(node):
            #path.append(node)
      return path
    visited.add(node)
    successors = problem.getSuccessors(node)
    for state, action, cost in successors:
      if state not in visited:
        que.push((state, path + [action]), cost)


def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  visited = set()
  que = util.PriorityQueue()
  que.push((problem.getStartState(), []), 0)

  while que:
    (node, path) = que.pop()
    if problem.isGoalState(node):
            #path.append(node)
      return path
    visited.add(node)
    successors = problem.getSuccessors(node)
    for state, action, cost in successors:
      if state not in visited:
        que.push((state, path + [action]), cost + heuristic(state, problem))



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
