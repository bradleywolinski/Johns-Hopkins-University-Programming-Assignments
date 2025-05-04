import Config
import DTM
import FileIO

def Main():
    FileIO.CreateFile()

    if (Config.PerformTraceRuns()):
        FileIO.Write("Performing Trace Runs... ", end="")
    elif (Config.PerformTestRuns()):
        FileIO.Write("Performing Test Runs... ", end ="")  

    DeterministicTuringMachine = None

    if (Config.RunPartA()):
        Sigma = Config.GetM()
        DeterministicTuringMachine = DTM.PartA_DTM(Sigma)

        FileIO.Write("Running Part A...")
        FileIO.Write()
        FileIO.Write("Input Tape: {}".format(Sigma))
        FileIO.Write()

    elif (Config.RunPartB1()):
        Sigma = Config.GetM()
        Sigma.append('b')
        Sigma = Sigma + Config.GetN()
        DeterministicTuringMachine = DTM.PartB1_DTM(Sigma)

        FileIO.Write("Running Part B1...")
        FileIO.Write()
        FileIO.Write("Input Tape: {}".format(Sigma))
        FileIO.Write()

    elif (Config.RunPartB2()):
        Sigma = Config.GetM()
        Sigma.append('b')
        Sigma = Sigma + Config.GetN()
        DeterministicTuringMachine = DTM.PartB2_DTM(Sigma)

        FileIO.Write("Running Part B2...")
        FileIO.Write()
        FileIO.Write("Input Tape: {}".format(Sigma))
        FileIO.Write()

    elif (Config.RunPartB3()):
        Sigma = Config.GetM()
        Sigma.append('b')
        Sigma = Sigma + Config.GetN()
        DeterministicTuringMachine = DTM.PartB3_DTM(Sigma)

        FileIO.Write("Running Part B3...")
        FileIO.Write()
        FileIO.Write("Input Tape: {}".format(Sigma))
        FileIO.Write()

    else:
        FileIO.Write("No Running Arguments Supplied")

    FileIO.Write("---------------------------------------------------------")     

    if (DeterministicTuringMachine is not None):
        DeterministicTuringMachine.Run()

Main()