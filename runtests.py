import os
from evaluate import evaluate
from os.path import basename
from main import solve

def getDirContent(basePath):
    return [os.path.join(basePath,f) for f in os.listdir(basePath)]

def getSubdirectiories(basePath):
    return filter(os.path.isdir,getDirContent(basePath))

def getFiles(basePath):
    return filter(os.path.isfile,getDirContent(basePath))

def runTests(dirs):
    baseResultPath = "results/"
    for directory in dirs:
        resultFilePath = baseResultPath + basename(directory)
        resultFile = open(resultFilePath,"w")
        testFilesNames = sorted(getFiles(directory))
        for f in testFilesNames:
            testFile = open(f,"r")
            solution = solve(testFile)
            resultFile.write(str(solution) + "\n")
            print f + " " + str(solution)
        resultFile.close()


baseTestPath = "tests/"
#get all tests dirs
dirs = getSubdirectiories(baseTestPath)
#/tests/15x15
#/tests/20x15
#/tests/20x20
#/tests/30x15
#/tests/30x20
runTests([""])


