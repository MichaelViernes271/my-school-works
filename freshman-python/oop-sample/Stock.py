class Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = str(symbol)
        self.__name = str(name)
        self.__previousClosingPrice = float(previousClosingPrice)
        self.__currentPrice = float(currentPrice)
        
    def getName(self):
        return self.__name
        
    def getSymbol(self):
        return self.__symbol
        
    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice
        
    def getCurrentPrice(self):
        return self.__currentPrice
        
    def setName(self, name):
        self.__name = float(name)
        
    def setSymbol(self, symbol):
        self.__symbol = float(symbol)
        
    def setPreviousClosingPrice(self, previousClosingPrice):
        self.__previousClosingPrice = float(previousClosingPrice)
        
    def setCurrentPrice(self, currentPrice):
        self.__currentPrice = float(currentPrice)
        
    def getChangePercent(self): # returns increase or decrease of price in percent
        return str(round(
        (((self.getPreviousClosingPrice()- self.getCurrentPrice()) / self.getPreviousClosingPrice())* 100),2)) + "%"
    
    def display(self):
        print(f"""\
{"*"*50}
The company name is {self.getName()}.
The symbol is {self.getSymbol()}.
The previous closing price is {self.getPreviousClosingPrice()}.
The current price is {self.getCurrentPrice()}.
The percent change is {self.getChangePercent()}.
""")

