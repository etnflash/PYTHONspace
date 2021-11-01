#정수를 입력받아 정수 만큼 반복하면서 키, 자료 쌍을 공백을 사이에 두고 입력 받아 딕셔너리에 추가한다.
#마지막으로 문자열을 하나 더 입력 받아, 그 문자열을 키 값으로 하는 자료를 출력하는 프로그램을 작성하시오
#동일한 키값이 두번 입력 되는 경우는 없다고 가정한다.
# 입력 예
# 6
# Adagio 60
# Andante 80
# Moderato 100
# Allegro 120
# Vivace 160
# Presto 180
# Allegro

#출력 예 :  120

n = int(input("any integer? "))

dict1 = dict()

for i in range(n):
    key, value = input(f"{i+1}. write key and value seperated by space(key value) : ").split()
    dict1[key] = value

munjaKey = input("write 'key' : ")

print(dict1[munjaKey])