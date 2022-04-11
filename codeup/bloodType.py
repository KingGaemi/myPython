temp =[]
baby =[]

mom,dad = map(str ,input().split())
mom = list(mom)
dad = list(dad)
for i in mom:
    for j in dad:
    #    print(i,end="")
    #    print(j)
        temp = []
        temp.append(i)
        temp.append(j)
        temp.sort()
    #    print("temp = ", temp)
        baby.append(temp[0] + temp[1])
baby = set(baby)
baby = list(baby)
baby.sort()
temp = []
for i in baby:
    if i[0] == i[1] or i[1] == 'O':
        temp.append(i[0])
    else:
        temp.append(i[0]+i[1])
temp = set(temp)
temp = list(temp)
temp.sort()

for i in temp:
    print(i, end=" ")
