#인터넷 게임 계정의 수를 입력 받은 후, 각 계정의 아이디, 승률, 계급을 입력 받아, 계급이' Bronze'가 아니면서
#승률이 60.0 이상이거나, 계급이 'platinum'인 아이디를 입력 받은 순서대로 출력 예와 같은 형식으로
#"[Gosu]"를 붙여 출력하는 프로그램을 작성
# 입력 예
# 5
# hec419 62.4 Platinum
# comkiwer 52.3 Platinum
# eva 60.7 Silver
# ohjtgood 49.7 Gold
# teriusu 65.1 Bronze

# 출력 예
#[Gosu] hec419
#[Gosu] comkiwer
#[Gosu] eva

number_of_id = int(input("the number of id : "))

ids = list()
for idRateClass in range(number_of_id):
    ids.append(input("write id rate class : "))

gosus = [id for id in ids if id.split()[2] != 'Bronze' and float(id.split()[1])>=60 
                            or id.split()[2] == 'Platinum' ]
# print(gosus)
for gs in['[Gosu] ' + gosu.split()[0] for gosu in gosus]:
    print(gs)

