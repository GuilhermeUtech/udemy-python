#aula sobre datetime

import datetime

t = datetime.time(4,20,1)
print(t.hour)
print(t.minute)
print(t.second)
print(datetime.MAXYEAR)
print(datetime.timedelta)
print(datetime.time.resolution)
today = datetime.date.today()
print(today)
print(today.ctime())
print(today.year)
print(today.isoweekday())