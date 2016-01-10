from evaluate import evaluate

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

class Solution:
    def __init__(self, problem):
        self.problem = problem

        self.START = len(problem.operations)
        self.END = len(problem.operations) + 1

        self.directed = [[] for x in range(0, len(problem.operations) + 2)]
        self.directed[self.START] = [Edge(job[0], False) for job in problem.jobs]
        for job in problem.jobs:
            self.directed[job[-1]].append(Edge(self.END, False))
        for (s, e) in self.__directedEdges(problem.jobs):
            self.directed[s].append(Edge(e, False))

        self.__initialSolution()

    def time(self, operationId):
        if operationId != solution.START and operationId != solution.END:
            return self.problem.operations[operationId].time
        return 0

    def __initialSolution(self):
        # Assumption: machine operations in problem are filled job by job
        # Warning: it can create duplicate edges, is that a problem?
        for ops in problem.machineOperations:
            for (s, e) in pair(ops):
                self.directed[s].append(Edge(e, True))

    def __directedEdges(self, jobs):
        paired = [pair(job) for job in jobs]
        return flatten(paired)

    def __str__(self):
        return str(self.__dict__)




problem = Problem(2, [ [(0, 2), (1, 2), (0, 1)], [(1, 3), (0, 3), (0, 4)] ] )
solution = Solution(problem)
print(problem)
print(solution)

print(evaluate(solution))
