# Graph Algorithms

def depthFirstPrint(graph, source):
    stack = [source]

    while len(stack) > 0:
        current = stack.pop()
        print(current)

        for neighbour in graph[current]:
            stack.append(neighbour)




graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}


# Depth first traversal: a -> b -> d: uses a stack: add to the top and remove from the top
# Using Depth first traversal: a, b, d, f, c, e


# breadth first traversal: a -> b -> c: explore all of the immediate neigbours for a node: uses a queue: add to the back remove the front
# Using Breadth first traversal: a, b, c, d, e, f


depthFirstPrint(graph, "a")


