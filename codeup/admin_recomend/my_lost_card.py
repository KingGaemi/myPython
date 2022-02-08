cards = []
n = int(input())

for i in range(n-1):
    cards.append(int(input()))
# print(cards)
cards.sort()
# print(cards)
# print(cards[n-2])
if cards[n-2] != n:
    print(n)
else:
    for i in range(1, n):
        if cards[i-1] != i:
            print(i)
            break
