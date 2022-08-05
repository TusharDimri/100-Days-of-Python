import datetime as dt

now = dt.datetime.now()
# print(now)
# print(type(now))
# print(str(now).split(" ")[0].split("-"))  # Non Pythonic way of doing things.

date = now.date()
day = now.day
month = now.month
year = now.year
print(date)
print(day)
print(month)
print(year)

day_of_week = now.weekday()
print(day_of_week)  # Integer and couing starts from Mondy = 0

date_of_birth = dt.datetime(year=2002, month=7, day=19, hour=19)
print(date_of_birth)