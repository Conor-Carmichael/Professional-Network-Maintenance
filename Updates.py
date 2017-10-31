import openpyxl
import datetime

######################################################################################################
#                                                                                                    #
#           open up the workbook and the worksheet. find the end of the column.                      #
#                                                                                                    #
######################################################################################################
EXCEL_FILE = openpyxl.load_workbook('/home/conor/testexcel.xlsx')
EXCEL_WS = EXCEL_FILE.get_active_sheet()


def set_file_to_rw(file):
    EXCEL_FILE = openpyxl.load_workbook(file)
    EXCEL_WS = EXCEL_FILE.get_active_sheet()


def get_next_open_row():
    return len(EXCEL_WS['A'])+1


def get_next_contact(priority, last_contact):
    # priority one contacts get contact once every month and a half, multiplier of priority val
    wait_time_weeks = priority*6
    if priority == 3:
        wait_time_weeks-4
    last_contact = datetime.datetime.strptime(last_contact,"%m/%d/%y")
    next_contact = last_contact + datetime.timedelta(weeks = wait_time_weeks)
    next_contact = next_contact.strftime('%m/%d/%y')
    return next_contact


def add_contact(fname,lname,email,priority,last_contact,next_talk_notes):
    # concatenate with current row to create key to write to; get next open row so that we right to the proper row
    if find_contact(fname,lname) == 0:
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
        # any sort of info relevant to the next time we talk
        EXCEL_WS[g] = next_talk_notes

        EXCEL_FILE.save('/home/conor/testexcel.xlsx')
        return 1
    else:
        print 0


def update_contact(fname,lname,attribute, new_val):
    # prompt user to enter the column (A,B,C,D...) that they want to update, and provide a new val. need to provide name
    # in order to locate the individual row
    #returns 1 to indicate success of operation, 0 to indicate failure

    row = find_contact(fname,lname)
    if row != 0:
        row = row.replace('A', attribute)
        EXCEL_WS[row] = new_val
        EXCEL_FILE.save('/home/conor/testexcel.xlsx')
        return 1
    else:
        return 0


def find_contact(fname, lname):

    for i in range(1,get_next_open_row()):
        print str(EXCEL_WS['A'+str(i)].value).lower()
        if str(EXCEL_WS['A'+str(i)].value).lower() == fname.lower() and str(EXCEL_WS['B'+str(i)].value).lower()==lname.lower():
            return 'A'+str(i)
        else:
            continue

    return 0


# To remove a contact going to need to find it, set it  '' then iterate and copy the cells forward, or copy all to a new
# sheet. moving all the cells could get a bit difficult so probably best to create new sheet and then rename to original
def remove_contact(fname,lname):
    row = find_contact(fname,lname)
