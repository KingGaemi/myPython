n, k = map(int, input().split())

# for i in range(n): print('*',end='')
# print()
counting_star = 0

for i in range(n):
    for j in range(n):
        if counting_star % k != 0 and counting_star % k != 1:
            print('*',end='')
        else:
            print(' ',end='')

        counting_star += 1

    print()
# for i in range(n): print('*',end='')
