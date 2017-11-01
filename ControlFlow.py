from Updates import *
from User import User


def initialize(user):
    while 1:
        fname = raw_input('\nEnter contacts first name: ').lower()
        lname = raw_input('\nEnter last name: ').lower()
        email = raw_input('\nEnter email address: ')
        priority = int(raw_input('\nEnter priority (value 1-3): '))
        last_contact = raw_input('\nEnter date of last contact (format = mm/dd/yy): ')
        notes = raw_input('\nEnter note to remind you of things to talk about next time you talk: ')

        if add_contact(user, fname, lname, email, priority, last_contact, notes):
            print '\n\n {0} {1} was added successfully to your contact list!'.format(fname, lname)
        else:
            print '\n\n {0} {1} already exists in your contact list!'.format(fname, lname)

        yn = raw_input('Add more contacts?(y or n)?: ')
        if yn == 'n':
            return


def update(user):
    fname = raw_input('First name of contact to update: \n')
    lname = raw_input('Last name of contact to update: \n')

    attr = raw_input('Enter the letter of corresponding column to update:\nemail (C), Priority (D), Last Contact (E), Next Contact (F), Notes (G)\n')
    val = raw_input('Enter new value for corresponding cell: ')

    if update_contact(user, fname, lname, attr.upper(), val):
        print 'Contact update successful'
    else:
        print 'Contact update failed, check spelling of name or column entered.'
        update(user)


def first_time_setup(user):
    fname = raw_input('Enter your first name: ')
    lname = raw_input('Enter your last name: ')
    user.user_fname = fname
    user.user_lname = lname
    user.create_workbook()
    print 'Now we can intialize the contacts in your workbook, if the file is not empty (but formatted properly) contacts will be added on.\n'
    initialize(user)
    set_email_pref(user)
    set_text_pref(user)
    print 'You will be notified accordingly when you should reach out to a contact!'
    user.store_info()
    user.EXCEL_FILE.save(user.file_path)


def home_screen():
    try:
        response = raw_input('Welcome, to begin first time setup press 1, to update a contacts information press 2.\n')
        if int(response )== 1:
            user = User()
            first_time_setup(user)
        elif int(response )== 2:
            user = User()
            user.retrieve_info()
            update(user)
            user.store_info()
        else:
            home_screen()
    except KeyboardInterrupt as k:
        user.store_info()
        user.EXCEL_FILE.save(user.file_path)
        print k

def set_email_pref(user):
    username = raw_input('Enter the email address where you would like to receive notification: ')
    yesorno = raw_input('Are you sure this email is correct <{0}>?(y or n)'.format(username))
    if yesorno.lower() == 'y':
        user.email=username
        print 'Email intialization complete'
    else:
        print 'No emails will be sent. Text messaging information will be needed.\n'
        return


def set_text_pref(user):
    phone = raw_input('Enter the phone number where you would like to receive notification: ')
    yesorno = raw_input('Are you sure this phone number is correct <{0}>?(y or n)'.format(phone))
    if yesorno.lower() == 'y':
        user.cell = phone
        print 'Cell phone intialization complete'
    else:
        if user.email is None:
            selection = raw_input('You have previously opted to not use email notifications, ' \
                  'would you prefer to use email or phone? ("email" or "phone:): ')
            if selection.lower() == 'email':
                set_email_pref()
            else:
                set_text_pref()
    return
