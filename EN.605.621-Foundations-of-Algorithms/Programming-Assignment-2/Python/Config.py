import sys as System

DEBUG = False

def PerformTraceRuns():
    if (len(System.argv) == 1):
        return False
    return "Trace Runs" in System.argv

def PerformTestRuns():
    if (len(System.argv) == 1):
        return False
    return "Test Runs" in System.argv

def RunPartA():
    if (len(System.argv) == 1):
        return False
    return "Part A" in System.argv

def RunPartB1():
    if (len(System.argv) == 1):
        return False
    return "Part B1" in System.argv

def RunPartB2():
    if (len(System.argv) == 1):
        return False
    return "Part B2" in System.argv

def RunPartB3():
    if (len(System.argv) == 1):
        return False
    return "Part B3" in System.argv

def GetM():
    return list(System.argv[2])

def GetN():
    return list(System.argv[3])

def GetOutputFile():
    return System.argv[4]