"""
This is a GUI made with PyGame that shows breadth first search in action at the moment.
Author: Viktor Basharkevich, github.com/ViktorBash

Imports:
PyGame - GUI to store grid and user interface
"""

import pygame
from graph_algorithms import bfs_shortest_path


# Creates graph for 1-256 numbers. Is a dict with node keyed to a list of it's neighbors
# Ex: {1: [2, 17], 2: [1, 3]}
def create_graph():
    graph_to_create = {}
    for j in range(1, 257):
        neighbors = []
        possible_neighbors = [j - 16, j - 1, j + 1, j + 16]
        if (j - 1) % 16 == 0:  # Left most column
            # print(i)
            possible_neighbors = [j - 16, j + 1, j + 16]
        elif j % 16 == 0:  # Right most column
            possible_neighbors = [j - 16, j - 1, j + 16]
        for k in range(len(possible_neighbors)):
            if 1 <= possible_neighbors[k] <= 256:
                neighbors.append(possible_neighbors[k])
        graph_to_create[j] = neighbors
    return graph_to_create


graph = create_graph()


# Grid we will use to graph all nodes on PyGame, will be nested list, 16x16 with colors as the values
def create_grid():
    grid_to_create = []
    for row in range(16):
        # Add an empty array that will hold each cell
        # in this row
        grid_to_create.append([])
        for column in range(16):
            grid_to_create[row].append("WHITE")  # Append a cell
    return grid_to_create


grid = create_grid()

# Setup for PyGame
BLACK = (0, 0, 0)  # For background/margin
WHITE = (255, 255, 255)  # All cells are white at the start
GREEN = (50, 168, 82)  # Cells that are part of the path are Green
WIDTH = 30  # Width of cell
HEIGHT = 30  # Height of cell
MARGIN = 1  # Margin between each cell

pygame.init()  # Initialize PyGame
WINDOW_SIZE = [697, 497]  # Set dimensions of screen
screen = pygame.display.set_mode(WINDOW_SIZE)  # Create screen with dimensions
pygame.display.set_caption("Breadth First Search")  # Set title of window

done = False  # Will be used to end while loop when program is finished
current_click = 0  # How many times user has clicked mouse
clock = pygame.time.Clock()  # How fast the screen will refresh (set to 144hz later down)
bfs_input = [-1, -1]  # Creating arbitrary values for the Breadth First Search function
# Main loop: Checks user input to do BFS or exit program
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close, we say done = True, and close loop
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:  # When user clicks something in program
            pos = pygame.mouse.get_pos()  # User clicks the mouse. Get the position
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            try:  # If this executes, then we clicked in the grid and not outside of it
                if current_click == 0:  # Change to green (start node)
                    grid[row][column] = "GREEN"
                    # Logic to get coordinates into format for breadth first search input
                    if row == 0:
                        bfs_input[0] = column + 1
                    else:
                        bfs_input[0] = row * 16 + (column + 1)
                    current_click += 1

                elif current_click == 1:  # Change to green (end node)
                    grid[row][column] = "GREEN"
                    # Logic to get coordinates into format for breadth first search input
                    if row == 0:
                        bfs_input[1] = column + 1
                    else:
                        bfs_input[1] = row * 16 + (column + 1)
                    current_click += 1

                if current_click == 2:  # When the end node is selected, (run the algorithm)
                    path = bfs_shortest_path(graph, bfs_input[0], bfs_input[1])  # Call BFS from other script import
                    # Path is the list containing nodes from start to end
                    current_click = 0
                    for i in range(len(path)):
                        rows = 0
                        while path[i] - 16 > 0:
                            path[i] -= 16
                            rows += 1
                        path[i] -= 1
                        # print(f"row: {rows} num: {path[i]}")
                        grid[rows][path[i]] = "GREEN"
                        updated_bfs = True

            except IndexError:  # We clicked out of the grid
                print("Grid not clicked")

    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid, (stays updated)
    for row in range(16):
        for column in range(16):
            color = WHITE
            if grid[row][column] == "GREEN":
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    clock.tick(144)  # Limit to 144 frames per second
    pygame.display.flip()  # Update screen

pygame.quit()  # Exit program
