from Updates import *
from GenerateMsg import *
from Driver import main
import sys


def initialize():
    print '~ctrl+c to exit~'
    try:
        while 1:
            fname = raw_input('\nEnter contacts first name: ').lower()
            lname = raw_input('\nEnter last name: ').lower()
            email = raw_input('\nEnter email address: ')
            priority = int(raw_input('\nEnter priority (value 1-3): '))
            last_contact = raw_input('\nEnter date of last contact (format = mm/dd/yy): ')
            notes = raw_input('\nEnter note to remind you of things to talk about next time you talk: ')
            if add_contact(fname,lname,email,priority,last_contact,notes):
                print '\n\n {0} {1} was added successfully to your contact list!'.format(fname,lname)
            else:
                print '\n\n {0} {1} already exists in your contact list!'.format(fname,lname)

    except KeyboardInterrupt as e:
        print 'End of initialization of contact list. {0}'.format(e)


def update():
    fname = raw_input('First name of contact to update: \n')
    lname = raw_input('Last name of contact to update: \n')

    attr = raw_input('Enter the letter of corresponding column to update:\nemail (C), Priority (D), Last Contact (E), Next Contact (F), Notes (G)\n')
    val = raw_input('Enter new value for corresponding cell: ')
    if update_contact(fname,lname,attr.upper(),val):
        print 'Contact update successful'
    else:
        print 'Contact update failed, check spelling of name or column entered.'
    main()


def new_file(file):
    global EXCEL_FILE
    EXCEL_FILE= openpyxl.load_workbook(file)
    global EXCEL_WS
    EXCEL_WS= EXCEL_FILE.get_active_sheet()
    EXCEL_WS['A1'],EXCEL_WS['B1'],EXCEL_WS['C1'],EXCEL_WS['D1'],EXCEL_WS['E1'],EXCEL_WS['F1'],EXCEL_WS['G1'] = 'First Name', 'Last Name', 'Email', 'Priority', 'Last Contact','Next Contact', 'Notes for Next Contact'



def first_time_setup():
    file_path = raw_input('To start, enter a file path to a Excel spreadsheet that is either blank, or already formatted, or you have yet to create.\n')
    print 'Now we can intialize the contacts in your workbook, if the file is not empty (but formatted properly) contacts will be added on.\n'
    initialize()
    main()

def home_screen():
    response = raw_input('Welcome, to begin first time setup press 1, to update a contacts information press 2.\n')
    if response == 1:
        first_time_setup()
    elif response == 2:
        update()
    else:
        home_screen()

