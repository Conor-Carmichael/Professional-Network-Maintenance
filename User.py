class User:

    def __init__(self):
        self.user_fname = None
        self.user_lname = None
        self.email = None
        self.cell = None
        self.file_path = None
        self.EXCEL_FILE = None
        self.EXCEL_WS = None

    def store_info(self):
        f = open('data/userinfo','w')
        to_store = [self.user_fname, self.user_lname, self.email, self.cell, self.file_path]
        f.write(','.join(to_store))
        print 'User info successfully written to file.'
        f.close()

    def retrieve_info(self):
        # TODO will need to read in the file path to the excel and reopen up the workbook and worksheet, cant store that
        import csv,openpyxl
        with open('data/userinfo','r') as f:
            r = csv.reader(f)
            data = next(r)
            self.user_fname = data[0]
            self.user_lname = data[1]
            self.email = data[2]
            self.cell = data[3]
            self.file_path = data[4]
            self.EXCEL_FILE = openpyxl.load_workbook(data[4])
            self.EXCEL_WS = self.EXCEL_FILE.get_active_sheet()

    def create_workbook(self):
        import openpyxl
        file = open('data/contact_spreadsheet.xlsx','w')
        self.file_path = file
        self.EXCEL_FILE = openpyxl.load_workbook(self.file_path)
        self.EXCEL_WS = self.EXCEL_FILE.get_active_sheet()
        self.EXCEL_WS['A1'], self.EXCEL_WS['B1'], self.EXCEL_WS['C1'], self.EXCEL_WS['D1'], self.EXCEL_WS['E1'], \
        self.EXCEL_WS['F1'], self.EXCEL_WS['G1'] \
            = 'First Name', 'Last Name', 'Email', 'Priority', 'Last Contact','Next Contact', 'Notes for Next Contact'
