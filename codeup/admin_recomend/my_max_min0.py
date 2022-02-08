mylist = []
max = -1000000
min = 1000000

for i in range(5):
    n = int(input())
    if(n > max): max = n
    if(n < min): min = n

print(max)
print(min)
