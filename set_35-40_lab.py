Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = {11, 22, 33, 44.5, 'Java', 'HTML', (100, 200), (300, 400), True}
a.add((500, 600))
a.add(22)
a.remove('HTML')
KeyboardInterrupt
a.pop()
True
a.add('CSS')
a.remove((300, 400))
a.add(True)
a.pop()
(100, 200)
a.add((700, 800))
a.add('Java')
a
{True, 33, 'Java', 44.5, 11, 'CSS', (500, 600), 22, (700, 800)}


a = {'A', 'B', 'C', 1, 2, 3.5, (11, 22), (33, 44), False}
a.add((55, 66))
a.add('C')
a
{False, 1, 2, 3.5, 'C', (55, 66), (11, 22), 'A', (33, 44), 'B'}
a.remove(1)
a.pop()
False
a.add(False)
a.remove((33, 44))
a
{False, 2, 3.5, 'C', (55, 66), (11, 22), 'A', 'B'}
a.add('D')
a.pop()
False
a.add((77, 88))
a.add(3.5)
a
{2, 3.5, 'D', 'C', (55, 66), (77, 88), (11, 22), 'A', 'B'}


a = {100, 200, 300.5, 'Red', 'Blue', True, (1, 10), (2, 20), 'Python'}
a.add((3, 30))
a.add(100)
a.remove('Blue')
a.pop()
True
a.add(True)
a
{True, (3, 30), 100, (2, 20), 'Python', 200, 300.5, (1, 10), 'Red'}
a.remove((2, 20))
a.add('Green')
a.pop()
(3, 30)
a.add((4, 40))
a.add('Python')
a
{True, 'Green', 100, 'Python', 200, 300.5, (4, 40), (1, 10), 'Red'}


a = {'Windows', 'Linux', 10, 20.5, (1, 2), (3, 4), False, 'Mac'}
a
{False, (1, 2), (3, 4), 'Windows', 10, 'Linux', 20.5, 'Mac'}
>>> a.add((5, 6))
>>> a.add('Linux')
>>> a
{False, (1, 2), (3, 4), 'Windows', 10, 'Linux', 20.5, (5, 6), 'Mac'}
>>> a.remove('Mac')
>>> a.pop()
False
>>> a.add('Ubuntu')
>>> a
{'Ubuntu', (1, 2), (3, 4), 'Windows', 10, 'Linux', 20.5, (5, 6)}
>>> a.remove((1, 2))
>>> a.add(False)
>>> a
{False, 'Ubuntu', (3, 4), 'Windows', 10, 'Linux', 20.5, (5, 6)}
>>> a.pop()
'Ubuntu'
>>> a.add((7, 8))
>>> a.add(100)
>>> a
{False, 100, (3, 4), 'Windows', 10, 'Linux', 20.5, (5, 6), (7, 8)}
>>> 
>>> 
>>> 
>>> 
>>> a = {5, 10, 15.5, 'AI', 'ML', (11, 12), (13, 14), True}
>>> a.add((15, 16))
>>> a.add('AI')
>>> a
{True, (13, 14), 'ML', 5, 10, 15.5, (11, 12), (15, 16), 'AI'}
>>> a.remove('ML')
>>> a.pop()
True
>>> a.add('DL')
>>> a
{(13, 14), 5, 10, 'DL', 15.5, (11, 12), (15, 16), 'AI'}
>>> a.remove((11, 12))
>>> a.add(True)
>>> a.pop()
(13, 14)
>>> a
{True, 5, 10, 'DL', 15.5, (15, 16), 'AI'}
>>> a.add((17, 18))
>>> a.add(25)
>>> a
{True, 5, 10, 'DL', 15.5, (15, 16), 25, (17, 18), 'AI'}
