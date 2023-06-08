import pygame
import time
from node import Node



global white, black, blue, red, yellow, orange, aqua

white = (255,255,255) #0
blue = (0,0,100) #1
yellow = (255,255,0) #2
red = (255,0,0) #3
black = (0,0,0) #4
orange = (255,128,0) #5
aqua = (0, 128, 128) #6

def tolist(st):
    splt = st.split(".")
    x = int(splt[0])
    y = int(splt[1])
    return [x,y]

def draw(screen, GRID, ROWS, MARGIN, WIDTH, HEIGHT): #draws the game based on the numbers present in the 2-d array
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


def makecolor(numb, TOTAL_GRID, ROWS, GRID):
    for row in range(ROWS):
        # Add an empty array that will hold each cell
        # in this row
        GRID.append([])
        for column in range(ROWS):
            GRID[row].append(numb)  # Append a cell
            TOTAL_GRID.append([row,column])

def drawer(lol, screen, GRID, END:Node, ROWS, MARGIN, WIDTH, HEIGHT):
    queue = []
    for lst in lol:
        # queue.append(tolist(lst))
        queue.append(lst)
    while len(queue) != 0:
            node = queue[0]
            x, y = node[0], node[1]
            if GRID[x][y] != 2 and GRID[x][y] != 1:
                GRID[x][y] = 6
                draw(screen,GRID,ROWS,MARGIN,WIDTH,HEIGHT)
            queue = queue[1:]
            time.sleep(0.05)
    x, y = END.x, END.y
    GRID[x][y] = 2
    draw(screen,GRID,ROWS,MARGIN,WIDTH,HEIGHT)
    pygame.display.set_caption("Finished")

