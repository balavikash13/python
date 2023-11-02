#def function for all arithmetic operations.

def add():
    a=10
    b=5
    c=a+b
    print('Calling adding func first time of a and b is ',c)
def sub2(a,b):
    c=a-b
    print('calling function with parameter for second time',c)
def mul3():
    a=int(input('Value of a :'))
    b=int(input('Value of b :'))
    c=a*b
    return(c)
def div4(a,b):
    a=int(input('Value of a :'))
    b=int(input('Value of b :'))
    c=a/b
    return(c)
#no parameters and no returns.
add()
#parameters and no returns
sub2(15,5)
#No parameters and returns
a3 = mul3()
print('calling function with return for third time',a3)
#parameters and returns
a4 = div4(15,15)
print('calling function with parameter and return for fourth time ',a4)
