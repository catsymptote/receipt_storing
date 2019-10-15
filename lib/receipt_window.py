from tkinter import *
import time

from lib import receipt
from lib import sheet_manager


class receipt_window:
    ##  File info and other info.
    directory       = "sheets/"
    filename        = "test"
    fileExtension   = ".xls"
    filePath        = "sheets/default.xls"
    sheet           = "default sheet name"
    test_checkbox   = ""
    

    def __init__(self, master_window):
        ##  Create the window frame.
        frame = Frame(master_window)
        frame.pack()

        ##  "Store" entry.
        self.label_one = Label(frame, text="Store")
        self.label_one.grid(row=0, column=0, sticky=W)
        self.entry_Store = Entry(frame)
        self.entry_Store.grid(columnspan=3, row=0, column=1)

        ##  "Location" entry.
        self.label_one = Label(frame, text="Location")
        self.label_one.grid(row=1, column=0, sticky=W)
        self.entry_Location = Entry(frame)
        self.entry_Location.grid(columnspan=3, row=1, column=1)
        
        ##  "Date" entry.
        self.label_one = Label(frame, text="Date")
        self.label_one.grid(row=2, column=0, sticky=W)
        self.entry_Date = Entry(frame)
        self.entry_Date.grid(columnspan=3, row=2, column=1)

        ##  "Time" entry.
        self.label_one = Label(frame, text="Time")
        self.label_one.grid(row=3, column=0, sticky=W)
        self.entry_Time = Entry(frame)
        self.entry_Time.grid(columnspan=3, row=3, column=1)

        ##  "Price" entry.
        self.label_one = Label(frame, text="Price")
        self.label_one.grid(row=4, column=0, sticky=W)
        self.entry_Price = Entry(frame)
        self.entry_Price.grid(columnspan=3, row=4, column=1)

        ##  "Type" entry.
        self.label_one = Label(frame, text="Type")
        self.label_one.grid(row=5, column=0, sticky=W)
        self.entry_Type = Entry(frame)
        self.entry_Type.grid(columnspan=3, row=5, column=1)

        ##  "Add receipt" button.
        self.add_button = Button(frame, text="Add receipt", command=self.makeReceipt)
        self.add_button.grid(columnspan=3, row=6, column=1)

        ##  "Test?" checkbox.
        self.test_checkbox   = IntVar()
        self.test_checkbox.set(1)
        self.checkbox_one = Checkbutton(frame, text="Test?", variable=self.test_checkbox)
        self.checkbox_one.grid(columnspan=1, row=1, column=4)

        ##  Excel intialization button.
        self.init_button = Button(frame, text="Initialize", command=self.initSheet)
        self.init_button.grid(columnspan=1, row=0, column=4)


    def makeReceipt(self):
        ##  Entry values.
        Store   = self.entry_Store.get()
        Location= self.entry_Location.get()
        Date    = self.entry_Date.get()
        Time    = self.entry_Time.get()
        Price   = self.entry_Price.get()
        Type    = self.entry_Type.get()

        ##  If entry rejected.
        if(not self.rept_entry_check([Store, Location, Date, Time, Price, Type])):
            print("Entry rejected. There is an issue with the entry.")
            return False

    ##  Receipt object construction.
        rept = receipt.receipt(Store, Location, Date, Time, Price, Type)
        reptEntry = rept.getAll()

        ##  If testing: use different filename.
        testbox = self.test_checkbox.get()
        if(not testbox == 0):
            self.filename   = "test_" + rept.getYear()
        else:
            self.filename   = rept.getYear()
        
        self.filePath = self.directory + self.filename + self.fileExtension

        ##  Set sheet name based on entry month, and initialize sheet.
        self.sheet = str(rept.getMonth())
        self.initSheet()
        
        ##  If entry added succesfully:
        if(sheet_manager.addEntry(self.filePath, self.sheet, reptEntry)):
           self.clearEntries()
           print("Entry add successful!")
           return True
        else:
            print("Entry not added.")
            return False


    def rept_entry_check(self, reptEntry):
        ##  Has 6 entries.
        if(not len(reptEntry) == 6):
            return False

        ##  Each entry has a value
        for i in range(len(reptEntry)):
            if(not self.check_entry_cell(reptEntry[i])):
                print("Empty entry section at cell " + str(i+1) + ".")
                return False

        return True
        

    def check_entry_cell(self, entryCell):
        ##  Check if cell exists and has a value.
        if(not entryCell or len(entryCell) < 1):
            return False
        return True


    def clearEntries(self):
        ##  Clears the entry cells.
        self.entry_Store.delete(0, 'end')
        self.entry_Location.delete(0, 'end')
        self.entry_Date.delete(0, 'end')
        self.entry_Time.delete(0, 'end')
        self.entry_Price.delete(0, 'end')
        self.entry_Type.delete(0, 'end')


    def initSheet(self):
        ##  If sheet is not made -> sheet already exists (probably).
        if(not sheet_manager.makeSheet(self.filePath, self.sheet)):
            #print("Sheet already exists")
            return False
        

        ##  Add default entries (before/above standard user entries).
        month = self.monthToName(self.sheet)
        sheet_manager.addEntry(
            self.filePath, self.sheet,
            [month, " ", " ", "Total:", "=SUM(E4:E10000)"]
        )

        sheet_manager.addEntry(self.filePath, self.sheet, " ")

        sheet_manager.addEntry(
            self.filePath, self.sheet,
            ["Store", "Location", "Date", "Time", "Price", "Type"]
        )

        sheet_manager.addEntry(
            self.filePath, self.sheet,
            "----------------------------------------------------------------------------------"
        )
        
        ##  Setting sheet column widths (not working).
        sheet_manager.setColWidth(self.filePath, self.sheet, 0, 1000)
        sheet_manager.setColWidth(self.filePath, self.sheet, 1, 1000)
        sheet_manager.setColWidth(self.filePath, self.sheet, 2, 500)
        sheet_manager.setColWidth(self.filePath, self.sheet, 3, 500)
        sheet_manager.setColWidth(self.filePath, self.sheet, 4, 1000)
        sheet_manager.setColWidth(self.filePath, self.sheet, 5, 5000)

        return True


    def monthToName(self, sheet):
        ## Return month as name
        return {
            "01" : "January",
            "02" : "February",
            "03" : "March",
            "04" : "April",
            "05" : "May",
            "06" : "June",
            "07" : "July",
            "08" : "August",
            "09" : "September",
            "10" : "October",
            "11" : "November",
            "12" : "December"
        }.get(sheet, "none")
