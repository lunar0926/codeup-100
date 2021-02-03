'''
h 세로 w 가로 n 개수 l 길이 d 방향(0 or 1)
x y 위치
<입력>
세로 가로 (고정된 값이 아님)
막대개수
길이 방향 좌표
...
입력받은 값대로 격자판 만들기(0부터 시작)
막대의 개수대로 막대 리스트 각각 만들기
n 개만큼 입력 받아서 변수로 저장.
stickList = [], append([2 0 1 1])
요소를 사용할 때는 stickList[0][2]와 같이

출력 시에 반복문 사용. 2 0 1 1을 예로 들면
격자판에서 x-1 y-1에서 if(d == 0): 같은 행에서 +1
반복 횟수는 2번
'''
## 격자판 만들기
h, w = map(int, input().split())
grid = [[0 for col in range(w)] for row in range(h)]
## 막대 리스트
stick = []
n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    stick.append([l, d, x-1, y-1]) # 좌표와 리스트 내의 값이 다름

# 격자판 막대 놓기
for i in range(n): # 막대의 개수
    for j in range(stick[i][0]): # 해당 막대의 길이
        if stick[i][1] == 0: # 가로
            grid[stick[i][2]][stick[i][3]] = 1
            stick[i][3] += 1 # 열 방향으로 +1
        elif stick[i][1] == 1: # 세로
            grid[stick[i][2]][stick[i][3]] = 1
            stick[i][2] += 1 # 행 방향으로 +1

## 출력
# 격자판 출력
for i in range(h):
    for j in range(w):
        print(grid[i][j], end = ' ')
    print()

