#Create a dictionary and display all keys using a while loop.
'''
d = {}

n = int(input("Enter number of elements: "))

i = 0
while i < n:
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value
    i += 1

keys = list(d.keys())

i = 0
while i < len(keys):
    print(keys[i])
    i += 1
'''

#2. Create a dictionary and display all values using a while loop.
'''
d={}
n=int(input("Enter number "))
i=0
while i< n:
    key=input("Enter key ")
    value=input("Enter value ")
    d[key]=value
    i+=1
value=list(values[i])
i=0
while i< len(values[i]):
    print(values[i])
    i+=1

'''
'''
3. Create a dictionary and display all key-value pairs using a while loop.

4. Count the number of items in a dictionary using a while loop.

5. Find the sum of all values in a dictionary using a while loop.

6. Find the maximum value in a dictionary using a while loop.

7. Find the minimum value in a dictionary using a while loop.

8. Print all keys whose values are even using a while loop.

9. Print all keys whose values are odd using a while loop.

10. Find the average of all values in a dictionary using a while loop.

11. Count how many values are greater than 50 using a while loop.

12. Count how many values are less than 50 using a while loop.

13. Search for a given key in a dictionary using a while loop.

14. Search for a given value in a dictionary using a while loop.

15. Find the key having the highest value using a while loop.

16. Find the key having the lowest value using a while loop.

17. Create a new dictionary containing only even values using a while loop.

18. Create a new dictionary containing only odd values using a while loop.

19. Copy one dictionary into another using a while loop.

20. Reverse keys and values of a dictionary using a while loop.
'''
# XYLEM Number or PHLOEM Number
'''
n=int(input('Enter your number'))    #1234
b=a=n                       #b=a=n=1234
c=n%10                       #4

while n>10:                   #1234>10    123>10    12>10  1>10 
    n =n//10
s=0
while b>0:
    ld=b%10
    s=s+ld
    b=b//10
if (n +c == s-n-c):
    print('XYLEM')
else:
    print('PHILEM')
'''
#Swap first digit to last digit of integer
#12345------> 52341
#1234------>4231
'''
n=int(input("Enter number "))
s=0
a=b=n
c=n%10

while a>10:
    a=a//10
count=0
while b >0:
    count +=1
    b//=10
middle= n- a*(10**(count-1))-c

swap = c *(10 ** (count-1)) +a      
print(swap +middle)
'''
#Swap first digit to last digit of integer
'''
n=int(input("Enter number "))
a=n
ld=n%10
count=0
while a>10:
    count=count+1
    a=a//10
dig=10**count
mid=n - a*dig-ld
swap=ld*dig+a
print(swap+mid)
'''
# XYLEM Number or PHLOEM Number
#1234----> 1+4=5 , 2+3 = 5 --Xylem
#1356---->1+6=7 , 3+5=8 --- phloem
'''
n=int(input("Enter number "))
sum=0
ld=n%10
while n>0:
    l=n%10
    sum+=l
    n=n//10
if l+ld == (sum-ld-1):
    print("XYLEM")
else:
    print("PHLOEM")
'''
#check given number is HARSHAD number or not
'''
num=int(input("Enter a number "))
a=num
sum=0
while a >0:
    ld=a%10
    sum=sum+ld
    a//=10               
if num%sum==0:
    print("HARSHAD")
else:
    print("not")
'''
#Automorphic number
'''
num=int(input("Enter number"))
a=num**2
d=1
c=num
while c>0:
        d=d*10
        c=c//10

if a%d==num:
    print("Automorphic")
else:
    print("not")
'''
#Fabnacci serise
'''
s=int(input("Enter total number of value in seris"))
a=0
b=1
i=0
while i<s:
    print(a , end=" ")
    a,b=b,a+b
    i=i+1
'''
#Duck Number or not
'''
n=int(input("Enter "))#1234
count=0
while n>0:
    l=n%10 
    if l==0:
        count+=1
    n=n//10
if count>0:
    print("duck")
else:
    print("not")
'''    
#sunny number or not
'''
s=float(input("Enter "))
n=int(s)
count=0
i=1    
while i<n:
    a=n+1
    if a == i**2:
        count+=1
    i+=1
if count ==1:
    print("sunny")
else:
    print("not")
'''
#Happy number
'''
n=int(input("Enter number "))
s=n

while n!=1 and n!=4:
    sum=0
    while n>0:
        l=n%10
        a=l**2
        sum+=a
        n=n//10
    n=sum
if sum==1:
    print(f"{s} is a happy number")
else:
    print(f"{s} is a not happy number")
'''
#Disarium number or not
#89--> 8**1 + 9**2 = 89 (it is a Disarium numer)
#135-->1**1 + 3**2 + 5**3 =135(it is a Disarium number)
#12-->1**1 + 2**2=5 (it is not a not Disarium number )
'''
n=int(input("Enter number "))
b=n
i=1
sum=0
reverse=0
while n>0:                        #123#12#1#0
    l=n%10                        #3#2#1
    reverse=reverse*10+l          #3#30+2=32#320+1=321
    n=n//10                       #12#1#0
s=reverse                         #321    

while s>0 :                       #321#32#3
    a=s%10                        #1#2#3
    sum=sum+(a**i)                #0+1**1=1#1+2**2=5#5+3**3=14
    s=s//10                       #32#3#0
    i+=1                          #i=2#i=3#i=4
                                            
if sum== b:
    print("Disarium")
else:
    print("Not Disarium ")
'''
# xY OR phL
'''
n=int(input("Enter a number "))
ld=n%10
sum=0
while n>0:
    fd=n%10
    sum=sum+fd
    n=n//10
if ld+fd == (sum-ld-fd):
    print("XYLEM")
else:
    print("PHLOEM")
   
'''
#NEON number or not
#9=9*9=81 8+1=9
'''
n=int(input("Enter a number "))
p=n*n
sum=0
while p>0:
    ld=p%10
    sum=sum+ld
    p=p//10
if sum == n:
    print("NEON")
else:
    print("Not NEON ")
'''
#
'''
n=int(input("Enter a number "))
sum =0
i=1
while i<n:
    p=n%i
    if p==0:
        sum=sum+i
    i+=1
print(sum)    
if sum == n:
    print("Perfect number")
else:
    print("Not Perfect number ")
'''
#
'''
n=int(input("Enter a number "))
a=n
sum=0
while a>0:
    ld=a%10
    sum=sum+ld
    a=a//10
if n % sum ==0:
    print("Harshad")
else:
    print("Not Harshad")
'''    
# happy number
#19=1^2+9^2=1+81
'''
n=int(input("Enter a number "))
while n!=1 and n!=4:
    sum=0
    while n>0:
        ld=n%10
        sum=sum+ld**2
        n=n//10
    n=sum
if sum == 1:
    print("Happy number")
else:
    print("Not happy number")
'''    
# slippery number
'''
n=int(input("Enter a number "))
while n!=4:
    sum=0
    while n>0:
        ld=n%10
        sum=sum+ld**2
        n=n//10
    n=sum
if sum == 4:
    print("slippery number")
elif n==4:
    print("slippery number")
else:
    print("Not slippery number")
'''    
#Disarium number or not
#89--> 8**1 + 9**2 = 89 (it is a Disarium numer)
#135-->1**1 + 3**2 + 5**3 =135(it is a Disarium number)
#12-->1**1 + 2**2=5 (it is not a not Disarium number )
'''
n=int(input("Enter a number "))
a=n
rev=0
sum=0
i=1
while n>0:
    ld=n%10
    rev=rev*10+ld
    n=n//10
while rev >0:
    ld=rev%10
    sum=sum+(ld**i)
    i+=1
    rev=rev//10
if a== sum :
    print("disarium number")
else:
    print("not a disarium number")
'''
#accept a sentense and create a dictionary when each
s=input("Ente somthing ")
p=s.split()
dc={}
f=len(p)
while f>0:
    i=0
    a=p[i]
    j=0
    sum=0
    q=len(a)
    while q>0:
        b=a[j]
        sum=sum+ord(b)
        j+=1
    dc[p[i]]= sum
    i+=1
print(dc)    


    
    




    


    
    
    
    


      

  
    
    
    

















        

        

