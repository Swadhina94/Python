#Find the vowel in a message using recursion.
'''
def rec(n,vowel='',i=0):
    if i>=len(n):
        return vowel
    elif n[i] in 'AEIOUaeiou':
        vowel+=n[i]
    return rec(n,vowel,i+1)
print(rec(input('Enter a massage')))
'''

# factorial
'''
def fact(n,fac=1):
    if n<=0:
        return fac
    fac=fac*n
    return fact(n-1,fac)
    
print(fact(int(input("Enter: "))))
'''
# check homo or hetro
'''
def fun(n,i=0):
    if i>=len(n):
        return 'home'
    elif type(n[0])!=type(n[i]):
        return 'hetro'
   
    return fun(n,i+1)
print(fun(eval(input())))
'''
# check give vowels from a message is palidrome or not
'''
def pal (n,vowels='',i=0):
    if i>=len(n):
        if vowels==vowels[::-1]:
            return 'palidrome'
        else:
            return 'not'
    elif n[i] in 'AEIOUaeiou':
        vowels+=n[i]
    return pal(n,vowels,i+1)
print(pal(input("Enter")))
'''
# revese
'''
def rev(n,r=0):
    if n==0:
        return r
    return rev(n//10,r*10+n%10)
print(rev(int(input("Enter a number"))))
'''
def fun(n,pro=1,i=0):
    if i==len(n):
        return pro
    return fun(n,pro*n[i],i+1)
print(fun(eval(input("Enter a list"))))



















        
    
