#윤년 판단
year = int(input("year? "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("leap year")
else:
    print("common year")