a, b, c = map(int, input().split())
triangle = [a, b, c]
triangle.sort()
if triangle[2] < triangle[0] + triangle[1]:
    print('yes')
else:
    print('no')

