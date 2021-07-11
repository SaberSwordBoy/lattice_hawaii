import os
import random
import time

"""Lattice Hawaii - In Python!

Created by Bryce Casamento

for instructions on how to play see https://github.com/SaberSwordBoy/lattice_hawaii

NOTE: running this file will do nothing! this is just the basic functions and logic for the game. 
Run lattice_cli.py to actually play!

"""

# Colors
RED = 'r'
GREEN = 'g'
BLUE = 'b'
CYAN = 'c'
PURPLE = 'p'
YELLOW = 'y'

# Patterns
TURTLE = '1'
LIZARD = '2'
FLOWER = '3'
FEATHER = '4'
BIRD = '5'
FISH = '6'

colors = [RED, GREEN, BLUE, CYAN, PURPLE, YELLOW]
patterns = [TURTLE, LIZARD, FLOWER, FEATHER, BIRD, FISH]

def create_tileset():
    tileset = []
    for i in colors:
        for p in patterns:
            tileset.append((i, p))
    return tileset * 2

# Other Tiles
BLANK = ('0', '0')
SUN_SPOTS = [ #  these give extra points
    (0, 0), (1, 1), (2, 2), (0, 4),
    (0, 8), (1, 7), (2, 6), (4, 8),
    (8, 0), (7, 1), (6, 2), (4, 0),
    (8, 8), (7, 7), (6, 6), (8, 4)
]
# Board Dimensions
board_width = 9
board_height = 9

def create_board():
    # setup the board
    latticeboard = {}
    for row in range(board_height):
        for col in range(board_width):
            latticeboard[(row, col)] = BLANK
    return latticeboard

def print_tiles(tileset):
    layout = "|{}|" * len(tileset)
    values = []
    for tile in tileset:
        values.append(f"{tile[0]}:{tile[1]}")
    print(layout.format(*values))

def print_board(board):
    layout = """| {} | {} | {} | {} | {} | {} | {} | {} | {} |\n\n""" * board_height
    values = []
    for val in board.values():
        values.append(f"{val[0]}:{val[1]}")
    print(layout.format(*values))

def print_board_keys(board):
    layout = """| {} | {} | {} | {} | {} | {} | {} | {} | {} |\n\n""" * board_height
    values = []
    for val in board.keys():
        if val in SUN_SPOTS:
            values.append(f"{val[0]}${val[1]}")
        else:
            values.append(f"{val[0]}:{val[1]}")
    print(layout.format(*values))

def check_legal_move(board, color, pattern, column, row):
    up = BLANK if board.get((column - 1, row)) is None else board.get((column - 1, row))
    left = BLANK if board.get((column, row - 1)) is None else board.get((column, row - 1))
    right = BLANK if board.get((column, row + 1)) is None else board.get((column, row + 1))
    down = BLANK if board.get((column + 1, row)) is None else board.get((column + 1, row))
    print(up, left, right, down)
    return all(
        [(up[0] == color or up[1] == pattern or up == BLANK),
         (left[0] == color or left[1] == pattern or left == BLANK),
         (right[0] == color or right[1] == pattern or right == BLANK),
         (down[0] == color or down[1] == pattern or down == BLANK)])

def get_empty_surrounding_tiles(board, column, row):
    result = [False, False, False, False]
    if board.get((column - 1, row)) == BLANK: # upper one
        result[0] = True
    if board.get((column, row-1)) == BLANK: # left one
        result[1] = True
    if board.get((column, row + 1)) == BLANK: # right one
        result[2] = True
    if board.get((column+1, row)) == BLANK: # lower one
        result[3] = True
    return result

def get_tile_points(board, col, row):
    points = 0
    surrounding_empty = get_empty_surrounding_tiles(board, col, row)
    if surrounding_empty.count(False) == 2:
        points = 1
    elif surrounding_empty.count(False) == 3:
        points = 2
    elif surrounding_empty.count(False) == 4:
        points = 4
    else:
        points = 0
    return points

def print_help():
    print("[$] HELP")
    print("""[#] Colors:
    RED : r
    GREEN : g
    BLUE : b
    YELLOW = y
    CYAN = c
    PURPLE = p""")
    print("""[#] Patterns:
    TURTLE : 1
    LIZARD : 2
    FLOWER : 3
    FEATHER : 4
    BIRD : 5 """)

