#SECTION A: BASIC WHILE LOOP
#Write a program to print numbers from 1 to 20.
'''
n=1
while n<=20:
    print(n,end=" ")
    n+=1
'''    
#Write a program to print numbers from 20 to 1.
'''
n=20
while n>=1:
    print(n,end=" ")
    n-=1
'''    
#Write a program to print all numbers from 1 to N.
'''
n=int(input("Enter Nth number "))
i=1
while i<=n:
    print(i,end=" ")
    i+=1
'''    
#Write a program to print all numbers from N to 1.
'''
n=int(input("Enter Nth number "))
while n>=1:
    print(n,end=" ")
    n-=1
'''    
#Write a program to print all even numbers from 1 to N.
'''
n=int(input("Enter Nth number "))
i=1
while i<=n:
    if i%2==0:
        print(i,end=' ')
    i+=1
'''    
#Write a program to print all odd numbers from 1 to N.
'''
n=int(input("Enter Nth number "))
i=1
while i<=n:
    if i%2==1:
        print(i,end=' ')
    i+=1
'''    
#Write a program to print the first N even numbers.
'''
n=int(input("Enter Nth number "))
i=1
while i<=2*n:
    if i%2==0:
        print(i,end=" ")      
    i+=1    
'''        
#Write a program to print the first N odd numbers.
'''
n=int(input("Enter Nth number "))
i=1
while i<=2*n:
    if i%2==1:
        print(i,end=" ")      
    i+=1
'''    
#Write a program to print the multiplication table of a given number.
'''
n=int(input("Enter a number  "))
i=1
while i<=10:
    print(f"{n} x {i} = {n*i}")
    i+=1
'''



#SECTION B: SUM AND PRODUCT
#Write a program to find the sum of numbers from 1 to N.
'''
n=int(input("Enter a number  "))
i=1
sum=0
while i<=n:
    sum=sum+i
    i+=1
print(sum)
'''
#Write a program to find the sum of all even numbers from 1 to N.
'''
n=int(input("Enter a number  "))
i=1
sum=0
while i<=n:
    if i%2==0:
        sum=sum+i
    i+=1
print(sum)
'''
#Write a program to find the sum of all odd numbers from 1 to N.
'''
n=int(input("Enter a number  "))
i=1
sum=0
while i<=n:
    if i%2==1:
        sum=sum+i
    i+=1
print(sum)
'''
#Write a program to find the product of numbers from 1 to N.
'''
n=int(input("Enter a number  "))
i=1
pro=1
while i<=n:    
    pro=pro*i
    i+=1
print(pro)
'''
#Write a program to find the sum of the squares of the first N natural numbers.
#Example:
#Input: 3
#Output: 14
#Explanation: 1² + 2² + 3² = 14
'''
n=int(input("Enter a number  "))
i=1
sum=0
while i<=n:
    sum=sum+i**2
    i+=1
print(sum)    
'''    

#Write a program to find the sum of the cubes of the first N natural numbers.
#Example:
#Input: 3
#Output: 36
#Explanation: 1³ + 2³ + 3³ = 36
'''
n=int(input("Enter a number  "))
i=1
sum=0
while i<=n:
    sum=sum+i**3
    i+=1
print(sum) 
'''



#SECTION C: FACTORIAL AND FACTORS
#Write a program to find the factorial of a given number.
#i/p- 5
#o/p= 1*2*3*4*5=120
'''
n=int(input("Enter a number  "))
i=1
fac=1
while i<=n:    
    fac=fac*i
    i+=1
print(fac)
'''
#Write a program to print all the factors of a given number.
#Example:
#Input: 12
#Output: 1 2 3 4 6 12
'''
n=int(input("Enter a number  "))
i=1
while i<=n:
    if n%i==0:
        print(i,end=" ")
    i+=1
'''    

     
#Write a program to count the number of factors of a given number.
#Example:
#Input: 12
#Output: Number of factors = 6
'''
n=int(input("Enter a number  "))
i=1
count=0
while i<=n:
    if n%i==0:
        count+=1
    i+=1
print("Number of factors =",count)
'''
#Write a program to check whether a given number is a perfect number or not.
#Example:
#Input: 6
#Output: 6 is a Perfect Number
#Explanation: 1 + 2 + 3 = 6
'''
n=int(input("Enter a number "))
i=1
sum=0
while i<=n :
    sum=sum+i
    i+=1
if sum==n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")
'''


