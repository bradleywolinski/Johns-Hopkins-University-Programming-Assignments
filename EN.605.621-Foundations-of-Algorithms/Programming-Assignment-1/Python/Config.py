import sys as System

DEBUG = False

def GET_PERFORM_TRACE_RUNS():
    if (len(System.argv) == 1):
        return False
    return System.argv[1] == "Trace Runs"

def GET_PERFORM_TEST_RUNS():
    if (len(System.argv) == 1):
        return False
    return System.argv[1] == "Test Runs"