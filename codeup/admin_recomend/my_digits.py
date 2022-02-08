n = int(input())
count = 0
compare = 1
while True:
    if compare > n:
        break
    else:
        count += 1
        compare *= 10

print(count)
