# Graph Algorithms

def depthFirstPrint(graph, source):
    stack = [source]

    while len(stack) > 0:
        current = stack.pop()
        print(current)

        for neighbour in graph[current]:
            stack.append(neighbour)



def depthFirstRecursivePrint(graph, source):
    print(source)
    for neighbour in graph[source]:
        depthFirstRecursivePrint(graph, neighbour)


from collections import deque

def breadthFirstPrint(graph, source):
    queue = deque([source])
    
    while len(queue) > 0:
        current = queue.popleft()
        print(current)
        # then consider the neighbours
        for neighbour in graph[current]:
            queue.append(neighbour)

        

# using an adjacency list to represent the graph
graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

graph_2 = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}





# Depth first traversal: a -> b -> d: uses a stack: add to the top and remove from the top
# Using Depth first traversal: a, b, d, f, c, e


# breadth first traversal: a -> b -> c: explore all of the immediate neigbours for a node: uses a queue: add to the back remove the front
# Using Breadth first traversal: a, b, c, d, e, f |||| a, c, b, e, d, f 


print("Depth First Traversal!")
depthFirstPrint(graph, "a")
print("===================================")
print("using recursion!")
depthFirstRecursivePrint(graph_2, "a")
print()
print("Breadth First Traversal!")
breadthFirstPrint(graph, "a")



# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import deque

def solution(N, A, B, H):
    # structure out the graph; an empty list of list
    graph = [[] for _ in range(N)]
    for u, v in zip(A, B):
        graph[u].append(v)
        graph[v].append(u)

    # consider every district to be infinitely far away
    dist = [float('inf')] * N

    # create queue for BFS
    queue = deque()
 
    # start BFS from all hospitals at the same time
    for hospital in H:
        dist[hospital] = 0
        queue.append(hospital)
    
    # Multi source BFS traversal
    while queue:
        current = queue.popleft()

        # visit all neighbouring districts
        for neighbour in graph[current]:
            if dist[neighbour] == float('inf'):
                dist[neighbour] = dist[current] + 1
                queue.append(neighbour)
    # is any district unreachable in terms of it being infinitely far away
    if any(d == float('inf') for d in dist):
        return -1
    return max(dist)
