# SMA-TradingBOT

This Bot is coded using Python for the QuantConnect platform. 

The logic here is whenever the current price is above the monthly SMA and we are close to the highest price of the year, we consider that we are in an uptrend and we buy.

On the other hand, whenever the price is lower than the monthly SMA and we are close to the lowest price of the year we consider this a downtrend and we short.
