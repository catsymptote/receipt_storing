from tkinter import *

from lib import receipt_window
from lib import sheet_manager


##  Create window.
root_window = Tk()

##  Create receipt window.
reptWin = receipt_window.receipt_window(root_window)

##  Start mainloop.
root_window.mainloop()
