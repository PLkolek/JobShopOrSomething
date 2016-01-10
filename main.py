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

class Solution:
    def __init__(self, problem):
        self.problem = problem

        self.START = len(problem.operations)
        self.END = len(problem.operations) + 1

        self.directed = [[] for x in range(0, len(problem.operations) + 2)]
        self.directed[self.START] = [job[0] for job in problem.jobs]
        for job in problem.jobs:
            self.directed[job[-1]].append(self.END)
        for (s, e) in self.__directedEdges(problem.jobs):
            self.directed[s].append(e)

        self.undirected = self.__undirectedEdges(problem.machineOperations)
        self.__initialSolution()

    def __initialSolution(self):
        # Assumption: machine operations in problem are filled job by job
        # Warning: it can create duplicate edges, is that a problem?
        for ops in problem.machineOperations:
            for (s, e) in pair(ops):
                self.directed[s].append(e)

    def __directedEdges(self, jobs):
        paired = [pair(job) for job in jobs]
        return flatten(paired)

    def __undirectedEdges(self, machineOperations):
        paired = [cyclePair(operations) for operations in machineOperations]
        directed = flatten(paired)
        return directed + [edge[::-1] for edge in directed]

    def __str__(self):
        return str(self.__dict__)

problem = Problem(2, [ [(0, 2), (1, 2), (0, 1)], [(1, 3), (0, 3), (0, 4)] ] )
print(problem)
print(Solution(problem))
