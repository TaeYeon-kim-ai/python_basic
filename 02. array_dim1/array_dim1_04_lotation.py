'''
n개의 숫자가 입력되면,

n개의 숫자를 왼쪽으로 하나씩 돌려서 출력하시오.

예) 1 2 3 4 5가 입력된 경우,

1 2 3 4 5

2 3 4 5 1

3 4 5 1 2

4 5 1 2 3

5 1 2 3 4

입력
첫째 줄에 숫자의 개수 n이 입력된다.( 1 <= n <= 1,000)

둘째 줄에 n개의 정수 k가 공백으로 구분되어 입력된다.(1 <= k <= 1,000)

출력
숫자를 로테이션한 결과를 출력한다.(단, 왼쪽으로만 돌린다.)

입력 예시   
5
1 2 3 4 5 

출력 예시
1 2 3 4 5 
2 3 4 5 1 
3 4 5 1 2 
4 5 1 2 3 
5 1 2 3 4 
'''


n = int(input())
k = list(map(int,input().split()))

for i in range(n) : #i를 n만큼 반복함
    for j in range(n) : #j를 n만큼 반복함 n 만큼 반복된 i n 이 들어감
        print("num : ", k[j], end=' ') # j부터 출력
    print()
    for z in range(n-1) : # 4번
        temp = k[z]
        print("temp : ", temp)
        k[z] = k[z+1]
        print("k[z] ", k[z])
        k[z+1] = temp
        print("k[z+1]", k[z+1])










