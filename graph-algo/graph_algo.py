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



