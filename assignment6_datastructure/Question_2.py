#세 리스트를 입력받은 후, 모두 셋으로 형변환한 후, 세 집합의 교집합과 합집합을 구하여 출력하는 프로그램을
#작성하시오
# 1 2 3 4 5 1 2 3 4 5
# 1 5 2 5 5 4
# 10 8 6 2 4

# Intersection : {2, 4}
# Union : {1, 2, 3, 4, 5, 6, 8, 10}

list1 = [int(num) for num in input("write numbers for list1 seperated by space : ").split()]
list2 = [int(num) for num in input("write numbers for list2 seperated by space : ").split()]
list3 = [int(num) for num in input("write numbers for list3 seperated by space : ").split()]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

print("Intersection :", set1&set2&set3)
print("Union :", set1|set2|set3)
