import time

current_time = time.time()
print(current_time)

def days(now_time):
    now_days = now_time // 86400
    print('days ' + str(now_days))
    days_remainder = now_time % 86400
    hours(days_remainder)
    
def hours(now_time):
    now_hours = now_time // 3600
    print('hours ' + str(now_hours))
    hours_remainder = now_time % 3600
    minutes(hours_remainder)
    
def minutes(now_time):
    now_minutes = now_time // 60
    print('minutes ' + str(now_minutes))
    minutes_remainder = now_time % 60
    seconds(minutes_remainder)
    
def seconds(now_time):
    print('seconds ' + str(now_time))
    
    
#def hours
days(current_time)