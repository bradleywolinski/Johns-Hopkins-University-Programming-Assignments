import Config
import os as OS

FilePath = Config.GetOutputFile()

def CreateFile():
    if OS.path.exists(FilePath):
        OS.remove(FilePath)
    open(FilePath, "x")

def Write(string = ""):
    print(string)
    WriteFileLine(string + "\n")

def WriteFileLine(string):
    with open(FilePath, "a") as File:
        File.write(string)