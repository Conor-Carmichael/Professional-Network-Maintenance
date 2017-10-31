from Updates import *
from GenerateMsg import *
import sys


def initialize():
    print 'ctrl+c to exit'
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



def main():

    # initialize()
    send_update('ccarmichael@umass.edu')
    return 0


if __name__ == "__main__":
    main()
