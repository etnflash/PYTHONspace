#삼각형 밑변의 길이와 높이 입력 받아 넓이 출력 후
#continue 에서 하나의 문자 입력 받아 'Y' 나 'y' 아닌 경우 종료
#넓이는 반올림하여 소수 첫째자리 까지

while True:
    base = float(input("base? "))
    height = float(input("height? "))
    triangle_width = base * height / 2
    print(round(triangle_width*10)/10)
    conti = input("continue? ")
    if conti == "Y" or conti == "y":
        continue
    else:
        break
