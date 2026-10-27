#1print * pattern in the form of column using both while and for loop
'''
n=int(input())

i=0
while i<n:
    print('*')
    i+=1


for i in range(n):
    print("*")
'''
#2print * pattern in the form of row using both while and for loop
'''
n=int(input())

i=0
while i<n:
    print('*',end=" ")
    i+=1
for i in range(n):
    print("*",end=" ")
'''
#3print numbers starting from 1 to n in the form of column
'''
n=int(input())
i=1
while i<=n:
    print(i,'*')
    i+=1
for i in range(1,n+1):
    print(i,'*')
'''
#4print numbers starting from 1 to n in the form of row
'''
n=int(input())
i=1
while i<=n:
    print(i,end=' ')
    i+=1
for i in range(1,n+1):
    print(i,end=' ')
'''
#5print the number from 5 to n+5 in the forn of column
'''
n=int(input())
i=5
while i<n+5:
    print(i)
    i+=1
'''
'''
n=int(input())
for i in range(5,n+5):
    print(i)
'''
#6print A B C D E in form of column
'''
n=int(input())
for i in range(n):
    print(chr(65+i),end=" ")
'''
#7print Z Y X W V U IN the form of row
'''
for i in range(90,84,-1):
    print(chr(i),end=" ")
'''
#8 printZ *
'''
for i in range(90,84,-1):
    print(chr(i),end=" ")
    
    if i==85:
        break
    print("*",end=' ')
'''
#print uppercase alphabets
'''
n=int(input())
if 65<=n<=90:
    for i in range(90,n+1,-1):
        print(chr(i),end=" ")
else:
    print(f'{n} not contains any uppercase alphabet')
'''
#
'''
n=int(input())
i=0
while i<n:
    print('* * * * *')
    i+=1
'''    
#
'''
n=int(input())
i=0
while i<n:
    print(f'{i*' * '}')
    i+=1
for i in range(n):
    print(f'{i*' * '}')
'''
# 2d patten
#
'''
n=int(input())
for i in range(1,n+1):
    j=1
    for j in  range(1,n+1):
        print(i,j,sep='',end=' ')
    print()    
'''
#print base pattern as *
'''
n=int(input())
for i in range(1,n+1):
    j=1
    for j in  range(1,n+1):
        print('*',sep='',end=' ')
    print()
'''
#
'''
n=int(input())
for i in range(1,n+1):
    j=1
    for j in  range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print(i,j,sep='',end=' ')
        else:
            print('  ',sep='',end=' ')
            
    print()
'''
#
'''
n=int(input())
for i in range(1,n+1):
    j=1
    for j in  range(1,n+1):
        if i==n or j==1 or i==j:
            print('*',sep='',end=' ')
        else:
            print(' ',sep='',end=' ')
            
    print()
'''
#
'''
n=int(input())
for i in range(1,n+1):
    j=1
    for j in  range(1,n+1):
        if i==1 or j==n or i==j:
            print('*',sep='',end=' ')
        else:
            print(' ',sep='',end=' ')
            
    print()
'''
#
'''
n=int(input())
for i in range(1,n+1):
    j=1
    for j in  range(1,n+1):
        if i==3  or (i==2 and j==2) or (i==1 and j==3) or (i==2 and j==4):
            print('*',sep='',end=' ')
        else:
            print(' ',sep='',end=' ')
            
    print()

'''
#
'''
n=int(input())
for i in range(1,n+1):
    j=1
    for j in  range(1,n+1):
        if j==1 or j==n  or i==n or i==1 :
            print(j,sep='',end=' ')
            
        else:
            print(' ',sep='',end=' ')
            
    print()
'''
#
'''
n=int(input())
for i in range(1,n+1):
    j=1
    for j in  range(1,n+1):
        if j==1 or j==n  or i==n or i==1 :
            print(i,sep='',end=' ')
            
        else:
            print(' ',sep='',end=' ')
            
    print()
'''
#
'''
n=int(input())
for i in range(1,n+1):
    j=1
    for j in  range(1,n+1):
        if j==1 or j==n  or i==n or i==1 :
            print(i+j,sep='',end='  ')
            
        else:
            print(' ',sep='',end='  ')
            
    print()
'''
#print hallow square from a base patten where the patten should be column number with 'B'
'''
n=int(input())
for i in range(1,n+1):
    j=1
    for j in  range(1,n+1):
        if j==1 or j==n  or i==n or i==1 :
            print(j,'B',sep='',end='  ')
            
        else:
            print(' ',sep='',end='   ')
            
    print()
'''
# WAP to print the hallow square where each row represent differant alphabate

