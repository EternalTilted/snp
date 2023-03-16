import datetime

def date_in_future(integer):
    date = str(datetime.datetime.today())
    if type(integer) == int:
        return date[0:8] + str(int(date[8:10])+integer) + date[10:19]
    else: 
        return date[0:19]

print(date_in_future([]))
print(date_in_future(2))
