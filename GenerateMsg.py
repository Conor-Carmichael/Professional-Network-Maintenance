import smtplib, datetime



def create_base_email(fname, lname, email, notes):
    subject = 'Hello {0}'.format(fname)
    body1 = 'I hope all is well since we last spoke.\n\n'
    body2 = 'I just wanted to catch up quickly and see how everything is going. My notes indicate \n{0}'.format(notes)
    sign_off = '''Sincerely,
    Conor Carmichael
    774-254-4238   |  ccarmichael@umass.edu 
    Class of 2019  |  B.S. Computer Science
    College of Information and Computer Science'''

def is_within_week(next_contact):
    today = datetime.datetime.now().strftime('%m/%d/%y')
    if datetime.timedelta(today,next_cont