#100이하의 양의 정수만 입력
#while문 이용하여 1부터 입력 받은 정수 까지의 합 구하여 출력

num = int(input("integer(1 to 100)? "))
sum = 0

for i in range (1, num+1):
    sum += i

print(sum)