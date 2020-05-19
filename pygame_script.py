
# graph = {'A': ['B', 'C', 'E'],
#          'B': ['A' ,'D', 'E'],
#          'C': ['A', 'F', 'G'],
#          'D': ['B'],
#          'E': ['A', 'B' ,'D'],
#          'F': ['C'],
#          'G': ['C']}
# graph = {1: [2, 3, 4],
#          2: [1],
#          }
graph = {}
for i in range(1, 257):
    neighbors = []
    possible_neighbors = [i-16, i-1, i+1, i+16]
    if (i -1) % 16 == 0:  # Left most column
        # print(i)
        possible_neighbors = [i - 16, i + 1, i + 16]
    elif i % 16 == 0:  # Right most column
        possible_neighbors = [i - 16, i - 1, i + 16]
    for k in range(len(possible_neighbors)):
        if 1 <= possible_neighbors[k] <= 256:
            neighbors.append(possible_neighbors[k])
    graph[i] = neighbors

print(graph)
# print(graph)
# for row in range(1, 11):
#     for column in range(1, 11):
#         num = column
#         left_to_add = row
#         if row > 1 and left_to_add > 0:
#             num += 10
#             left_to_add -= 1
#
#         print(num)



# graph = {1: [],}

# # visits all the nodes of a graph (connected component) using BFS
# def bfs_connected_component(graph, start):
#     # keep track of all visited nodes
#     explored = []
#     # keep track of nodes to be checked
#     queue = [start]
#
#
# # visits all the nodes of a graph (connected component) using BFS
# def bfs_connected_component(graph, start):
#     # keep track of all visited nodes
#     explored = []
#     # keep track of nodes to be checked
#     queue = [start]
#
#     # keep looping until there are nodes still to be checked
#     while queue:
#         # pop shallowest node (first node) from queue
#         node = queue.pop(0)
#         if node not in explored:
#             # add node to list of checked nodes
#             explored.append(node)
#             neighbours = graph[node]
#
#             # add neighbours of node to queue
#             for neighbour in neighbours:
#                 queue.append(neighbour)
#     return explored


# print(bfs_connected_component(graph, 'A'))  # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']


# finds shortest path between 2 nodes of a graph using BFS


import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell
MARGIN = 1

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(16):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(16):
        grid[row].append("WHITE")  # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[1][5] = 1

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [497, 497]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Loop until the user clicks the close button.
done = False
current_click = 0
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
bfs_input =[-1, -1]
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            # grid[row][column] = 1

            if current_click == 0:  # Change to green (start node)
                grid[row][column] = "GREEN"

                if row == 0:
                    bfs_input[0] = column + 1
                else:
                    bfs_input[0] = row * 16 + (column + 1)
                    # print(row)
                    # print(column)
                    # print(bfs_input[0])

                current_click += 1
            elif current_click == 1:  # Change to red (end node)
                grid[row][column] = "RED"
                if row == 0:
                    bfs_input[1] = column + 1
                else:
                    bfs_input[1] = row * 16 + (column + 1)
                current_click += 1
            # print("Click ", pos, "Grid coordinates: ", row, column)
            def bfs_shortest_path(graph, start, goal):
                # keep track of explored nodes
                explored = []
                # keep track of all the paths to be checked
                queue = [[start]]

                # return path if start is goal
                if start == goal:
                    return "That was easy! Start = goal"

                # keeps looping until all possible paths have been checked
                while queue:
                    # pop the first path from the queue
                    path = queue.pop(0)
                    # get the last node from the path
                    node = path[-1]
                    if node not in explored:
                        neighbours = graph[node]
                        # go through all neighbour nodes, construct a new path and
                        # push it into the queue
                        for neighbour in neighbours:
                            new_path = list(path)
                            new_path.append(neighbour)
                            queue.append(new_path)
                            # return path if neighbour is goal
                            if neighbour == goal:
                                return new_path

                        # mark node as explored
                        explored.append(node)

                # in case there's no path between the 2 nodes
                return "So sorry, but a connecting path doesn't exist :("

            if current_click == 2:
                print(f"Input {bfs_input}")
                print(f"Shortest Path{bfs_shortest_path(graph, bfs_input[0], bfs_input[1])}")  # returns ['G', 'C', 'A', 'B', 'D']
                path = bfs_shortest_path(graph, bfs_input[0], bfs_input[1])
                # Path is the list containing path from start to end ^
                current_click += 1

                for i in range(len(path)):
                    rows = 0
                    while path[i] - 16 > 0:
                        path[i] -= 16
                        rows += 1
                    path[i] -= 1
                    print(f"row: {rows} num: {path[i]}")
                    grid[rows][path[i]] = "RED"

    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(16):
        for column in range(16):
            color = WHITE
            if grid[row][column] == "GREEN":
                color = GREEN
            elif grid[row][column] == "RED":
                color = RED
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
