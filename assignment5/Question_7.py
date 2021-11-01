# 자연수 n을 입력 받아 "출력 예"와 같이 공백으로 구분하여 출력
#     1
#   1 2
# 1 2 3

n = int(input("any natural number? "))

for i in range(n):
    for j in range(i+1,n):
        print(" ", end = " ")
    for k in range(i+1):
        print(k+1, end = " ")
    print()