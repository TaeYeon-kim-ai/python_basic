#find() 왼족부터 찾아서 처음 등장하는 위치를 찾음
#rfind() 오른쪽부터 찾아서 처음 등장하는 위치를 찾음

a = "안안녕하세요".find("안녕")
print(a)
#1
b = "안녕안녕하세여".rfind("안녕")
print(b)
#2

#문자열 내부에 없으면 -1을 출력 