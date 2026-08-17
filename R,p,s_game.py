# RPS Game
'''
print("               Welcome the Game ")
print("---------------Start Gam--------------")

print("             ")
print("Winning the Game rule is ")
print("-->Rock breaks or crushes scissors. ")
print("-->Scissors cut paper.")
print('-->Paper covers or wraps rock.')
print("The standard game is designed for 2 player.")
print("Pair players up into 1-on-1 matches.")
import random
coll=["rock", "paper", "scissors"]
computer= random.choice(coll)
print("        ")
name= input("Enter your name :-")
print("                  ")
player=input("Chose the Move like (rock , paper ,scissors )  ").lower()
if computer == player:
    print("Match Draw")
elif (player== 'rock' and computer == 'scissors')  or (player=='paper' and computer == 'rock')or (player=='scissors' and computer == 'paper') :
    print(f"{name} Win the Game")
else:
    print(f"{name} loss the Game")
'''

# develop a program for love caiculator
'''
import random
user = input("Enter your name ")
crush= input("Enter your crush name ")
percent = random.uniform(0,100)
if percent > 85:
    print(percent)
    print("Best couple in the World ")
elif 70 <=percent<=85:
    print(percent)
    print("Lovely couple")
elif 50<= percent <= 69:
    print(percent)
    print("Try to another girl")
else:
    print(percent)
    print("To aaj hi brack up kar")
'''    
#predict the favourite keyword of your bestie
'''
import keyword
import random
word = random.choice(keyword.kwlist)
bestie = input("oye bestie ake keyword likho ")
print(word)
if bestie == word :
    print("We think same")
'''
# check the type of triangle
#Equilateral = 3 side are equal
#Isoscales = 2 sides are equle
#Scalene 3 sides are different
'''
side = eval (input("Enter 3 side value  of triangle "))

b=int(side[0])
c=int(side[1])
d=int(side[2])             
            
if b == c and b == d:
    print("Equilateral = 3 side are equal")
elif b== c or b == d or c == d:
    print('Isoscales = 2 sides are equle')
else:
    print("Scalene 3 sides are different")
'''

'''
month_no = input('Enter month name ').lower()
if month_no in ['march','april','may','june']:
    print('Summer season')
elif month_no in ['july','august','september','october']:
    print('Rain')
elif month_no in ['november','december','january','february']:
    print('winter')
else:
    print("Not a month")
'''   
'''
month = input('Enter month name ').lower()

match month:
    case 'march' :
        print('Summer season')
    case  'april':
        print('Summer season')
    case 'may':
        print('Summer season')

    case 'june':
        print('Summer season')
    case 'july' | 'august' | 'september' | 'october':
        print('Rain season')
        
    case 'november' | 'december' | 'january' | 'february':
        print('winter season')
        
    case _:

        print("Not a month")
'''       

'''
day_no = int(input('Enter day number '))
match day_no:
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesda')        
    case 4:
        print('Thursday')
    case 5:
        print('Friday')
    case 6:
        print('Saturday')
    case 7:
        print('Sunday')
    case _:
              
        print("NOt a day")
'''              
num = eval(input("Enter 4 different integer number "))
a= int(num[0])
b= int(num[1])
c=int(num[2])
d= int(num[3])
if a > b and a> c and a> d:
    print(f"{a} is largest ")
elif b > a and b> c and b> d:
    print(f"{b} is largest ")
elif c > a and c> b and c> d:
    print(f"{c} is largest ")
elif d > a and d> c and d> b:
    print(f"{d} is largest ")    




