gender = input("gender(M or F)? ")
age = int(input("age? "))

if gender == "M":
    if age >= 18:
        print("Man")
    elif age > 0 & age < 18:
        print("Boy")
elif gender == "F":
    if age >= 18:
        print("Woman")
    elif age > 0 & age < 18:
        print("Girl")