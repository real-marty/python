import heapq
import parser_1

def a_star(maze, start, goal):
    """
    Finds the shortest path using the A* algorithm.

    Args:
        maze: A 2D list representing the maze. Each element can be:
              - 0: An open space
              - 1: An obstacle
        start: Starting coordinates (row, col)
        goal: Goal coordinates (row, col)

    Returns:
        A list of coordinates representing the path from start to goal,
        or None if no path exists.
    """

    num_rows = len(maze)
    num_cols = len(maze[0])

    # Define heuristic function (Manhattan distance is common)
    def heuristic(pos):
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

    # Create sets for tracking visited and open nodes
    visited = set()
    open_heap = []  # Use a heap for efficient priority access

    # Add the starting node
    heapq.heappush(open_heap, (heuristic(start), start))

    # Keep track of where we came from for path reconstruction
    came_from = {}

    # Cost so far
    g_score = {start: 0}

    while open_heap:
        _, current = heapq.heappop(open_heap)

        if current == goal:
            return reconstruct_path(came_from, current)

        visited.add(current)

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # 4-way movement
            neighbor = (current[0] + dx, current[1] + dy)

            # Check for valid movement (within bounds and not an obstacle)
            if (0 <= neighbor[0] < num_rows and 
                0 <= neighbor[1] < num_cols and 
                maze[neighbor[0]][neighbor[1]] != 1):

                tentative_g_score = g_score[current] + 1 

                if neighbor not in visited and (neighbor not in g_score or tentative_g_score < g_score[neighbor]):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor)
                    heapq.heappush(open_heap, (f_score, neighbor))

    return None  # No path found

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path

# Example usage
maze = [
    [0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
]
start = (0, 0)
goal = (4, 4)

path = a_star(maze, start, goal)
print(path) 


def a_star_graph(graph, start, goal, heuristic):
    """
    Finds the shortest path using A* algorithm on a graph.

    Args:
        graph: A dictionary representing the graph, where keys are nodes
               and values are lists of tuples (neighbor, cost).
        start: The starting node
        goal: The goal node

    Returns:
        A list of nodes representing the path from start to goal,
        or None if no path exists.
    """

    # Define heuristic function 
    def heuristic(node):
        if node in heuristics_:  # If a heuristic is provided, use it 
            return heuristics_[node]
        else:
            return 0

    visited = set()
    open_heap = []
    heapq.heappush(open_heap, (heuristic(start), start))

    came_from = {}
    g_score = {start: 0}

    while open_heap:
        _, current = heapq.heappop(open_heap)

        if current == goal:
            return reconstruct_path(came_from, current)

        visited.add(current)

        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost

            if neighbor not in visited and (neighbor not in g_score or tentative_g_score < g_score[neighbor]):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor)
                heapq.heappush(open_heap, (f_score, neighbor))

    return None  # No path found

# ... (reconstruct_path function remains the same)

graph_, start_, goal_, heuristics_ = parser_1.graph_file_parser('cv4_vstup_test.txt')

path = a_star_graph(graph_, start_, goal_, heuristics_)
print(path)


graph_, start_, goal_, heuristics_ = parser_1.graph_file_parser('cv4_vstup.txt')
path = a_star_graph(graph_, start_, goal_, heuristics_)
print(path)



# Example Usage:
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('D', 5)],
    'C': [('A', 4), ('D', 1), ('G', 3)],
    'D': [('B', 5), ('C', 1), ('G', 2)],
    'G': [('C', 3), ('D', 2)]
}
start = 'A'
goal = 'G'

path = a_star_graph(graph, start, goal, None)
print(path) 