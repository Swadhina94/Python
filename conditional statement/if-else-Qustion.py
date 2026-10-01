# Check given number is even or odd
'''
num=int(input("Enter a number "))
if num%2 == 0:
    print("Even")
else:
    print('Odd')
'''
# Check given character is special symbel or not in python
'''
char = input('Enter a cheracter ')
if not ('A' <= char <= 'A' or 'a'<=char<='z' or '0'<=char<= '9') :
    print('special symbel')
else :
    print('Not a special symbel')
    '''
# Check given string is palindrome or not
'''
a=input('Enter a string ')
if a == a[::-1] :
    print('palindrome')
else:
    print("not palindrome")
'''
#11.Wap to check whether the data is mutable or not.
'''
data= eval(input("Enter a data "))
s= type(data)
if s in (list,set,dict):
    print('the data is mutable')
else:
    print("the data is not mutable")
'''
#12.Wap to check whether the given character is digit or not.
'''
char = input('Enter a cheracter ')
if '0'<= char <= '9':
    print("the given character is digit ")
else:
    print("the given character is not a digit ")
'''    
#13.Wap to check whether the given character is special or not.
'''
char = input('Enter a cheracter ')
if not ('A' <= char <= 'A' or 'a'<=char<='z' or '0'<=char<= '9') :
    print('special symbel')
else :
    print('Not a special symbel')
'''
#14.Wap to check whether a list consists of middle value or not.
data = eval(input('Enter lisi value : '))
if len(data)% 2 == 0:
    print("list not consists of middle value")
else:
    print("list consists of middle value")

#15.Wap to check whether the number is even or odd.
'''
num=int(input("Enter a number "))
if num%2 == 0:
    print("Even")
else:
    print('Odd')
'''
#16.Wap to check whether the given data is mutable or immutable.
'''
data= eval(input("Enter a data "))
s= type(data)
if s in (list,set,dict):
    print('the data is mutable')
else:
    print("the data is immutable")
'''
#17.Wap to check whether 2 values are pointing to the same memory or not.
'''
a = eval(input("Enter 1st value"))
b= eval(input("Enter 2nd value"))
if a is b :
    print('2 values are pointing to the same memory')
else:
    print("2 values are pointing to the not same memory")
'''    
#18.Consider a tuple of length 2 and check whether the tuple is homogenous or not.
'''
data=eval(input("Enter 2 length of tuple value "))
a= type(data[0])
b=type(data[1])
if a == b :
    print("homogenous value")
else:
    print("heterogenous value")
'''
#19.Wap to check whether the string is palindrome or not.
'''
a=input('Enter a string ')
if a == a[::-1] :
    print('palindrome')
else:
    print("not palindrome")
'''
#20.Wap to check whether the number is positive or negative.
'''
num=int(input("Enter a number "))
if num >0 :
    print('positive')

else:
    print('negative')
'''    
