Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
friend = []
friend.appened('somesri')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    friend.appened('somesri')
AttributeError: 'list' object has no attribute 'appened'. Did you mean: 'append'?
friend.append('somsri')_
SyntaxError: invalid syntax
friend = []
friend.append('somsri')
print(friend)
['somsri']
friend.append('somsak')
print(friend)
['somsri', 'somsak']
friend.append('somchai')
print(friend)
['somsri', 'somsak', 'somchai']
friend.insert(1, 'sompong')
friend.remove('somepong')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    friend.remove('somepong')
ValueError: list.remove(x): x not in list
friend.insert(0, 'somepong')
friend.insert(2, 'somkiat')
print(friend)
['somepong', 'somsri', 'somkiat', 'sompong', 'somsak', 'somchai']
del friend[0]
print(friend)
['somsri', 'somkiat', 'sompong', 'somsak', 'somchai']
friend.insert(0, friend.pop(3) )
print(friend)
['somsak', 'somsri', 'somkiat', 'sompong', 'somchai']
friend.insert(1, friend.pop(3) )
print(friend)
['somsak', 'sompong', 'somsri', 'somkiat', 'somchai']
friend.remove('somchai')
print(friend)
['somsak', 'sompong', 'somsri', 'somkiat']
print(friend.remove('somkiat'))
None
print(friend)
['somsak', 'sompong', 'somsri']
print(friend.pop(2))
somsri
print(friend)
['somsak', 'sompong']
type(friend)
<class 'list'>
teacher = ('Korkai','Khorkai','Korkwai')
teacher.append('Sorsear')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    teacher.append('Sorsear')
AttributeError: 'tuple' object has no attribute 'append'
type(teacher)
<class 'tuple'>
coin = (5,1,10,2,5,1,10,2,10,10,10,10)
coin.count(10)
6
coin.count(2)
2
coin.count(5)
2
teacher = ('Korkai','Khorkai','Korkwai')
teacher.index('Korkai')
0
print(teacher[-1])
Korkwai
print(teacher[-2])
Khorkai
character = ['A','Z','C','X','Y']
character.sort()
print(character)
['A', 'C', 'X', 'Y', 'Z']
character.sort(reverse=True)
print(character)
['Z', 'Y', 'X', 'C', 'A']
character = ['A','Z','C','X','Y']
sorted(character)
['A', 'C', 'X', 'Y', 'Z']
print(character)
['A', 'Z', 'C', 'X', 'Y']
character.reverse()
print(character)
['Y', 'X', 'C', 'Z', 'A']
