import Config
import Signal

def Main():

    TestCase = Config.GetTestCase()
    S = Config.GetS()
    X = Config.GetX()
    Y = Config.GetY()

    print("----------------------------------------------------------------")
    print("Test Case: {}".format(TestCase))
    print()
    print("S: {}".format(S))
    print("X: {}".format(X))    
    print("Y: {}".format(Y))
    
    NewSignal = Signal.Signal(S, X, Y)

    if (NewSignal.IsInterweaving):
        print("Signal Is An Interweaving Of X And Y")
        print()

        print("X Groupings:")
        for i in range(0, len(NewSignal.XPositionGroupings)):
            print("- {}".format(NewSignal.XPositionGroupings[i]))
        
        print()

        print("Y Groupings:")
        for i in range(0, len(NewSignal.YPositionGroupings)):
            print("- {}".format(NewSignal.YPositionGroupings[i]))
        
        print()

        print("Noise Groupings:")
        if (len(NewSignal.NoisePositionGroupings) == 0):
            print("- None")
        else:
            for i in range(0, len(NewSignal.NoisePositionGroupings)):
                print("- {}".format(NewSignal.NoisePositionGroupings[i]))

    else:
        print("Signal Is Not An Interweaving Of X And Y")

    print()
    print("Expected Key Points: {}".format(len(NewSignal.S)))
    print("Actual Key Points: {}".format(NewSignal.KeyPoints))

    print("----------------------------------------------------------------")
    print()

Main()