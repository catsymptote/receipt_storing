from tkinter import *
import time

from lib import receipt
from lib import sheet_manager

class receipt_window:
    ## Basic window class for adding a recipt.
    filename    = "2017.xls"
    sheet       = "12 - December"

    def __init__(self, master_window):
        frame = Frame(master_window)
        frame.pack()
        ## Construct the window
        self.label_one = Label(frame, text="Hello there.")
        self.label_one.grid(row=0)

        self.checkbox_one = Checkbutton(frame, text="Hi there")
        self.checkbox_one.grid(columnspan=2, row=1)


    def makeReceipt(self):
        rept = receipt.receipt("Meny", "Kongsberg", "2017.11.24", "22:48", "299,90", "Food")
        reptEntry = rept.getAll()
        sheet_manager.addEntry(self.filename, self.sheet, reptEntry)
        #print(rept.getAll())


    def initSheet(self):
        #now = datetime.datetime.now()
        #month   = now.month
        #year    = now.year

        if(not sheet_manager.addFile(self.filename, self.sheet)):
            if(not sheet_manager.addSheet(self.filename, self.sheet)):
                print("Cannot overwrite!")
                return False
        
        sheet_manager.addEntry(
            self.filename, self.sheet,
            [self.sheet, " ", " ", "Total:", "=SUM(E5:E10000)", "=4+5", "hi"])
        sheet_manager.addEntry(
            self.filename, self.sheet,
            ("Store", "Location", "Date", "Time", "Price", "Type"))
        sheet_manager.addEntry(
            self.filename, self.sheet,
            " ")
        return True