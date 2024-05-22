import datetime
d = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3), "BRT"))
print(d)

d_utc = d.astimezone(datetime.timezone.utc)
print(d_utc)

