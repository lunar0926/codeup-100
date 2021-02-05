h, w = map(float, input().split())
standard_Weight = (h - 100) * 0.9
obesity = (w - standard_Weight) * 100 / standard_Weight
if obesity <= 10:
    print('정상')
elif obesity > 10 and obesity <= 20:
    print('과체중')
elif obesity > 20:
    print('비만')
