#print first five natural numbers from a set of number
'''
i=1
while i<=5 :
    print(i)
    i += 1
'''    
#first 7 no.in reverse
'''
i=7
while i>=1:
    print(i)
    i-=1
'''    
#table of 8
'''
i=1
while i<=10:
    print(f"8*{i}= {8*i}")
    i+=1
'''
#table of 8 print in reverse
'''
i=10
while i>=1:
    print(f"8*{i}= {8*i}")
    i-=1
    
'''
#print first n natural number
'''
n=int(input("Enter a number"))
i=1
while i<= n:
    print(i)
    i+=1
'''
#print first n even number
'''
n=int(input("Enter a number"))
i=1
while i<= n:
    print(i*2-2)
    i+=1
'''
#print even upto 15
'''
n=int(input("Enter a number"))
i=0
while i<= n:
    print(i)
    i+=2
'''
#print first n odd number
'''
n=int(input("Enter a number"))
i=1
while i<= n:
    print(i*2-1)
    i+=1
'''    
#print odd upto 15
'''
n=int(input("Enter a number"))
i=1
while i<= n:
    print(i)
    i+=2    
'''
#print first n even number reverse
'''
n=int(input("Enter a number"))
i=n
while i>=0:
    print(i*2)
    i-=1
'''    
#print even upto 15 reverse
'''
i=15
while i>=1:
    print(i-1)
    i-=2
'''
#print first n odd number reverse
'''
n=int(input("Enter a number"))
i=n
while i>=1:
    print(i*2-1)
    i-=1
'''
#print odd upto 15 revese
'''
i=15
while i>=1:
    print(i)
    i-=2
'''
#Print numbers from 1 to 10 using a while loop.
'''
i=1
while i<=10:
    print(i)
    i+=1
'''
#Print numbers from 10 to 1 in reverse order.
'''
i=10
while i>=1:
    print(i)
    i-=1
'''    
#Print all even numbers from 1 to 20.
'''
i=1
while i<=20:
    print(i+1)
    i+=2
'''
#Print all odd numbers from 1 to 20.
'''
i=1
while i<=20:
    print(i)
    i+=2
'''
#Print the multiplication table of 5 using a while loop.
'''
i=1
while i<=10:
    print(f"5*{i}={5*i}")
    i+=1
'''
#Find the sum of numbers from 1 to 10.
'''
sum=0
i=1
while i <= 10:
    
    sum=sum+i
   
    i+=1
print(sum)    
'''    
#Find the sum of even numbers from 1 to 20.
'''
sum=0
i=2
while i<=20 :
    sum=sum+i
    i+=2
print(sum)
'''
#Count how many numbers are present from 1 to 50.
'''
coun=0
i=1
while i<=50:
    coun+=1
    i+=1
    
print(coun)    
'''
#Find the product of numbers from 1 to 5.
'''
mul=1
i=1
while i<=5:
    mul=mul*i
    i+=1
print(f"product={mul}")
'''
#Find the sum of odd numbers from 1 to 25.
'''
i=1
sum=0
while i <= 25:
    sum=sum+i
    i+=2
print(sum)    
'''    
#SPY number or not = the number whose sum of digits is equle to product of digit.
'''
n=int(input("enter a number "))
i= n
sum=0
prod=1
while i>0:
    id = i%10
    sum += id
    prod *= id
    i=i//10
if sum == prod:
    print("it is spy number ")
else:
    print("not a spy number")
'''
#From a given integer, find the lagest digit
'''
n=int(input("enter a number "))
i= n
l=0
while i>0:
    id=i%10
    if id>l:
        l=id
    i=i//10
print(f"From {n} , {l} is largest digit ")    
'''
# #From a given integer, find the lagest digit
'''
n=int(input("enter a number "))
i= n
s=n%10
while i>0:
    id=i%10
    if id<s:
        s=id
    i=i//10
print(f"From {n} , {s} is smallest digit ")  
'''
#From first 20 natural number store even numbers seperatly and odd numbers seperately in a list
'''
i=1
even=[]
odd=[]
while i<=20:
    if i%2==0:
        even=even+[i]
    else:
        odd.append(i)
    i+=1    
    
print(even,odd)   
'''
#print all number which are divisible by 3 and 5 in a tuple(1000)
'''
i=1
div=[]
while i<=1000:
    if i%3==0 and i%5==0:
        div=div+[i]
    i+=1
   
print(tuple(div))        
'''        
# store all the numbers in set which are factors of 23 upto 500
'''
i=1
s=[]
while i<=500:
    if i%23==0:
        s=s+[i]
    i+=1
print(set(s))    
'''
# count total number of even digits and odd digits from a given intiger
'''
n=int(input("Enter a number "))
even=0
odd=0
i=n
while i>0:
    ld=i%10
    if ld%2==0:
        even=even+1
    else:
        odd=odd+1
    i=i//10


print(even, odd)    
'''   
# Factorial of a given number
'''
n=int(input("Enter a number "))
i=n
fact=1
while i>0:
    fact=fact*i
    i-=1
print(fact)    
'''    
# print first 5 multiples of 7 , wher it should be in dictionary format (keys should be numbers, values should be its cube )
'''
dic={}
i=1
while i<=5:
    dic[i*7]= (i*7)**3
    i+=1
print(dic)
'''
#1. Store 5 Numbers in a List
'''
li=[]
i=1
while i<=5:
    n=int(input())
    li.append(n)
    i+=1
    
print(li)    
'''    
#2. Store 10 Numbers in a List
'''
li=[]
i=1
while i<=10:
    n=int(input())
    li.append(n)
    i+=1
    
print(li) 
'''
#3. Store 5 Names in a List
'''
li=[]
i=1
while i<=5:
    n=input()
    li.append(n)
    i+=1
    
print(li)
'''
#4. Store 5 Cities in a List
'''
li=[]
i=1
while i<=5:
    n=input("Enter your city")
    li.append(n)
    i+=1
    
print(li)
'''
#5. Store 5 Floating Point Values in a List
'''
li=[]
i=1
while i<=5:
    n=float(input("Enter your floating point value"))
    li.append(n)
    i+=1
print(li)
'''
#6. Store Numbers Until User Enters 0
'''
li=[]
i=1
while True:
    n=int(input())
    if n==0:
        break
    else:
        li.append(n)
print(li)
'''
#7. Store 5 Employee IDs in a List
'''
li=set()
i=1
while i<=5:
    n=int(input("Enter your id "))
    li.add(n)
    i+=1
print(list(li))
'''
#8. Store 5 Mobile Numbers in a List
'''
li=set()
i=1
while i<=5:
    n=int(input("Enter your mobile number "))
    li.add(n)
    i+=1
print(list(li))
'''
#9. Store 5 Email IDs in a List
'''
li=set()
i=1
while i<=5:
    n=input("Enter your gmail ")
    if "@gmail.com" in n:
        li.add(n)
        
    else:
        print("Enter valid gmail")
    i+=1    
print(list(li))
'''
#10. Store 5 College Names in a List
'''
li=set()
i=1
while i<=5:
    n=input("Enter college name ")
    li.add(n)
    i+=1
print(list(li))
'''    
#11. Store 5 Numbers in a Tuple
'''
tu=()
i=1
while i<=5:
    n=int(input())
    tu=tu +(n,)
    i+=1
    
print(tu)
'''
#12. Store 10 Names in a Tuple
'''
tu=()
i=1
while i<=10:
    n=int(input())
    tu=tu +(n,)
    i+=1
    
print(tu)
'''
#13. Store 5 Cities in a Tuple
'''
tu=()
i=1
while i<=5:
    n=input("Enter citie name")
    tu=tu +(n,)
    i+=1
    
print(tu)
'''
#14. Store 5 Subjects in a Tuple
'''
tu=()
i=1
while i<=5:
    n=input("Enter subject name")
    tu=tu +(n,)
    i+=1
    
print(tu)
'''
#15. Store 5 Product Names in a Tuple
'''
tu=()
i=1
while i<=5:
    n=input("Enter Product Names ")
    tu=tu +(n,)
    i+=1
    
print(tu)
'''
#16. Store 5 Unique Numbers in a Set
'''
se=set()
i=1
while i<=5:
    n=int(input())
    se.add(n)
    i+=1
    
print(se)
'''
#17. Store 10 Unique Numbers in a Set
'''
se=set()
i=1
while i<=10:
    n=int(input())
    se.add(n)
    i+=1
    
print(se)
'''
#18. Store 5 Unique Names in a Set
'''
se=set()
i=1
while i<=5:
    n=input("Enter name")
    se.add(n)
    i+=1
    
print(se)
'''
#19. Store 5 Unique Cities in a Set
'''
se=set()
i=1
while i<=5:
    n=input("Enter citie")
    se.add(n)
    i+=1
    
print(se)
'''
#20. Store 5 Unique Course Names in a Set
'''
se=set()
i=1
while i<=5:
    n=input("Enter Course Names")
    se.add(n)
    i+=1
    
print(se)
'''
#21. Store 5 Key-Value Pairs in Dictionary
'''
di={}
i=1
while i<=5:
    k=input()
    v=input()
    di[k]= v
    i+=1
print(di)
'''
#22. Store Student Name and Marks in Dictionary
'''
di={}
i=1
while i<=5:
    name=input("Enter name ")
    mark=int(input("Enter mark"))
    di[name]=mark
    i+=1
print(di)
'''
#23. Store Employee ID and Name in Dictionary
'''
di={}
i=1
while i<=5:
    id=int(input("Enter Emp_ID "))
    name=input("Enter name")
    di[id]=name
    i+=1
print(di)
'''
#24. Store Product ID and Product Name in Dictionary
'''
di={}
i=1
while i<=5:
    pro_id=int(input("Enter Product ID "))
    pro_name=input("Enter Product name")
    di[pro_id]=pro_name
    i+=1
print(di)
'''
#25. Store Country and Capital in Dictionary
'''
di={}
i=1
while i<=5:
    coun=input("Enter country name ")
    cap=input("Enter country's capital ")
    di[coun]=cap
    i+=1
print(di)    
'''
#26. Store 5 Student Names in List
'''
li=[]
i=1
while i<=5:
    n=input("Enter Student Name ")
    li.append(n)
    i+=1
    
print(li)
'''
#27. Store 5 Student Marks in List
'''
li=[]
i=1
while i<=5:
    n=input("Enter Student mark ")
    li.append(n)
    i+=1
    
print(li)
'''
#28. Store 5 Salaries in List
'''
li=[]
i=1
while i<=5:
    n=int(input("Enter Salaries "))
    li.append(n)
    i+=1
    
print(li)
'''
#29. Store 5 Ages in List
'''
li=[]
i=1
while i<=5:
    n=int(input("Enter age "))
    li.append(n)
    i+=1
    
print(li)
'''
#30. Store 5 Blood Groups in List
'''
li=[]
i=1
while i<=5:
    n=input("Enter blood Groups ")
    li.append(n)
    i+=1
    
print(li)
'''
#31. Store 5 Colors in List
'''
li=[]
i=1
while i<=5:
    n=input("Enter color ")
    li.append(n)
    i+=1
    
print(li)
'''
#32. Store 5 Fruits in List
'''
li=[]
i=1
while i<=5:
    n=input("Enter Fruits ")
    li.append(n)
    i+=1
    
print(li)
'''
#33. Store 5 Vegetables in List
'''
li=[]
i=1
while i<=5:
    n=input("Enter Vegetables ")
    li.append(n)
    i+=1
    
print(li)
'''
#34. Store 5 Bike Names in List
'''
li=[]
i=1
while i<=5:
    n=input("Enter Bike Name ")
    li.append(n)
    i+=1
    
print(li)
'''
#35. Store 5 Car Names in List
'''
li=[]
i=1
while i<=5:
    n=input("Enter car Name ")
    li.append(n)
    i+=1
    
print(li)
'''

