#WAP to print multiple of 3 as FIZZ , Multiple of 5 as BUZZ or both print FIZZBUZZ
'''
num=int(input('Enter a num '))
if num%5 == 0 and num% 3==0:
    print("FIZZBUZZ")
elif num%5==0:
    print("BUZZ")
elif num%3 == 0:
    print("FIZZ")
'''
#check given number is positive, Negative or Zero.
'''
num=int(input('Enter a num '))
if num==0:
    print("Zero")
elif num >0:
    
    print("Positive")
elif num <0:
    
    print("Negetive")    
'''
#chek the relation between 2 intiger
'''
num1=int(input('Enter a num '))
num2=int(input('Enter a num '))
if num1 == num2 :
    print("both number are equal")
elif num1 > num2:
    print(f"{num1} is grater then {num2}")
elif num1 < num2:
    print(f"{num2} is grater then {num1}")    
'''
# check given character is uppercase ,lowercase or digit
'''
char = input("Enter a character ")
if '0' <= char <= '9':
    print(F"{char} is digit")
elif 'A' <= char <= 'Z':
    print(F"{char} is Uppercase")
elif 'a' <= char <= 'z':
    print(F"{char} is lowercase")
'''
#check the current day and suggest user for some good lunch
'''
day=input("Enter today is which day : -").lower()
if day == 'sunday' or day == 'Wednusday':
    print("good lunch is Biriyani")
elif day == 'monday'or day == 'thusrsday':
    print("good lunch is roti and paneer curry")
elif day == 'Tuesday'or day == 'friday' or day == 'saturday' :
    print("good lunch is hostel food")
else:
    print("this is invalid day")
'''    
# Design Traffic Signal Lights with Suitable message
'''
light=input("Enter color of Traffic light : -").lower()
if light == 'red':
    print("Stop")
elif light == 'green':
    print("go")
elif light == 'yellow':
    print("To ready for go")
else:
    print("this is not a traffic light color ")
'''    
# find gratest of 3 number assuming all 3 are different integers

'''
num1=int(input('Enter a num '))
num2=int(input('Enter a num '))
num3=int(input('Enter a num '))
if num1 > num2 and num1 >num3:
    print(f"{num1} is greater ")

elif num2 > num1 and num2 >num3:
    print(f"{num2} is greater ")
elif num3 > num1 and num3 >num2:
    print(f"{num3} is greater ")
else:
    print("not in different number")
'''    
# find smallest of 3 number assuming all 3 are different
'''
num1=int(input('Enter a num '))
num2=int(input('Enter a num '))
num3=int(input('Enter a num '))
if num1 < num2 and num1 <num3:
    print(f"{num1} is smallest ")

elif num2 < num1 and num2 <num3:
    print(f"{num2} is smallest ")
elif num3 < num1 and num3 <num2:
    print(f"{num3} is smallest ")
else:
    print("not in different number")
'''
#1. Accept a number and check whether it is positive, negative, or zero.
'''
num=int(input('Enter a num '))
if num==0:
    print("Zero")
elif num >0:
    
    print("Positive")
elif num <0:
    
    print("Negetive") 
'''
#2. Accept a number and check whether it is a single-digit, two-digit, or three-digit number.
'''
num=int(input('Enter a num '))
if -9<= num <= 9:
    print("single-digit")
elif -99<=num<=-10 or 10<= num <=99:
    
    print("two-digit")
elif -999<=num <=-100 or 100<= num<= 999:
    
    print("three-digit")
'''
#3. Accept a person's age and determine whether they are a Child, Teenager, Adult, or Senior Citizen.
'''
age = int(input('Enter your age '))
if age < 13 :
    print("Child")
elif 13 <=age < 18:
    print("Teenager")
elif 18<= age < 60 :
    print('Adult')
else:
    print('Senior Citizen')
    
'''
#4. Accept a student's marks and display the grade:
#   * 90-100 → A
#   * 75-89 → B
#   * 60-74 → C
#   * 35-59 → D
#   * Below 35 → Fail
'''
mark = int(input('Enter your mark '))

if 90<= mark<=100:
    print('A')
elif 75<= mark<=89:
    print('B')
elif 60<= mark<=74:
    print('C')
elif 35<= mark<=59:
    print('D')
elif mark < 35 :
    print('Fail')
    
    
'''
#5. Accept a number and check whether it is positive even, positive odd, or negative.
'''
num=int(input('Enter a num '))
if num >0 and num%2==0:
    print("positive even")
elif num >0 and num%2 != 0:
    
    print("positive odd")
elif num <0:
    
    print("Negetive") 

'''
#6. Accept a month number (1-12) and display the month name.
'''
month_no = int(input('Enter month number '))
if month_no == 1:
    print('January')
elif month_no == 2:
    print('February')
elif month_no == 3:
    print('March')
elif month_no == 4:
    print('April')
elif month_no == 5:
    print('May')
elif month_no == 6:
    print('June')
elif month_no == 7:
    print('July')
elif month_no == 8:
    print('August')
elif month_no == 9:
    print('September')
elif month_no == 10:
    print('October')
elif month_no == 11:
    print('November')
elif month_no == 12:
    print('December')
else: 
    print('This is not a month number')
    
    
'''
#7. Accept a day number (1-7) and display the day name., Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday

