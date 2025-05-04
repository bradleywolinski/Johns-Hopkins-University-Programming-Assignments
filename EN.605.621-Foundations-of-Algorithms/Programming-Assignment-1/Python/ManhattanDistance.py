import Config

class Point:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

class DataEntry:
    """
    Contains two points, P1 and P2. \n
    Contains the manhattan distance, between the two points.
    """
    def __init__(self, P1, P2):
        self.P1 = P1
        self.P2 = P2
        self.ManhattanDistance = CalculateManhattanDistance(P1, P2)

def CalculateManhattanDistance(P1, P2):
    return abs(P1.X - P2.X) + abs(P1.Y - P2.Y)

def CalculateClosestPoints(P, m):
    ClosestPoints = []

    KeyPointCount = 0

    # loop through entire list one at a time
    i = 0
    while (i < len(P)):

        if (Config.GET_PERFORM_TRACE_RUNS()):
            print()
            print("Current P[i]: P[{}] : ({}, {})".format(i, P[i].X, P[i].Y))
            print("------------------------------------------------------------------------------------------------------------------------")

        # on each iteration, compare to all other points (start at j = i because all previous indices have been checked already)
        j = i + 1
        while (j < len(P)):
            CurrDataPoint = DataEntry(P[i], P[j])

            if (Config.GET_PERFORM_TRACE_RUNS()):
                print("- Current P[j]: P[{}] : ({}, {})".format(j, P[j].X, P[j].Y, CurrDataPoint.ManhattanDistance))
                print("- Manhattan Distance : {}".format(CurrDataPoint.ManhattanDistance))
                print()

            PointInserted = False

            # loop through list of closest points
            k = 0
            while (k < len(ClosestPoints) and not PointInserted):

                # if current distance is less than an existing closest distance
                if (CurrDataPoint.ManhattanDistance < ClosestPoints[k].ManhattanDistance):

                    if (Config.GET_PERFORM_TRACE_RUNS()):
                        print("- Result: Current Manhattan Distance < Some Point In Closest Points : Insert Into Sorted Points")

                    # insert current point at current index, all points of greater distance will be shifted
                    ClosestPoints.insert(k, CurrDataPoint)

                    PointInserted = True

                    # pop off end of list at capacity, removes point with the longest distance
                    if (len(ClosestPoints) > m):
                        
                        if (Config.GET_PERFORM_TRACE_RUNS()):
                            print("- Insert Caused List Overflow : Pop Last Index")

                        ClosestPoints.pop()

                KeyPointCount = KeyPointCount + 1
                k = k + 1

            # current distance is greater than all existing distances but list is not at capacity
            if (len(ClosestPoints) < m):
                
                if (Config.GET_PERFORM_TRACE_RUNS()):
                    if (len(ClosestPoints) == 0):
                        print("- Result: List Empty : Append")
                    else:
                        print("- Result: Current Manhattan Distance Larger Than Any In Sorted Array : List Is Not Full : Append")

                ClosestPoints.append(CurrDataPoint)
            else:
                if (Config.GET_PERFORM_TRACE_RUNS()):
                    if (not PointInserted):
                        print("- Result: Current Manhattan Distance Larger Than Any In Sorted Array: List Is Full : Do Nothing")

            if (Config.GET_PERFORM_TRACE_RUNS()):
                print()
                print("- List After Iteration:")
                for l in range(len(ClosestPoints)):
                    print("- P[{}] : P1({}, {}) : P2({}, {}) : {}".format(l,
                                                                          ClosestPoints[l].P1.X, 
                                                                          ClosestPoints[l].P1.Y, 
                                                                          ClosestPoints[l].P2.X, 
                                                                          ClosestPoints[l].P2.Y, 
                                                                          ClosestPoints[l].ManhattanDistance))
                print(("------------------------------------------------------------------------------------------------------------------------"))

            KeyPointCount = KeyPointCount + 1
            j = j + 1

        KeyPointCount = KeyPointCount + 1
        i = i + 1

    if (Config.GET_PERFORM_TRACE_RUNS()):
        print()
        print("CalculateClosestPoints Method Completed")

    return ClosestPoints, KeyPointCount