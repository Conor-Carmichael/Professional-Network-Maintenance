import openpyxl,datetime

######################################################################################################
#                                                                                                    #
#           open up the workbook and the worksheet. find the end of the column.                      #
#                                                                                                    #
######################################################################################################
EXCEL_FILE = openpyxl.load_workbook('/home/conor/testexcel.xlsx')
EXCEL_WS = EXCEL_FILE.get_active_sheet()


def get_next_open_row():
    #returns
    return len(EXCEL_WS['A'])+1


def get_next_contact(priority, last_contact):
    #priortiy one contacts get contact once every month and a half, multiplier of priority val
    wait_time_weeks = priority*6
    if priority==3:
        wait_time_weeks-4
    last_contact = datetime.datetime.strptime(last_contact,"%m/%d/%y")
    next_contact = last_contact + datetime.timedelta(weeks = wait_time_weeks)
    next_contact = next_contact.strftime('%m/%d/%y')
    return next_contact


def add_contact(fname,lname,email,priority,last_contact,next_talk_notes):
    #concatenate with current row to create key to write to; get next open row so that we right to the proper row
    i=get_next_open_row()
    a = 'A'+str(i)
    EXCEL_WS[a] = fname
    b='B'+str(i)
    EXCEL_WS[b] = lname
    c='C'+str(i)
    EXCEL_WS[c] = email
    d='D'+str(i)
    EXCEL_WS[d] = priority
    e='E'+str(i)
    EXCEL_WS[e] = last_contact
    f='F'+str(i)
    EXCEL_WS[f] = get_next_contact(priority,last_contact)
    g = 'G'+str(i)
    #any sort of info relevant to the next time we talk
    EXCEL_WS[g] = next_talk_notes

    EXCEL_FILE.save('/home/conor/testexcel.xlsx')


def update_contact(contact_,attribute, new_val):
    #prompt user to enter the column (A,B,C,D...) that they want to update, and provide a new val


def find_contact(fname, lname):
    # columns = ['A','B','C','D','E','F','G']

    for i in range(1,get_next_open_row()):
        if EXCEL_WS['A'+str(i)]== fname and EXCEL_WS['B'+str(i)]:
                return 'A'+str(i)
            else:
                continue

    return 'Contact not found.'




