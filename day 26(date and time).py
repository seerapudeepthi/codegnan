DATE AND TIME:
_________________

->python provides the built-in datetime module to work with dates and time....

import datetime
----------------
import datetime
today = datetime.date.today()
now = datetime.datetime.now()
print(now)
print(today)
____________________________________________________

YEAR AND MONTH:
    
import datetime
no = datetime.datetime.now()
print(f"year is  : {now.year}")
print(f"Month is : {now.month}")
print(f"Day is   : {now.day}")
print(f"Hour is  : {now.hour}")
print(f"Min is   : {now.minute}")
print(f"seconds  : {now.second}")
____________________________________________________________

FORMATTING DATE AND TIME:
    
->strftime() is used to formate date and time
->%d is day
->%m is month
->%Y is year
->%H is hour
->%M is min
->%S is sec

import datetime
now = datetime.datetime.now()
print(now.strftime("%d-%m-%y"))
print(now.strftime("%H-%M-%S"))

___________________________________________________________________

DIFFERENCE FROM YEAR TO YEAR:
    
import datetime
date_1 = datetime.date(2026,6,1)
date_2 = datetime.date(2025,6,1)
differ = date_1 - date_2
print(differ)
____________________________________________________________________

TIMEDELTA:

import datetime
today = datetime.date.today()
future = today + datetime.timedelta(days = 7)
print(future)

___________________________________________________________________
C-TIME:

import datetime
day = datetime.date.today()
print(day.ctime())
__________________________________________________________________
CALENDAR FOR ONE MONTH:

import calendar
import datetime
today = datetime.date.today()
year = today.year
month = today.month
print(calendar.month(year,month))

             (or)
             
import calendar
import datetime
today = datetime.date.today()
year = 2027
month = 8
print(calendar.month(year,month))
________________________________________________________
CALENDAR OF AN YEAR:

import calendar
print(calendar.calendar(2027))

___________________________________________________________
PROJECT ON DATETIME THROUGH EMAIL:

import smtplib
from email.message import EmailMessage
import datetime
from datetime import datetime

sender = "deepthiseerapu2004@gmail.com"
password = 'zcfrvlwlkygkpvjg'
receiver = "kavs14345@gmail.com"
target_time = '10:37'

msg = EmailMessage()
msg['subject']='greetings'
msg['From']= sender
msg['To']= receiver
msg.set_content('hello hii good morning ')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(msg)
server.quit()

_____________________________________________________________________________________




























