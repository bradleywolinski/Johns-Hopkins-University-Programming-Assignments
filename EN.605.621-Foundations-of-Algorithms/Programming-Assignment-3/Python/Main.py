import Config
import Quicksort
import math as Math
import random as Random
import matplotlib.pyplot as Plot 

def RandomizedArray(Size):
    A = []
    for i in range(Size):
        A.append(Random.randint(1, 100000))
    return A

def Main():

    if (Config.PerformTraceRuns()):

        Method = ""
        if (Config.UseTextbookMethod()):
            Method = Config.GetTextbookMethodString()
        elif (Config.UseMedianOfThreeMethod()):
            Method = Config.GetMedianOfThreeMethodString()

        print("Performing Trace Runs...{}".format(Method))
        print("------------------------")

        n = 10

        print("n = {}\n".format(n))

        A = RandomizedArray(n)

        print("Input Array:")
        print("- {}\n".format(A))

        if (Config.UseTextbookMethod()):
            KeyPoints = Quicksort.TextbookMethod(A, 0, len(A) - 1)
        elif (Config.UseMedianOfThreeMethod()):
            KeyPoints = Quicksort.MedianOfThreeMethod(A, 0, len(A) - 1)
        else:
            print("No Running Argument Supplied")

        print("Output Array:")
        print("- {}\n".format(A))

        print("Key Points: {0}".format(KeyPoints))
        print("------------------------")

    elif (Config.PerformTestRuns()):

        TestPoints = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

        if (Config.UseTextbookMethod()):

            print("Performing Test Runs On Worst-Case Asymptotic Behavior...{}".format(Config.GetTextbookMethodString()))
            print("------------------------")

            TestResults = []

            for i in (range(len(TestPoints))):

                print("n = {}\n".format(TestPoints[i]))

                A = RandomizedArray(TestPoints[i])

                # sorting to force worst-case scenario

                A.sort()

                KeyPoints = Quicksort.TextbookMethod(A, 0, len(A) - 1)

                TestResults.append(KeyPoints)

                print("Key Points: {0}".format(KeyPoints))
                print("------------------------")


            # generate and plot for worst-case

            X = list(range(TestPoints[0], TestPoints[len(TestPoints) - 1] + 1))
            Y = [(n * n) for n in X]
    
            Plot.plot(X, Y, label="Worst-Case Behavior $(n^2)$", color="lightcoral")

            # scatter plot test points

            Plot.scatter(TestPoints, TestResults, label="Experimental Behavior")

            #configure and show plot

            Plot.title('Textbook Method - Worst-Case Behavior vs Experimental Behavior')
            Plot.xlabel('Size of N')
            Plot.ylabel('Number of Key Points')

            Plot.legend()
            Plot.show()

        if (Config.UseMedianOfThreeMethod()):

                print("Performing Test Runs On Worst-Case Asymptotic Behavior...{}".format(Config.GetMedianOfThreeMethodString()))
                print("------------------------")

                TestResults = []

                for i in (range(len(TestPoints))):

                    print("n = {}\n".format(TestPoints[i]))

                    A = RandomizedArray(TestPoints[i])

                    # sorting to force worst-case scenario

                    A.sort()

                    KeyPoints = Quicksort.MedianOfThreeMethod(A, 0, len(A) - 1)

                    TestResults.append(KeyPoints)

                    print("Key Points: {0}".format(KeyPoints))
                    print("------------------------")

                # initialize first plot 

                Plot.figure()

                # generate and plot for worst-case

                X = list(range(TestPoints[0], TestPoints[len(TestPoints) - 1] + 1))
                Y = [(n * n) for n in X]
        
                Plot.plot(X, Y, label="Worst-Case Behavior $(n^2)$", color="lightcoral")

                # scatter plot test points

                Plot.scatter(TestPoints, TestResults, label="Experimental Behavior")

                #configure first plot

                Plot.title('Median Of Three Method - Worst-Case Behavior vs Experimental Behavior')
                Plot.xlabel('Size of N')
                Plot.ylabel('Number of Key Points')
                Plot.legend()

                # initialize second plot 

                Plot.figure()

                # generate and plot for average-case

                X = list(range(TestPoints[0], TestPoints[len(TestPoints) - 1] + 1))
                Y = [(n * Math.log2(n)) for n in X]
        
                Plot.plot(X, Y, label="Average-Case $(nlg_2(n))$", color="lightcoral")

                # scatter plot test points

                Plot.scatter(TestPoints, TestResults, label="Experimental Behavior")

                # configure second plot

                Plot.title('Median Of Three Method - Average-Case Behavior vs Experimental Behavior')
                Plot.xlabel('Size of N')
                Plot.ylabel('Number of Key Points')
                Plot.legend()

                # show both plots

                Plot.show()

    else:
        print("No Running Argument Supplied")

Main()