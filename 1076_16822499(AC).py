# 문자를 순서대로 출력 아스키 코드로 변환해서? 
# 해당 문자가 아스키 코드에서 몇 번째인지를 통해 len 구하기
# 반복문에서 n - len 부터 1씩 더해가며 입력 문자까지 나오도록.
# print() end=''로 줄바꿈 되지 않도록.
# 97~122

c = ord(input())
len = c - 96 # len은 반복 횟수
for i in range(len): # 0부터... 
    n = 97 + i
    print(chr(n), end=' ')
    
    
