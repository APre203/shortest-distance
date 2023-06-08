import time, pygame
from pygame.locals import *


from node import Node, Stack, Queue
from graph_maker import drawer, draw


global black
black = (0,0,0) #4


def find(start:Node, end:Node, screen, track, TOTAL_GRID, GRID, t, ROWS, MARGIN, WIDTH, HEIGHT) -> list:
    path_found = False
    if t == "Stack":
        queue = Stack()
    else:
        queue = Queue()
    queue.add(start)
    tracker = track +  [start.x,start.y]
    mapper = {}
    mapper[start.hashable()] = None #Maps the starting node to None
    while not queue.empty():
        node = queue.remove()
        
        if node.hashable() == end.hashable():
            path_found = True
            end.parent = node
            
        for nodes in adjacencylist(node,TOTAL_GRID):
            x, y = nodes[0], nodes[1]
            if [x,y] not in tracker and GRID[x][y] != 1: #Checks to see if in tracker and if grid is not blue

                tracker.append([x,y])
                n = Node(x,y,node)
                queue.add(n)
                
                if GRID[x][y] == 0:
                    GRID[x][y] = 3
                draw(screen,GRID,ROWS,MARGIN,WIDTH,HEIGHT)
                
        time.sleep(0.03)

    path = []

    if path_found:
        end_node = end
        while end_node.parent != None:
            path.append([end_node.x,end_node.y])
            end_node = end_node.parent
        path = path[1:]
        path.reverse()
        print(path)
    else:
        print("Path not found!")
        pygame.display.set_caption("Path Not Found!")
        time.sleep(10)
        exit()
    return path 


def adjacencylist(node:Node,TOTAL_GRID) -> list:
    x = node.x
    y = node.y
    right, down, up, left = [x+1,y], [x,y+1], [x, y-1], [x-1,y]
    retval = []
    for vals in [right,down,up,left]:
        if vals in TOTAL_GRID:
            retval.append(vals)
    return retval



def play_game(START,END, GRID, WINDOW_SIZE, SIZE, ROWS, count, t, MARGIN, WIDTH, HEIGHT, TOTAL_GRID):
    screen = pygame.display.set_mode(WINDOW_SIZE)

    pygame.display.set_caption(f"Array Backed Grid: {count}")

    
    play = True

    #START COLORS FOR START AND FINISH
    
    GRID[START.x][START.y] = 2
    GRID[END.x][END.y] = 2
    
    clock = pygame.time.Clock()

    tracker = []

    while play: #this happens when game starts

        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    block_size = SIZE / ROWS

                    x = int(mx // block_size)
                    y = int(my // block_size)

                    num = GRID[y][x]
                    if num != 2 and num != 3 and count > 0 and num != 1: #checks if its a color other than white
                        GRID[y][x] = 1 #Sets color of the clicked to blue
                        count -= 1
                        tracker.append([y,x]) #Adds to track the positions of the walls, start, and end
                    
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    pass
        screen.fill(black)
 
        # Draw the grid
        
        pygame.display.set_caption(f"Array Backed Grid: {count}")
        
        if count == 0: #if count reaches 0 then start the finding algorithm
            count = -1
            pygame.display.set_caption("Finding Path")
            path = find(START,END, screen, tracker, TOTAL_GRID, GRID, t, ROWS, MARGIN, WIDTH, HEIGHT)
            pygame.display.set_caption("Path Found")
            drawer(path, screen, GRID, END, ROWS, MARGIN, WIDTH, HEIGHT)
            time.sleep(5)
            break
        else: #else keep waiting and drwaing wherever they click
            draw(screen,GRID,ROWS,MARGIN,WIDTH,HEIGHT)
            
        
        clock.tick(120)

        
        pygame.display.flip()
        # print("inloop")
        
    pygame.display.set_caption("Finished")
    time.sleep(10)
    exit()
