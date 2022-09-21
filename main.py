from tkinter import Toplevel
import pygame
from pygame.locals import *

import grid as g
import time, math


global white, black, blue, red, yellow, orange, aqua
global mapper
global SIZE, ROWS, WINDOW_SIZE, WIDTH, HEIGHT, MARGIN
global GRID, TOTAL_GRID
global count
global START, END

SIZE = 500
ROWS = 20

MARGIN = 5
WINDOW_SIZE = [SIZE + MARGIN, SIZE + MARGIN]

WIDTH = 20
HEIGHT = 20
 
GRID = []
TOTAL_GRID = []

START = [0,0]
END = [ROWS - 2, ROWS - 2]

count = 25


def makecolor(numb):
    for row in range(ROWS):
        # Add an empty array that will hold each cell
        # in this row
        GRID.append([])
        for column in range(ROWS):
            GRID[row].append(numb)  # Append a cell
            TOTAL_GRID.append([row,column])



white = (255,255,255) #0
blue = (0,0,100) #1
yellow = (255,255,0) #2
red = (255,0,0) #3
black = (0,0,0) #4
orange = (255,128,0) #5
aqua = (0, 128, 128) #6

 


def adjacencylist(lst):
    x = lst[0]
    y = lst[1]
    right, down, up, left = [x+1,y], [x,y+1], [x, y-1], [x-1,y]
    retval = []
    for vals in [right,down,up,left]:
        if vals in TOTAL_GRID:
            retval.append(vals)
    return retval


def tonode(lst:list):
    # print("LST: " + str(lst))
    return str(lst[0]) + "."+ str(lst[1])

def tolist(st):
    x = int(st.split(".")[0])
    y = int(st.split(".")[1])
    # y = float((num - x) * 10 ** 2)
    return [x,y]


def find(start,end,screen, track:list):
    path_found = False
    queue = [start]
    tracker = track +  [start]
    # print(f"Tracker: {tracker}")
    mapper = {}
    mapper[tonode(start)] = None #Maps the starting node to None
    while len(queue) != 0:
        # print(f"Queue: {queue}")
        node = queue[0]
        if tonode(node) == tonode(end):
            path_found = True
        for nodes in adjacencylist(node): 
            # print(f"Nodes: {nodes}")
            x, y = nodes[0], nodes[1]
            if nodes not in tracker and GRID[x][y] != 1: #Checks to see if in tracker and if grid is not blue
                tracker.append(nodes)
                queue.append(nodes)
                mapper[tonode(nodes)] = tonode(node)
                # print(f"Grid: {x,y}")
                if GRID[x][y] == 0:
                    GRID[x][y] = 3
                draw(screen)
                
        queue = queue[1:]
        time.sleep(0.03)

    path = []
    # print("Done with color red")
    if path_found:
        end_node = tonode(end)
        while mapper[end_node] != None:
            path.append(mapper[end_node])
            # print(f"Checking node: {mapper[end_node]}")
            end_node = mapper[end_node]
        path.reverse()
    else:
        print("Path not found!")
    return path 

def direct_path(path, screen):
    while len(path) != 0:
        node = path[0]
        x, y = tolist(node)[0] , tolist(node)[1] 
        if GRID[x][y] == 0:
            # print(f"Grid: {x,y}")
            GRID[x][y] = 6
        draw(screen)


# start = [1,1]
# end = [18,18]
# print(find(start,end))

def draw(screen):
    for row in range(ROWS):
        for column in range(ROWS):
            color = white
            if GRID[row][column] == 1:
                color = blue
            elif GRID[row][column] == 2:
                color = yellow
            elif GRID[row][column] == 3:
                color = red
            elif GRID[row][column] == 4:
                color = black
            elif GRID[row][column] == 5:
                color = orange
            elif GRID[row][column] == 6:
                color = aqua
            pygame.draw.rect(screen,
                            color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH,
                            HEIGHT])
    pygame.display.flip()


def drawer(lol, screen):
    # print(f"lol: {lol}")
    queue = []
    for lst in lol:
        queue.append(tolist(lst))
    print(f"Queue: {queue}")
    while len(queue) != 0:
            node = queue[0]
            x, y = node[0], node[1]
            if GRID[x][y] != 2 and GRID[x][y] != 1:
                GRID[x][y] = 6
                draw(screen)
            queue = queue[1:]
            time.sleep(0.05)
    x, y = END[0], END[1]
    GRID[x][y] = 2
    draw(screen)

def main():
    global count
    screen = pygame.display.set_mode(WINDOW_SIZE)

    pygame.display.set_caption(f"Array Backed Grid: {count}")

    
    play = True

    #START COLORS FOR START AND FINISH
    
    GRID[START[0]][START[1]] = 2
    GRID[END[0]][END[1]] = 2
    
    
    clicking = "Not Clicking"
    
    clock = pygame.time.Clock()

    tracker = []

    while play:

        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    block_size = SIZE / ROWS
                    clicking = "Clicking"
                    x = int(mx // block_size)
                    y = int(my // block_size)
                    # print(x,y)
                    num = GRID[y][x]
                    if num != 2 and num != 3 and count > 0 and num != 1: #checks if its a color other than white
                        GRID[y][x] = 1 #Sets color of the clicked to blue
                        count -= 1
                        tracker.append([y,x]) #Adds to track the positions of the walls, start, and end
                    
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    clicking = "Not Clicking"
                    # print(clicking)

        screen.fill(black)
 
        # Draw the grid
        
        pygame.display.set_caption(f"Array Backed Grid: {count}")

        if count == 0:
            count = -1
            path = find(START,END, screen, tracker)
            # print(f"Path: {path}")
            drawer(path, screen)

        else:
            draw(screen)

        clock.tick(60)

        

        pygame.display.flip()

makecolor(0)
main()



#If c is alive and has fewer than 2 live neighbors, it dies.
#If c is alive and has more than 3 live neighbors, it dies.
#If c is alive and has exactly 2 or 3 live neighbors, it remains alive.
#If c is dead and has exactly 3 live neighbors, it becomes alive


# neighbors alive of [y,x] = [y-1,x] [y+1,x] [y,x-1] [y,x+1] [y+1, x+1] [y-1,x-1] [y+1,x-1] [y-1, x+1]

# import numpy


# [[0,0],[1,0],[2,0]],
# [[0,1],["X,Y"],[2,1]],
# [[0,2],[1,2],[2,2]]

# up = [y-1][x]
# down = [y+1][x]
# right = [y][x+1]
# left = [y][x-1]
# top_right = [y-1][x+1]
# top_left = [y-1][x-1]
# bot_right = [y+1][x+1]
# bot_left = [y+1][x-1]

# dead = 0
# alive = 0
# total = 0
# for status in [up,down,right,left,top_left,top_right,bot_right,bot_left]:
#     if status == -1:
#         dead += 1
#     else:
#         alive += 1
#     total += 1


# if x,y = 1:
#     if getstatus_alive(x,y) == 2 or getstats_alive == 3:
#         x,y = alive
#     else:
#         x,y = dead
# else:
#     if getstatus_alive == 3:
#         x,y = alive

#Set a prev variable that will be used to check for the next generation for each tile
