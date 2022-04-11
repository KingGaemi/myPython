month = 3
date = 1
maxDay = 1
day = 1
compliment = 1
students = 1
goal = 1000
def isPrime(day):
    for i in range(2,day+1):
        if(day%i == 0 and day!=i):
            return False
    return True

if month == 1 or month == 3 or month == 5 or month  == 7 or month == 8 or month == 10 or month ==12:
    maxDay = 31
elif month == 2:
    maxDay = 28
elif month == 4 or month == 6 or month == 9 or month == 11:
    maxDay = 30
else:
    maxDay = 1

for month in range(3,14):
    if month == 13:
        month = 1
    for date in range(1, maxDay+1):
        print(month,"월 ", date,"일")
        if(isPrime(day)):
            students += compliment*3
            compliment*=3
        else:
            students += compliment*2
            compliment*=2
        day += 1
        print(compliment)
        if compliment>goal:
            break
    if compliment>goal:
        break
