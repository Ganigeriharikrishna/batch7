

# ! method riding
# * polymorphism in classes

# class bank:
#     def ratio(self):
#         print("all banks has repo rate")
        
# class SBI(bank):
#     def ratio(self):
#         print("SBI rate is 9%")
        
# class IOB(bank):
#     def ratio(self):
#         print("IOB rate is 7.5%")

# i=IOB()
# i.ratio()

# s=SBI()
# s.ratio()

# ? eg :2
# class USA:
#     def language(self):
#         print("english")
    
#     def capital(self):
#         print("Washington")
        
# class INDIA(USA):
#     def language(self):
#         print("NONE")
    
#     def capital(self):
#         print("NEW DELHI")
        
# I = USA()
# I.language()
# I.capital()

# EG:3
# POLYmorphism using objects

# c1, c2 ----> c1 = print(c1), print(c2)
# f1, f2
# class c1:
#     def multi1(self):
#         print("class1")
        
# class c2(c1):
#     def multi2(self):
#         super.multi1()       
#         print("class2")

# obj1 =c2()
# obj2 =c1()

# eg 4:
# def display(a):
#     a.multi1()
    
# display(obj1)
# display(obj2)


# obj2 =c1()
# obj2.multi2()

# changw the functionality of built in functions
# eg 5
# a = 9
# b = 6
# print(a. __add__(b)) #? duner method or marfic method
# print(a. __sub__(b))

# eg 6
# class shoping:
#     def __item__(self, l1):
#         self.items = len(l1)
        
#     def __len__(self):
#         length = len(self.items)
#         return length
        
# s =  shoping([1,2,3,4,5])
# print(len(s))

# ! ---> method overloading
# class suming:
#     def add(self, a, b):
#         print(a+b)
        
#     def add(self, a, b, c):
#         print(a+b+c)
    
    
# s = suming()
# s.add(4,5)
# s.add(4,5,1)

# eg:2
# class suming:
#     def add(self, a=None, b=None, c=None):
#         if a!=None and b!=None and c!=None:
#             print(a+b+c)
#         elif a!=None and b!=None:
#             print(a+b)
#         else:
#             print(a)
            
# obj=suming()
# obj.add(2)
# obj.add(3, 4)
# obj.add(1,20,3)

# ! ------> abstraction
