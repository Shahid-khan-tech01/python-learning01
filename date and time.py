import datetime

from docutils.nodes import target

# For a chosen date
date = datetime.date(2026, 8, 7)
print(date)
# for today's date
today = datetime.date.today()
print(today)
# for chosen time
time = datetime.time(23,59,59)
print(time)
# for exact today's date with the time
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %d/%m/%y")
print(now)
print()

# A simple exercise for the checking the target
target_datetime = datetime.datetime(2025, 8, 7, 12, 30, 1)
current = datetime.datetime.now()

if target_datetime > current:
    print("The target date is in the future")
else:
    print("The target date is not in the future")