import datetime

now=datetime.datetime.now()

print(now.strftime("%d:%m:%Y"))

print(datetime.date.today().month)

x=datetime.datetime(2020,4,12)
y=datetime.datetime(2019,2,13)

dif=x-y
print(dif)

end=datetime.datetime.now()

difference=end-now

print(difference)
print(y)
print(x)
