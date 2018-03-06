# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:08:43 2018

@author: cen
"""

stoneLocation=[2, 7]  #[row, column]
positiveTerminalLocation = [0,9,2]  #[row, column, utility value]
nagativeTerminalLocation = [1,9, -2]  #[row, column, utility value]
iteration=30
noise=0.15
discount=0.91
row = 10
column = 10
import sys
direction = "n"
value = float(0)
matrix = []
for i in range (row): 
    lists = []
    item = []
    item.append(value)
    item.append(direction)
    for j in range (column):
        lists.append(item)
    matrix.append(lists)   
    
matrix[stoneLocation[0]][stoneLocation[1]] = ["STONE","None"] 
iterations = iteration

def start():
    global matrix
    _print(tuple(matrix))
    global iteration
    iteration -= 1
    matrix[positiveTerminalLocation[0]][positiveTerminalLocation[1]]= [positiveTerminalLocation[2],"n"]
    matrix[nagativeTerminalLocation[0]][nagativeTerminalLocation[1]]= [nagativeTerminalLocation[2],"n"]
    for i in range (row):
        for j in range (column):
            direction = get_max_direction(matrix,i,j)
            matrix[i][j]=[matrix[i][j][0],direction]
    _print(matrix)
   
    
    while iteration > 0:
        iteration -= 1
        former_matrix = tuple(matrix)
        current_matrix = []
        for i in range (row):
            list = []
            for j in range (column):
                value= get_max_value(tuple(former_matrix),i,j)
                list.append((value,former_matrix[i][j][1]))
            current_matrix.append(list)
        #_print(tuple(current_matrix))
        for i in range (row):
            for j in range (column):
                direction = get_max_direction(current_matrix,i,j)
                current_matrix[i][j]=[current_matrix[i][j][0],direction]
        matrix = current_matrix
        _print(tuple(matrix))
       
        
def get_max_direction(matrix,a,b): 
    best_value = -sys.maxsize-1
    best_direction = "n"
    if a == positiveTerminalLocation[0] and b == positiveTerminalLocation[1]:
        return "n"
    if a == nagativeTerminalLocation[0] and b == nagativeTerminalLocation[1]:
        return "n"
    if a ==stoneLocation[0] and b == stoneLocation[1]:
        return "NONE"
    dir_x = [-1,0,1,0]
    dir_y = [0,1,0,-1]
    value = [0.0,0.0,0.0,0.0]
    dire = ["n","e","s","w"]
    for i in range (4):
        if isvalid(matrix, a + dir_x[i], b + dir_y[i]):
            value[i] = matrix[a + dir_x[i]][b+dir_y[i]][0]
        else: 
            value[i] = matrix[a][b][0]
    for i in range(4):
        temp_value = value[i]*(1-noise) + value[int((i-1+4)%4)]*noise/2 + value[int((i+1)%4)]*noise/2
        if temp_value > best_value:
            best_direction = dire[i]
            best_value = temp_value
    return best_direction

def get_max_value(matrix,a,b):
    if a == positiveTerminalLocation[0] and b == positiveTerminalLocation[1]:
        return positiveTerminalLocation[2]
    if a == nagativeTerminalLocation[0] and b == nagativeTerminalLocation[1]:
        return nagativeTerminalLocation[2]
    if a ==stoneLocation[0] and b == stoneLocation[1]:
        return "STONE"
    dir_x = [-1,0,1,0]
    dir_y = [0,1,0,-1]
    dire = ["n","e","s","w"]
    value = [0.0,0.0,0.0,0.0]
    for i in range (4):
        if isvalid(matrix, a + dir_x[i], b + dir_y[i]):
            value[i] = matrix[a + dir_x[i]][b+dir_y[i]][0]
        else: 
            value[i] = matrix[a][b][0]
    for i in range(4):
        if dire[i] == matrix[a][b][1]:
            return discount*(value[i]*(1-noise) + value[(i-1+4)%4]*noise/2 + value[int((i+1)%4)]*noise/2)
    return -20

def _print(matrix): 
    print("iteration number:",iterations-iteration)
    for i in range (row):
        for each in matrix[i]:  
            if isinstance(each[0],str):
                print("(",each[0],")",sep="", end = " ")
            else:
                print( "%.2f"%each[0],"(",each[1],")",sep="", end = " ")
                
        print()
    print()
def isvalid(matrix, a, b):
    if a < 0 or a >= row:
        return False
    if b < 0 or b >= column:
        return False
    if isinstance(matrix[a][b][0],str):
        return False
    return True
        
start()