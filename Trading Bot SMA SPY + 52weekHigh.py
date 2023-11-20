class CryingTanHyena(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2021, 1, 1)  # Set Start Date
        self.SetEndDate(2023, 5, 1)
        self.SetCash(100000)  # Set Strategy Cash
        
        self.spy = self.AddEquity("SPY", Resolution.Daily).Symbol

        self.sma = self.SMA(self.spy, 30, Resolution.Daily)
        

        

    
    def OnData(self, Data):
        if not self.sma.IsReady:
            return
        
        hist = self.History(self.spy, timedelta(365), Resolution.Daily)
        low = min(hist["low"])
        high = max(hist["high"])

        price = self.Securities[self.spy].Price

        if price * 1.05 >= high and self.sma.Current.Value < price:
            if not self.Portfolio[self.spy].IsLong:
                self.SetHoldings(self.spy, 1)

                
        elif price * 0.95 <= low and self.sma.Current.Value > price:
            if not self.Portfolio[self.spy].IsShort:
                self.SetHoldings(self.spy, -1)
        
        else: 
            self.Liquidate()


self.Plot("Benchmark", "52w-High", high)
self.Plot("Benchmark", "52w-low", low)
self.Plot("Benchmark", "SMA", self.sma.Current.Value)
