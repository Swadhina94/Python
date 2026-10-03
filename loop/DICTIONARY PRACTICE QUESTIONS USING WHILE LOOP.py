
#1. Store 5 Student Roll Numbers and Names in a Dictionary.
'''
i=1
di={}
while i<=5:
    roll=int(input("Enter roll number "))
    name = input("Enter name ")
    di[roll]=name
    i+=1
print(di)    
'''
#2. Store 5 Employee IDs and Employee Names in a Dictionary.
'''
i=1
di={}
while i<=5:
    id=int(input("Enter Employee Id "))
    name = input("Enter Employee name ")
    di[id]=name
    i+=1
print(di)
'''
#3. Store 5 Product IDs and Product Names in a Dictionary.
'''
i=1
di={}
while i<=5:
    id=int(input("Enter product Id "))
    name = input("Enter product name ")
    di[id]=name
    i+=1
print(di)
'''
#4. Store 5 Country Names and Capitals in a Dictionary.
'''
i=1
di={}
while i<=5:
    country=input("Enter country ")
    capital = input("Enter capital ")
    di[country]=capital
    i+=1
print(di)
'''
#5. Store 5 State Names and Capitals in a Dictionary.
'''
i=1
di={}
while i<=5:
    state=input("Enter state ")
    capital = input("Enter capital ")
    di[state]=capital
    i+=1
print(di)
'''
#6. Store 5 Subject Codes and Subject Names in a Dictionary.
'''
i=1
di={}
while i<=5:
    code=int(input("Enter subject code "))
    name = input("Enter subject name ")
    di[code]=name
    i+=1
print(di)
'''
#7. Store 5 Mobile Numbers and Owner Names in a Dictionary.
'''
i=1
di={}
while i<=5:
    mobile=int(input("Enter mobile number "))
    name = input("Enter owner name ")
    di[mobile]=name
    i+=1
print(di)
'''
#8. Store 5 Vehicle Numbers and Owner Names in a Dictionary.
'''
i=1
di={}
while i<=5:
    number=input("Enter vehicle number ")
    name = input("Enter owner name ")
    di[number]=name
    i+=1
print(di)
'''
#9. Store 5 Book IDs and Book Names in a Dictionary.
'''
i=1
di={}
while i<=5:
    id=input("Enter Book id ")
    name = input("Enter Book name ")
    di[id]=name
    i+=1
print(di)
'''
#10. Store 5 Course IDs and Course Names in a Dictionary.
'''
i=1
di={}
while i<=5:
    id=input("Enter course id ")
    name = input("Enter course name ")
    di[id]=name
    i+=1
print(di)
'''
#11. Store 5 Department IDs and Department Names in a Dictionary.
'''
i=1
di={}
while i<=5:
    id=input("Enter Department id ")
    name = input("Enter Department name ")
    di[id]=name
    i+=1
print(di)
'''
#12. Store 5 Customer IDs and Customer Names in a Dictionary.
'''
i=1
di={}
while i<=5:
    id=input("Enter customer id ")
    name = input("Enter customer name ")
    di[id]=name
    i+=1
print(di)
'''
#13. Store 5 Hospital IDs and Hospital Names in a Dictionary.
'''
i=1
di={}
while i<=5:
    id=input("Enter Hospital id ")
    name = input("Enter Hospital name ")
    di[id]=name
    i+=1
print(di)
'''
#14. Store 5 Teacher IDs and Teacher Names in a Dictionary.
'''
i=1
di={}
while i<=5:
    id=input("Enter Teacher id ")
    name = input("Enter Teacher name ")
    di[id]=name
    i+=1
print(di)
'''
#15. Store 5 College Codes and College Names in a Dictionary.
'''
i=1
di={}
while i<=5:
    code=input("Enter college code ")
    name = input("Enter college name ")
    di[code]=name
    i+=1
print(di)
'''
#16. Store 5 Website Names and URLs in a Dictionary.
'''
i=1
di={}
while i<=5:
    URLs=input("Enter Website URLs ")
    name = input("Enter Website name ")
    di[URLs]=name
    i+=1
print(di)
'''
#17. Store 5 Usernames and Passwords in a Dictionary.
'''
i=1
di={}
while i<=5:
    User_name=input("Enter college code ")
    passwords = input("Enter college name ")
    di[User_name]= passwords
    i+=1
print(di)
'''
#18. Store 5 Product Names and Prices in a Dictionary.
'''
i=1
di={}
while i<5:
    name=input("Enter product name ")
    price=float(input("Enter product price "))
    di[name]=price
    i+=1
print(di)    
'''
#19. Store 5 Student Names and Marks in a Dictionary.
'''
20. Store 5 Employee Names and Salaries in a Dictionary.

21. Store 5 City Names and Pincodes in a Dictionary.

22. Store 5 Village Names and Population in a Dictionary.

23. Store 5 Countries and Currency Names in a Dictionary.

24. Store 5 Programming Languages and Creators in a Dictionary.

25. Store 5 Operating Systems and Their Developers in a Dictionary.

26. Store 5 Cricket Players and Their Teams in a Dictionary.

27. Store 5 Movies and Their Directors in a Dictionary.

28. Store 5 Books and Their Authors in a Dictionary.

29. Store 5 Courses and Their Fees in a Dictionary.

30. Store 5 Students and Their CGPA in a Dictionary.

31. Store 5 Employees and Their Departments in a Dictionary.

32. Store 5 Products and Available Quantities in a Dictionary.

33. Store 5 Bank Names and IFSC Codes in a Dictionary.

34. Store 5 Email IDs and User Names in a Dictionary.

35. Store 5 Aadhaar Numbers and Person Names in a Dictionary.

36. Store 5 PAN Numbers and Person Names in a Dictionary.

37. Store 5 Train Numbers and Train Names in a Dictionary.

38. Store 5 Flight Numbers and Airline Names in a Dictionary.

39. Store 5 Shop IDs and Shop Names in a Dictionary.

40. Store 5 Branch Codes and Branch Names in a Dictionary.

41. Store n Student Roll Numbers and Names in a Dictionary.

42. Store n Product IDs and Product Names in a Dictionary.

43. Store n Employee IDs and Employee Names in a Dictionary.
'''
#44. Store Data Until User Enters 'stop' as Key.
'''
di={}
while True:
    id=input("Enter id ").lower()
    name = input("Enter name ")
    if id == 'stop':
        break
    else:
        di[id]= name
    
print(di)    
'''
#45. Store Student Names and Marks Until User Enters 'exit'.
'''
di={}
while True:
    name=input("Enter name ").lower()
    mark = int(input("Enter mark "))
    if name == 'exit':
        break
    else:
        di[name]= mark
    
print(di)
'''
#46. Store Employee IDs and Salaries Until User Enters 'quit'.
'''
di={}
while True:
    id=input("Enter Employee IDs ").lower()
    until = int(input("Enter Salaries Until "))
    if id == 'quit':
        break
    else:
        di[id]= until
    
print(di)
'''
#47. Store Product IDs and Prices Until User Enters 'done'.
'''
di={}
while True:
    id=input("Enter Product IDs ").lower()
    until = int(input("Enter Prices Until "))
    if id == 'done':
        break
    else:
        di[id]= until
    
print(di)
'''
#48. Store Country and Capital Pairs Until User Enters 'stop'.

