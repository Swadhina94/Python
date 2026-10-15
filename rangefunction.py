#1to print first n even numbers (including 0)
'''
n= int(input("Enter a nth number "))

for i in range(2*n):
    if i%2==0:
        print(i, end=' ')
'''
#2to print first n even numbers (including 0) in reverse
'''
for i in range(2*n,-1,-2):
        print(i, end=' ')
'''
#3to print first n odd numbers (including 0)
'''
for i in range(1,2*n,2):
        print(i, end=' ')
'''
#4to print first n odd numbers (including 0) in reverse
'''
for i in range(2*n-1,0,-2):
        print(i, end=' ')
'''
#5multiplication table
'''
n=int(input("Enter a number "))
for i in range(1,11):
    print(f"{n}x{i}={n*i}")
'''
#6 find all the index position where svdt is present in given tuple
'''
t=eval(input("Enter a tuple list "))
tu=()
for i in range(len(t)):
    if type(t[i]) in (int,float,complex,bool):
        print(i,end=' ')
        
'''
#7 find all the index positions where svdt is not present in given tuple
'''
t=eval(input("Enter a tuple list "))
tu=()
for i in range(len(t)):
    if type(t[i]) not in (int,float,complex,bool):
        print(i,end=' ')

'''
#8 find the sum of all index position where number is present in a given list
'''
t=eval(input("Enter a list "))
sum=0
for i in range(len(t)):
    if type(t[i]) ==int and t[i]%2==0:
        sum+=i
print(sum)    
'''
#9 find sum of all the index position where a integer is present and is divisible by 3 or
#find sum values which are float from a list.
'''
t=eval(input("Enter a list "))
sum=0
s=0
for i in range(len(t)):
    if type(t[i]) ==int and t[i]%3==0:
       
        s+=i
        
    elif type(t[i]) ==float :
        sum+=t[i]
 
print(s+sum)
'''
#10 -'apple'
#204
'''
n=input()
s=0
for i in range(len(n)):
    if n[i] in 'AEIOUaeiou':
        s=s+i+ord(n[i])
print(s)
'''
#Wap to check collection is homogenous or heteregenous
'''
n=eval(input())
for i in  n:
    if type(n[0])!=type(i):
        print("hetrogenous")
        break
else:
    print("homegenous")
'''
# check given number is prime or not using for loop
'''
n=int(input())
count=0
for i in range(1,n):
    if n%i==0:
        count+=1
if count==1:
    print("prime number")
else:
    print("not prime number")
'''
#56. Write a program to find the first perfect number in a given range.
'''
start=int(input())
end=int(input())


for j in range(start,end):
    sum=0
    for i in range(1,j):
        if j%i == 0:
            sum+=i
    if sum==j:
        print(j,end=" ")
'''
    
#57. Write a program to check whether all characters in a string are unique.
'''
n=input()
s=''
for i in range(len(n)):
    if n[i] not in s:
        s+=n[i]
if len(s)== len(n):
    print("unique")
else:
    print("not unique")

'''
#58. Write a program to find the first number divisible by both 7 and 11.
'''
start=int(input())
end=int(input())
for i in range(start,end):
    if i%7==0 and i%11==0:
        print(i)
        break
        
'''

#59. Write a program to search for a username in a list of usernames.
'''
col=eval(input())
n=input()
for i in range(len(col)):
    if n == col[i]:
        print(i)
'''        
#60. Write a program to check whether a given number is prime and print an appropriate message using for-else.
'''
n=int(input())
count=0
for i in range(1,n):
    if n%i==0:
        count+=1
if count==1:
    print("prime number")
else:
    print("not prime number")
'''













        
