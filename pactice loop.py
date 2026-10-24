#1.Second Largest Digit
#Find the second largest digit in a number.
#Example: 58392 → 8
'''
n=int(input("Enter a number "))
lar1=0
lar2=0
s=0
r=0
while n>0:
    ld=n%10
    if lar1 <=ld :
        lar1=ld
    else:
        s=ld
        r=r*10+ld             
    n=n//10
while r >0:
    l=r%10
    if lar2 < l:
        lar2=l
    r=r//10
print(f"Second largest number is {lar2}")    
'''
n = int(input("Enter a number: "))

largest = -1
second = -1

while n > 0:
    digit = n % 10

    if digit > largest:
        second = largest
        largest = digit

    elif digit > second and digit != largest:
        second = digit

    n = n // 10

if second == -1:
    print("No second largest number is present")
else:
    print("Second largest digit is", second)
#2.Remove Repeated Digits
#Print only the digits that occur once.
#Example: 112345533 → 24 
#Frequency of Each Digit


#3.Count how many times every digit 0–9 occurs.
#Example: 1223341
#Output: 1 → 2 times, 2 → 2 times, 3 → 2 times, 4 → 1 time
'''
n=int(input("Enter a number "))
a=0
rev=0
while n>0:
    ld=n%10
    if ld != a:
        rev=rev*10+ld
        a=ld
    n=n//10
print (rev)
'''