'''
49. Store Book Names and Authors Until User Enters 'exit'.

50. Store Usernames and Passwords Until User Enters 'done'.
'''
#find the voiwl in string
'''
word='apple'
s=''
i=0
while i<len(word) :
    if word[i] in 'aeiou':
        s=s+word[i]
    i+=1
print(s)        
'''
'''
i=0 o=a a in aeiou so take this inside of s
then i=1  1=p p not in aeiou so not take this
then i=2 2=p same so not take
same as l so l not take
then e is in aeiou so take 
'''
#Extract all the lowercase alphabets from a given messaage
'''
s=''
i=0
mess=input()
while i<len(mess):
    if 'a'<=mess[i]<='z':
        
        s=s+mess[i]
    i+=1
print(s)    
'''
#Toggle a given string
'''
m=input("enter something ")
s=''
i=0
while i< len(m):
    if 'a'<= m[i] <='z':
        s=s+(m[i].upper())
    elif 'A'<= m[i]<='Z':
        s=s+(m[i].lower())
    else:
        s=s+m[i]
    i+=1
    
print(s)
'''
#Extract all the characters which are present at odd index of agiven message(without slicing)
'''
m=input("Enter something ")
s=''
i=1
while i< len(m):
    s=s+m[i]
    i+=2
print(s)    
'''
#Reverse a string without using any inbult method
'''
m=input("Enter something ")
s=''
i=len(m)-1
while i >= 0:
    s=s+m[i]
    i-=1
print(s)    
'''
#Reverse a string without using any inbult method
'''
m=input("Enter something ")
s=''
i=0

while i <= len(m)-1:
    s=m[i]+s
    i+=1
print(s)
'''
#Extract all the SVDT from a list
'''
li=eval(input("Enter "))
i=0
l=[]
while i < len(li):
    
    if type(li[i]) in [int,float,complex,bool]:
        l.append(li[i])
    i+=1
print(l)    
'''
# check given list is homogenous or heterogenous list
'''
li=eval(input("Enter "))
i=0
count=0
l=[]
while i < len(li):
    if type(li[i])== type(li[0]):
        count+=1
    i+=1    
if count==len(li):
    print("honogenous")
else:
    print("heterogenous")
'''    
#Remove duplicate values from a list without typecasting
'''
li=eval(input("Enter value of list "))
i=0

l=[]
while i < len(li):
    if li[i]not in l:
        l.append(li[i])
    i+=1
print(l)    
'''
#From two list , Find  all the common elements present in a first list
'''
a=eval(input("Enter value of list "))        
b=eval(input("Enter value of list "))
i=0

l=[]
while i < len(a):
    if a[i] in b:
        l.append(a[i])
    i+=1
print(l)     
'''
#From a Tuple, collect all the palindromic words
'''
t=eval(input())
i=0
l=()
while i<len(t):
    p=str(t[i])
    if p == p[::-1]:
        l=l+(p,)
    i+=1
print(l)    
'''        
#Check given number is prime number or not prime number
'''
n= int(input())
if n<2:
    print("not a prime number ")
else:
    i=2
    flag=0
    while i<n:
        if n%i==0:
            flag+=1
        i+=1
    if flag ==0:
        print("prime number ")
    else:
        print("not a prime number ")

'''
#given number is strong number or not
'''
n=int(input("enter the number "))
i=n
s=0

while i>0:
    id=i%10
    fac=1
    while id>0:
        fac=fac*id
        id=id-1
    s=s+fac
    i=i//10
if s==n:
    print("strong number ")
else:
    print("Not a strong number")
'''
#given number is armstrong number or not
'''
n=int(input("enter the number "))
i=n
s=0
a=str(n)
l=len(a)


while i>0:
    id=i%10
    arm=1
    while id:
        arm=id**l
        break
    s=s+arm
    i=i//10
if s==n:
    print("armstrong number ")
else:
    print("Not a armstrong number")
'''
#Revese a given int
'''
n=int(input("enter the number "))
s=str(n)
if n>0:
    d=s[::-1]
    print(d)
else:
    c=abs(n)
    s=str(c)
    d=s[::-1]
    print(f"-{d}")
#use while loop
n=int(input("enter the number "))
a=abs(n)
rev=0
while a>0:
    ld = a%10
    rev = rev*10+ld
    a=a//10
if n>0:
    print(rev)
else:
    print(-rev)
'''
#find first n int
'''n=int(input("enter the number "))
i=n//2
a= -i
if n%2==0:
    while a < i:
        print(a)
        a+=1
else:
    while a < i:
        print(a)
        a+=1
'''    
















    






