a = list(map(int, input().split()));

a.sort();
day = a[0];
while(day%a[0]!=0 or day%a[1] != 0 or day%a[2] != 0):
    day += a[0]

print (day)
