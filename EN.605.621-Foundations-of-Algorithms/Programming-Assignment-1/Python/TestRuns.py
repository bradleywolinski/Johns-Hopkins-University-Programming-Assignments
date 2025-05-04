import ManhattanDistance
import math as Math
import random as Random
import matplotlib.pyplot as Plot 

def TestRun_CalculateClosestPoints():
    print("############")
    print("# Test Run #")
    print("############")
    print()
    print("Conducting Test Runs For CalculateClosestPoints Method")
    print()

    TestPoints = [10, 25, 50, 100, 250]

    # generate and plot asymptotic points

    TheoreticalX = list(range(TestPoints[0], TestPoints[len(TestPoints) - 1] + 1))
    AsymptoticY = [(n * n * n * n) for n in TheoreticalX]

    Plot.plot(TheoreticalX, AsymptoticY, label="Asymptotic Worst-Case $(n^4)$", color="green")

    # generate and plot precise worst case points

    TheoreticalY = [(n * (n - 1) / 4) * (n * (n - 1) / 2) for n in TheoreticalX]

    Plot.plot(TheoreticalX, TheoreticalY, label=r'Precise Worst-Case ($\frac{n^2(n-1)^2}{8}$)', color="blue")

    # generate and plot test points

    TestResults = []

    for i in (range(len(TestPoints))):
        print("Conducting Test Run: n = {}".format(TestPoints[i]))
        
        print("- Generating Random Points...")
        P = []
        for j in range(TestPoints[i]):
            P.append(ManhattanDistance.Point(Random.randrange(-1000, 1001), Random.randrange(-1000, 1001)))

        m = Math.comb(TestPoints[i], 2)
        print("- Running CalculateClosestPoints Method On Array P (m = {})...".format(m))

        ClosestPoints, KeyActionCount = ManhattanDistance.CalculateClosestPoints(P, m)

        print("- Resulting Key Action Count: {}".format(KeyActionCount))
        print("- Ensuring Key Action Does Not Exceed Worst-Case Running Time: {}".format(KeyActionCount < (TestPoints[i] * (TestPoints[i]-1) / 2) * (TestPoints[i] * (TestPoints[i]-1) / 2)))
        print()

        TestResults.append(KeyActionCount)

    
    Plot.scatter(TestPoints, TestResults, label="Experimental", color="red")

    #configure and show plot

    Plot.title('Asymptotic vs Precise vs Experimental Running Times')
    Plot.xlabel('Size of P')
    Plot.ylabel('Number of Key Actions')

    Plot.legend()
    Plot.show()

def PerformTestRuns():
    TestRun_CalculateClosestPoints()