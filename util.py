import os
from os.path import basename

def getDirContent(basePath):
    return [os.path.join(basePath,f) for f in os.listdir(basePath)]

def getSubdirectiories(basePath):
    return filter(os.path.isdir,getDirContent(basePath))

def getFiles(basePath):
    return filter(os.path.isfile,getDirContent(basePath))