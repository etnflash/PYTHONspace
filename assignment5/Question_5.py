#자연수 n을 입력받아서 다음과 같이 출력하는 프로그램을 작성
# *****
#  ***
#   *

n = int(input("natural number? "))

for i in range(n):
    for j in range(i):
        print(" ", end = "")
    print('*'*((n-i)*2-1),end="")
    print()