from algorithm import play_game, Node
from graph_maker import makecolor

global SIZE, ROWS, WINDOW_SIZE, WIDTH, HEIGHT, MARGIN
global GRID, TOTAL_GRID
global count

#determines grid size
ROWS = 10 #change this to increase the rows
SIZE = ROWS * 25

#Do not change
MARGIN = 5
WINDOW_SIZE = [SIZE + MARGIN, SIZE + MARGIN]

WIDTH = 20
HEIGHT = 20

GRID = []
TOTAL_GRID = []

#Change to increase the total number of barriers able to be placed
COUNT = 15

TYPE = "Queue" #Change to either "Stack" (for DFS) or "Queue" (for BFS) -- Queue will find shortest path using BFS however Stack does not guarantee a shortest path (DFS)

def main():
    START = Node(0,0,None)
    END = Node(ROWS-2,ROWS-2,None)
    makecolor(0,TOTAL_GRID, ROWS, GRID)
    play_game(START, END, GRID, WINDOW_SIZE, SIZE, ROWS, COUNT, TYPE,MARGIN,WIDTH,HEIGHT, TOTAL_GRID)

main()
