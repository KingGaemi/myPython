a, b = map(int,input().split())

# lengthes=[]

def get_length(n):
    count = 0
    while n != 1:
        if n % 2 == 1:
            n = 3*n+1
        else:
            n = int(n / 2)
        # print("n = ", n)
        count += 1
    return count+1

# print(get_length(5))

highest = 1
longest = 1
for i in range(a,b+1):
    if longest < get_length(i):
        highest = i
        longest = get_length(i)
    print("longest={},highest={}".format(highest,longest))
print(highest,longest)
