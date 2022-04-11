dong,chul,yoo = map(int, input().split())


year = 2100
month = 1
date = 1
maxDate = 31
dow = ['MON','TUE','WED','THU','FRI','SAT','SUN']
sameDay = 0;
def getMaxDate(month):
    if month == 1 or month == 3 or month == 5 or month  == 7 or month == 8 or month == 10 or month ==12:
        maxDate = 31
    elif month == 2:
        if year%400 == 0:
            maxDate = 29
        elif (year % 4 == 0) and (year % 100 != 0):
            maxDate = 29
        else:
            maxDate = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        maxDate = 30
    else:
        maxDate = 1

    return maxDate




#print(year,format(month,'02'),format(date,'02'),sep="-",end=" ")
#print(dow[5])
if dong > chul:
    dong, chul = chul, dong
if dong > yoo:
    dong, yoo = yoo, dong
if chul > yoo:
    chul, yoo = yoo, chul

while True:
    if(sameDay%dong == 0 and sameDay%chul == 0 and sameDay % yoo == 0 and sameDay != 0):
        break
    sameDay += dong

#print(sameDay)
days = 1
maxDate = getMaxDate(month)
for i in range(sameDay):
    date += 1
    days += 1
    if date > maxDate:
        date = 1
        month += 1
        if month >= 12:
            month = 1
            year += 1
        maxDate = getMaxDate(month)
    #print(year,format(month,'02'),format(date,'02'),sep="-", end=" ")
#    print(dow[(days+4)%7])

print(year,format(month,'02'),format(date,'02'),sep="-", end=" ")
print(dow[(days+3)%7])
