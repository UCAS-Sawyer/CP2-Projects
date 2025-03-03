#Sawyer Wood Advances Functions Notes

def is_int(user_input):
    try:
        int(user_input)
    except:
        print("BAD PERSON BE BETTER.")
        user_input = is_int(input("What is your age and your social security number?\n"))
    return user_input

def age():
    old = is_int(input("What is your age and your social security number?\n"))

    print(f"Cool. You are {old} and you social security number ends with {old}.")
#age()

def add(a):
    b = int(input("GIVE NUMBER NOW\n"))

    def addition():
        print(a+b)
    addition()

#add(3)

import logging
logging.basicConfig(level = logging.INFO)

def logger(func):

    def wrapper(*args, **kwargs):
        logging.info(f"EXECUTING {func.__name__} with {args}, {kwargs}")
        return func(*args, *kwargs)
    return wrapper

#@logger
def adder(a, b):
    return a + b
#print(adder(3,4))


def add(a):
    def addition(b):
        return a+b
    return addition

base = add(10)

#print(base(5))

#EX:
def math(income):
    
    def perc(amount, type):
        percent = amount / income
        print(f"Your {type} is ${amount}, and that is {percent} of your income.")
    
    return perc

    
def user_inputs(type):
    return  int(input(f"What is your monthly {type}\n$"))

income = user_inputs("income")
rent = user_inputs("rent")
utilities = user_inputs("utilities")
groceries = user_inputs("groceries")
transportation = user_inputs("transportation")

start = math()