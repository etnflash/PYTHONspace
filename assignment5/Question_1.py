# 자연수 n 을 입력 받고 1부터 홀수를  차례대로 더해가면서 합이 n이상이면
# 그때까지 더해진 홀수의 개수와 그 합을  출력하는 프로그램을 작성하시오.


cnt = 0
sum = 0
n = int(input("natural number? "))

#나중에 딴걸로도 해보자!
#뒤에는 임의의 큰 수 넣었는데 다른 범위 구하는 내장함수 알아보기..
for i in range(1, n+1):
    if sum < n:
        if i % 2 == 1:
            sum += i
            cnt += 1

print(cnt, sum)