#type-1 without argument and with out return.
#1 WAP using type 1 function to find average of 5 integer numbers.
'''
def avg():
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    e=int(input())
    ave=(a+b+c+d+e)/5
    print(ave)
avg()    
'''
'''
def fun():
    s=0
    for i in range(1,6):
        n = int(input())
        s=s+n
    print("average :- ",s/5)
fun()        
'''
#2 Find simple interest of given data using type 1 function.
'''
def simple_interest():
    p=int(input("enter principal amount "))
    t=int(input("enter time duration "))
    r=float(input("enter rate of interest "))
    s= (p*t*r)/100
    print(s)
simple_interest()    
'''
#type-2 without argument and with return.
'''
def python():
    subject=input("Which subject are you studying")
    return subject
print(python())
'''
#1
'''
def fun():
    s=0
    for i in range(1,6):
        n = int(input())
        s=s+n
    return "average :- ",s/5
print(fun())
'''
'''
def hey():
    return 'how are you'
    print("hiii")
print(hey())
'''
#type-3 with argument and with out return.
'''
def python(a):
    print(a)
python('hello ')
'''
'''
def python(a,b):
    print(a,b)
python(input("which language do you want choose "),input("at what time"))    
'''
#type-4 with argument and with return.
'''
def fun(a,b,c,d,e):
    return f'average of {a},{b},{c},{d},{e} is {(a+b+c+d+e)/5}'
print(fun(int(input('enter 1st number')),int(input('enter 2nd number')),int(input('enter 3rd number')),int(input('enter 4th number')),int(input('enter 5th number'))))
'''    
