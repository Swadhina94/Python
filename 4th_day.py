#apple is a fruit
#{'apple': 'elppa', 'is': 'si', 'a': 'a', 'fruit': 'tiurf'}
'''
n=input().split()
di={}
for i in n:
    di[i]=i[::-1]
print(di)    
'''


#apple is red and sweet
#{'apple': 5, 'is': 2, 'red': 3, 'and': 3, 'sweet': 5}
'''
n=input().split()

di={}
i=0
for i in n:
    di[i]=len(i)
print(di)    
'''
#apple is red and sweet
#{'apple': 'APPLE', 'is': 'IS', 'red': 'RED', 'and': 'AND', 'sweet': 'SWEET'}
'''
n=input().split()
di={}

for i in n:
    d=''
    for j in i:
      if 'a'<=j<='z' :
           d+=chr(ord(j)-32)      
    di[i]=d
print(di)    
'''
#ap456lwer45
#{4:fact4, 5:fact5, 6:fact6 , 4:fact4 ,5:fact5}
'''
n=input().split()
li=''
dic={}
for i in n:
    if i.isdigit():
        continue
    else:
        print("start i",i)
        for j in i:
            print("start j",j)
            if '0'<=j<='9' :
                li+=j
                print("strting li",li)
            else:
                n.append(li)
                li=''
        li+=j
print(n)
'''            
            
        
        
            

##n=input()
##di=[]
##for i in n:
##    di[i]= chr(ord(i)-32)
##
##print(di)    
##n=input().split()
##
##di={}
##for i in m:
##    di[i]=i**3
##print(di)
##i = 1
##d = {}
##n = input()
##while i < n :
##    key =int(n[0::2])
##    val = int(n[1::2])
##    d[key] = val
##    i+=1
##print(d)    



    
    

    
        
        
