class receipt:
    Store       = "Kiwi"
    Location    = "Kongsberg"
    Date        = "2017.12.27"
    Time        = "16:17"
    Price       = 74.80
    Type        = "Food"

    Year    = "1993"
    Month   = "04"
    Day     = "08"


    def __init__(self, Store, Location, Date, Time, Price, Type):
        self.Store      = Store
        self.Location   = Location
        self.Date       = Date
        self.Time       = Time
        self.Price      = Price
        self.Type       = Type

        self.setFormattedDate()


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

    def getYear(self):
        return self.Year
    def getMonth(self):
        return self.Month
    def getDay(self):
        return self.Day


    def getAll(self):
        return (
            self.Store,
            self.Location,
            self.Date,
            self.Time,
            self.Price,
            self.Type
        )


    def setFormattedDate(self):
        date = self.Date
        if(self.dateFormatRejected(date)):
            print("Format rejected")
            return False
        
        self.Year   = date[0] + date[1] + date[2] + date[3]
        self.Month  = date[5] + date[6]
        self.Day    = date[8] + date[9]

        """
        print(self.Year)
        print(self.Month)
        print(self.Day)
        """

        
        """
        print(date[0] + date[1] + date[2] + date[3])
        print(date[5] + date[6])
        print(date[8] + date[9])
        """

        return True

    
    def dateFormatRejected(self, date):
        ## Check date string length
        if(not len(date) == 10):
            #print("Date format rejected:  Date is not correct length (10), but ("  + len(date) + "):\n\"" + date + "\"")
            return False
        
        ## Check date formatting
        yearAcceptable  = (date[0] + date[1] + date[2] + date[3]).isdigit()
        monthAcceptable = (date[5] + date[6]).isdigit()
        dayAcceptable   = (date[8] + date[9]).isdigit()
        dotsAcceptable  = (date[4] == '.' and date[7] == '.')

        """
        print(date[0] + date[1] + date[2] + date[3])
        print(date[5] + date[6])
        print(date[8] + date[9])
        """

        if(yearAcceptable and monthAcceptable and dayAcceptable and dotsAcceptable):
            return False

        #print("Date format rejected:  Date format unacceptable (yyyy.mm.dd), aka (num.num.num):\n" + date)
        print("Date format rejected.")
        return True