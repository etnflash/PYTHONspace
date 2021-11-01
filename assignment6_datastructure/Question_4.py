#매 년 피아노 콩쿠르 최우수상을 받은 학새을의 이름과 정수 하나를 입력 받아, 입력받은 정수 만큼
#최우수상을 받은 학생들은 모두 출력하는 프로그램을 작성하시오. (먼저 입력된 이름을 우선하여 출력)
# 입력 예 : Cindy Katherine Mark Mark Cindy Jack Cindy Maria Katherine      ,     2
# 출력 예 : Katherine Mark

list_of_winner = [x for x in input("write names seperated by space : ").split()]
count_of_win = int(input("how many times, awarded? : "))
countwin = dict()
for winner in list_of_winner:
    if winner in countwin:
        countwin[winner] += 1
    elif winner not in countwin:
        countwin[winner] = 1


# print(countwin.keys() if countwin.values() == 2 else '')   #엥
# print(1 if countwin.values() == 2 else 2)   #엥
for key in countwin:
    if countwin[key] == 2:
        print(key)