##n=int(input())
##for i in range(1,n+1):
##    
##    for j in  range(1,n+1):
##        if j==1 or j==n  or i==n or i==1 :
##            print(chr(64+i),sep=' ',end='  ')
##            
##        else:
##            print(' ',sep='',end='  ')
##            
##    print()
#WAP to print the hallow square where each row represent differant alphabate
'''
n=int(input())
for i in range(1,n+1):
    j=1
    for j in  range(1,n+1):
        if j==1 or j==n  or i==n or i==1 :
            print(chr(64+j),sep='',end='  ')
            
        else:
            print(' ',sep='',end='  ')
            
    print()
'''
'''
n=int(input())
for i in range(1,n+1):
    
    for j in  range(1,n+1):
        s=i*j
        if j==1 or j==n  or i==n or i==1 :
            if 1<=s<=9 :
                print(f'{s}',end='  ')
            else:
                print(f'{s}',end=' ')
            
        else:
            print('  ',end=' ')
            
            
    print()
'''
#1hallow inverted right angled triangel use of '*'
'''
n=int(input())
for i in range(1,n+1):
    j=1
    for j in  range(1,n+1):
        if i==1 or j==n  or i==j :
            print('*',sep='',end='  ')
            
        else:
            print(' ',sep='',end='  ')
            
    print()
'''
#2hallow inversly right angled triangel use of '*'
'''
n=int(input())
for i in range(1,n+1):
    j=1
    for j in  range(1,n+1):
        if i==1 or j==1   or i+j==n+1 :
            print('*',sep='',end='  ')
            
        else:
            print(' ',sep='',end='  ')
            
    print()
'''
#3hallow inversly left angled traingel
'''
n=int(input())
for i in range(1,n+1):
    j=1
    for j in  range(1,n+1):
        if i==n or j==n   or i+j==n+1 :
            print('*',sep='',end='  ')
            
        else:
            print(' ',sep='',end='  ')
            
    print()
'''
#4hallow clock
'''
n=int(input())
for i in range(1,n+1):
    j=1
    for j in  range(1,n+1):
        if i==1 or i==n   or i+j==n+1 or i==j :
            print('*',sep='',end='  ')
            
        else:
            print(' ',sep='',end='  ')
            
    print()
'''
# hallow butterfly
'''
n=int(input())
for i in range(1,n+1):
    j=1
    for j in  range(1,n+1):
        if j==1 or j==n   or i+j==n+1 or i==j :
            print('*',sep='',end='  ')
            
        else:
            print(' ',sep='',end='  ')
            
    print()
'''
#
'''
n=int(input())
for i in range(1,n+1):
    j=1
    for j in  range(1,n+1):
        if i==1 or i==n   or i+j==n+1 or i==j :
            print('*',sep='',end='  ')
        elif i<j and i+j <=n+1:
            print('*',sep='',end='  ')
            
            
        else:
            print(' ',sep='',end='  ')
            
    print()
'''
#
'''
n=int(input())
for i in range(1,n+1):
    j=1
    for j in  range(1,n+1):
        if i==1 or i==n   or i+j==n+1 or i==j :
            print('*',sep='',end='  ')
        elif (i>j and i+j >=n+1) or (i<j and i+j <=n+1) :
            print('*',sep='',end='  ')
            
            
        else:
            print(' ',sep='',end='  ')
            
    print()
'''
#
'''
n=int(input())
for i in range(1,n+1):
    j=1
    for j in  range(1,n+1):
        if j==1 or j==n   or i+j==n+1 or i==j :
            print('*',sep='',end='  ')
        elif j<i and i+j<=n+1 or i<j and i+j>=n+1:
            print('*',sep='',end='  ')
            
            
            
        else:
            print(' ',sep='',end='  ')
            
    print()
'''
#
'''
n=int(input())
s=(n+1)/2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if i==s or j==s or i+j==n+1 or i==j or(j==1 and i<s)or(i==1 and j>s)or(j==n and i>s)or(i==n and j<s):
            print('*',sep='',end='  ')
        elif i<s and i>j and i+j<=n+1:
            print('*',sep='',end='  ')
        elif j>s and i<j and i+j<=n+1 :
            print('*',sep='',end='  ')
        elif i>s and i<j and i+j>=n+1 :
            print('*',sep='',end='  ')
        elif j<s and i>j and i+j>=n+1 :
            print('*',sep='',end='  ')      
        else:
            print(' ',sep='',end='  ')
            
    print()
'''
#
'''
n=int(input())
s=(n+1)/2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if i==s or j==s or i+j==n+1 or i==j or(j==1 and i>s)or(i==1 and j<s)or(j==n and i<s)or(i==n and j>s):
            print('*',sep='',end='  ')
        elif j<s and i<j and i+j<=n+1 :
            print('*',sep='',end='  ')
        elif i>s and i>j and i+j<=n+1 :
            print('*',sep='',end='  ')
        elif j>s and i>j and i+j>=n+1 :
            print('*',sep='',end='  ')
        elif i<s and i<j and i+j>=n+1 :
            print('*',sep='',end='  ')              
        else:
            print(' ',sep='',end='  ')
            
    print()
'''
# print('A')
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if (i==1 and j==s-2) or (i==1 and j==s+3):
            print(' ',sep='',end='')
        elif j==s-2 or j==s+2 or (i==s and s-2<=j<=s+2) or (i==1 and s-2<=j<=s+2) :
            print('*',sep='',end='  ')
                      
        else:
            print(' ',sep='',end='  ')
            
    print()
