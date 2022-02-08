mylist = []
for i in range(5):
    mylist.append(int(input()))
mylist.sort(reverse = True)
print(mylist[0])
mylist.sort()
print(mylist[0])
