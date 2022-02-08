n, k = map(int, input().split())


my_stars=[]
for i in range(n):
    my_stars.append([])
    for j in range(n):
        my_stars[i].append('*')

if n >= 3:
    for i in range(2,n):
        for j in range(2,n):
            my_stars[i-1][j-1] = ' '


start_star = 1
counting_star = start_star
for i in range(n):
    for j in range(n):
        if counting_star % k == 0:
            my_stars[i][j] = '*'
        counting_star += 1
    start_star += 1
    counting_star = start_star

for i in my_stars:
    for j in i:
        print(j, end='')
    print()
