from GenerateMsg import *
import datetime
from User import User

today = datetime.datetime.now().strftime('%m/%d/%y')
user = User()
user.retrieve_info()

contacts = user.retrieve_objects_from_csv()
contact_within_week = []
contact_now = []

for c in contacts:
    if is_within_week(c.next_contact):
        contact_within_week.append(c)
    if is_today(c.next_contact):
        contact_now.append(c)

message = 'Hello {0}, here is your outlook for this week.\n\n'.format(user.user_fname)

if contact_within_week != []:
    message += 'Who you need to contact within the next week:\n'
    for c in contact_within_week:
        message += '{0} {1}, should be contacted by {2} at {3}. ' \
                   'You last contacted them on {4}, and wanted ' \
                   'to talk to them about"{5}"\n'.format(c.fname, c.lname, c.next_contact, c.email, c.last_contact, c.notes)


if contact_now != []:
    message += '\nHere is who you should reach out to as soon as possible:\n'

    for c in contact_now:
        message += '{0} {1}, should be contacted today ({2}) at {3}. ' \
                   'You last contacted them on {4} and wanted ' \
                   'to talk to them about"{5}"\n'.format(c.fname, c.lname, today, c.email, c.last_contact, c.notes)

if contact_now != [] or contact_within_week != []:
    send_update(user.email, message)
