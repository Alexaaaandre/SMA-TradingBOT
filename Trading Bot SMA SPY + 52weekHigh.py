class CryingTanHyena(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2021, 1, 1)  # Set Start Date
        self.SetEndDate(2023, 5, 1)
        self.SetCash(100000)  # Set Strategy Cash

        self.spy = self.AddEquity("SPY", Resolution.Daily).Symbol  # Add the equity

        self.sma = self.SMA(self.spy, 30, Resolution.Daily)  # Specify which parameters you want for your SMA

    def OnData(self, Data):
        if not self.sma.IsReady:  # check is SMA is ready
            return

        hist = self.History(self.spy, timedelta(365), Resolution.Daily)  # Get the 52week high
        low = min(hist["low"])  # Get the lowest value for trading strategy
        high = max(hist["high"])  # Get the highest value for trading strategy

        price = self.Securities[self.spy].Price  # loc the price into a variable

        if price * 1.05 >= high and self.sma.Current.Value < price:  # Trading logic
            if not self.Portfolio[self.spy].IsLong:
                self.SetHoldings(self.spy, 1)


        elif price * 0.95 <= low and self.sma.Current.Value > price:
            if not self.Portfolio[self.spy].IsShort:
                self.SetHoldings(self.spy, -1)

        else:
            self.Liquidate()


self.Plot("Benchmark", "52w-High", high)  # Plot the graph
self.Plot("Benchmark", "52w-low", low)
self.Plot("Benchmark", "SMA", self.sma.Current.Value)
