import xlrd, xlwt
from xlutils.copy import copy as xl_copy
from xlutils.margins import number_of_good_rows
from xlrd import *
from xlwt import *
from openpyxl import load_workbook
import os.path
from shutil import copyfile
from shutil import copyfileobj


def addEntry(filename, sheet, entry):
    ##  Open and copy workbook: https://stackoverflow.com/questions/2725852/writing-to-existing-workbook-using-xlwt
    rb = xlrd.open_workbook(filename)
    wb = xl_copy(rb)
    
    ##  Get number of rows.
    sheets = rb.sheets()
    sheetIndex = get_sheet_by_name(sheets, sheet)
    if(sheetIndex == -1):
        return False
    
    ##  Open sheet by index.
    rowCount = sheets[sheetIndex].nrows
    sh = wb.get_sheet(sheetIndex)

    ##  If entry is a tuple.
    if(isinstance(entry, tuple) or isinstance(entry, list)):
        if(entry is None):
            return False
        ##  Loop through tuple indexes.
        for i in range(len(entry)):
            ##  Chech if entry exists.
            if(entry[i] is None):
                continue

            ##  If number
            elif(is_number(entry[i])):

                ##  Replace '.' with ',' for excel reasons.
                tmp = entry[i].replace('.', ',')
                sh.write(rowCount, i, label=tmp)

            ##  If entry is a formula (deactivated).
            elif(False and entry[i][0] == '='):
                formula = entry[i][1:]
                print("Formula: " + formula)
                sh.write(rowCount, i, xlwt.Formula(formula))
            
            ##  If default (not specialized) input style.
            else:
                sh.write(rowCount, i, label=entry[i])
    else:
        ##  If entry is not a tuple.
        sh.write(rowCount, 0, entry)
    
    wb.save(filename)
    return True


def get_sheet_by_name(sheets, sheet):
    ## https://stackoverflow.com/questions/14587271/accessing-worksheets-using-xlwt-get-sheet-method
    """ Get a sheet by name from xlwt.Workbook, a strangely missing method.
    Returns None if no sheet with the given name is present. """
    ##  Note, we have to use exceptions for flow control because the
    ##  xlwt API is broken and gives us no other choice.
    try:
        for i in range(len(sheets)):
            if(sheets[i].name == sheet):
                return i
    except IndexError:
        print("Sheet lookup failed.")
        return -1


def is_number(s):
    ##  Check if (s) is a number: https://www.pythoncentral.io/how-to-check-if-a-string-is-a-number-in-python-including-unicode/
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


def makeSheet(filename, sheet):
    ##  If file does not exist.
    if(not os.path.exists(filename)):
        ##  Bool of whether copy: default.xls -> yyyy.xls was successful.
        default = defaultSheet(filename)
        ##  If unsuccessful (because no default-file or otherwise).
        if(not default):
            ##  Create a new file with sheet.
            addFile(filename, sheet)
            return True
    
    ##  If sheet added successfully.
    if(addSheet(filename, sheet)):
        return True

    return False
    

def defaultSheet(filename):
    ##  File path of default file
    defaultFilePath = "excel_related/default.xls"

    ##  If default.xls exists.
    if(os.path.exists(defaultFilePath)):
        print("Copies dafault file.")
        ##  Copy default.xls -> yyyy.xls.
        copyfile(defaultFilePath, filename)
        return True
    return False


def addSheet(filename, sheet):
    ##  https://stackoverflow.com/questions/38081658/adding-a-sheet-to-an-existing-excel-worksheet-without-deleting-other-sheet
    ##  Open existing workbook
    rb = xlrd.open_workbook(filename, formatting_info=True)
    ##  Make a copy of the master workbook or something.
    wb = xl_copy(rb)
    
    ##  Try to add sheet to workbook with existing sheets.
    try:
        Sheet1 = wb.add_sheet(sheet)
        ##  Remove "default" sheet if existing here?
    except Exception:
        return False

    wb.save(filename)
    return True


def addFile(filename, sheet):
    ##  https://stackoverflow.com/questions/13437727/python-write-to-excel-spreadsheet
    ##  Create a new workbook, add a sheet (sheet), and save as (filename)
    book = xlwt.Workbook()
    sh = book.add_sheet(sheet)
    book.save(filename)
    return True


##  Set column widths (not working): https://youtu.be/x18V8SyNiXo
def setColWidth(filename, sheet, c, w):
    ##  Open workbook, copy master file, open sheet, change the width of column (c) to (w), and save.
    rb = xlrd.open_workbook(filename)
    wb = xl_copy(rb)
    sh = wb.get_sheet(0)
    sh.col(c).width = w
    wb.save(filename)
