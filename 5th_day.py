#1Write a program to accept a string of words and create a dictionary where each word is the key
#and its length is the value.
'''
n=input().split()
di={}
for i in n:
    di[i]=len(i)
print(di)
'''
#2Write a program to accept a string containing multiple words and create a dictionary where each word is the
#key and its first character is the value.
'''
n=input().split()
di={}
for i in n:
    di[i]=i[0]
print(di)
'''
#3Write a program to accept a string of words and create a dictionary where each word is the key and its
#last character is the value.
'''
n=input().split()
di={}
for i in n:
    di[i]=i[-1]
print(di)
'''
#4Write a program to accept a string of words and create a dictionary where each word is the key and
#its reverse is the value.
'''
n=input().split()
di={}
for i in n:
    di[i]=i[::-1]
print(di)
'''
##5Write a program to accept a string of words and create a dictionary where each word is the key and
#its lowercase form is the value.
'''
n=input().split()
di={}
for i in n:
    d=''
    for j in i:
        if 'A'<=j<='Z':
            d=d+chr(ord(j)+32)
        else:
            d+=jS  
    di[i]=d
print(di)    
'''                
#6Write a program to accept a string of words and create a dictionary containing each word and the number
#of vowels present in that word.
'''
n=input().split()
di={}
for i in n:
    d=''
    for j in i:
        if j in 'AEIOUaeiou':
            d=d+j    
    di[i]=d
print(di)
'''
#7Write a program to accept a string of words and create a dictionary containing each word and the
#number of consonants present in that word.
'''
n=input().split()
di={}
for i in n:
    d=''
    for j in i:
        if j not in 'AEIOUaeiou':
            d=d+j    
    di[i]=d
print(di)
'''
#8Write a program to accept a string of numbers separated by spaces and create a dictionary where
#each number is the key and its square is the value.
'''
n=input().split()
di={}
for i in n :
    di[i]=int(i)**2
print(di)
'''
#9Write a program to accept a string of numbers separated by spaces and create a dictionary where
#each number is the key and its double is the value.
'''
n=input().split()
di={}
for i in n :
    di[i]=int(i)*2
print(di)
'''
#10Write a program to accept a string of words and create a dictionary where the first character of
#each word is the key and the number of words starting with that character is the value
'''
n=input().split()
di={}

for i in n:
    count=0
    for j in i:
        if i[0]==j:
            count+=1
            
    di[i[0]]=count
print(di)    
'''        
#11Write a program to accept a string of words and create a dictionary where each word is the key and
#"Vowel" or "Consonant" is the value depending on whether the word starts with a vowel or consonant.
'''
n=input().split()
di={}
for i in n:
    
    fi=i[0]
    if fi in 'AEIOUaeiou':
        v='Vowel'
    else:
        v='Consonant'
    di[i]=v
print(di)    
'''
    
#12Write a program to accept a string containing student names and ages in pairs and create a dictionary
##where the name is the key and age is the value.
'''
n=input().split()
di={}
name=n[::2]
mark=n[1::2]
for i in range(len(name)):
    di[name[i]]=mark[i]
print(di)
'''
#13Write a program to accept a string of words and create a dictionary containing only those words whose
##length is greater than 4, with the word as the key and its length as the value.
'''
n=input().split()
di={}
l=0
for i in n:
    l=0
    if len(i)>=4:
        l=len(i)
        di[i]=l
print(di)
'''
#14Write a program to accept a string containing repeated words and create a dictionary where each word is
#the key and the number of characters in all its occurrences combined is the value.
#apple is apple good very good
#{'apple': 10, 'is': 2, 'good': 8, 'very': 4}
n=input().split()
di={}
for i in n:
    count=0
    for j in n:
        if i == j:
            count+=1
    di[i]=len(i)*count
print(di)    
                

