Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = [12, 24, 36, 48,60,72，84]
SyntaxError: invalid character '，' (U+FF0C)
a=[12,24,36,48,60,72,84]
a.append(96)
a
[12, 24, 36, 48, 60, 72, 84, 96]
a.extend([108,120])
a
[12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
a.insert(3,30)
a
[12, 24, 36, 30, 48, 60, 72, 84, 96, 108, 120]
a.pop()
120
a
[12, 24, 36, 30, 48, 60, 72, 84, 96, 108]
a.remove(48)
a
[12, 24, 36, 30, 60, 72, 84, 96, 108]
a.append([132,144])
a
[12, 24, 36, 30, 60, 72, 84, 96, 108, [132, 144]]
a.extend([156,168])
a
[12, 24, 36, 30, 60, 72, 84, 96, 108, [132, 144], 156, 168]
a.insert(0,6)
a
[6, 12, 24, 36, 30, 60, 72, 84, 96, 108, [132, 144], 156, 168]
a.pop(5)
60
a
[6, 12, 24, 36, 30, 72, 84, 96, 108, [132, 144], 156, 168]
a.remove(72)
a
[6, 12, 24, 36, 30, 84, 96, 108, [132, 144], 156, 168]



a=['Python','Java','C','C++','SQL','HTML']
a.insert(2,'CSS')
a
['Python', 'Java', 'CSS', 'C', 'C++', 'SQL', 'HTML']
a.append('JavaScript')
a.extend(['React','Angular'])
a
['Python', 'Java', 'CSS', 'C', 'C++', 'SQL', 'HTML', 'JavaScript', 'React', 'Angular']
a.extend(['React','Angular'])
a
['Python', 'Java', 'CSS', 'C', 'C++', 'SQL', 'HTML', 'JavaScript', 'React', 'Angular', 'React', 'Angular']
a.remove('C++')
a
['Python', 'Java', 'CSS', 'C', 'SQL', 'HTML', 'JavaScript', 'React', 'Angular', 'React', 'Angular']
a.pop()
'Angular'
a
['Python', 'Java', 'CSS', 'C', 'SQL', 'HTML', 'JavaScript', 'React', 'Angular', 'React']
a=['Python', 'Java', 'CSS', 'C', 'C++', 'SQL', 'HTML', 'JavaScript', 'React', 'Angular']
a.remove('C++')
a
['Python', 'Java', 'CSS', 'C', 'SQL', 'HTML', 'JavaScript', 'React', 'Angular']
a.pop()
'Angular'
a
['Python', 'Java', 'CSS', 'C', 'SQL', 'HTML', 'JavaScript', 'React']
a.insert(-2,'Bootstrap')
a
['Python', 'Java', 'CSS', 'C', 'SQL', 'HTML', 'Bootstrap', 'JavaScript', 'React']
a.append(['Django','Flask'])
a
['Python', 'Java', 'CSS', 'C', 'SQL', 'HTML', 'Bootstrap', 'JavaScript', 'React', ['Django', 'Flask']]
a.extend("AI")
a
['Python', 'Java', 'CSS', 'C', 'SQL', 'HTML', 'Bootstrap', 'JavaScript', 'React', ['Django', 'Flask'], 'A', 'I']
a.pop()
'I'
a
['Python', 'Java', 'CSS', 'C', 'SQL', 'HTML', 'Bootstrap', 'JavaScript', 'React', ['Django', 'Flask'], 'A']
a.remove('HTML')
a
['Python', 'Java', 'CSS', 'C', 'SQL', 'Bootstrap', 'JavaScript', 'React', ['Django', 'Flask'], 'A']




a=[5.5,10.5,15.5,20.5,25.5,30.5]
a.append(35.5)
a
[5.5, 10.5, 15.5, 20.5, 25.5, 30.5, 35.5]
a.insert(1,7.5)
a
[5.5, 7.5, 10.5, 15.5, 20.5, 25.5, 30.5, 35.5]
a.extend([40.5,45.5])
a
[5.5, 7.5, 10.5, 15.5, 20.5, 25.5, 30.5, 35.5, 40.5, 45.5]
a.remove(20.5)
a
[5.5, 7.5, 10.5, 15.5, 25.5, 30.5, 35.5, 40.5, 45.5]
a.pop()
45.5
a
[5.5, 7.5, 10.5, 15.5, 25.5, 30.5, 35.5, 40.5]
a.append([50.5,55.5])
a
[5.5, 7.5, 10.5, 15.5, 25.5, 30.5, 35.5, 40.5, [50.5, 55.5]]
a.extend("XY")
a
[5.5, 7.5, 10.5, 15.5, 25.5, 30.5, 35.5, 40.5, [50.5, 55.5], 'X', 'Y']
a.insert(-2,60.5)
a
[5.5, 7.5, 10.5, 15.5, 25.5, 30.5, 35.5, 40.5, [50.5, 55.5], 60.5, 'X', 'Y']
a.pop(4)
25.5
a
[5.5, 7.5, 10.5, 15.5, 30.5, 35.5, 40.5, [50.5, 55.5], 60.5, 'X', 'Y']
a.remove(30.5)
a
[5.5, 7.5, 10.5, 15.5, 35.5, 40.5, [50.5, 55.5], 60.5, 'X', 'Y']


a=[[1],[2],[3],[4],[5],[6]]
a.append([7])
a
[[1], [2], [3], [4], [5], [6], [7]]
a.extend([[8],[9]])
a
[[1], [2], [3], [4], [5], [6], [7], [8], [9]]
a.insert(3,[10])
a
[[1], [2], [3], [10], [4], [5], [6], [7], [8], [9]]
a.remove([2])
a
[[1], [3], [10], [4], [5], [6], [7], [8], [9]]
apop()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    apop()
NameError: name 'apop' is not defined
a.pop()
[9]
a
[[1], [3], [10], [4], [5], [6], [7], [8]]
a.append((11,12))
a
[[1], [3], [10], [4], [5], [6], [7], [8], (11, 12)]
a.extend("AB")
a
[[1], [3], [10], [4], [5], [6], [7], [8], (11, 12), 'A', 'B']
a.insert(0,[0])
a
[[0], [1], [3], [10], [4], [5], [6], [7], [8], (11, 12), 'A', 'B']
a.pop(5)
[5]
a
[[0], [1], [3], [10], [4], [6], [7], [8], (11, 12), 'A', 'B']
a.remove([5])
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a.remove([5])
ValueError: list.remove(x): x not in list
a
[[0], [1], [3], [10], [4], [6], [7], [8], (11, 12), 'A', 'B']


a=[100,'Python',3.14,True,[10,20],[30,40],'AI']
a.append(False)
a
[100, 'Python', 3.14, True, [10, 20], [30, 40], 'AI', False]
a.insert(2,'ML')
a
[100, 'Python', 'ML', 3.14, True, [10, 20], [30, 40], 'AI', False]
a.extend([200,300])
a
[100, 'Python', 'ML', 3.14, True, [10, 20], [30, 40], 'AI', False, 200, 300]
a.remove(True)
a
[100, 'Python', 'ML', 3.14, [10, 20], [30, 40], 'AI', False, 200, 300]
a.pop()
300
a
[100, 'Python', 'ML', 3.14, [10, 20], [30, 40], 'AI', False, 200]
a.append(['DL','NLP'])
a
[100, 'Python', 'ML', 3.14, [10, 20], [30, 40], 'AI', False, 200, ['DL', 'NLP']]
a.extend("CD")
a
[100, 'Python', 'ML', 3.14, [10, 20], [30, 40], 'AI', False, 200, ['DL', 'NLP'], 'C', 'D']
a.insert(-1,'Resume')
a
[100, 'Python', 'ML', 3.14, [10, 20], [30, 40], 'AI', False, 200, ['DL', 'NLP'], 'C', 'Resume', 'D']
a.pop(4)
[10, 20]
a.remove('Python')
a
[100, 'ML', 3.14, [30, 40], 'AI', False, 200, ['DL', 'NLP'], 'C', 'Resume', 'D']



a=[11,22,33,44,55,66,77,88]
a.append(99)
a
[11, 22, 33, 44, 55, 66, 77, 88, 99]
a.append([111,122])
a
[11, 22, 33, 44, 55, 66, 77, 88, 99, [111, 122]]
a.insert(4,49)
a
[11, 22, 33, 44, 49, 55, 66, 77, 88, 99, [111, 122]]
a.pop(2)
33
a.remove(66)
a
[11, 22, 44, 49, 55, 77, 88, 99, [111, 122]]
a.append([133,144])
a
[11, 22, 44, 49, 55, 77, 88, 99, [111, 122], [133, 144]]
a.extend((155,166))
a
[11, 22, 44, 49, 55, 77, 88, 99, [111, 122], [133, 144], 155, 166]
a.pop()
166
a
[11, 22, 44, 49, 55, 77, 88, 99, [111, 122], [133, 144], 155]
a.remove(22)
a
[11, 44, 49, 55, 77, 88, 99, [111, 122], [133, 144], 155]



a=['Red','Blue','Green','Yellow','Black','White','Pink']
a.insert(3,'Orange')
a
['Red', 'Blue', 'Green', 'Orange', 'Yellow', 'Black', 'White', 'Pink']
a.append('Purple')
a
['Red', 'Blue', 'Green', 'Orange', 'Yellow', 'Black', 'White', 'Pink', 'Purple']
a.extend(['Brown','Gray'])
a.remove('Yellow')
a.pop()
'Gray'
a=['Red', 'Blue', 'Green', 'Orange', 'Yellow', 'Black', 'White', 'Pink', 'Purple']
a.extend(['Brown','Gray'])
a
['Red', 'Blue', 'Green', 'Orange', 'Yellow', 'Black', 'White', 'Pink', 'Purple', 'Brown', 'Gray']
a.remove('Yellow')
a.pop(4)
'Black'
a
['Red', 'Blue', 'Green', 'Orange', 'White', 'Pink', 'Purple', 'Brown', 'Gray']
a.append(['Gold','Silver'])
a
['Red', 'Blue', 'Green', 'Orange', 'White', 'Pink', 'Purple', 'Brown', 'Gray', ['Gold', 'Silver']]
a.extend("UV")
a
['Red', 'Blue', 'Green', 'Orange', 'White', 'Pink', 'Purple', 'Brown', 'Gray', ['Gold', 'Silver'], 'U', 'V']
a.insert(0,'color')
a
['color', 'Red', 'Blue', 'Green', 'Orange', 'White', 'Pink', 'Purple', 'Brown', 'Gray', ['Gold', 'Silver'], 'U', 'V']
a.pop()
'V'
a
['color', 'Red', 'Blue', 'Green', 'Orange', 'White', 'Pink', 'Purple', 'Brown', 'Gray', ['Gold', 'Silver'], 'U']
a.remove('Blue')
a
['color', 'Red', 'Green', 'Orange', 'White', 'Pink', 'Purple', 'Brown', 'Gray', ['Gold', 'Silver'], 'U']



a=[2.5,5.5,8.5,11.5,14.5,17.5,20.5]
a.append(23.5)
a
[2.5, 5.5, 8.5, 11.5, 14.5, 17.5, 20.5, 23.5]
a.extend([26.5,29.5])
a
[2.5, 5.5, 8.5, 11.5, 14.5, 17.5, 20.5, 23.5, 26.5, 29.5]
a.insert(2,7.5)
a
[2.5, 5.5, 7.5, 8.5, 11.5, 14.5, 17.5, 20.5, 23.5, 26.5, 29.5]
a.pop(5)
14.5
a
[2.5, 5.5, 7.5, 8.5, 11.5, 17.5, 20.5, 23.5, 26.5, 29.5]
a.remove(17.5)
a
[2.5, 5.5, 7.5, 8.5, 11.5, 20.5, 23.5, 26.5, 29.5]
a.append((32.5,35.5))
a
[2.5, 5.5, 7.5, 8.5, 11.5, 20.5, 23.5, 26.5, 29.5, (32.5, 35.5)]
a.extend("AB")
a
[2.5, 5.5, 7.5, 8.5, 11.5, 20.5, 23.5, 26.5, 29.5, (32.5, 35.5), 'A', 'B']
a.insert(-2,38.5)
a
[2.5, 5.5, 7.5, 8.5, 11.5, 20.5, 23.5, 26.5, 29.5, (32.5, 35.5), 38.5, 'A', 'B']
a.pop()
'B'
a
[2.5, 5.5, 7.5, 8.5, 11.5, 20.5, 23.5, 26.5, 29.5, (32.5, 35.5), 38.5, 'A']
a.remove(5.5)
a
[2.5, 7.5, 8.5, 11.5, 20.5, 23.5, 26.5, 29.5, (32.5, 35.5), 38.5, 'A']



a=[[10],[20],[30],[40],[50],[60],[70]]
a.append([80])
a
[[10], [20], [30], [40], [50], [60], [70], [80]]
a.extend([[90],[100]])
a
[[10], [20], [30], [40], [50], [60], [70], [80], [90], [100]]
a.insert(5,[45])
a
[[10], [20], [30], [40], [50], [45], [60], [70], [80], [90], [100]]
a.remove([20])
a
[[10], [30], [40], [50], [45], [60], [70], [80], [90], [100]]
a.pop(3)
[50]
a
[[10], [30], [40], [45], [60], [70], [80], [90], [100]]
a.append((110,120))
a
[[10], [30], [40], [45], [60], [70], [80], [90], [100], (110, 120)]
a.extend("PQ")
a
[[10], [30], [40], [45], [60], [70], [80], [90], [100], (110, 120), 'P', 'Q']
a.insert(1,[5])
a
[[10], [5], [30], [40], [45], [60], [70], [80], [90], [100], (110, 120), 'P', 'Q']
a.pop()
'Q'
a
[[10], [5], [30], [40], [45], [60], [70], [80], [90], [100], (110, 120), 'P']
a.remove([70])
a
[[10], [5], [30], [40], [45], [60], [80], [90], [100], (110, 120), 'P']



a=[100, 'Python',3.14,False,[10,20],[30,40],'AI',500]
>>> a
[100, 'Python', 3.14, False, [10, 20], [30, 40], 'AI', 500]
>>> a.append(True)
>>> a
[100, 'Python', 3.14, False, [10, 20], [30, 40], 'AI', 500, True]
>>> a.aextend([600,700])
Traceback (most recent call last):
  File "<pyshell#226>", line 1, in <module>
    a.aextend([600,700])
AttributeError: 'list' object has no attribute 'aextend'. Did you mean: 'extend'?
>>> a.extend([600,700])
>>> a
[100, 'Python', 3.14, False, [10, 20], [30, 40], 'AI', 500, True, 600, 700]
>>> a.insert(3,'ML')
>>> a
[100, 'Python', 3.14, 'ML', False, [10, 20], [30, 40], 'AI', 500, True, 600, 700]
>>> a.pop(6)
[30, 40]
>>> a
[100, 'Python', 3.14, 'ML', False, [10, 20], 'AI', 500, True, 600, 700]
>>> a.remove(false)
Traceback (most recent call last):
  File "<pyshell#233>", line 1, in <module>
    a.remove(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> a.remove(False)
>>> a
[100, 'Python', 3.14, 'ML', [10, 20], 'AI', 500, True, 600, 700]
>>> a.append(['DL','NLP'])
>>> a
[100, 'Python', 3.14, 'ML', [10, 20], 'AI', 500, True, 600, 700, ['DL', 'NLP']]
>>> a.extend("XY")
>>> a
[100, 'Python', 3.14, 'ML', [10, 20], 'AI', 500, True, 600, 700, ['DL', 'NLP'], 'X', 'Y']
>>> a.insert(-2,'CV')
>>> a
[100, 'Python', 3.14, 'ML', [10, 20], 'AI', 500, True, 600, 700, ['DL', 'NLP'], 'CV', 'X', 'Y']
>>> a.pop(1)
'Python'
>>> a
[100, 3.14, 'ML', [10, 20], 'AI', 500, True, 600, 700, ['DL', 'NLP'], 'CV', 'X', 'Y']
>>> a.remove(500)
>>> a
[100, 3.14, 'ML', [10, 20], 'AI', True, 600, 700, ['DL', 'NLP'], 'CV', 'X', 'Y']
