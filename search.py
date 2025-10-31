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
from game import Directions
from typing import List

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




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
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
def depthFirstSearch(problem):
    from util import Stack
    pilha = Stack()
    inicio = problem.getStartState()
    pilha.push((inicio, []))  # (estado, caminho)
    visitados = set()

    while not pilha.isEmpty():
        estado, caminho = pilha.pop()

        if problem.isGoalState(estado):
            return caminho  # achou o objetivo!

        if estado not in visitados:
            visitados.add(estado)
            for prox, acao, custo in problem.getSuccessors(estado):
                if prox not in visitados:
                    pilha.push((prox, caminho + [acao]))

    return []
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    from util import Queue
    fila = Queue()
    inicio = problem.getStartState()
    fila.push((inicio, []))
    visitados = set([inicio])

    while not fila.isEmpty():
        estado, caminho = fila.pop()

        if problem.isGoalState(estado):
            return caminho

        for prox, acao, custo in problem.getSuccessors(estado):
            if prox not in visitados:
                visitados.add(prox)
                fila.push((prox, caminho + [acao]))

    return []

    util.raiseNotDefined()

def uniformCostSearch(problem):
    from util import PriorityQueue
    fila = PriorityQueue()
    inicio = problem.getStartState()
    fila.push((inicio, [], 0), 0)
    visitados = {}

    while not fila.isEmpty():
        estado, caminho, custo = fila.pop()

        if problem.isGoalState(estado):
            return caminho

        if estado in visitados and visitados[estado] <= custo:
            continue
        visitados[estado] = custo

        for prox, acao, custoPasso in problem.getSuccessors(estado):
            novoCusto = custo + custoPasso
            fila.push((prox, caminho + [acao], novoCusto), novoCusto)

    return []

    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=lambda s, p: 0):
    from util import PriorityQueue
    fila = PriorityQueue()
    inicio = problem.getStartState()
    fila.push((inicio, [], 0), heuristic(inicio, problem))
    visitados = {}

    while not fila.isEmpty():
        estado, caminho, custo = fila.pop()

        if problem.isGoalState(estado):
            return caminho

        if estado in visitados and visitados[estado] <= custo:
            continue
        visitados[estado] = custo

        for prox, acao, custoPasso in problem.getSuccessors(estado):
            novoCusto = custo + custoPasso
            prioridade = novoCusto + heuristic(prox, problem)
            fila.push((prox, caminho + [acao], novoCusto), prioridade)

    return []

    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
