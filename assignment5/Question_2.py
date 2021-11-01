# 2 부터 9까지의 수 입력 받아 입력받은 수 사이의 구구단을 출력
# 단 반드시 먼저 입력 된 수의 구구단 부터 형식에 맞게 출력
# 구구단 사이의 공백은 3칸

num_1 = int(input("first number: "))
num_2 = int(input("second number: "))

if num_1 > num_2:
    for j in range (1,10):
        for i in range (num_1, num_2-1, -1):
            print(f"{i} * {j} = {i*j:2d}   ",end="")
        print()
else:
    for j in range (1,10):
        for i in range (num_1, num_2+1):
            print(f"{i} * {j} = {i*j:2d}   ",end="")
        print()