'''
#print('B')
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if (j==n and i==1)or(i==s and j==n)or(i==n and j==n):
            print(' ',sep='',end='')
            
        elif  j==1 or (i==n and j<n-1) or (i==1 and j<n-1) or (i==s and j<n-1) or j==n :
            print('*',sep='',end='')
            
                      
        else:
            print(' ',sep='',end='')
            
    print()
'''
#print('C')
'''

n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if (j==1 and i==1)or(i==n and j==1):
            print(' ',sep='',end='')
            
        elif  j==1 or i==1 or i==n :
            print('*',sep='',end='')
            
                      
        else:
            print(' ',sep='',end='')
            
    print()
'''    
# print('E')
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if j==1 or i== 1 or i==n or (i==s and j<n)   :
            print('*',sep='',end='')
                      
        else:
            print(' ',sep='',end='')
            
    print()    
'''
#print('f')
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if j==1 or i== 1  or (i==s and j<n)   :
            print('*',sep='',end='')
                      
        else:
            print(' ',sep='',end='')
            
    print()
'''
#print('H')
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if j==1 or j== n  or i==s    :
            print('*',sep='',end='')
                      
        else:
            print(' ',sep='',end='')
            
    print()
'''
#print('I')
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if (i==1 and 2<j<n-1) or (i== n and 2<j<n-1)  or j==s    :
            print('*',sep='',end='')
                      
        else:
            print(' ',sep='',end='')
            
    print()
'''
#print('J')
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if i==n and j==1:
            print(' ',sep='',end='')
            
        elif i==1  or (i== n and j<s)or j==s or (j==1 and i>s)    :
            print('*',sep='',end='')
                      
        else:
            print(' ',sep='',end='')
            
    print()
'''   
#print('K')
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if  j==s or (j==i and i>s) or ((j+i==n+1 and j>s))    :
            print('*',sep='',end='')
                      
        else:
            print(' ',sep='',end='')
            
    print()    
'''
#print('L')
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if  j==1 or i==n    :
            print('*',sep='',end=' ')
                      
        else:
            print(' ',sep='',end=' ')
            
    print() 
'''
#print('M')
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if  j==1 or j==n or (i==j and j<=s) or (i+j==n+1 and j>=s)    :
            print('*',sep='',end=' ')
                      
        else:
            print(' ',sep='',end=' ')
            
    print()
'''
#print('N')
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if  j==1 or j==n or i==j    :
            print('*',sep='',end=' ')
                      
        else:
            print(' ',sep='',end=' ')
            
    print()
'''
#print('O')
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if (i==1 and j==1)or(j==1 and i==n)or(i==n and j==n)or(i==1 and j==n):
            print(' ',sep='',end=' ')
            
        elif  j==1 or j==n or i==1 or i==n    :
            print('*',sep='',end=' ')
                      
        else:
            print(' ',sep='',end=' ')
            
    print()
'''    
#print('P')
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if (i==1 and j==n) or (i==s and j==n):
            print(' ',sep='',end=' ')
            
        elif  j==1 or i==1 or i==s or (j==n and i<s)    :
            print('*',sep='',end=' ')
                      
        else:
            print(' ',sep='',end=' ')
            
    print()
