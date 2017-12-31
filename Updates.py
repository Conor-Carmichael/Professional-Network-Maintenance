import datetime
import re

######################################################################################################
#                                                                                                    #
#           open up the workbook and the worksheet. find the end of the column.                      #
#                                                                                                    #
######################################################################################################



def get_next_open_row(user):
    return user.EXCEL_WS.max_row+1


def get_next_contact(priority, last_contact):
    # priority one contacts get contact once every month and a half, multiplier of priority val
    wait_time_weeks = priority*6
    if priority == 3:
        wait_time_weeks-4
    last_contact = datetime.datetime.strptime(last_contact,"%m/%d/%y")
    next_contact = last_contact + datetime.timedelta(weeks = wait_time_weeks)
    next_contact = next_contact.strftime('%m/%d/%y')
    return next_contact


def add_contact(user,fname,lname,email,priority,last_contact,next_talk_notes):
    # concatenate with current row to create key to write to; get next open row so that we write to the proper row
    if find_contact(user, fname, lname) == 0:
        i=get_next_open_row(user)
        a = 'A'+str(i)
        user.EXCEL_WS[a] = fname.title()
        b='B'+str(i)
        user.EXCEL_WS[b] = lname.title()
        c='C'+str(i)
        user.EXCEL_WS[c] = email
        d='D'+str(i)
        user.EXCEL_WS[d] = priority
        e='E'+str(i)
        user.EXCEL_WS[e] = last_contact
        f='F'+str(i)
        user.EXCEL_WS[f] = get_next_contact(priority,last_contact)
        g = 'G'+str(i)
        # any sort of info relevant to the next time we talk
        user.EXCEL_WS[g] = next_talk_notes

        user.EXCEL_FILE.save(user.file_path)
        return 1
    else:
        print 0


def update_contact(user,fname,lname,attribute, new_val):
    # prompt user to enter the column (A,B,C,D...) that they want to update, and provide a new val. need to provide name
    # in order to locate the individual row
    #returns 1 to indicate success of operation, 0 to indicate failure

    row = find_contact(user, fname, lname)
    if row != 0:
        pattern = re.compile("\d{2}/\d{2}/\d{2}")
        if row == 'E' or row == 'F':
            if pattern.findall(new_val) != []:
                row = row.replace('A', attribute)
                user.EXCEL_WS[row] = new_val
                user.EXCEL_FILE.save(user.file_path)
                return 1
            else:
                return 0
        else:
            row = row.replace('A', attribute)
            user.EXCEL_WS[row] = new_val
            user.EXCEL_FILE.save(user.file_path)
            return 1

    else:
        return 0


def find_contact(user, fname, lname):
    for i in range(2, get_next_open_row(user)):

        if str(user.EXCEL_WS['A'+str(i)].value).lower() == fname.lower() and str(user.EXCEL_WS['B'+str(i)].value).lower()== lname.lower():
            return 'A'+str(i)

    return 0


def return_next_dates(user):
    ret_list = []
    for i in range(2, get_next_open_row(user)):
        ret_list.append(user.EXCEL_WS['F'+str(i)])
    return ret_list

# To remove a contact going to need to find it, set it  '' then iterate and copy the cells forward, or copy all to a new
# sheet. moving all the cells could get a bit difficult so probably best to create new sheet and then rename to original
# def remove_contact(fname,lname):
#     row = find_contact(fname,lname)
