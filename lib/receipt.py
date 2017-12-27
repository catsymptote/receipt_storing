class receipt:
    Store   = "Stringtype"
    Date    = [2017, 12, 27] #datetype
    Price   = 3.0 #floattype
    Type    = "Stringtype"


    def __init__(self, Store, Date, Price, Type):
        self.Store  = Store
        self.Date   = Date
        self.Price  = Price
        self.Type   = Type


    ## Get methods
    def getStore(self):
        return self.Store
    def getDate(self):
        return self.Date
    def getPrice(self):
        return self.Price
    def getType(self):
        return self.Type


    def getAll(self):
        return [
            self.Store,
            self.Date,
            self.Price,
            self.Type
        ]
