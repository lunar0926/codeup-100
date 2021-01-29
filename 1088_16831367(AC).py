'''
3의 배수는 n % 3 == 0 인 경우 출력하지 않기(continue)
1부터 입력한 정수까지
'''
n = int(input())
for i in range(1, n+1):
    if i % 3 == 0:
        continue
    print(i, end = ' ')
    

