START = "start:"
FINISH = "cil:"
NEIGHBORHOOD = "seznam sousednosti:"
HEURISTICS = "vzdusna vzdalenost od cile:"



def graph_file_parser(filename):
    graph = {}
    start = None
    goal = None
    heuristics = {}

    with open(filename, 'r') as file:
        # Read start and goal
        for label in [START, FINISH]: 
            file.readline()  # Skip the label line
            value = file.readline().strip()  # Read the value
            if label == "start:":
                start = value
            else:
                goal = value

        # Skip the 'seznam sousednosti:' line
        file.readline() 

        # Parse adjacency list
        for line in file:
            line = line.strip()
            if not line: 
                continue
            if line == HEURISTICS:
                break

            node, neighbors_str = line.split(';', maxsplit=1)
            neighbors = []
            for neighbor_str in neighbors_str.split(';'):
                neighbor, weight = neighbor_str.split('=')
                neighbors.append((neighbor, int(weight)))
            graph[node] = neighbors

        # Parse heuristic distances
        for line in file:
            for dist_line in file:
                node, distance_str = dist_line.strip().split('=')
                heuristics[node] = int(distance_str)
            break

    return graph, start, goal, heuristics