'''
#print('R')
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if (i==1 and j==n) or (i==s and j==n):
            print(' ',sep='',end=' ')
            
        elif  j==1 or i==1 or i==s or (j==n and i<s)or(i==j and j>s)    :
            print('*',sep='',end=' ')
                      
        else:
            print(' ',sep='',end=' ')
            
    print()
'''    
# 'D'
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if (j==n and i==1)or(i==n and j==n):
            print(' ',sep='',end='')
            
        elif  j==1 or i==n  or i==1   or j==n :
            print('*',sep='',end=' ')
            
                      
        else:
            print(' ',sep='',end=' ')
            
    print()
'''    
# 'S'
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if (j==1 and i==1)or(i==s and j==1)or(i==s and j==n)or(i==n and j==n):
            print(' ',sep='',end=' ')
            
        elif  i==1 or i==n or i==s or (j==1 and i<=s)or (j==n and i>=s) :
            print('*',sep='',end=' ')
            
                      
        else:
            print(' ',sep='',end=' ')
            
    print()
'''
#'T'
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if  i==1 or j==s    :
            print('*',sep='',end=' ')
                      
        else:
            print(' ',sep='',end=' ')
            
    print()
'''
#'U'
'''
n=int(input())
for i in range(1,n+1):
    for j in  range(1,n+1):
        if (j==1 and i==n)or(i==n and j==n):
            print(' ',sep='',end=' ')
            
        elif  j==1 or i==n or j==n  :
            print('*',sep='',end=' ')
            
                      
        else:
            print(' ',sep='',end=' ')
            
    print()
'''
#'W'
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if  j==1 or j==n or (i==j and j>=s) or (i+j==n+1 and j<=s)    :
            print('*',sep='',end=' ')
                      
        else:
            print(' ',sep='',end=' ')
            
    print()
'''
#'X'
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if  i==j  or i+j==n+1:
            print('*',sep='',end=' ')
                      
        else:
            print(' ',sep='',end=' ')
            
    print()
'''
#'Y'
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if  (i==j and i<=s ) or (i+j==n+1 and i<=s) or (j==s and i>=s)    :
            print('*',sep='',end=' ')
                      
        else:
            print(' ',sep='',end=' ')
            
    print()
'''
#'Z'
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if  i==1 or i==n or i+j==n+1:
            print('*',sep='',end=' ')
                      
        else:
            print(' ',sep='',end=' ')
            
    print()
'''    
#'G'
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if (j==1 and i==1)or(i==n and j==1)or (i==n and j==n)or(i==1 and j==n) :
            print(' ',sep='',end=' ')
            
        elif  j==1 or i==n or (j==n and i>s) or (i==s and j>=s)or i==1 or (j==n and i==2)  :
            print('*',sep='',end=' ')
            
                      
        else:
            print(' ',sep='',end=' ')
                   
    print()
'''
# 'Q'
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,n+1):
        if (j==1 and i==1)or(i==n-1 and j==1)or(i==1 and j==n-1) :
            print(' ',sep='',end=' ')
            
        elif  (j==1 and i<n) or (i==n-1 and j<n) or (j==n-1and i<n)or  (i==1 and j<n)or(i==j and j>=s)  :
            print('*',sep='',end=' ')
            
                      
        else:
            print(' ',sep='',end=' ')
                   
    print()
'''
#'V'
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,2*n):
        if  i==j or i+j==2*n :
            print('*',sep='',end=' ')
            
                      
        else:
            print(' ',sep='',end=' ')
                   
    print()
'''
#'A'
'''
n=int(input())
s=(n+1)//2
for i in range(1,n+1):
    for j in  range(1,2*n):
        if  i+j==n+1 or j-i==n-1 or (i==s and s<j<(2*n)-s):
            print('*',sep='',end=' ')             
        else:
            print(' ',sep='',end=' ')
                   
    print()

'''

n=int(input())
for i in range(1,n+1):
    

    for j in  range(1,n+1):
        
        print(i,j,sep='',end='  ')
            
    print()
    print()




    
