import copy

class Time:
    """Represents the time of day.
    
    attributes: hour, minute, second
    """

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

def mul_time(time, numb):
    newtime = copy.copy(time)
    newint = time_to_int(time) * numb
    return(int_to_time(newint))

def ave_pace(time, dist):
    print_time(mul_time(time, dist**-1))

time1 = Time()
time1.hour = 4
time1.minute = 00
time1.second = 0
distance = 33

ave_pace(time1, distance)
