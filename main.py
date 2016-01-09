class Operation:
    def __init__(self, machine, time, job):
        self.machine = machine
        self.time = time
        self.job = job

    def __str__(self):
        return "({0}, {1}, {2})".format(self.machine, self.time, self.job)

    def __repr__(self):
        return self.__str__()

class Job:
    def __init__(self, operations):
        self.operations = operations

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
        self.jobs = jobs
        self.machineOperations = [[] for i in range(numberOfMachines)]
        for job in self.jobs:
            for op in job.operations:
                self.machineOperations[op.machine].append(op)

    def __directedEdges(self):
        paired = [pair(job.operations) for job in self.jobs]
        return flatten(paired)

    def __undirectedEdges(self):
        paired = [cyclePair(operations) for operations in self.machineOperations]
        directed = flatten(paired)
        return directed + [edge[::-1] for edge in directed]

    def asGraph(self):
        initial = "START"
        last = "END"
        initialEdges = [(initial, job.operations[0]) for job in self.jobs]
        lastEdges = [(job.operations[-1], last) for job in self.jobs]
        directed = initialEdges + self.__directedEdges() + lastEdges
        return ProblemGraph(initial, last, directed, self.__undirectedEdges())

class ProblemGraph:
    def __init__(self, initial, end, directedEdges, undirectedEdges):
        self.initial = initial
        self.end = end
        self.directedEdges = directedEdges
        self.undirectedEdges = undirectedEdges

    def __str__(self):
        return str(self.__dict__)

problem = \
    Problem(2,
        [ Job(
            [ Operation(0, 2, 0)
            , Operation(1, 2, 0)
            ])
        , Job(
            [ Operation(1, 3, 1)
            , Operation(0, 3, 1)
            ])
        ]
    )

expectedGraph = \
    ProblemGraph("START", "END",
        [ ("START", Operation(0, 2, 0))
        , ("START", Operation(1, 3, 1))
        , (Operation(0, 2, 0), Operation(1, 2, 0))
        , (Operation(1, 3, 1), Operation(0, 3, 1))
        , (Operation(1, 2, 0), "END")
        , (Operation(0, 3, 1), "END")
        ]
    ,
        [ (Operation(0, 2, 0), Operation(0, 3, 1))
        , (Operation(1, 2, 0), Operation(1, 3, 1))
        , (Operation(0, 3, 1), Operation(0, 2, 0))
        , (Operation(1, 3, 1), Operation(1, 2, 0))
        ]
    )

print(problem.asGraph())
print(expectedGraph)
