class VertexMetadata:
    def __init__(self):
        self.inDegree = 0
        self.longestPath = 0
        self.previousV = -1
    def __str__(self):
        return str(self.__dict__)
    def __repr__(self):
        return self.__str__()


def evaluate(solution):
    v = [VertexMetadata() for i in range(0, len(solution.edges))]
    __inDegrees(solution, v)
    noInputV = [solution.START]
    while noInputV:
        current = noInputV.pop()
        path = v[current].longestPath + solution.time(current)

        for edge in solution.edges[current]:
            adj = edge.target
            v[adj].inDegree -= 1
            if path >= v[adj].longestPath:
                v[adj].longestPath = path
                v[adj].previousV = current
            if v[adj].inDegree == 0:
                noInputV.append(adj)

    __checkCycle(v, solution)
    path = __criticalPath(solution, v)
    pathLength = v[solution.END].longestPath
    return (path, pathLength)

def __inDegrees(solution, v):
    for s in range(0, len(solution.edges)):
        for e in solution.edges[s]:
            v[e.target].inDegree += 1

def __checkCycle(v, solution):
    if v[solution.END].inDegree != 0:
        print("Cycle detected, current graph is: ")
        print(solution)
        print("Subgraph with cycle is: ")
        print(__graphLeft(v))
        raise "Suicide"

def __graphLeft(v):
    vi = [(i, v[i]) for i in range(0, len(v))]
    res = []
    for (i, m) in vi:
        if m.inDegree > 0:
            res.append(i)
    return res


def __criticalPath(solution, v):
    path = []
    current = v[solution.END].previousV
    while current != solution.START:
        path.append(current)
        current = v[current].previousV
    return list(reversed(path))
