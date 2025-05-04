import Config
import FileIO

class ControlRecord:
    def __init__(self, NextState, SymbolToWrite, DirectionToMove):

        self.NextState = NextState
        self.SymbolToWrite = SymbolToWrite
        self.DirectionToMove = DirectionToMove

class QState:
    def __init__(self, Key,
                 ZeroNextState = None, ZeroSymbolToWrite = None, ZeroDirection = None,
                 OneNextState = None, OneSymbolToWrite = None, OneDirection = None,
                 BlankNextState = None, BlankSymbolToWrite = None, BlankDirection = None,  
                 IsHaltingState = False):
        
        self.Key = Key

        self.Commands = {"0" : ControlRecord(ZeroNextState, ZeroSymbolToWrite, ZeroDirection), 
                         "1" : ControlRecord(OneNextState, OneSymbolToWrite, OneDirection), 
                         "b" : ControlRecord(BlankNextState, BlankSymbolToWrite, BlankDirection)}
        
        self.IsHaltingState = IsHaltingState

class DTM:
    def __init__(self, Gamma, Q, S, Delta, Sigma, B):

        self.Gamma = Gamma # finite set of symbols
        self.Q = Q         # finite set of states
        self.S = S         # direction (left, right, halt)
        self.Delta = Delta # transition function
        self.Sigma = Sigma # set of input symbols
        self.B = B         # blank symbol

        self.CurrentIndex = 0
        self.CurrentState = Q["Q0"]

    def Run(self):
        while self.IsRunning():
            self.Update()

    def IsRunning(self):
        Running = not self.CurrentState.IsHaltingState

        if (not Running):
            FileIO.Write()
            FileIO.Write("Turing Machine Halted...")
            FileIO.Write("Final Tape: {}".format(list(filter(lambda x: x != "b", self.Sigma))))

        return Running

    def Update(self):

        self.HandleOutOfBoundsIndex()

        FileIO.Write("Current State: {}".format(self.CurrentState.Key))
        FileIO.Write("Current Index: {}".format(self.CurrentIndex))
        FileIO.Write("Current Tape: {}".format(self.Sigma))
            
        # add underscore underneath current index

        WhiteSpace = "                "

        for i in range(0, self.CurrentIndex):

            WhiteSpace = WhiteSpace + "     "

        FileIO.Write(WhiteSpace + "_")

        if (Config.PerformTraceRuns()):
            FileIO.Write()
            FileIO.Write("Reading '{}' From Index {}".format(self.Sigma[self.CurrentIndex], self.CurrentIndex))
            FileIO.Write()

        for Symbol in self.Gamma:
            if (self.Sigma[self.CurrentIndex] == Symbol):
                self.UpdateBasedOnCurrentSymbol(Symbol)
                break
            
    def HandleOutOfBoundsIndex(self):
        if (self.CurrentIndex < 0):

            if (Config.PerformTraceRuns()):
                FileIO.Write("Inserting Blank To Beginning And Resetting Index")
                FileIO.Write()

            self.CurrentIndex = 0
            self.Sigma.insert(0, self.B)

        if (self.CurrentIndex > len(self.Sigma) - 1):

            self.Sigma.append(self.B)

    def UpdateBasedOnCurrentSymbol(self, Symbol):
        
        FileIO.Write("Updating Turing Machine...")

        # update current position with desired symbol
        
        NewSymbol = self.CurrentState.Commands[Symbol].SymbolToWrite

        FileIO.Write("- Writing '{}' To Index {}".format(NewSymbol, self.CurrentIndex))
        
        self.Sigma[self.CurrentIndex] = NewSymbol

        # update current index with desired direction

        if (self.CurrentState.Commands[Symbol].DirectionToMove == "-1"):

            FileIO.Write("- Moving Read-Write Head Left")

            self.CurrentIndex = self.CurrentIndex - 1

        elif (self.CurrentState.Commands[Symbol].DirectionToMove == "+1"):

            FileIO.Write("- Moving Read-Write Head Right")

            self.CurrentIndex = self.CurrentIndex + 1

        # update current state with desired state

        NewState = self.CurrentState.Commands[Symbol].NextState

        FileIO.Write("- Moving State To {}".format(NewState))
        FileIO.Write("---------------------------------------------------------")

        self.CurrentState = self.Q[NewState]

def PartA_DTM(Sigma):
    Q = {"Q0" : QState("Q0", "Q0", "0", "+1", "Q0", "1", "+1", "Q1", "b", "-1"), 
         "Q1" : QState("Q1", "Q2", "b", "-1", "Q3", "b", "-1", "QN", "b", "-1"),
         "Q2" : QState("Q2", "QY", "b", "-1", "QN", "b", "-1", "QN", "b", "-1"),
         "Q3" : QState("Q3", "QN", "b", "-1", "QN", "b", "-1", "QN", "b", "-1"),
         "QY" : QState("QY", IsHaltingState = True),
         "QN" : QState("QN", IsHaltingState = True)}

    return DTM(Gamma = ["0", "1", "b"], 
               Q = Q, 
               S = None, 
               Delta = None, 
               Sigma = Sigma, 
               B = "b")

