from collections import deque

#bfs algorithm 
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft() 
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")
            queue.extend([node for node in graph[vertex] if node not in visited])


#dfs algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=" ")
    
    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)



def move_disks_bfs(num_disks):
    start = (tuple(range(1, num_disks + 1)), tuple(), tuple())
    target = (tuple(), tuple(), tuple(range(1, num_disks + 1)))
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        state, path = queue.popleft()
        if state == target:
            return path + [target]
        
        for i, source in enumerate(state):
            if source:
                for j in range(3):
                    if i != j:
                        if not state[j] or source[0] < state[j][0]:
                            new_state = list(map(list, state))
                            disk = new_state[i].pop(0)
                            new_state[j].insert(0, disk)
                            new_state = tuple(map(tuple, new_state))
                            if new_state not in visited:
                                visited.add(new_state)
                                queue.append((new_state, path + [(state, new_state)]))
    return []




def move_disks_dfs(num_disks):
    start = (tuple(range(1, num_disks + 1)), tuple(), tuple())
    target = (tuple(), tuple(), tuple(range(1, num_disks + 1)))
    stack = [(start, [])]
    visited = set([start])

    while stack:
        state, path = stack.pop()
        if state == target:
            return path + [target]
        
        for i, source in enumerate(state):
            if source:
                for j in range(3):
                    if i != j:
                        if not state[j] or source[0] < state[j][0]:
                            new_state = list(map(list, state))
                            disk = new_state[i].pop(0)
                            new_state[j].insert(0, disk)
                            new_state = tuple(map(tuple, new_state))
                            if new_state not in visited:
                                visited.add(new_state)
                                stack.append((new_state, path + [(state, new_state)]))
    return []


def move_disks_bfs_verbose(num_disks):
    start = (tuple(range(1, num_disks + 1)), tuple(), tuple())
    target = (tuple(), tuple(), tuple(range(1, num_disks + 1)))
    queue = deque([(start, [(start,)])])
    visited = set([start])

    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        
        for i, source in enumerate(state):
            if source:
                for j in range(3):
                    if i != j:
                        if not state[j] or source[0] < state[j][0]:
                            new_state = list(map(list, state))
                            disk = new_state[i].pop(0)
                            new_state[j].insert(0, disk)
                            new_state_tuple = tuple(map(tuple, new_state))
                            if new_state_tuple not in visited:
                                visited.add(new_state_tuple)
                                queue.append((new_state_tuple, path + [new_state_tuple]))
    return []

steps_bfs = move_disks_bfs_verbose(3)

def move_disks_dfs_verbose(num_disks):
    def dfs(state, path, visited):
        if state == target:
            return path
        
        for i, source in enumerate(state):
            if source:
                for j in range(3):
                    if i != j and (not state[j] or source[0] < state[j][0]):
                        new_state = list(map(list, state))
                        disk = new_state[i].pop(0)
                        new_state[j].insert(0, disk)
                        new_state_tuple = tuple(map(tuple, new_state))
                        if new_state_tuple not in visited:
                            visited.add(new_state_tuple)
                            result = dfs(new_state_tuple, path + [new_state_tuple], visited)
                            if result is not None:
                                return result
        return None

    start = (tuple(range(1, num_disks + 1)), tuple(), tuple())
    target = (tuple(), tuple(), tuple(range(1, num_disks + 1)))
    visited = set([start])
    steps = dfs(start, [start], visited)
    
    for index, step in enumerate(steps):
        print(f"Krok {index + 1}: {step}")


move_disks_dfs_verbose(3)


for index, step in enumerate(steps_bfs):
    print(f"Krok {index + 1}: {step} - Přesun disku z {('prvního', 'druhého', 'třetího')[index % 3]} sloupu na {('první', 'druhý', 'třetí')[index % 3]} sloup.")

