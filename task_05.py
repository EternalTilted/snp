import datetime

def date_in_future(integer):
    date = str(datetime.datetime.today())
    if type(integer) == int:
        return str(int(date[8:10])+integer) + date[4:8] + date[0:4] + date[10:19]
    else: 
        return date[8:10]  + date[4:8] + date[0:4] + date[10:19]

print(date_in_future([]))
print(date_in_future(2))
