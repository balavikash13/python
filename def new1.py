#def function for circle, triangle, square and rectangle

def squ():
    a=int(input('value of a :'))
    c= a**2
    print('Area of square :',c)
def rec(l,w):
    l=int(input('value of l :'))
    w=int(input('value of w :'))
    r = l*w
    print('area of rectangle ',r)

def cir():
    r=int(input('value of r :'))
    ci=3.14*(r**2)
    return(ci)
def tri(b,h):
    b= int(input('value of b:'))
    h=int (input('value of h:'))
    t =0.5*(b*h)
    return(t)

squ()
rec(10,5)
cr3 = cir()
print('area of circle :',cr3)
t4 =tri(7,5)
print('area of triangle :' ,t4)
