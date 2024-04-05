"""
Tic Tac Toe Player
"""

from copy import copy, deepcopy
from logging import exception
import math
import re

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Xs_count = 0
    Os_count = 0
    # count  X's and O's 
    for row in board:
        for cell in row :
            if cell == X :
                Xs_count += 1
            elif cell == O :
                Os_count += 1 

    if (Xs_count > Os_count):
        return O
    else :
        return X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == EMPTY:
                actions_set.add((i,j))
    return actions_set
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    result_board = deepcopy(board)
    row = action[0]
    cell = action[1]

    # check if action is valid
    if result_board[row][cell] != EMPTY :
        raise ValueError("the action is invalid")
    else:
        result_board[row][cell] = player(board)
    
    return result_board
    
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        cell_value = row[0]
        has_winner = True
        for cell in row:
            if cell != cell_value:
                has_winner = False 
                break
        if(has_winner):
            return cell_value
    for j in range(0,3):
        cell_value = board[0][j]
        has_winner = True
        for i in range(0,3):
            if board[i][j] != cell_value :
                has_winner = False
                break
        if(has_winner):
            return cell_value
    
    cell_value = board[1][1]
    if(cell_value == board[0][0] == board[2][2]):
        return cell_value
    if(cell_value == board[0][2] == board[2][0]):
        return cell_value
    
    return None

    raise NotImplementedError

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board) != None ):
        return True 
    
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False 
    
    return True 
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    Winner =  winner(board)
    if Winner == X:
        return 1 
    elif Winner == O:
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) :
        return None
    
    value , action = minimax_algorithm(board)

    return action

    raise NotImplementedError

def minimax_algorithm(board):
    Player = player(board)

    # max implementation
    if Player == X :

        max_value = float("-inf")
        best_action = (-1,-1)
        possible_actions = actions(board)

        for action in possible_actions:

            if (max_value == 1):
                return max_value , best_action

            result_board = result(board , action)
            board_value = float("-inf")

            if terminal(result_board):
                board_value = utility(result_board)
            else:
                board_value , first_action = minimax_algorithm(result_board)

            if (board_value > max_value):
                    max_value = board_value
                    best_action = action
        
        return max_value , best_action

    
    # min implementation
    elif Player == O:
        min_value = float("inf")
        best_action = (-1,-1)
        possible_actions = actions(board)
        
        for action in possible_actions:

            if(min_value == -1):
                return min_value , best_action
            
            result_board = result(board , action)
            board_value = float("inf")

            if terminal(result_board):
                board_value = utility(result_board)
            else:
                board_value , first_action = minimax_algorithm(result_board)
            
            if(board_value < min_value):
                min_value = board_value
                best_action = action
            
        return min_value , best_action
    


