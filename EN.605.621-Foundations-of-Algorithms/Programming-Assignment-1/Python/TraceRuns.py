import ManhattanDistance

def TraceRun_CalculateManhattanDistance():
    print("#############")
    print("# Trace Run #")
    print("#############")
    print()
    print("Conducting Trace Run For CalculateManhattanDistance Method")
    print()

    P1 = ManhattanDistance.Point(13, 23)
    P2 = ManhattanDistance.Point(0, 0)
    print("Testing P1 > P2")
    print("- P1({}, {}) : P2({}, {})".format(P1.X, P1.Y, P2.X, P2.Y))
    print("- Distance = {}".format(ManhattanDistance.CalculateManhattanDistance(P1, P2)))
    print()

    P1 = ManhattanDistance.Point(-3, -9)
    P2 = ManhattanDistance.Point(0, 0)
    print("Testing P1 < P2")
    print("- P1({}, {}) : P2({}, {})".format(P1.X, P1.Y, P2.X, P2.Y))
    print("- Distance = {}".format(ManhattanDistance.CalculateManhattanDistance(P1, P2)))
    print()

    print("Testing P1 = P2")
    P1 = ManhattanDistance.Point(5, 5)
    P2 = ManhattanDistance.Point(5, 5)
    print("- P1({}, {}) : P2({}, {})".format(P1.X, P1.Y, P2.X, P2.Y))
    print("- Distance = {}".format(ManhattanDistance.CalculateManhattanDistance(P1, P2)))
    print()

def TraceRun_CalculateClosestPoints():
    print("#############")
    print("# Trace Run #")
    print("#############")
    print()
    print("Conducting Trace Run For CalculateClosestPoints Method")
    print()

    P = [ManhattanDistance.Point(0, 0), 
         ManhattanDistance.Point(1, 1), 
         ManhattanDistance.Point(2, 2),
         ManhattanDistance.Point(3, 3), 
         ManhattanDistance.Point(4, 4)]

    print("Input List:")
    for i in range(len(P)):
        print("- P[{}] : ({}, {})".format(i, P[i].X, P[i].Y))

    ClosestPoints, KeyPointCount = ManhattanDistance.CalculateClosestPoints(P, 3)

    print()
    print("Output List:")
    for i in range(len(ClosestPoints)):
        print("- P[{}] : P1({}, {}) : P2({}, {}) : {}".format(i,
                                                              ClosestPoints[i].P1.X, 
                                                              ClosestPoints[i].P1.Y, 
                                                              ClosestPoints[i].P2.X, 
                                                              ClosestPoints[i].P2.Y, 
                                                              ClosestPoints[i].ManhattanDistance))
    print()

def PerformTraceRuns():
    TraceRun_CalculateManhattanDistance()
    TraceRun_CalculateClosestPoints()