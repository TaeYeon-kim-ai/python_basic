'''
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

제한사항
전체 학생의 수는 2명 이상 30명 이하입니다.
체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
입출력 예
n	lost	reserve	return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	4
3	[3]	[1]	2
입출력 예 설명
예제 #1
1번 학생이 2번 학생에게 체육복을 빌려주고, 3번 학생이나 5번 학생이 4번 학생에게 체육복을 빌려주면 학생 5명이 체육수업을 들을 수 있습니다.

예제 #2
3번 학생이 2번 학생이나 4번 학생에게 체육복을 빌려주면 학생 4명이 체육수업을 들을 수 있습니다.
'''
# 번호 체격순
# 앞번호 학생 / 뒷번호 학생 체육복
# 4번 학생 - 3번 or 5번
# 최대한 많은 학생이 수업참여
# 전체학생수 n
# 도난당한 학생번호 배열 lost
# 여벌 체육복 학생 번호 : reserve
# 체육수업 들을 수 있는 학생 최대값 return
# solution함수 작성

# 체육복이 있는지 판단
# 
def solution(n, lost, reserve):
    answer = 0
    n = n >= 2, n <= 30    
    arr = [0]*n #arr은 순서대로임

    #lost 도난당한 학생
    for i in range(len(lost)) :  #도난당한 학생은 빌려줄수 없음 
        arr[lost[i] -1] -= 1     #가진 체육복에서 -

    #여별 체육복이 있는 학생 수
    for i in range(len(reserve)) : 
        arr[reserve[i]-1] += 1 #여벌 체육복이 있는 학생은 +1처리

    for i in range(len(arr)) :
        if i == 0 :
            # 0번째 학생 체육복 없음, 1번째 학생 여벌 체육복 있는 경우
            if arr[i] == -1 and arr[i+1] == 1:
                arr[i] += 1
                arr[i+1] -= 1

        elif i == len(arr) -1 :
            #마지막 학생이 체육복 없음, 그 앞 학생이 여벌의 체육복 있음
            if arr[i] == -1 and arr[i-1] == 1 :
                arr[i] += 1
                arr[i-1] -= 1

        else : 
            #양쪽에 학생이 체육복이 있음 나이스
            if arr[i] == -1 : 
                if arr[i-1] == 1 : #앞의 학생이 빌려주는 경우
                    arr[i] += 1
                    arr [i-1] -= 1
                    continue
                if arr [i+1] == 1 : # 뒤에 있는학생것 유지 or 빌려줌
                    arr[i] += 1
                    arr[i+1] -= 1

    print('arr : ', arr)
    return arr.count(0) + arr.count(1)
    return answer

#고득점자 풀이
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)