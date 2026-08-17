Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
10%3
1
25%4
1
100%7
2
20%5
0
15%2
1
99%10
9
num1=559
even=num1%2=0
SyntaxError: cannot assign to expression
KeyboardInterrupt
even=num1%2==0
odd=num1%2==1
even
False
odd
True
num1
559
num1%2
1
num=145687
last_digit= num%10
last_digit
7
123%10
3
50%7
1
7%2
1
>>> 1000%100
0
>>> num=999
>>> div3=num%3
>>> div3
0
>>> num=555
>>> div3
0
>>> num=565685
>>> div5=num%5
>>> div5
0
>>> 250%12
10
>>> 15%4
3
>>> -15%4
1
>>> 20%6
2
>>> num=456
>>> a=num%10
>>> num2=num//10
>>> b=num2%10
>>> num3=num2//10
>>> c=num3%10
>>> reverse= c*100 + b*10 +c
>>> reverse
454
>>> reverse= c*100 + b*10 +a
>>> reverce
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    reverce
NameError: name 'reverce' is not defined. Did you mean: 'reverse'?
>>> reverse
456
>>> reverse= a*100 + b*10 +c
>>> reverse
654
>>> 10%0
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    10%0
ZeroDivisionError: division by zero
