#Sawyer wood, multiple python pages notes

#Alising is where you import a function and give it a new function

from calc import addition as add, subtraction as sub, numb as num
print(num)
print(add())
print(sub())

#Its better to return a variable from a function

def get_user_info():
    name = input("WHATISYONAMEBOZO? ")
    age = input("WHATISYOAGEBOZO? ")

    return name, age

names, ages = get_user_info()
print(ages)