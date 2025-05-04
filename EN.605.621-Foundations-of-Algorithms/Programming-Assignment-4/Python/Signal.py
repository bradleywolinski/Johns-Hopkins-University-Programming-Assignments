class Signal:
    def __init__(self, S, X, Y):
        self.S = S
        self.X = X
        self.Y = Y

        self.IsInterweaving = False

        self.XPositionGroupings = []
        self.YPositionGroupings = []
        self.NoisePositionGroupings = []

        self.CurrentXPositions = []
        self.CurrentYPositions = []
        self.CurrentNoisePositions = []

        self.KeyPoints = 0

        print()
        print("Processing Signal...")
        print()


        self.Decode()

    def Decode(self):

        # loop over entire signal as if it were being read live

        for i in range(0, len(self.S)):
            
            if (self.S[i] == self.X[len(self.CurrentXPositions)] and self.S[i] == self.Y[len(self.CurrentYPositions)]):

                # current symbol fits in x and y

                if (len(self.XPositionGroupings) > len(self.YPositionGroupings)):

                    # more x signals have been found than y signals, add to y

                    self.UpdateY(i)

                elif (len(self.XPositionGroupings) < len(self.YPositionGroupings)):

                    # more y signals have been found than x signals, add to x

                    self.UpdateX(i)

                else:

                    # equal amount of x and y signals have been found

                    if (len(self.CurrentXPositions) > len(self.CurrentYPositions)):

                        # x is further along, add to x

                        self.UpdateX(i)

                    else:

                        # x is further along, add to y

                        self.UpdateY(i)

            elif (self.S[i] == self.X[len(self.CurrentXPositions)]):

                # current symbol fits in x only

                self.UpdateX(i)

            elif (self.S[i] == self.Y[len(self.CurrentYPositions)]):

                # current symbol fits in y only

                self.UpdateY(i)

            else:

                # current symbol does not fit in x or y, add to noise and handle accordingly

                self.CurrentNoisePositions.append(i + 1)

                # add noise from x and y to noise, then sort

                for j in range(0, len(self.CurrentXPositions)):
                    
                    self.CurrentNoisePositions.append(self.CurrentXPositions[j])

                    self.KeyPoints = self.KeyPoints + 1

                for j in range(0, len(self.CurrentYPositions)):

                    self.CurrentNoisePositions.append(self.CurrentYPositions[j])

                    self.KeyPoints = self.KeyPoints + 1
                
                self.CurrentNoisePositions.sort()

                # clear out noise added to x and y

                self.CurrentXPositions = []
                self.CurrentYPositions = []

            self.KeyPoints = self.KeyPoints + 1

        # add possible noise at end

        self.HandleNoise()

        # determine interweaving

        self.IsInterweaving = len(self.XPositionGroupings) > 0 and len(self.YPositionGroupings) > 0

    def UpdateX(self, i):

        self.CurrentXPositions.append(i + 1)

        if (len(self.CurrentXPositions) == len(self.X)):

            # reached full instance of x, save positions to array and reset

            self.XPositionGroupings.append(self.CurrentXPositions)

            self.CurrentXPositions = []

            # reached full signal, handle noise

            self.HandleNoise()

    def UpdateY(self, i):

        self.CurrentYPositions.append(i + 1)

        if (len(self.CurrentYPositions) == len(self.Y)):

            # reached full instance of y, save positions to array and reset

            self.YPositionGroupings.append(self.CurrentYPositions)

            self.CurrentYPositions = []

            # reached full signal, handle noise

            self.HandleNoise()

    def HandleNoise(self):

        if (len(self.CurrentNoisePositions) > 0):
            
            self.NoisePositionGroupings.append(self.CurrentNoisePositions)

            self.CurrentNoisePositions = []
