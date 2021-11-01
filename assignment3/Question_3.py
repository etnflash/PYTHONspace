def switch(num):
    return{
        1:'개',
        2:'고양이',
        3:'병아리',
    }.get(num, "I don't know")

def translate(animal):
    return{
        '개':'dog',
        '고양이':'cat',
        '병아리':'chick'
    }.get(animal, "i don't know")

num = int(input("number? "))

print(translate(switch(num)))