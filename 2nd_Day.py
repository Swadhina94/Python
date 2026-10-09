#From a given string remove all the duplicates typecasting
'''
n=input("enter something ")
s=''
for i in n:
    if i not in s:
        s+=i
print(s)        
'''
#remove the last character from a given string
'''
n=input()
s=''
for i in n:
    if i!=n[-1]:
        s+=i
print(s)        
'''
#Remove the first occerance
'''
n=input()
s=''
for i in n:
    if i!=n[0]:
        s+=i
print(s)
'''
# remove the middle occerance
'''
n=input()
if len(n)%2==1:
    m=len(n)//2
    s=''
    for i in n:
        if i!=n[m]:
            s+=i
    print(s)
else:
    print(n)

'''
# find sum of ascii value of all the characters
'''
m=input("Enter a message ")
sum=0
for i in m:
    sum=sum+ord(i)
print(sum)    
'''
#find product of ascii value of all the characters 
'''
m=input("Enter a message ")
pro=0
for i in m:
    pro*=ord(i)
print(pro)    
'''
#froma message collect all the vowels and consonants seperately(duplicates not allowed)
'''
m=input("Enter a message ")
s1=''
s2=''
for i in m:
    if i in 'aeiou':
        if i not in s1:
            s1+=i
    else:
        if i not in s2:
            s2+=i
print("Vowel = ",s1)
print("Consonants= ",s2)
'''
#
'''
l=eval(input("enter "))
pro=1
add=0
for i in l:
    if type(i) == int:
        pro*=i
    elif type(i)==float:
        add+=i
print(pro)
print(add)
'''
a=range(1,10)
print(*a)





