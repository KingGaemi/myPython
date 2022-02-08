n = int(input())

square = []

for i in range(n):
    square.append([])
    for j in range(n):
        square[i].append(0)

square[0][n//2] = 1

count = 2
i = 0
j = n//2
while True:

# ?    else:
    i += n - 1
    i = i % n
    j += 1
    j = j % n

    if count > n*n:
        break
    square[i][j] = count
    if count % n == 0:
        i += 1
        i = i % n
        count += 1
        if count > n*n:
            break
        square[i][j] = count
    # j -= 1
    # j = j % n
    count += 1

    # for k in square:
    #     for l in k:
    #         print(l, end=' ')
    #     print()
    # print()




for i in square:
    for j in i:
        print(j, end=' ')
    print()
