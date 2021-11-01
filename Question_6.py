#100미만 정수 입력 후 배수 차례대로 출력하다가 10의 배수출력되면 종료

num = int(input("less than 100? "))

# for i in range (1, 100):
#     print(num * i, end=" ")
#     if num * i % 10 == 0:
#         break

for i in range (1,100):
    baesu = [num * i for i in range(1, 100) if num * i < 100] 
    for j in baesu:
        print(j, end = " ")
        if j % 10 == 0:
            break
    break

        