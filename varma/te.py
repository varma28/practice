'''
while 1:
    print('varma')
    for i in range(1):
        print('varma')
        break
    break
if False:#True:
    print('varma')
elif True:
    print('varma1')
else:
    print('varma')
def func1():
    print('varma2')
func1()
l1 = 123
l2 = 123.34
l3 = True #False
l4 = bytearray(2)
l4[0] = l4[1] = l4[2] = 12
print(l4)
x = memoryview(bytes(5))
str1 = 'varma123'
str2 = str1[::-1]
print(l4)

x = bytearray('ABCDEFGH2','utf-8')
print(x[0]+1,x[1],x[2])
l1 = str(x[0])
print(l1)
x = 'varma{}'
y = x.upper()
print(x.format(23),y.format('23'))

x = 'varma'
y = x.encode(encoding = "ascii",errors = 'strict')
print(y,x)

x = [1,2,3,34,5,6]
print(x[0])
def binary_and(a: int, b: int) -> str:
    
    if a < 0 or b < 0:
        raise ValueError("the value of both inputs must be positive")

    a_binary = str(bin(a))[2:]  # remove the leading "0b"
    b_binary = str(bin(b))[2:]  # remove the leading "0b"

    max_len = max(len(a_binary), len(b_binary))

    return "0b" + "".join(
        str(int(char_a == "1" and char_b == "1"))
        for char_a, char_b in zip(a_binary.zfill(max_len), b_binary.zfill(max_len))
    )

print(binary_and(5,6))


dict1 = {'1':'2','3':'4'}
print(dict1.items())

for keys,values in dict1.items():
    print(keys,values)
thislist = ["apple", "banana", "cherry"]
thislist.pop(0)
del thislist[0]
thislist.clear()
print(thislist)
a = 2
b = 1
print("values of a and b",a,b)
print("logical or operation",a|b)
print("logical and operation",a&b)
print("logical exor operation",a^b)
print("logical not operation",~a)
print("logical left shift operation",1<<a)
print("logical right operation",a>>1)

thislst = [1,2,3]
del(thislst)
#print(thislst)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
n = x.symmetric_difference(y)
print(n)

dict1 = {1:2,3:4,5:6}

for x,y in dict1.items():
    print(x,y)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict =thisdict
print(mydict)

mydict = {'varma':{
1:'Rupa sesha varma',
     2:'Brahma Raju'
                },
            
            }
i = 0
while i<6:
    i += 1
    print(i)
    if i == 3:
        break
else:
    print("varma")

def fun1(var,*list1):
    print(var)
    for i in list1:
        print(i)
fun1(var = 1,'varma','Rupa',"sesha",1,2,3,4,5)
# Python program to illustrate
# *kwargs for variable number of keyword arguments

def myFun(**kwargs):
	for key, value in kwargs.items():
		print ("%s == %s" %(key, value))

# Driver code
myFun(first ='Geeks', mid ='for', last='Geeks')	

def fun1(**args):
    for i in args:
        print(args[i])

fun1(ass = 'donkey',mass = 'nagarjuna')
varma = 'test'
print("The unknown %s is a very easy " % varma)
#print("The price of %dkgs aloo is %dRs what is your respose on this %s"%1%24%'Fu**')
print(f"The most hilarious ay to to the math {2+3}")

a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
print(a+b)
for i in range(2):
    numof_lists = int(input())

in1 = [1,2,3,4,5,6,7,8]
l1 = iter(in1)
print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))'''


class b1:
    def __init__(self,num):
        self.num = num
        print(self.num)
    def path(self):
        print(self.num)
    def __add__(self,other):
        print(self.num+other.num)

n1 = b1(1)
n2 = b1(1)
n1+n2











