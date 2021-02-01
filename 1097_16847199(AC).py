## 입력 1: 바둑판
baduk = [] # 바둑판 리스트
for i in range(19): # 입력받은 바둑판
    line = input().split()
    baduk.append(line)
'''
for i in range(19):
    for j in range(19):
        print(baduk[i][j], end = ' ')
    print()
'''
## 입력 2: 횟수
n = int(input()) # 뒤집기 횟수 
## 입력 3: 좌표 
xy = []
for i in range(n): # n 개의 좌표
    x, y = input().split()
    xy.append([int(x)-1, int(y)-1])
    # xy = [[10, 10], [12, 12]...]

## 뒤집기(각 행과 열에서 각각 뒤집어야 함.)
for i in range(n): # i는 좌표 개수
    for j in range(19): # j는 바둑판 반복 횟수
        # 행
        if baduk[xy[i][0]][j] == '1':
            baduk[xy[i][0]][j] = '0'
        elif baduk[xy[i][0]][j] == '0':
            baduk[xy[i][0]][j] = '1'
        # 열
        if baduk[j][xy[i][1]] == '1':
            baduk[j][xy[i][1]] = '0'
        elif baduk[j][xy[i][1]] == '0':
            baduk[j][xy[i][1]] = '1'

## 바둑판 출력
for i in range(19):
    for j in range(19):
        print(baduk[i][j], end = ' ')
    print()    
        
        


