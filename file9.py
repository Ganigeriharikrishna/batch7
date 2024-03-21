s1= "Hello how are you"
s2="Hello how is"
s1=s1.split(" ")
s2=s2.split(" ")
for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)

        
#unparametarised constructor
class profile:
    def __init__ (self):
        print("hello world")
obj =profile()
obj.__init__()

# find the 8th fibanochi number
num=8
n1=0
n2=1

for val in range(num):
    ans=n1+n2
    n1=n2
    n2=ans
print(ans)

    
