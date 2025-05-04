import sys as System

DEBUG = False

def PerformTraceRuns():
    return "Trace Runs" in System.argv

def PerformTestRuns():
    return "Test Runs" in System.argv

def UseTextbookMethod():
    return "Textbook Method" in System.argv

def GetTextbookMethodString():
    if (UseTextbookMethod()):
        return "Textbook Method"

def UseMedianOfThreeMethod():
    return "Median Of Three Method" in System.argv

def GetMedianOfThreeMethodString():
    if (UseMedianOfThreeMethod()):
        return "Median Of Three Method"
