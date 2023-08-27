import copy

class Time:
    """Represents the time of day.
    
    attributes: hour, minute, second
    """
    def is_after(self, other: "Time") -> bool:
        return time_to_int(self) > time_to_int(other)
        
def print_time(teatime):
    print('%.2d' % teatime.hour,':','%.2d' % teatime.minute,':','%.2d' % teatime.second)

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def increment(time,seconds):
    seconds += time_to_int(time)
    return(int_to_time(seconds))

#def increment(time, seconds):
#    newtime = copy.copy(time)
#    newtime.second += seconds
#    if newtime.second >= 60:
#        newtime.minute += newtime.second // 60
#        newtime.second = newtime.second % 60
#    if newtime.minute >= 60:
#        newtime.hour += newtime.minute // 60
#        newtime.minute = newtime.minute % 60
#    return(newtime)
    

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

print(time2.is_after(time1))

print_time(increment(time1,6190))
print_time(time1)