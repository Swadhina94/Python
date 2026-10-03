#a='apple is red'
#o/p:-{'apple':5,'is':2, 'red':3}
'''
a= input().split()
d={}
i=0
while i<len(a):
    d[a[i]]=len(a[i])
    i+=1
print(d)
'''
#input='apple carrot onion cucumber'
#output= {'apple':ae,}
'''
a= input().split()#['apple','carrot','onion','cucumber']
d={}
i=0

while i<len(a):#lenth is 4 so while loop is happening 4 times
    j=0
    vowels=''
    while j<len(a[i]):# i=0 so a[0]=apple , length of apple is 5 so 5 time while loop are repite 
        if a[i][j] in 'AEIOUaeiou':#j=0 so a[0][0]= a , a in 'aeiou' 
            vowels+= a[i][j] # so a is add inside of vowels='a' 
        j+=1    # then j value is incresed 1 so j=1 then again repite it .
    d[a[i]]=vowels #vowels='ae' and d[a[i]]= 'apple' so 'apple':'ae'
    i+=1 # then incresed i value then repite in last.
print(d)#print all the value of dic in all itration
'''
#nput='apple carrot onion cucumber'
#output= {'apple':}
'''
a=['apple','carrot','onion','cucumber']
d={}

i=0

while i<len(a):#lenth is 4 so while loop is happening 4 times
    j=0
    count=0
    while j<len(a[i]):# i=0 so a[0]=apple , length of apple is 5 so 5 time while loop are repite 
        if a[i][j] == 'a' or a[i][j] == 'A':#j=0 so a[0][0]= a , 'a' == 'a' 
            count+= 1 # so count 1 
        j+=1    # then j value is incresed 1 so j=1 then again repite it .
    d[a[i]]=count #count='1' and d[a[i]]= 'apple' so 'apple':1
    i+=1 # then incresed i value then repite in last.
print(d)
'''
'''
a= input().split()
d={}
i=0
while i<len(a):
    j=0
    p=''
    b=''
    while j<len(a[i]):
        if a[i][j] in p:
            b+= a[i][j]
        else:
            p+=a[i][j]
        j+=1    
    d[a[i]]= b
    i+=1 
print(d)
'''
'''
a= input().split()
d={}
i=0
while i<len(a):
    j=0
    p=''
    b=''
    while j<len(a[i]):
        if a[i][j] in p:
            b+= a[i][j]
        
        else:
            p+=a[i][j]
        j+=1    
    d[a[i]]= p
    i+=1 
print(d)

'''
#apple orange banana ppe pineapple
#{'p': 'ppe', '': 'orange', 'ana': 'banana', 'ppe': 'pineapple'}
'''
a= input().split()
d={}
i=0
while i<len(a):
    j=0
    p=''
    b=''
    while j<len(a[i]):
        if a[i][j] in p:
            b+= a[i][j]
        else:
            p+=a[i][j]
        j+=1    
    d[b]= a[i] 
    i+=1 
print(d)
'''








