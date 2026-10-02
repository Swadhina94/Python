#Enter a number and find their bainary number
n= int(input())
s=""
while n>0:
    ld=n%2
    s=str(ld)+s
    n=n//2
print(s)


    
  
