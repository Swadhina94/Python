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
