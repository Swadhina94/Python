#1. Find largest of 3 number
'''
a=int(input('Enter your number1 :'))
b=int(input('Enter your number2 :'))
c=int(input('Enter your number3 :'))
if a>b:
    if a>c:
        print(a)
    elif a==c:
        print(a,c)
    else:
        print(c)
elif a==b:
    if a>c:
        print(a,b)
    elif a==c:
        print(a,b,c)
    else:
        print(c)
else:
    if b>c:
        print(b)
    elif b==c:
        print(b,c)
    else:
        print(c)
'''        
#1. Find largest of 4 number
'''
a=int(input('Enter your number1 :'))
b=int(input('Enter your number2 :'))
c=int(input('Enter your number3 :'))
d=int(input('Enter your number4 :'))
if a>=b:
    if a>=c:
        if a>=d:
            print(a)
        else:
            print(d)
    else:
        if c >=d:
            print(c)
        else:
            print(d)
     
else :
    if b>=c:
        if b>=d:
            print(b)
        else:
            print(d)
    else:
        if c >= d:
            print(c)
        else:
            print(d)
'''
# Wap to print the middle value of list only if it is string
my_list = eval(input("Enter a list: "))

middle = my_list[len(my_list) // 2]

if len(my_list) % 2 != 0:
    if type(middle) == str:
        print("Middle value:", middle)
    else:
        print("Middle value is not a string")
else:
    print("No single middle value")
    

    
        
            










        
