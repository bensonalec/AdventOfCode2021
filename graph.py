from collections import defaultdict

class Edge:
    def __init__(self, parent, child ,weight):
        self.parent = parent
        self.child = child
        self.weight = weight

class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False
    def addEdge(self,edge):
        self.edges.append(edge)
    def __repr__(self):
        return f"Node({self.value}, {len(self.edges)})"

def aStar(startNode, targetCritera, h):
    def reconstructPath(cameFrom, current):
        totalPath = [current]
        while current in cameFrom.keys():
            current = cameFrom[current]
            totalPath.insert(0,current)
        return totalPath
    openSet = [startNode]
    cameFrom = {}
    gScore = defaultdict(lambda: float('inf'))
    gScore[startNode] = 0
    fScore = defaultdict(lambda: float('inf'))
    fScore[startNode] = 0
    while len(openSet) > 0:
        current = min(openSet, key=lambda x: fScore[x])
        if targetCritera(current):
            return reconstructPath(cameFrom, current)
        q = openSet.pop(openSet.index(current))
        for edge in q.edges:
            neighbor = edge.child
            tentative_gScore = gScore[current] + edge.weight
            if tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + h(neighbor)
                try:
                    openSet.index(neighbor)
                except ValueError:
                    openSet.append(neighbor)
    return "Failed"
