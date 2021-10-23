import datetime
date = str(datetime.date.today()).split("-")
year,month,day = date[0],date[1],date[2]
DATE = input("Enter 'day','month','year', separated by ',': ")
Event = input("Enter Event: ")
date = [day,month,year]
Date = DATE.split(",")
result = (date == Date)
while True:
     if result:
               print(Event)
               result = False
     else:
          continue
