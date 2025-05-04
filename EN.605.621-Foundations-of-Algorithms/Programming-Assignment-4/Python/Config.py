import sys as System

DEBUG = False

def PerformTraceRuns():
    return "Trace Runs" in System.argv

def PerformTestRuns():
    return "Test Runs" in System.argv

def GetTestCase():
    return System.argv[1]

def GetS():
    return list(System.argv[2])

def GetX():
    return list(System.argv[3])

def GetY():
    return list(System.argv[4])