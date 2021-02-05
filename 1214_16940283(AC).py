month = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 29]
y, m = map(int, input().split())
if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    print(month[13])
else:
    print(month[m])
