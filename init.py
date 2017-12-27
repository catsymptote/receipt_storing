from tkinter import *

from lib import recipt_window
from lib import file_manager
from lib import sheet_manager



sheet_manager.addFile("mep1.xls", "SHeet 1")
sheet_manager.addEntry("mep1.xls", "SHeet 1", "Hi")
sheet_manager.addEntry("mep1.xls", "SHeet 1", ["Hi", "1", "five"])
sheet_manager.addSheet("mep1.xls", "SHeet 14")
sheet_manager.addFile("mep2.xls", "Sheet maf")





# Start ----------
root_window = Tk()  # Window constructor / blank window
# Start ----------


recipt = recipt_window.recipt_window(root_window)
recipt.makeRecipt()

#if(add_rept.new_file()):
    ## New window: add new file? (Yes/No). Display file info.
#if(add_rept.entry_copy()):
    ## Open Yes/No window for adding a copy as (2) or whatever. Display info.


# Stop ---------------
root_window.mainloop()
# Stop ---------------
