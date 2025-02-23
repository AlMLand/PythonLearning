import datetime
from datetime import time, timedelta

time_1 = time(1, 2, 3)
print(time_1)

date = datetime.time(1, 2, 3)
print(date)

now = datetime.datetime.now()
now_formatted = now.strftime("%d.%m.%Y - %H:%M:%S")
print(now_formatted)

today = datetime.date.today()
print(today)

###

date_1 = datetime.datetime(1234, 12, 23, 11, 22, 33)
date_2 = datetime.datetime(1236, 12, 23, 11, 22, 33)
print(timedelta(12, 34))
