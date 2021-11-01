#자연수 n을 입력 받아 "출력 예"와 같이 공백으로 구분하여 출력
# 1 2 3
#   4 5
#     6

n = int(input("natural number? "))

d = 1
for i in range(n):
    for j in range(0, i):
        print(" ",end = " ")
    for k in range(i,n):
        print(d, end =" ")
        d += 1
    print()