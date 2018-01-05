class receipt:
    ##  Attribute initialization with example values.
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


    ##  Get methods
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
        ##  Get all values as tuple.
        return (
            self.Store,
            self.Location,
            self.Date,
            self.Time,
            self.Price,
            self.Type
        )


    ##  Note to self: This could be re-written to allow different date formats
    ##  dd.mm.yyyy, mm.dd.yyyy, etc.
    def setFormattedDate(self):
        date = self.Date
        ##  If date has acceptable format.
        if(self.dateFormatRejected(date)):
            print("Format rejected")
            return False
        
        ##  Get "yyyy.mm.dd" as variables.
        self.Year   = date[0] + date[1] + date[2] + date[3]
        self.Month  = date[5] + date[6]
        self.Day    = date[8] + date[9]

        return True

    
    def dateFormatRejected(self, date):
        ##  Check date string length.
        if(not len(date) == 10):
            return False
        
        ##  Make bools of acceptable (True)/unacceptable (False) date formatting.
        yearAcceptable  = (date[0] + date[1] + date[2] + date[3]).isdigit()
        monthAcceptable = (date[5] + date[6]).isdigit()
        dayAcceptable   = (date[8] + date[9]).isdigit()
        dotsAcceptable  = (date[4] == '.' and date[7] == '.')

        ##  Check if date format is acceptable based on acceptability bools.
        if(yearAcceptable and monthAcceptable and dayAcceptable and dotsAcceptable):
            return False

        print("Date format rejected.")
        return True
