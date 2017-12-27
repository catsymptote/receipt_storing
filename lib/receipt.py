class receipt:
    Store       = "Kiwi"
    Location    = "Kongsberg"
    Date        = "2017.12.27"
    Time        = "16:17"
    Price       = 74.80
    Type        = "Food"


    def __init__(self, Store, Location, Date, Time, Price, Type):
        self.Store      = Store
        self.Location   = Location
        self.Date       = Date
        self.Time       = Time
        self.Price      = Price
        self.Type       = Type


    ## Get methods
    def getStore(self):
        return self.Store
    def getLocation(self):
        return self.Location
    def getDate(self):
        return self.Date
    def getTime(self):
        return self.Time
    def getPrice(self):
        return self.Price
    def getType(self):
        return self.Type


    def getAll(self):
        return [
            self.Store,
            self.Location,
            self.Date,
            self.Time,
            self.Price,
            self.Type
        ]
