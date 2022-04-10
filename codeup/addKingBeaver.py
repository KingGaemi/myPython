# 최대 갯수 입력 받기
n = int(input())

# 최대 갯수 크기의 리스트 생성
a = [n]

# temp 리스트 생성 후 입력 받기
temp = list(map(int,input().split()))

# a[0]부터 a[n-1]까지  temp에 있던 자료 복사
for i in range(n):
    a.append(temp[i])

# 연속 부분 수열 시작점과 끝점 입력받기 s =start, e = end
s, e = map(int, input().split())

# targetSum = s~e까지의 합
targetSum = 0

# sum = 현재 연속 부분 수열의 합
sum = 0

# count = 찾아낸 동일한 sum 값을 갖고있는 연속 부분 수열의 갯수
count = 0

# s~e까지의 합 = targetSum 구하기
for i in range(s,e+1):
    targetSum += a[i]
    # print(a[i])
# print ("targetSum = ", targetSum)


# 수열의 처음부터 끝까지 s가 될 수 있다
for i in range (0, n+1):
    sum = 0
    for j in range(i, n+1):
        sum+=a[j]
        #print(a[j],end=' ')
        if(sum == targetSum):
            count += 1
            # print("sum= ", sum," ", "count= ", count)
#    print("sum = " , sum, "")



print(count)
