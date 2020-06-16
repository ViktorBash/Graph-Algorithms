"""
Will hold the graph algorithms to import to the pygame_GUI script.
Currently only have breadth first search in.
"""

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


def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]

    # return path if start is goal
    if start == goal:
        print(f"START {start}")
        return [start]
        # return "That was easy! Start = goal"

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
    return []