def PartB1_DTM(Sigma):
    Q = {"Q0" : QState("Q0", "Q0", "0", "+1", "Q0", "1", "+1", "Q1", "b", "+1"), # traverse over m
         "Q1" : QState("Q1", "Q1", "0", "+1", "Q1", "1", "+1", "Q2", "b", "-1"), # traverse over n
         "Q2" : QState("Q2", "Q2", "0", "-1", "Q3", "0", "+1", "Q8", "b", "+1"), # decrement n, cleanup if 'b' (n = 0)
         "Q3" : QState("Q3", "Q3", "1", "+1", "X", "X", "X", "Q4", "b", "-1"),   # decrement n
         "Q4" : QState("Q4", "Q4", "0", "-1", "Q4", "1", "-1", "Q5", "b", "-1"), # traverse back over n 
         "Q5" : QState("Q5", "Q0", "1", "+1", "Q6", "0", "-1", "Q0", "1", "+1"), # increment m
         "Q6" : QState("Q6", "Q0", "1", "+1", "Q6", "0", "-1", "Q0", "1", "+1"), # increment m, handle carry
         "Q8" : QState("Q8", "Q8", "b", "+1", "Q8", "b", "+1", "QY", "b", "X"),  # cleanup 
         "QY" : QState("QY", IsHaltingState = True)}

    return DTM(Gamma = ["0", "1", "b"], 
               Q = Q, 
               S = None, 
               Delta = None, 
               Sigma = Sigma, 
               B = "b")

def PartB2_DTM(Sigma):
    Q = {"Q0" : QState("Q0", "Q0", "0", "+1", "Q0", "1", "+1", "Q1", "b", "+1"), # traverse over m
         "Q1" : QState("Q1", "Q1", "0", "+1", "Q1", "1", "+1", "Q2", "b", "-1"), # traverse over n
         "Q2" : QState("Q2", "Q2", "0", "-1", "Q3", "0", "+1", "Q8", "b", "+1"), # decrement n, halt if 'b' (n = 0)
         "Q3" : QState("Q3", "Q3", "1", "+1", "X", "X", "X", "Q4", "b", "-1"),   # decrement n
         "Q4" : QState("Q4", "Q4", "0", "-1", "Q4", "1", "-1", "Q5", "b", "-1"), # traverse back over n 
         "Q5" : QState("Q5", "Q5", "0", "-1", "Q6", "0", "+1", "Q7", "b", "+1"), # decrement m, special case if 'b' (m = 0, m < n)
         "Q6" : QState("Q6", "Q6", "1", "+1", "X", "X", "X", "Q1", "b", "+1"),   # decrement m, handle borrow
         "Q7" : QState("Q7", "Q7", "0", "+1", "Q7", "0", "+1", "Q8", "b", "+1"), # clear n when m < n  
         "Q8" : QState("Q8", "Q8", "b", "+1", "Q8", "b", "+1", "QY", "b", "X"),  # cleanup        
         "QY" : QState("QY", IsHaltingState = True)}

    return DTM(Gamma = ["0", "1", "b"], 
               Q = Q, 
               S = None, 
               Delta = None, 
               Sigma = Sigma,
               B = "b")

def PartB3_DTM(Sigma):
    Q = {"Q0" : QState("Q0", "Q0", "0", "+1", "Q0", "1", "+1", "Q1", "b", "+1"),    # traverse over m
         "Q1" : QState("Q1", "Q1", "0", "+1", "Q1", "1", "+1", "Q2", "b", "-1"),    # traverse over n
         "Q2" : QState("Q2", "Q2", "0", "-1", "Q3", "0", "+1", "Q7", "b", "-1"),    # decrement n, special case if 'b' (n = 0)
         "Q3" : QState("Q3", "Q3", "1", "+1", "X", "X", "X", "Q4", "b", "-1"),      # decrement n
         "Q4" : QState("Q4", "Q4", "0", "-1", "Q4", "1", "-1", "Q5", "b", "-1"),    # traverse back over n 
         "Q5" : QState("Q5", "Q5", "0", "-1", "Q6", "0", "-1", "Q0", "0", "+1"),    # shift 0 left
         "Q6" : QState("Q6", "Q5", "1", "-1", "Q6", "1", "-1", "Q0", "1", "+1"),    # shift 1 left
         "Q7" : QState("Q7", "Q7", "0", "-1", "Q7", "1", "-1", "Q8", "b", "+1"),    # traverse back over m
         "Q8" : QState("Q8", "Q8", "0", "+1", "Q9", "0", "+1", "Q10", "b", "X"),    # shift 0 right
         "Q9" : QState("Q9", "Q8", "1", "+1", "Q9", "1", "+1", "Q10", "b", "X"),    # shift 1 right
         "Q10" : QState("Q10", "Q10", "b", "+1", "Q10", "b", "+1", "QY", "b", "X"), # cleanup
         "QY" : QState("QY", IsHaltingState = True)}

    return DTM(Gamma = ["0", "1", "b"], 
               Q = Q, 
               S = None, 
               Delta = None, 
               Sigma = Sigma,
               B = "b")   