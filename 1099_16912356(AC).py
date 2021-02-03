## 미로 입력 받기
maze = []
for i in range(10):
    row = map(int, input().split())
    row = list(row)
    maze.append(row)

## (2, 2)에서 개미 출발 / 개미 위치
# 개미 위치 리스트 만들기
row, column = 1, 1

## 이동하거나 머무르기
while(True):
    # 현재 위치 확인하는 조건문
    if maze[row][column] == 0 or maze[row][column] == 9:
        maze[row][column] = 9
    else: # 현재 위치가 0 또는 9가 아닌 경우(2인 경우)
        maze[row][column] = 9
        break
    # 다음 위치 확인하는 조건문
    if maze[row][column+1] == 0: # 오른쪽으로 이동 가능할 때
        column += 1 # 개미가 오른쪽으로 이동
        maze[row][column] = 9
    elif maze[row][column+1] == 1: # 오른쪽으로 이동 불가능할 때
        if maze[row+1][column] == 2: # 아래에 먹이
            row += 1
            maze[row][column] = 9
            break
        elif maze[row+1][column] == 1: # 아래로도 이동 불가능할 때
            break
        else:
            row += 1 # 개미가 아래로 이동
            maze[row][column] = 9
    elif maze[row][column+1] == 2: # 오른쪽에 먹이
        column += 1 # 개미가 오른쪽으로 이동
        maze[row][column] = 9
        break
## 미로 출력
for i in range(10):
    for j in range(10):
        print(maze[i][j], end= ' ')
    print()

