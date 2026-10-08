#1
'''
fruit=['apple','mango','banana']
for var in fruit:
    print(var)
'''
#
'''
vegetable=eval(input("Enter some vegetables name "))
for var in vegetable:
    print(var)
'''
#
'''
a=['apple','mango','banana',1,1.3,True]
print(a)
l=[]
for var in a:
    if type(var) in (int,float,bool,complex):
        l.append(var)
print(l)
'''
#
'''
a=['apple','mango','banana',1,1.3,True]
print(a)
l=0
for var in a:
    if type(var) in (int,float,bool,complex):
        l+=var
print(l)        
'''
#Toggle a string
'''
a=input()
s=''
for var in a:
    if 'A' <= var <= 'Z' :
        s+=var.lower()
    elif 'a'<= var <='z':
        s+=var.upper()
    else:
        s+=var
print(s)
'''
#Extract only alphabate
'''
a=input()
s=''
for var in a:
    if 'A' <= var <= 'Z' :
        s+=var
    elif 'a'<= var <='z':
        s+=var
print(s)        
'''
#
'''
a=input()
s=()
for var in a:
    s=s+(var,)
print(s)
'''
#
'''
a=input()
s=()
for var in a:
    if var not in s:
        s=s+(var,)
print(s)
'''
#input 1
#print one

n=int(input("Enter a number "))
m=n
ones = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine "]
teens = ["ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
tens = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
cent=["","","","hundred ","thousand "]        
count=0
sum=0
while n>0:
    ld=n%10
    count+=1    
    sum=sum+ld
    n//=10   
s=m%10    
md=sum-ld-s
w=m//10
md3=w%10
md2=sum-s-ld-md3
if count==1:
    print(ones[m])
elif count==2:
    if ld==1:
        print(teens[m-10])
    else:
        print(tens[ld]+ones[s])
elif count == 3:
    if md ==1:
        print(ones[ld]+cent[count]+teens[s])
    else:    
        print(ones[ld]+cent[count]+tens[md]+ones[s])
elif count == 4:
    if md2 >0:
        h_part=(ones[md2]+"hunderat ")
    else:
        h_part=""
        
    if md3 ==1:
        print(ones[ld]+cent[count]+h_part+teens[s])
    else:    
        print(ones[ld]+cent[count]+h_part+tens[md3]+ones[s])
elif m == 10000 :
    print(teens[ld-1]+cent[count-1])
    










        
    




    
    

    
