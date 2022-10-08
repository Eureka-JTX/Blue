from datetime import datetime,timedelta
start=datetime(1970,1,1)
delta=timedelta(milliseconds=1)
t=int(input())
for i in range(t):
    end=int(input())
    end=start+end*delta
    print("%02d:%02d:%02d"%(end.hour,end.minute,end.second))
