#주차장에 세워진 자동차의 차종을 모두 입력받아, 중복되어 입력된 이름을 제거한 후, 알파벳 순서대로 출력하고,
#그 개수를 출력하는 프로그램을 작성하시오.

#입력 예 : Grandeur Avante Sonata Sonata Avante Genesis Sonata
#출력 예 : Avante Genesis Grandeur Sonata
#          4

cars = input("which cars? (seperated by space) : ").split()
species = set(cars)
speciesSorted = sorted(list(species))    #speciesSorted = list(species).sort() #는 왜 오류가 날까

for car in speciesSorted:
    print(car, end = " ")

print()

print(len(speciesSorted))