import datetime

#def birthday_time(year,month,day):


from datetime import datetime
today = datetime.today()

print(today.day)
print(today.strftime('%A'))

birthday = '03/04/1971'

bday = datetime.strptime(birthday, '%d/%m/%Y')
print(bday)
next_bday = bday.replace(year=today.year)
if next_bday < today:
    next_bday = next_bday.replace(year=today.year+1)
print(next_bday)

until_next_bday = next_bday - today
print(until_next_bday)

print("Your current age:")
last_bday = next_bday.replace(year=next_bday.year-1)
age = last_bday.year - bday.year
print(age)


#def what_day():
#    date(2002, 12, 4).weekday()
    