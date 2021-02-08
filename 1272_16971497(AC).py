a, b = map(int, input().split())
'''
person = [a, b]
money = [0, 0]
for i in range(2):
    if person[i] % 2 == 0: # 짝수인 경우
        result = 5 * person[i]
        money[i] = result
    else: # 홀수인 경우
        result = 0.5 * (person[i] + 1)
        money[i] = result
print(money[0] + money[1])
'''
dic = {}
dic[a] = 0
dic[b] = 0
for i in dic.keys():
    if i % 2 == 0:
        dic[i] = 5 * i
    else:
        dic[i] = 0.5 * (i + 1)
print('%d'%(dic[a] + dic[b]))

