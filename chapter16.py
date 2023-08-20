import copy

class Time:
    """Represents the time of day.
    
    attributes: hour, minute, second
    """

def print_time(teatime):
    print('%.2d' % teatime.hour,':','%.2d' % teatime.minute,':','%.2d' % teatime.second)

def is_after(t1,t2):
    return(t1.hour > t2.hour 
           or (t1.hour == t2.hour and t1.minute > t2.minute)  
           or (t1.hour == t2.hour and t1.minute == t2.minute and t1.second > t2.second)) 

def increment(time, seconds):
    newtime = copy.copy(time)
    newtime.second += seconds
    if newtime.second >= 60:
        newtime.minute += newtime.second // 60
        newtime.second = newtime.second % 60
    if newtime.minute >= 60:
        newtime.hour += newtime.minute // 60
        newtime.minute = newtime.minute % 60
    return(newtime)
    

time1 = Time()
time1.hour = 4
time1.minute = 29
time1.second = 1
time2 = Time()
time2.hour = 4
time2.minute = 29
time2.second = 0

#print_time(time1)
#print_time(time2)

#print(is_after(time1,time2))

print_time(increment(time1,6190))
print_time(time1)