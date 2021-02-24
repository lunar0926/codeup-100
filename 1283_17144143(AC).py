money = int(input())
day = int(input())
percent = list(map(int, input().split()))
result = money
for i in range(day):
    result += float(result) * float(percent[i]) / 100.0
earning = result - money # 순수익 = 최종 값 - 투자한 액수
earning = round(earning)
print(earning)
if earning > 0:
    print('good')
elif earning == 0:
    print('same')
else:
    print('bad')


