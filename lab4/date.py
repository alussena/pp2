#1
from datetime import datetime, timedelta

current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print(new_date.strftime("%d-%m-%Y"))

#2
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(yesterday.strftime("%d-%m-%Y"))
print(today.strftime("%d-%m-%Y"))
print(tomorrow.strftime("%d-%m-%Y"))

#3
from datetime import datetime

now = datetime.now().replace(microsecond=0)
print(now)

#4
from datetime import datetime

date2 = datetime(2025, 2, 10, 22, 13, 0)
date1 = datetime(2006, 12, 1, 4, 30, 0)

difference = (date2 - date1).total_seconds()
print(int(difference))