import math
import numpy as np
import random

def find_indices(list_to_check, item_to_find):
    """searchs for items in a list

    Args:
        list_to_check (list): list to search
        item_to_find (any): item to be found in a list

    Returns:
        list: idnexis of found items
    """
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices

def sudoku(nnums = 81):
    random.seed(1)
    board = [[0 for i in range(9)] for j in range(9)]
    #print(board)
    #print(shadow_board)
    for q in range(nnums):
        #print(q)
        shadow_board = [[list(range(1, 10)) for i in range(9)] for j in range(9)]
        p_coords = []
        for y in range(9):
            for x in range(9):
                if(board[y][x] == 0):
                    p_coords.append((y, x))
                    for temp_y in range(9):#check column
                        if(board[temp_y][x] in shadow_board[y][x]):
                            shadow_board[y][x].remove(board[temp_y][x])
                    for temp_x in range(9):#check row
                        if(board[y][temp_x] in shadow_board[y][x]):
                            shadow_board[y][x].remove(board[y][temp_x])
                    big_x = 3*math.floor(x/3)#check square
                    big_y = 3*math.floor(y/3)
                    for temp_y in range(big_y, big_y+3):
                        for temp_x in range(big_x, big_x+3):
                           if(board[temp_y][temp_x] in shadow_board[y][x]):
                               shadow_board[y][x].remove(board[temp_y][temp_x])
        p_shadow_board = [shadow_board[coord[0]][coord[1]] for coord in p_coords]
        lens = [len(i) for i in p_shadow_board]
        #print(lens)
        p_shots = find_indices(lens, min(lens))
        #print(p_shots)
        shot = random.choice(p_shots)
        #print(shot)
        shot_y = p_coords[shot][0]
        shot_x = p_coords[shot][1]
        #print(shot_y, shot_x)
        #print(board[shot_y][shot_x])
        #print(shadow_board[shot_y][shot_x])
        board[shot_y][shot_x] = random.choice(shadow_board[shot_y][shot_x])
    for i in board:
        for j in i:
            print(j, end='  ')
        print('\n')

sudoku()
