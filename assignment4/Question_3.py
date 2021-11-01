#natural number 입력받아 그 수의 배수를 차례대로 10개 출력

natural_num = int(input("natural number? "))

for i in range (10):
    print(natural_num * (i+1), "",end="")