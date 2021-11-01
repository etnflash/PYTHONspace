#자연수 n을 입력받아서 n줄만큼 다음과 같이 출력하는 프로그램을 작성
# *
# **
# ***
# ****
# *****

n = int(input("natural number? "))

for i in range(1,n+1):
    print("*"*i)