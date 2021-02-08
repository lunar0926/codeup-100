a, b = map(int, input().split())
list = [a, b]
list.sort()
while(True):
    if list[0] <= list[1]:
        print(list[0], end = ' ')
        list[0] += 1
    else:
        break