'''
day_no = int(input('Enter day number '))
if day_no == 1:
    print('Monday')
elif day_no == 2:
    print('Tuesday')
elif day_no == 3:
    print('Wednesda')
elif day_no == 4:
    print('Thursday')
elif day_no == 5:
    print('Friday')
elif day_no == 6:
    print('Saturday')
elif day_no == 7:
    print('Sunday')    

    

'''
#8. Accept a character and check whether it is a vowel, consonant, or digit.
'''
char=input('Enter a character ').lower()
if char in 'aeiou':
    print(F"{char} is Vowel")
elif 'a' <= char <= 'z':
    print(F"{char} is consonant")
elif '0' <= char <= '9':
    print(F"{char} is digit")    
'''
#9. Accept a year and check whether it belongs to the 20th century, 21st century, or another century.
year=int(input("Enter a year "))
if 1901<= year <= 2000:
    print("this is 20th century")
elif 2001 <= year <= 2100:
    print("this is 21th century")
else:
    print('another century')
    
'''
10. Accept a temperature and display:
    * Cold
    * Warm
    * Hot
11. Accept two numbers and display the greater number or "Both are Equal".
12. Accept three numbers and display the largest number.
13. Accept a salary and calculate the employee category:
    * Below 20,000 → Low
    * 20,000 to 50,000 → Medium
    * Above 50,000 → High
14. Accept a percentage and determine the class:
    * Distinction
    * First Class
    * Second Class
    * Pass Class
    * Fail
15. Accept a number and determine whether it is:
    * Less than 0
    * Between 0 and 50
    * Between 51 and 100
    * Greater than 100
16. Accept a mobile battery percentage and display:
    * Low
    * Medium
    * High
    * Fully Charged
17. Accept the amount of purchase and display discount category.
18. Accept internet speed and classify as:
    * Slow
    * Average
    * Fast
    * Very Fast
19. Accept a person's height and classify as:
    * Short
    * Average
    * Tall
20. Accept a person's BMI value and classify it.
21. Accept a number (1-7) and display the corresponding weekday.
22. Accept a number (1-12) and display the corresponding month.
23. Accept a traffic signal color and display:
    * Red → Stop
    * Yellow → Ready
    * Green → Go
24. Accept a fruit name and display its color category.
25. Accept a programming language name and display its category (Compiled/Interpreted).
26. Accept marks and display Pass, Fail, or Distinction.
27. Accept electricity units consumed and display the bill slab category.
28. Accept a package amount and display Bronze, Silver, Gold, or Platinum membership.
29. Accept an exam score and display performance level.
30. Accept a customer's age and suggest:
    * Kids Ticket
    * Student Ticket
    * Adult Ticket
    * Senior Citizen Ticket
31. Accept a character and determine whether it is:
    * Uppercase Letter
    * Lowercase Letter
    * Digit
    * Special Character
32. Accept a year and determine whether it is:
    * Leap Year
    * Century Year
    * Normal Year
33. Accept three numbers and display:
    * Largest
    * Smallest
    * Equal
34. Accept a percentage and determine scholarship eligibility category.
35. Accept login attempts and display security level.
36. Accept a movie ticket price and display ticket type.
37. Accept a cricket score and classify batting performance.
38. Accept a water level percentage and display tank status.
39. Accept a train speed and classify the train type.
40. Accept a product rating and display:
    * Excellent
    * Good
    * Average
    * Poor
'''    
