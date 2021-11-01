#100이하의 정수를 입력받아 입력받은 정수부터 100까지의 합을 출력

num = int(input("integer(1 to 100)? "))
sum = 0

for i in range (num, 101):
    sum += i

print(sum)