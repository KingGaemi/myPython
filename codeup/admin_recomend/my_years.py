year = int(input())

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if (year % 4) == 0 and (year // 4) >= 1 and (year % 100) != 0:
        return True
    else:
        return False

if is_leap_year(year):
    print('yes')
else:
    print('no')
