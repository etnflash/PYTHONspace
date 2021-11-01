# n 입력받아 10미만의 홀수를 nxn크기로 공백으로 구분하여 출력
# n = 3
# 1 3 5
# 7 9 1
# 3 5 7

n = int(input("natural number? "))

for i in range (1, n*n+1):
    print((2 * i - 1) % 10, end=" ")
    if i % n == 0:
        print()

