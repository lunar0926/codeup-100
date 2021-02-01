# 값 입력 n 
# 1부터 해당 값까지 나열. 그 중에서 2로 나누어지는 수는 리스트에
# 리스트에서 반복문으로 요소들 합하기 
n = int(input())
evenList = []
for i in range(1, n+1):
    # ex 5가 입력되면 5까지 반복
    if i % 2 == 0:
        evenList.append(i)
# 리스트 요소들 합하기
sum = 0
for j in evenList:
    sum += j
print(sum)
    