#print first 10 natural numbers in reverse and store in the dic,where key should be square of the numbers and value should be only the number
'''
di={}
i=10
while i>=1:
    di[i**2]= i
    i-=1
print(di)    
'''
#print all the multiples of 3 and 7 upto 400 and store dictionary key should be number and value should be squ of number
'''
di={}
i=1
while i<=400:
    
    if i%3==0 and i%7==0 :
        di[i]= (i**2)
    i+=1    
print(di)        
'''
#36Store 5 Student Names and Marks as Nested List
'''
li=[]
i=1
while i<=5:
    a=input("Enter name  ")
    b=int(input("Enter  mark "))
    li.append([a,b])
    i+=1
print(li)
'''
#37. Store 5 Employee Details as Nested List
'''
li=[]
i=1
while i<=5:
    a=input("Enter employee_name  ")
    b=int(input("Enter employee_id  "))
    li.append([b,a])
    i+=1
print(li)
'''
#38. Store 5 Product Details as Nested List
'''
li=[]
i=1
while i<=5:
    a=input("Enter product_name  ")
    b=int(input("Enter product_id  "))
    li.append([b,a])
    i+=1
print(li)
'''
#39. Store 5 Book Details as Nested List
'''
li=[]
i=1
while i<=5:
    a=input("Enter book_name  ")
    b=int(input("Enter book_id  "))
    li.append([b,a])
    i+=1
print(li)
'''
#40. Store 5 Movie Details as Nested List
'''
li=[]
i=1
while i<=5:
    a=input("Enter movie_name  ")
    b=int(input("Enter ticket price  "))
    li.append([a,b])
    i+=1
print(li)
'''
x = 3
while x > 0:
    x -= 1
    print(x)

    



    
