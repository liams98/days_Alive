import datetime
import time

def leapYear(year): #it checks if the year is a leap year or not
    if(year % 400 == 0):
        return True
    if(year % 100 == 0):
        return False
    if(year % 4 == 0):
        return True
    return False

def dateIsBefore(y1,m1,d1, y2,m2,d2): #it checks if the first date is before the second date
    if(y1 < y2):
        return True
    if(y1 == y2):
        if(m1 < m2):
            return True
        if(m1 == m2):
            if(d1 < d2):
                return True
        print("Son you better stop playing with my program and add the date correctly")
        return False

def daysInMonth(year , month): # it shows how many days are there in every month
    if(month in(1,3,5,7,9,10,12)):
       return 31
    if(month == 2):
       if(leapYear(year)):
          return 29
       return 28
    return 30

def nextDay(year,month,day): # this function adds on days and month and year when they reach maximum
    if(day < daysInMonth(year,month)):
       return year,month,day + 1
    else:
       if(month == 12):
           return year + 1,1,1
       else:
           return year,month + 1,1

def Days_Alive(year1,month1,day1, year2,month2,day2): # this is the main function that calculates the days you have lived between 2 dates
    assert not dateIsBefore(year2,month2,day2, year1,month1,day1)
    days = 0
    while(dateIsBefore(year1, month1, day1, year2, month2, day2)):
          year1,month1,day1 = nextDay(year1,month1,day1)
          days+=1
    return days

now = datetime.datetime.now()# gets the current date in digits

print("\nHello my aging friend! I want you to add your birthdate:\n")
print("Your birthdate must be in numbers\n")



#takes the input of the user
Year = " "
Month = " "
Day = " "

print("Year you're born on: " + Year)
Year = int(input(Year))

print("Month you're born on: " + Month)
Month = int(input(Month))

print("Day you're born on: " + Day)
Day = int(input(Day))


print(Days_Alive(Year,Month,Day, now.year,now.month,now.day))

time.sleep(5)
    


       
       
        
