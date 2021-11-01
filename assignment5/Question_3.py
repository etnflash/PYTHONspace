#행과 열의 수를 입력 받아 다음과 같이 출력하는 프로그램을 작성하시오.
# 입력 예
# 3 4
# 출력 예
# 1 2 3 4 
# 2 4 6 8
# 3 6 9 12 

row = int(input("row? "))
column = int(input("column? "))

for i in range (row):
    for j in range (column):
        print((i+1)*(j+1), "", end="")
    print()