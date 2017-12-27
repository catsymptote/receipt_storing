from tkinter import *

from lib import receipt


class reciept_window:
    ## Basic window class for adding a recipt.

    def __init__(self, master_window):
        frame = Frame(master_window)
        frame.pack()
        ## Construct the window
        self.label_one = Label(frame, text="Hello there.")
        self.label_one.grid(row=0)

        self.checkbox_one = Checkbutton(frame, text="Hi there")
        self.checkbox_one.grid(columnspan=2, row=1)
        self.printMessage()


    def printMessage(self):
        print("Here is the printed message.")
        sys.stdout.flush()


    def makeReceipt(self):
        rept = receipt.receipt("hi", [2017, 12, 24], 3.14, "Food")
        print(rept.getAll())
