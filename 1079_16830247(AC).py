'''
문자열을 입력받음 - 공백을 기준으로 문자열 리스트로 
반복문으로 리스트 요소들을 줄바꿔서 출력
if문으로 q가 나올 때 q까지 출력하고 반복이 끝나도록
'''
stringList = input().split()
for c in stringList:
    if c == 'q':
        print(c)
        break
    print(c)
