# -*- coding: utf-8 -
import smtplib, datetime
from email.mime.text import MIMEText
from email.header    import Header



def create_base_email(fname, lname, email, notes):

    body1 = 'I hope all is well since we last spoke.\n\n'
    body2 = 'I just wanted to catch up quickly and see how everything is going. My notes indicate \n{0}'.format(notes)
    sign_off = '''Sincerely,
    Conor Carmichael
    774-254-4238   |  ccarmichael@umass.edu 
    Class of 2019  |  B.S. Computer Science
    College of Information and Computer Science'''
    return body1+body2+sign_off


def is_within_week(next_contact):
    next_contact = datetime.datetime.strptime(next_contact,'%m/%d/%y')
    today = datetime.datetime.now()
    return today < next_contact < today + datetime.timedelta(today, weeks =1)


def is_today(next_contact):
    today = datetime.datetime.now().strftime('%m/%d/%y')
    return today == next_contact


def send_update(send_to_email):
    user = 'social_netw_update_noreply@yahoo.com'
    pw = 'prof_netw_up_cc**'
    smtp_host = 'smtp.mail.yahoo.com'
#, contact_email,fname, lname, notes
    # body = create_base_email(fname, lname, contact_email, notes)
    body = 'this is a test'
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header('subject…', 'utf-8')
    msg['From'] = user
    msg['To'] = send_to_email

    s = smtplib.SMTP(smtp_host, 587, timeout=10)
    s.set_debuglevel(1)
    try:
        s.starttls()
        s.login(user, pw)
        s.sendmail(msg['From'], send_to_email, msg.as_string())
    finally:
        s.quit()


