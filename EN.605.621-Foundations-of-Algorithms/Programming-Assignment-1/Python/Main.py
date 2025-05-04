import Config
import TraceRuns
import TestRuns

def Main():
    if (Config.GET_PERFORM_TRACE_RUNS()):
        TraceRuns.PerformTraceRuns()
    elif (Config.GET_PERFORM_TEST_RUNS()):
        TestRuns.PerformTestRuns()
    else:
        print("No Arguments Supplied")

Main()