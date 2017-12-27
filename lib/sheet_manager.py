import xlrd, xlwt
from xlutils.copy import copy as xl_copy
from xlutils.margins import number_of_good_rows
from xlrd import *
from xlwt import *
from openpyxl import load_workbook
import os.path


def addEntry(filename, sheet, entry):
    ## https://stackoverflow.com/questions/2725852/writing-to-existing-workbook-using-xlwt
    rb = xlrd.open_workbook(filename)
    wb = xl_copy(rb)
    #book = xl_copy(open_workbook(filename))
    # Get number of rows
    sheets = rb.sheets()
    rowCount = sheets[0].nrows
    #print(rowCount)
    sh = wb.get_sheet(0)
    #print(sh.max_row)

    # Check if a tuple or not (for index reasons).
    if(isinstance(entry, tuple) or isinstance(entry, list)):
        #print("Tuple")
        # Loop through tuple indexes.
        for i in range(len(entry)):
            # If formula
            a = entry[i][0]
            style = xlwt.XFStyle()
            if(a == '='):
                formula = entry[i][1:]
                print("Formula: " + formula)
                #sh.write(rowCount, i, xlwt.Formula('%s' % formula))
                sh.write(rowCount, i, xlwt.Formula("-(134.8780789e-10+1)"))
            # If number
            elif(a == '0' or a == '1' or a == '2' or a == '3' or a == '4' or
                    a == '5' or a == '6' or a == '7' or a == '8' or a == '9'):
                sh.write(rowCount, i, label=entry[i])
            else:
                sh.write(rowCount, i, label=entry[i])
    else:
        #print("Not tuple")
        sh.write(rowCount, 0, entry)
    #book.get_sheet(0).write(0, 0, entry)
    wb.save(filename)


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
        #print("Sheet already exists")
        return False
    wb.save(filename)
    return True


def addFile(filename, sheet):
    ## https://stackoverflow.com/questions/13437727/python-write-to-excel-spreadsheet
    if(os.path.exists(filename)):
        #print("File already exists")
        return False
    book = xlwt.Workbook()
    sh = book.add_sheet(sheet)
    book.save(filename)
    return True
