##1. Write a program to check whether a given number is prime or not using for-else.
'''
n=int(input("enter a number "))
s=0
for i in range(1,n):
    if n%i==0:
        s+=1
if s==1:
    print("prime number ")
else:
    print("not prime number ")
'''    
##2. Write a program to find whether a number is divisible by any number from 2 to n-1.
'''
n=int(input("enter a number "))
for i in range(2,n):
    if n%i==0:
        print(i,end=" ")
'''        
##3. Write a program to search for a given element in a list using for-else.
'''
col=eval(input())
n=input()
for i in range(len(col)):
    if n == col[i]:
        print(i)
'''     
##4. Write a program to check if a character exists in a string using for-else.
'''
n=input()
s=input()
for i in range(len(n)):
    if s == n[i]:
        print("exists")
        break
else:
    print('not exists')
'''    
##5. Write a program to find the first even number in a list and stop using break.
'''
n=eval(input())
for i in n:
    if i%2==0:
        print(i)
        break
'''    
##6. Write a program to find the first odd number greater than 50 in a list.
'''
n=eval(input())
for i in n:
    if i%2!=0 and i>50:
        print(i)
        break
'''        
##7. Write a program to check whether all elements in a list are positive using for-else.
'''
n=eval(input())
for i in n:
    if i<0:
        print('Negative is present')
        break
else:
    print("all elements in a list are positive")
'''        
##8. Write a program to check whether a string contains a digit.
'''
n=input()
for i in n:
    if i in '123456789' :
        print("string contains a digit")
        break
else:
    print("string not contains a digit")
'''    
##9. Write a program to check whether a string contains a vowel.
'''
n=input()
for i in n:
    if i in 'AEIOUaeiou' :
        print("string contains a vowel")
        break
else:
    print("string not contains a vowel")
'''    
##10. Write a program to check whether a list contains duplicate values.
'''
n=eval(input())
dup=[]
for i in range(len(n)):
    if n[i] not in dup:
        dup.append(n[i])
if len(n)==len(dup):
    print("list not contains duplicate values")
else:
    print("list contains duplicate values")
'''    
##11. Write a program to find the first multiple of 7 between 1 and 100.
'''
for i in range(1,100):
    if i%7==0:
        print(i)
        break
'''        
##12. Write a program to find the first number divisible by both 3 and 5 in a list.
'''
n=eval(input())
for i in range(len(n)):
    if n[i]%3==0 and n[i]%5==0:
        print(n[i])
        break
'''        
##13. Write a program to check whether a number is a perfect square using for-else.
'''
n=int(input())
for i in range(1,n+1):
    if i*i==n:
        print("perfect squar")
        break
else:
    print("not perfect squar")
'''    
##14. Write a program to check whether a number is composite.
'''
n=int(input("enter a number "))
s=0
for i in range(1,n):
    if n%i==0:
        s+=1
if s==1:
    print("prime number ")
else:
    print("composite number ")
'''    
##15. Write a program to find the first negative number in a list.
'''
n=eval(input())
for i in n:
    if i<0:
        print(i)
        break
'''        
##16. Write a program to search for a specific word in a sentence.
##n= input("Enter a sentence").split()
##a=input("Enter a word ")
##for i in n:
##    if i == a:
##        print(i)
##        break
##
##17. Write a program to check whether all characters in a string are alphabets.
##
##18. Write a program to check whether a string contains any special character.
##
##19. Write a program to find the first vowel in a string.
##
##20. Write a program to find the first uppercase letter in a string.
##
##21. Write a program to check whether all numbers in a list are even.
##
##22. Write a program to check whether all numbers in a list are odd.
##
##23. Write a program to check if a list contains zero.
##
##24. Write a program to search for a student's roll number in a list.
##
##25. Write a program to find the first number greater than 100 in a list.
##
##26. Write a program to check whether a number is divisible by 11.
##
##27. Write a program to find the first character repeated in a string.
##
##28. Write a program to search for a city name in a list.
##
##29. Write a program to check whether all characters are lowercase.
##
##30. Write a program to find the first consonant in a string.
##
##31. Write a program to check whether a number is an Armstrong number using for-else.
##
##32. Write a program to find the first palindrome word in a list.
##
##33. Write a program to search for a product ID in a list.
##
##34. Write a program to check whether a list contains any negative numbers.
##
##35. Write a program to find the first number divisible by 9 in a list.
##
##36. Write a program to check whether all values in a list are unique.
##
##37. Write a program to find the first number ending with digit 5.
##
##38. Write a program to search for a specific character in a string.
##
##39. Write a program to check whether a string contains spaces.
##
##40. Write a program to find the first word whose length is greater than 5.
##
##41. Write a program to check whether a number is a factor of another number.
##
##42. Write a program to find the first leap year in a given list of years.
##
##43. Write a program to check whether all elements are integers.
##
##44. Write a program to search for a given age in a list of ages.
##
##45. Write a program to find the first number divisible by 13.
##
##46. Write a program to check whether a string contains only digits.
##
##47. Write a program to find the first prime number in a list.
##
##48. Write a program to search for a book title in a list.
##
##49. Write a program to check whether all numbers are greater than zero.
##
##50. Write a program to find the first number that is both even and greater than 50.
##
##51. Write a program to find the first prime number between 100 and 200.
##
##52. Write a program to check whether a list contains at least one palindrome number.
##
##53. Write a program to find the first repeated element in a list.
##
##54. Write a program to check whether all words in a list start with a vowel.
##
##55. Write a program to search for a substring inside a string using for-else.
