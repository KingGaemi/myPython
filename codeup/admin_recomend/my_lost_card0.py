cards = []
n = int(input())

for i in range(n+1):
    cards.append(0)

for i in range(n-1):
    j = int(input())
    cards[j] = 1

for i in range(1,n+1):
    if cards[i] == 0:
        print(i)
