#ex 2.2.1
radius = 5
pi = 3.1415926535897932
vol = (4/3)*pi*(radius**3)
print(vol)
#ex 2.2.2
unitprice = 24.95
discprice = unitprice * 0.6
no_copies = 60
shipping = 3 + ((no_copies - 1) * 0.75)
wholesale = (no_copies * discprice) + shipping
print(wholesale)
#ex 2.2.3
current_time_secs = (6*3600) + (52*60)
run_time_secs = (((8*60) + 15) * 2) + (((7*60) + 12) * 3)
total_secs = current_time_secs + run_time_secs
print(total_secs)
finish_time_hrs = (total_secs) // 3600
print(finish_time_hrs)
finish_time_mins = ((total_secs) - (finish_time_hrs * 3600)) // 60
print(finish_time_mins)
finish_time_secs = ((total_secs) - (finish_time_hrs * 3600) - (finish_time_mins * 60))
print(finish_time_secs)