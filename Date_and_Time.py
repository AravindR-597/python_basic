import datetime

print(datetime.datetime.now())
print(datetime.date.today())
now=datetime.datetime.now()
print(now.strftime("%d-%m-%Y"))

x=datetime.datetime(2020,2,13)
y=datetime.datetime(2021,5,13)
diff=y-x
print(diff)
end=datetime.datetime.now()
dif=end-now
print(dif)