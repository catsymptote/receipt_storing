import xlrd, xlwt
from xlutils.copy import copy as xl_copy
from xlrd import *
from openpyxl import load_workbook
import os.path


def addEntry(filename, sheet, entry):
    ## https://stackoverflow.com/questions/2725852/writing-to-existing-workbook-using-xlwt
    book = xl_copy(open_workbook(filename))
    for i in range(len(entry)):
        book.get_sheet(0).write(0, i, entry[i])
    #book.get_sheet(0).write(0, 0, entry)
    book.save(filename)

"""
def addEntry2(filename, sheet, entry):
    book = xlwt.Workbook()
    sh = book.add_sheet(sheet)
    col1_name = "Hello there"
    col2_name = "maff maff"
    sh.write(0, 0, col1_name)
    sh.write(0, 1, col2_name)
    #sh.write(y, x, output)
    book.save(filename)
"""


def addSheet(filename, sheet):
    ## https://stackoverflow.com/questions/38081658/adding-a-sheet-to-an-existing-excel-worksheet-without-deleting-other-sheet

    # Open existing workbook
    rb = xlrd.open_workbook(filename, formatting_info=True)
    # Make a copy of it
    wb = xl_copy(rb)

    # Check if sheet already exists
    ## https://stackoverflow.com/questions/37966536/python-validate-if-a-sheet-exists-in-my-document-xls
    #if(sheet in [filename.Sheets(i).Name for i in range(1,excel_file.Sheets.Count+1)])
    #if(sheet in rb.sheets().name):
    #sheets = rb.sheets()
    #if([s.name for s in rb.sheets()].index(sheet)):
    #    print("Sheet already exists")
    #    return False
    # Add sheet to workbook with existing sheets
    try:
        Sheet1 = wb.add_sheet(sheet)
    except Exception:
        print("Sheet already exists")
        return False
    wb.save(filename)
    return True


def addFile(filename, sheet):
    ## https://stackoverflow.com/questions/13437727/python-write-to-excel-spreadsheet
    if(os.path.exists(filename)):
        print("File already exists")
        return False
    book = xlwt.Workbook()
    sh = book.add_sheet(sheet)
    book.save(filename)
    return True
