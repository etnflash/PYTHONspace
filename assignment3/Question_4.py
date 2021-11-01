# 평년인 경우의 일수 구하기 : 1~12사이의 정수 입력
month = int(input("which month? "))

days_31 = [1,3,5,7,8,10,12]
days_30 = [4,6,9,11]
days_28 = [2]

if month in days_31:
    print(31)
elif month in days_30:
    print(30)
elif month in days_28:
    print(28)
else:
    print("error")