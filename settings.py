import openpyxl
def init():
    global EXCEL_FILE
    # EXCEL_FILE= openpyxl.load_workbook('testexcel.xlsx')
    global EXCEL_WS
    EXCEL_WS = EXCEL_FILE.get_active_sheet()
