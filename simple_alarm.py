import datetime,winsound
hour = input("Enter Hour: ")
minute = input("Enter minutes: ")
message = input("Enter Message: ")
while True:
    date_time = str(datetime.datetime.now())
    time_now = str(str(date_time.split(" ")[-1]).split(".")[0]).split(":")
    hour_now = (time_now[0])
    min_now  =  (time_now[1])
    sec_now   =  (time_now[2])
    if hour_now == hour and min_now == minute:
        if sec_now == "01":
            print(message)
        winsound.Beep(500,1500)
    else:
        pass
