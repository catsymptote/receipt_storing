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
        if(entry is None):
            return False
        # Loop through tuple indexes.
        for i in range(len(entry)):
            
            style = xlwt.XFStyle()

            if(entry[i] is None):
                pass
            # If number
            elif(is_number(entry[i])):
                #print("Number: " + str(entry[i]))
                sh.write(rowCount, i, label=entry[i])
            # If formula
            elif(False and entry[i][0] == '='):
                formula = entry[i][1:]
                print("Formula: " + formula)
                #sh.write(rowCount, i, xlwt.Formula('%s' % formula))
                #sh.write(rowCount, i, xlwt.Formula("-(134.8780789e-10+1)"))
                sh.write(rowCount, i, xlwt.Formula(formula))
                # If default input style
            else:
                sh.write(rowCount, i, label=entry[i])
    else:
        #print("Not tuple")
        sh.write(rowCount, 0, entry)
    #book.get_sheet(0).write(0, 0, entry)
    wb.save(filename)
    return True


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


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


# Not working
# https://youtu.be/x18V8SyNiXo
def setColWidth(filename, sheet, c, w):
    rb = xlrd.open_workbook(filename)
    wb = xl_copy(rb)
    sh = wb.get_sheet(0)
    sh.col(c).width = w
    wb.save(filename)
