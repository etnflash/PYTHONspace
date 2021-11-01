#0이 입력될 때 까지 정수를 계속 입력받아 3의 배수와 5의 배수를 제외한 수들의 개수를 출력

cnt = 0
while True:
    num = int(input("any integer? "))
    if num == 0:
        break
    elif num % 3 == 0 or num % 5 == 0:
        continue
    else:
        cnt += 1
    
print(cnt)