from collections import defaultdict


##function add edges to graph

graph = defaultdict(list)

def addEdge(graph, u, v):
    graph[u].append(v)
    
def generate_edges(graph):
    edges = []

    for node in graph:
        
        for neighbour in graph[node]:
            
            edges.append((node, neighbour))
        
    return edges
        
        
addEdge(graph, 'a','c')
addEdge(graph, 'b','e')
addEdge(graph, 'f','g')
addEdge(graph, 'i','h')

print(generate_edges(graph))

graph = [('a', 'c'), ('b', 'e'), ('f', 'g'), ('i', 'h')]



def shortestPath(graph, start, end , path = []):
    print(graph)
    path = path + [start]
    if start == end:
        return path
    shortest = None
    for node in graph[start]:
        newPath = shortestPath(graph, node , end, path)
        if newPath:
            if not shortest or len(newpath) < len(shortest):
                shortest = newpath
        return shortest
    
print(shortestPath(graph,'f','i'))
        