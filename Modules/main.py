#import datetiome and bday_message module
import datetime
import bday_message

today = datetime.date.today()
next_birthday = datetime.date(2026, 2, 18)

days_away = next_birthday - today

if today == next_birthday:
    print(bday_message.random_message)
else:
    print("My next birhday is ", days_away.days, "days away")