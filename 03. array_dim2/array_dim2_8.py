'''
?에 들어갈 숫자가 무엇인지 알면 IQ 150이라는 문제이다.

원리는 조금만 생각해보면 쉽게 알 수 있다. 따라서 우리는 충분히 IQ 150이라는...

이 상황을 좀 더 일반화하여 각 행의 제일 첫 번째 숫자들만 주어지면 N크기의 모든 격자판 정보를 출력하는 프로그램을 작성하시오.

입력
첫 줄에 이 삼각격자의 세로 길이 N이 입력된다.(2 <= N <= 20)

둘째 줄부터 N+1째 줄까지 (k, 1)의 격자판의 정보가 입력된다. ( 1 <= k <= N)

출력
N크기의 삼각 격자판을  출력하시오.

(출력할 때 각 행의 마지막에 공백을 넣어 출력하세요.(표현 오류때문))

입력 예시   
4
4
6
9
19

출력 예시
4 
6 2 
9 3 1 
19 10 7 6 
'''

n = int(input())

m = []


for i in range(1, n+1) :
    temp = [0] * i
    m.append(temp)

for i in range(0, n) :
    k = int(input())
    m[i][0] = k
    for j in range(1, len(m[i])) : 
        m[i][j] = m[i][j-1] - m[i-1][j-1] # 사각형 기준 우측 아래 것은 좌측 위에것 - 좌측아래것
        
for i in range(0, n) : 
    for j in range(0, len(m[i])) :
        print(m[i][j], end=' ') 
    print()




