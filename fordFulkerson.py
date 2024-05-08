graph = {
    'A': ['B','C','D'],
    'B': ['A','C','E'],
    'C': ['A','B','D','E'],
    'D': ['A','C','E','F'],
    'E': ['B','C','D','G'],
    'F': ['D','G'],
    'G': ['E','F'],
}
adjMat = [[0,3,0,3,0,0,0],
          [0,0,4,0,0,0,0],
          [3,0,0,1,2,0,0],
          [0,0,0,0,2,6,0],
          [0,1,0,0,0,0,1],
          [0,0,0,0,0,0,9],
          [0,0,0,0,0,0,0]]
order = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
}

def dfs(start,goal):
    visited = list()
    stack = [[start,[]]]

    while stack:
        current, path = stack.pop()

        if current == goal:
            temp = (path+[current])
            return temp
        
        if current not in visited:
            visited.append(current)
            neighbours = graph[current]
            for neighbour in neighbours:
                if neighbour not in visited and adjMat[order[current]][order[neighbour]]!=0:
                    stack.append([neighbour,path+[current]])
    
    return 0

def fordFulkerson(source,sink):
    maxflow = -1
    while True:
        path = dfs(source,sink)
        if path!=0:
            min = 9999
            for i in range(len(path)-1):
                temp = adjMat[order[path[i]]][order[path[i+1]]]
                if temp<min:
                    min = temp
            for i in range(len(path)-1):
                adjMat[order[path[i]]][order[path[i+1]]]-=min
                adjMat[order[path[i+1]]][order[path[i]]]+=min
            maxflow+=min
            print(f"PATH : {path}")
            print(adjMat)
            print(f"PATH FLOW: {min}\n")
        else:
            break
    print(f"MAX FLOW: {maxflow}")

fordFulkerson('A','G')