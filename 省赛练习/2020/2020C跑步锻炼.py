import datetime
start=datetime.datetime(2000,1,1)
end=datetime.datetime(2020,10,1)
delta=datetime.timedelta(days=1)
res=0
while(start<=end):
    if start.isoweekday()==1 or start.day==1:
        res+=2
    else:
        res+=1
    start+=delta
print(res)
