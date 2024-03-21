
# ! Eg:3

def profile(name, age, place):
    txt = "My name is {}. Iam {} years old. Iam from {}."
    print(name, age, place)
profile("sid", 29, "cbe")


# ! Eg:4
# ? function with return statement

def f1():
    z = 8
f1()
print(z) # error --> cannot use outside the funtion



def f1(a, b):
    c = a*b
    return c
# print(f1(6, 8))
obj = f1(6, 8)
obj1 = f1(4, 6)

def gracemark(object):
    print(object+4)
gracemark(obj-24)
gracemark(obj1)


#123
# ? problem:1

def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n, "palindrome")
    else:
        print("Not polindrome")
a = int(input("Enter the value: "))
palindrome(a)



# ? Based on the declaration of parameter and args
# ? functions are divided into 5 catagories

# Positional args
# keyword args
# default args
# variable length args
# keyword variable length args
# Positional args

# * positional args
# Eg:1

def profile(name, phone, mark):
    txt = "My name is {}. My phone number is {}. I got {} marks."
    print(txt.format(name, phone, mark))

profile(9376857648, "sidhu", 97) # unexpected output



# * Keyword args
# ! Eg:1
# ? To overcome the disadvantage of position args, we use keyword args
# ? it is process of initiating the parameter with args while calling the
# funtions

def profile(name, phone, mark):
    txt = "My name is {}. My phone number is {}. I got {} marks."
    print(txt.format(name, phone, mark))

profile(name="somu", mark=85, phone=9478387654)



# todo --> Exception of keyword args function

def profile(name, phone, mark):
    txt = "My name is {}. My phone number is {}. I got {} marks."
    print(txt.format(name, phone, mark))

profile(name="somu", mark=85, phone=1234556678)



# * Default args
# ! Eg:1
def profile(name, phone, place="kadapa"):
    txt = "My name is {}. My phone number is {}. I am from {}."
    print(txt.format(name, phone, place))

profile("somu", 8767676767)


# ! Eg:2
def profile(name, phone, place="kadapa"):
    txt = "My name is {}. My phone number is {}. I am from {}."
    print(txt.format(name, phone, place))

profile("somu", 8767676767, "Guntur")




# ! Eg:1
#To pass more then 1 arg to a paremeter means we use variable length args
# To convert normal paremeter to variable length param, add to ther prefix of param

#name="Usman", " Charan ", " NAresh "
#print(name)


def profile(*name):
    for val in
    name:
        print(" My name is",val)
profile("USman", 'Ussu', 'Alone')


# Eg:2

def profile(name,age):
    for val in name:
        print("My name is", val,"My age is",age)
print("My name is", val,"My age is",age)("kalyan",'name2','name3',28) # error ---> age has no args


def profile(name,age):
    for val in name:
        print("My name is", val,"My age is",age)
profile(28,"kalyan")


#! Eg:6
# constructors  -->__init__()
# This is a special method which has the ability to execute to itself without
# calling it manullay through the process of instantiation

class profile:
    def __init__(self): # constructor method
        print("hey")
p = profile() # throught this process
p.__init__()







