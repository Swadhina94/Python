#1.check given character is digit or not
'''
char=input('enter the character :')
if char.isdigit():
    
    print('this is digite')

'''

#2.check given password is correct or not
'''
orginal_password = input('orginal password is: ')
user_password = input('user_password is :')
if orginal_password == user_password :
    print('this is correct password')

 '''   
#3. check whether 'a' is greater 'b' or not
'''
if ord('a') < ord('b'):
    print(' a is not greater then b')
'''
'''
a=input()
print(a)
'''
#1. Wap to print the square of a number only if it is even.
'''
num=int(input('Enter a number '))
if num % 2 ==0 :
    print('Square = ',num*num)
'''
#2. Wap to check whether the character is vowel or not.
'''
char=input('Enter a character ')
if char in 'AEIOUaeiou':
    print('this is vowel')
'''

#3. Wap to print Ascii value of a character only if it is upper case.
'''
char = input('Enter a char ')

if chr(65)<= char <= chr(90):
    print(ord(char))
'''

#4. Wap to print the cube of a number only if it is divisible by 9 or 6.
'''
num= int(input('Enter a number '))
if num % 9 ==0 or num% 6 ==0:
    print('cube of number is ', num*num*num)
 '''   
#5. Wap to check whether the given integer is 3 Digit number.
'''
dig=int(input('Enter a integer number'))
b=str(dig)
if len(b)== 3:
    
    print('It is 3 digit number')
    
 '''       

#6. Wap to check whether the last digit of a given number is 5.
'''
num=int(input('Enter a number : '))
if num%10 == 5:
    print('the last digit of a given number is 5')
'''
#7. Wap to check whether the given data is float.
'''
data = eval(input('Enter data : '))
s= type(data)
if s is float :
    print('the given data is float')
'''
#8. Wap to check whether the data is single value data.
'''
data = eval(input('Enter data : '))
s= type(data)
if s is float or s is int or s is complex or s is bool :
    print('the data is single value data')
'''
#9. Wap to check whether the given character is digit or not.
'''
char=input('enter the character :')
if char.isdigit():
    
    print('this is digite')
 '''   

#10. Wap to check whether the given integer is multiple of 3.
'''
num= int(input('Enter a number '))
if num % 3 ==0 :
    print('the given integer is multiple of 3')
'''
# even or not
'''
num=int(input('Enter a number:- '))
if num % 2 ==0 :
    print('this number is Even')
'''
# Odd or not
'''
num=int(input('Enter a number:- '))
if num % 2 !=0 :
    print('this number is Odd')
'''
#last digit is 5 or not
'''
num=int(input('Enter a number:- '))
a= num%10
if a==5:
    print('last digit is 5')
 '''   
#last digit is even or not
'''
num=int(input('Enter a number:- '))
a= num%10
if a%2==0:
    print('last digit is even')
'''    
#number is divisible by 3 or not
'''
num= int(input('Enter a number '))
if num % 3 ==0 :
    print('the given integer is multiple of 3')
'''    
#number is multiple of 5 of not
'''
num= int(input('Enter a number '))
if num % 5 ==0 :
    print('number is multiple of 5')
'''    
#total marks of 5 subjects
'''
mark1 = int(input('Enter your mark'))
mark2 = int(input('Enter your mark'))
mark3 = int(input('Enter your mark'))
mark4 = int(input('Enter your mark'))
mark5 = int(input('Enter your mark'))
total= mark1+mark2+mark3+mark4+mark5
print('Total mark is ',total)
'''
#calculate total salary of an employee (BASIC + HRA + DA)
'''
basic=float(input('Basic salary is '))
hra = int(input("Enter HRA "))
da= int(input('Enter DA '))
print('Total salary is ',(basic+hra+da))
'''
#calculate total expenses  -----> Total salary - saving

#calculate age from birth year------> 2026 - birth year
#find remaining marks to reach 100----> 100 - getmark
#area of rectangle------> length*breadth
#cube of a number----> num*num*num or num **3
#calculate salary for N days-----> 500 * 30 
#Area of circle -------> 3.14 * r*r
#Calculate speed (distance/time)-----> distance / time
#Çalculate unit price-----------> Total_amount /no_of _products
#calculate total seconds available in a given minute ------->60* minutes

#convert the given days into week----> given_day // 7

#convert minutes into hours ---> minutes / 60

#convert months into years----> months / 12

#convert rupees into paise-----> rupees * 100

#find square of a number-----> a**2

#find cube of a number----> a**3

#swap two integers----> a^b^b =a , a^b^a = b or a,b = 1,2-> a=a+b , b=a-b , a=a-b 


#find average of 3 numbers----->num1+num2+num3 / 3

#calculate percentage-----> mark / total_mark * 100

#Calculate EMI---->  p

#calculate BMI---->w / h **2

#calculate total bill with 18% GST------> total_bill + (total_bill*18)/100
