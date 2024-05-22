import datetime

d = datetime.datetime.now()

print(d.strftime("%d/%m/%Y,%H:%M:%S"))

date_string = " 22/05/2023 14:00"
d = datetime.datetime.strptime(date_string,"%d/%m/%Y,%H:%M:%S")
print(d)