from evaluate import evaluate
import copy

class Operation:
    def __init__(self, id, machine, time, job):
        self.id = id
        self.machine = machine
        self.time = time
        self.job = job

    def __str__(self):
        return "({0}, {1}, {2})".format(self.machine, self.time, self.job)

    def __repr__(self):
        return self.__str__()

def pair(l):
    return list(zip(l[:-1], l[1:]))

def pairAll(l):
    result = []
    for i in range(0, len(l)):
        for j in range(i + 1, len(l)):
            result.append((l[i], l[j]))
    return result

def cyclePair(l):
    if len(l) <= 3:
        return pair(l)
    cycled = l[1:]
    cycled.append(l[0])
    return list(zip(l, cycled))

def flatten(list):
    return [item for sublist in list for item in sublist]

class Problem:
    def __init__(self, numberOfMachines, jobs):
        self.numberOfMachines = numberOfMachines
        self.jobs = []
        self.machineOperations = [[] for i in range(numberOfMachines)]
        self.operations = []
        for jobI in range(0, len(jobs)):
            self.jobs.append([])
            for (machine, time) in jobs[jobI]:
                op = Operation(len(self.operations), machine, time, jobI)
                self.jobs[jobI].append(op.id)
                self.operations.append(op)
                self.machineOperations[op.machine].append(op.id)
    def __str__(self):
        return str(self.__dict__)

class Edge:
    def __init__(self, target, reversable):
        self.target = target
        self.reversable = reversable
    def __str__(self):
        return str(self.__dict__)
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        return self.target == other.target and self.reversable == other.reversable

class Solution:
    @staticmethod
    def initial(problem):
        START = len(problem.operations)
        END = len(problem.operations) + 1

        edges = [[] for x in range(0, len(problem.operations) + 2)]
        edges[START] = [Edge(job[0], False) for job in problem.jobs]
        for job in problem.jobs:
            edges[job[-1]].append(Edge(END, False))

        paired = [pair(job) for job in problem.jobs]
        jobEdges = flatten(paired)
        for (s, e) in jobEdges:
            edges[s].append(Edge(e, False))

        # Assumption: machine operations in problem are filled job by job
        # Warning: it can create duplicate edges, is that a problem?
        for ops in problem.machineOperations:
            for (s, e) in pairAll(ops):
                edges[s].append(Edge(e, True))
        return Solution(problem, START, END, edges)

    def __init__(self, problem, start, end, edges):
        self.problem = problem
        self.START = start
        self.END = end
        self.edges = edges

    def time(self, operationId):
        if operationId != solution.START and operationId != solution.END:
            return self.problem.operations[operationId].time
        return 0

    def neighbours(self, criticalPath):
        neighbours = []
        for (s, e) in pair(criticalPath):
            if self.__hasReversableEdge(s, e):
                neighbours.append(solution.__revertedEdge(s, e))
        return neighbours

    def __hasReversableEdge(self, s, e):
        return Edge(e, True) in self.edges[s]

    def __revertedEdge(self, s, e):
        edgesCopy = [copy.copy(edges) for edges in self.edges]
        edgesCopy[s].remove(Edge(e, True))
        edgesCopy[e].append(Edge(s, True))
        return Solution(self.problem, self.START, self.END, edgesCopy)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()



problem = Problem(2, [ [(0, 2), (1, 2), (0, 1)], [(1, 3), (0, 3), (0, 4)] ] )
solution = Solution.initial(problem)
print(problem)
print(solution)

(path, length) = evaluate(solution)
print((path, length))

print(solution.neighbours(path))
