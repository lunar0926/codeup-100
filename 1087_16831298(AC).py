'''
정수 1개 입력받음 
sum = 0
if sum >= n:
합이 더 커지는 순간의 값. 더하고나서 조건문 확인
조건문에서 비교하는 값은 합과 입력값. 변수의 쓰임을 잘 구분하기(문제 요구사항과 관련)
반복문의 범위는 최솟값에서 최댓값을 모두 고려할 수 있어야 함.
break
'''
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
    if sum >= n:
        print(sum)
        break

