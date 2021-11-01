#정수를 입력받아 입력받은 정수만큼 반복하면서, 각 줄에 나라의 이름과 그 나라의 수도를 공백을 사이에 두고
#입력 받는다. 그 후에, 나라의 이름을 입력바아 그 나라의 수도를 출력하는 프로그램을 작성하라.
#만약 나라가 입력된 적이 없으면, Unknown Country을 출력한다.
# 입력 예
# 5
# Korea Seoul
# Russia Moscow
# USA Washington_D.C
# Britain London
# Germany Berlin
# USA

# 출력 예
# Washington_D.C


# num_of_country = int(input("how many? "))
# list_of_country = list()
# for i in range(num_of_country):
#     list_of_country.append(input("write ; country capital : ").split())

# print(list_of_country.index(input("write the name of country : "))) #리스트로 했을 때 해결법 찾아보자..

num_of_country = int(input("how many? "))
list_of_country = dict()
for i in range(num_of_country):
    country, capital = input(f"{i+1}. write ; country capital : ").split()
    list_of_country[country] = capital

# print(list_of_country[input("write the name of country : ")])

print(list_of_country.get(input("write the name of country : "),'Unknown Country'))