#SECTION D: DIGIT-BASED PROGRAMS
#Write a program to count the number of digits in a given positive integer.
#Example:
#Input: 12345
#Output: Number of digits = 5
'''
n=int(input("Enter a number "))
count=0
while n>0:
    ld=n%10
    count+=1
    n=n//10
print(count)    
'''
#Write a program to find the sum of all digits of a given positive integer.
#Example:
#Input: 1234
#Output: Sum = 10
'''
n=int(input("Enter a number "))
sum=0
while n>0:
    ld=n%10
    sum+=ld
    n=n//10
print("sum=",sum)
'''
#Write a program to find the product of all digits of a given positive integer.
#Example: Input: 1234
#Output: Product = 24
'''
n=int(input("Enter a number "))
pro=1
while n>0:
    ld=n%10
    pro*=ld
    n=n//10
print("product=",pro)
'''
#Write a program to find the sum of all digits of a given negative integer.
#Example: Input: -1234
#Output: Sum = 10
'''
m=int(input("Enter a negetive number"))
n=m*(-1)
sum=0
while n>0:
    ld=n%10
    sum+=ld
    n=n//10
print("sum=",sum)
'''
#Write a program to find the product of all digits of a given negative integer.
#Example: Input: -1234
#Output: Product = 24
'''
m=int(input("Enter a negetive number"))
n=m*(-1)
pro=1
while n>0:
    ld=n%10
    pro*=ld
    n=n//10
print("product=",pro)
'''
#Write a program to find the first digit of a given number.
#Example: Input: 12345
#Output: First digit = 1
'''
n=int(input("Enter a number "))
while n>10:
    n=n//10
print(n)
'''
#Write a program to find the last digit of a given number.
#Example: Input: 12345
#Output: Last digit = 5
'''
n=int(input("Enter a number "))
ld=n%10
print(ld)
'''
#Write a program to reverse a given number.
#Example: Input: 12345
#Output: 54321
'''
n=int(input("Enter a number "))
rev=0
while n>0:
    ld=n%10
    rev=rev*10+ld
    n=n//10
print(rev)
'''
#Write a program to check whether a given number is a palindrome or not.
#Example: Input: 121
#Output: 121 is a Palindrome Number
'''
n=int(input("Enter a number "))
s=n
rev=0
while n>0:
    ld=n%10
    rev=rev*10+ld
    n=n//10
if s==rev:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")
'''
#Write a program to count the number of even digits in a given number.
#Example: Input: 123456
#Output: Number of even digits = 3
'''
n=int(input("Enter a number "))
count=0
while n>0:
    ld=n%10
    if ld %2==0:
        count+=1
    n=n//10
print("Number of even digits =",count)    
'''
#Write a program to count the number of odd digits in a given number.
#Example: Input: 123456
#Output: Number of odd digits = 3
'''
n=int(input("Enter a number "))
count=0
while n>0:
    ld=n%10
    if ld %2==1:
        count+=1
    n=n//10
print("Number of odd digits =",count)
'''




#SECTION E: NUMBER CHECKING PROGRAMS
#Write a program to check whether a given number is even or odd.
'''
n=int(input("Enter a number "))
if n%2==0:
    print(f"{n} is a even number")
else:
    print(f"{n} is a odd number")
'''    
#Write a program to check whether a given number is positive, negative, or zero.
'''
n=int(input("Enter a number "))
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")
'''
#Write a program to check whether a given number is divisible by 5 or not.
'''
n=int(input("Enter a number "))
if n%5==0:
    print("Number is divisible by 5")
else:
    print("number is not divisible by 5")
'''
#Write a program to check whether a given number is divisible by both 3 and 5.
'''
n=int(input("Enter a number "))
if n%5==0 and n%3==0:
    print("Number is divisible by both 3 and 5")
else:
    print("number is not divisible by both 3 and 5")
'''
#Write a program to check whether a given number is a Spy Number.
'''
n=int(input("Enter a number "))
pro=1
sum=0
while n>0:
    ld=n%10
    pro*=ld
    sum+=ld
    n=n//10
if pro==sum:
    print("Spy number")
else:
    print("Not a Spy number")
'''
#Write a program to check whether a given number is an Armstrong Number.
#Example:
#Input: 153
#Explanation: 1³ + 5³ + 3³ = 153
#Output: 153 is an Armstrong Number
'''
n=int(input("Enter a number "))
q=p=n
count=0
sum=0
while n>0:
    ld=n%10
    count+=1
    n//=10
while p>0:
    ld=p%10
    sum=sum+ld**count
    p//=10
if q== sum:
    print("Armstrong Number")
else:
    print(" Not Armstrong Number")   
'''
#Write a program to check whether a given number is a Strong Number.
#Example: Input: 145
#Explanation: 1! + 4! + 5! = 145
#Output: 145 is a Strong Number
'''
n=int(input("Enter a number "))
q=p=n
sum=0
while n>0:
    ld=n%10
    fac=1
    i=1
    while i<=ld:
        fac*=i
        i+=1
    sum=sum+fac
    n=n//10
if sum == q:
    print("Strong number")
else:
    print("Not a Strong number ")
        
    
'''
#Write a program to check whether a given number is a Perfect Number.
'''
n=int(input("Enter a number "))
i=1
sum=0
while i<=n :
    sum=sum+i
    i+=1
if sum==n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")
'''
#Write a program to check whether a given number is a Prime Number.
'''
n=int(input("Enter a number "))
i=1
count=0
while i<=n:
    if n%i==0:
        count+=1
    i+=1    
if count==2:
    print("prime number ")
else:
    print("not a prime number")
'''    
#Write a program to check whether a given number is a Palindrome Number.
'''
n=int(input("Enter a number "))
s=n
rev=0
while n>0:
    ld=n%10
    rev=rev*10+ld
    n=n//10
if s==rev:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")
'''
   






