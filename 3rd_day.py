#1 Check given list is homogenous or heterogenous
'''
n=eval(input("Enter a list "))
count=0
for i in n:
    if type(n[0])!=type(i):
        count+=1
if count==0:
    print("homogenous")
else:
    print("heterogenous")
'''    
#2 Reverse a list
'''    
n=eval(input("Enter a list "))
rev=[]
for i in n:
    rev=[i]+rev
print(rev)    
'''
#3 Reverse in string
# input = apple is red
#output= red is apple
'''
m=input("enter a message ").split()
rev=''
for i in m:
    rev=i+' '+rev
print(rev)
'''
#with out use split()
'''
m=input("enter a message ")
li=[]
l=''
rev=''
for i in m: 
    if i!= ' ':
        l=l+i
    else:
        li.append(l)
        l =''
li.append(l)        
for i in li:
    rev=i+' '+rev
print(rev)    
'''
#4
'''
a=input("enter a message ").split()
odd=a[1::2]
even=a[::2]
m=odd + even
rev=''
for i in m:
    rev=rev+' '+i
print(rev)    
'''
#5
'''
n=input("enter a message ").split()
odd=n[1::2]
even=n[::2]
rev=[]
for i in odd:
    b=i[::-1]
    rev.append(b)
print(rev+even)
'''
#6 i/p= apple is a red and sweet fruit
#o/p=['si' 'der' 'teews' 'apple' 'a' 'and' ''fruit]
'''
n=input("enter a message ").split()
odd=n[1::2]
even=n[::2]
rev=[]
for i in even:
    b=i[::-1]
    rev.append(b)
print(odd+rev)
'''
#7 input- apple is a red and sweet fruit
#output - ['elppa' 'si' 'a' 'der' 'dna' 'teews' 'tiurf']
'''
m=input("enter a message ")
n=m[::-1].split()
odd=n[1::2]
even=n[::2]
q=even+odd
print(q[::-1])
'''
'''
rev=''
for i in q:
    rev=i+' '+rev
print(rev.split())    
'''
#8 input- apple is a red and sweet fruit
#output - ['apple' 'si' 'a' 'der' 'and' 'teews' 'fruit']
'''
####n=input("enter a message ").split()
####odd=n[1::2]
####even=n[::2]
####rev=[]
####r=[]
####for i in odd:
####    b=i[::-1]
####    rev.append(b)
####mix=even+rev
####half=mix//3
####if mix%2==0:
####    for i in len
####n=input("enter a message ").split()
####for i in range(len(n)):
####    if i%2==0:
####       n[i]=n[i]
####    else:
####        n[i]= n[i][::-1]
####        
####print(n)
'''
##n=input("Enter a messsage ").split()
##count=0
##for i in n:
##    count+=1
##for i in count:
##    if i%2==0:
##        n[i]=n[i]
##    else:
##        n[i]=n[i][::-1]    
##print(n)        
n= int(input("Enter a number "))
m=n
sum=0
while n>9:
    ld=n%10
    sum+=ld
    n=n//10
l=m%10
print
if (n+l)==(sum-l):
    print("x")
else:
    print("p")
    
    

        
        
        
        

