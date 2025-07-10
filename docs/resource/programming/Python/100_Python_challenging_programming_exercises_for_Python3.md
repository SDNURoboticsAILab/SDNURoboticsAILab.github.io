---
comments: true
---
# 100+ 道 Python 3 具有挑战性的编程练习题

## 1. 级别说明
### 级别 1	初级
初级指的是刚刚学完 Python 入门课程的学员。他们能够用 1 到 2 个 Python 类或函数解决一些问题。通常，答案可以直接在教科书中找到。

### 级别 2	中级
中级指的是刚刚学习 Python，但之前已有较强编程背景的学员。他们应该能够解决可能涉及 3 个或更多 Python 类或函数的问题。答案无法直接在教科书中找到。

### 级别 3	高级
高级学员应能使用 Python 解决更复杂的问题，运用更丰富的库函数、数据结构和算法。他们应当能够使用多个 Python 标准包和高级技术来解决问题。

----

## 2. 问题模板

问题
提示
解法

----

## 3. 问题

### 问题 1
级别 1

问题:
编写一个程序，找到所有在 2000 到 3200（含）之间，可以被 7 整除但不是 5 的倍数的数字。
得到的数字应在一行中以逗号分隔的序列形式打印出来。

提示: 
考虑使用 `range(#begin, #end)` 方法。

解法:
```python
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))
```

### 问题 2
级别 1

问题:
编写一个可以计算给定数字的阶乘的程序。
结果应在一行中以逗号分隔的序列形式打印出来。
假设向程序提供以下输入：
8
那么，输出应该是：
40320

提示:
如果问题提供了输入数据，应假定为控制台输入。

解法:
```python
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print(fact(x))
```

### 问题 3
级别 1

问题:
给定一个整数 n，编写一个程序生成一个包含 (i, i*i) 的字典，其中 i 是 1 到 n（含）之间的整数。然后程序应打印该字典。
假设向程序提供以下输入：
8
那么，输出应该是：
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

提示:
如果问题提供了输入数据，应假定为控制台输入。
考虑使用 `dict()`。

解法:
```python
n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print(d)
```

### 问题 4
级别 1

问题:
编写一个程序，它接受来自控制台的逗号分隔的数字序列，并生成一个包含每个数字的列表和元组。
假设向程序提供以下输入：
34,67,55,33,12,98
那么，输出应该是：
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

提示:
如果问题提供了输入数据，应假定为控制台输入。
`tuple()` 方法可以将列表转换为元组。

解法:
```python
values=input()
l=values.split(",")
t=tuple(l)
print(l)
print(t)
```

### 问题 5
级别 1

问题:
定义一个至少有两个方法的类：
getString: 从控制台输入获取一个字符串。
printString: 以大写形式打印字符串。
也请包含简单的测试函数来测试类方法。

提示:
使用 `__init__` 方法来构造一些参数。

解法:
```python
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()
```

### 问题 6
级别 2

问题:
编写一个程序，根据给定的公式计算并打印值：
Q = [(2 * C * D)/H] 的平方根
以下是 C 和 H 的固定值：
C 是 50。H 是 30。
D 是一个变量，其值应以逗号分隔的序列形式输入到你的程序中。
例如：
假设以下逗号分隔的输入序列被提供给程序：
100,150,180
程序的输出应该是：
18,22,24

提示:
如果收到的输出是小数形式，应四舍五入到最接近的整数值（例如，如果收到的输出是 26.0，应打印为 26）。
如果问题提供了输入数据，应假定为控制台输入。

解法:
```python
import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))
```

### 问题 7
级别 2

问题:
编写一个程序，它以 2 个数字 X,Y 作为输入，并生成一个二维数组。数组中第 i 行第 j 列的元素值应为 i*j。
注意：i=0,1.., X-1; j=0,1,...,Y-1。
例如：
假设向程序提供以下输入：
3,5
那么，程序的输出应该是：
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

提示:
注意：如果问题提供了输入数据，应假定为逗号分隔形式的控制台输入。

解法:
```python
input_str = input()
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print(multilist)
```

### 问题 8
级别 2

问题:
编写一个程序，接受逗号分隔的单词序列作为输入，并按字母顺序排序后以逗号分隔的序列形式打印这些单词。
假设向程序提供以下输入：
without,hello,bag,world
那么，输出应该是：
bag,hello,without,world

提示:
如果问题提供了输入数据，应假定为控制台输入。

解法:
```python
items=[x for x in input().split(',')]
items.sort()
print(','.join(items))
```

### 问题 9
级别 2

问题:
编写一个程序，接受多行序列作为输入，并将句子中的所有字符大写后打印出来。
假设向程序提供以下输入：
Hello world
Practice makes perfect
那么，输出应该是：
HELLO WORLD
PRACTICE MAKES PERFECT

提示:
如果问题提供了输入数据，应假定为控制台输入。

解法:
```python
lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print(sentence)
```

### 问题 10
级别 2

问题:
编写一个程序，接受一个以空格分隔的单词序列作为输入，并在删除所有重复单词并按字母数字顺序排序后打印这些单词。
假设向程序提供以下输入：
hello world and practice makes perfect and hello world again
那么，输出应该是：
again and hello makes perfect practice world

提示:
如果问题提供了输入数据，应假定为控制台输入。
我们使用集合（set）容器自动删除重复数据，然后使用 `sorted()` 对数据进行排序。

解法:
```python
s = input()
words = [word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))
```

### 问题 11
级别 2

问题:
编写一个程序，接受逗号分隔的 4 位二进制数序列作为输入，然后检查它们是否能被 5 整除。能被 5 整除的数字将以逗号分隔的序列形式打印出来。
例如：
0100,0011,1010,1001
那么输出应该是：
1010
注意：假设数据由控制台输入。

提示:
如果问题提供了输入数据，应假定为控制台输入。

解法:
```python
value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print(','.join(value))
```

### 问题 12
级别 2

问题:
编写一个程序，找到所有在 1000 到 3000（含）之间的数字，要求该数字的每一位都是偶数。
得到的数字应在一行中以逗号分隔的序列形式打印出来。

提示:
如果问题提供了输入数据，应假定为控制台输入。

解法:
```python
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))
```

### 问题 13
级别 2

问题:
编写一个程序，接受一个句子并计算字母和数字的数量。
假设向程序提供以下输入：
hello world! 123
那么，输出应该是：
LETTERS 10
DIGITS 3

提示:
如果问题提供了输入数据，应假定为控制台输入。

解法:
```python
s = input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])
```

### 问题 14
级别 2

问题:
编写一个程序，接受一个句子并计算大写字母和小写字母的数量。
假设向程序提供以下输入：
Hello world!
那么，输出应该是：
UPPER CASE 1
LOWER CASE 9

提示:
如果问题提供了输入数据，应假定为控制台输入。

解法:
```python
s = input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print("UPPER CASE", d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])
```

### 问题 15
级别 2

问题:
编写一个程序，计算 a+aa+aaa+aaaa 的值，其中 a 是一个给定的数字。
假设向程序提供以下输入：
9
那么，输出应该是：
11106

提示:
如果问题提供了输入数据，应假定为控制台输入。

解法:

```python
a = input()
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print(n1+n2+n3+n4)
```

### 问题 16
级别 2

问题:
使用列表推导式对列表中的每个奇数进行平方。该列表由逗号分隔的数字序列输入。
假设向程序提供以下输入：
1,2,3,4,5,6,7,8,9
那么，输出应该是：
1,9,25,49,81

提示:
如果问题提供了输入数据，应假定为控制台输入。

解法:

```python
values = input()
numbers = [str(int(x)**2) for x in values.split(",") if int(x)%2!=0]
print(",".join(numbers))
```

### 问题 17
级别 2

问题:
编写一个程序，根据控制台输入的交易日志计算银行账户的净额。交易日志格式如下：
D 100
W 200

D 表示存款，W 表示取款。
假设向程序提供以下输入：
D 300
D 300
W 200
D 100
那么，输出应该是：
500

提示:
如果问题提供了输入数据，应假定为控制台输入。

解法:

```python
netAmount = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print(netAmount)
```

### 问题 18
级别 3

问题:
一个网站要求用户输入用户名和密码进行注册。编写一个程序来检查用户输入的密码的有效性。
以下是检查密码的标准：
1. 至少 1 个 [a-z] 之间的字母
2. 至少 1 个 [0-9] 之间的数字
3. 至少 1 个 [A-Z] 之间的字母
4. 至少 1 个来自 [$#@] 的字符
5. 交易密码的最小长度：6
6. 交易密码的最大长度：12
你的程序应接受一串逗号分隔的密码，并根据上述标准进行检查。符合标准的密码将被打印出来，每个密码用逗号分隔。
例如：
如果向程序提供以下密码作为输入：
ABd1234@1,a F1#,2w3E*,2We3345
那么，程序的输出应该是：
ABd1234@1

提示:
如果问题提供了输入数据，应假定为控制台输入。

解法:

```python
import re
value = []
items=[x for x in input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))
```

### 问题 19
级别 3

问题:
你需要编写一个程序，按升序对 (name, age, height) 元组进行排序，其中 name 是字符串，age 和 height 是数字。元组由控制台输入。排序标准是：
1: 按 name 排序；
2: 然后按 age 排序；
3: 最后按 score（译者注：原文为 height）排序。
优先级是 name > age > score。
如果向程序提供以下元组作为输入：
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
那么，程序的输出应该是：
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

提示:
如果问题提供了输入数据，应假定为控制台输入。
我们使用 `itemgetter` 来启用多个排序键。

解法:
```python
from operator import itemgetter, attrgetter

l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print(sorted(l, key=itemgetter(0,1,2)))
```

### 问题 20
级别 3

问题:
定义一个带生成器的类，该生成器可以迭代在给定范围 0 到 n 之间能被 7 整除的数字。

提示:
考虑使用 `yield`。

解法:

```python
def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in putNumbers(100):
    print(i)
```

### 问题 21
级别 3

问题:
一个机器人在一个平面上从原点 (0,0) 开始移动。机器人可以向上、向下、向左和向右移动给定的步数。机器人移动的轨迹如下所示：
UP 5
DOWN 3
LEFT 3
RIGHT 2
…
方向后面的数字是步数。请编写一个程序，计算经过一系列移动后，当前位置与原点的距离。如果距离是浮点数，则只打印最接近的整数。
例如：
如果向程序提供以下元组作为输入：
UP 5
DOWN 3
LEFT 3
RIGHT 2
那么，程序的输出应该是：
2

提示:
如果问题提供了输入数据，应假定为控制台输入。

解法:

```python
import math
pos = [0,0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
```

### 问题 22
级别 3

问题:
编写一个程序来计算输入中单词的频率。输出应在按键字母数字顺序排序后输出。
假设向程序提供以下输入：
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
那么，输出应该是：
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

提示:
如果问题提供了输入数据，应假定为控制台输入。

解法:

```python
freq = {}   # 文本中单词的频率
line = input()
for word in line.split():
    freq[word] = freq.get(word,0)+1

words = sorted(freq.keys())

for w in words:
    print("%s:%d" % (w,freq[w]))
```

### 问题 23
级别 1

问题:
编写一个可以计算数字平方值的方法。

提示:
使用 `**` 运算符。

解法:

```python
def square(num):
    return num ** 2

print(square(2))
print(square(3))
```

### 问题 24
级别 1

问题:
Python 有许多内置函数，如果你不知道如何使用它，可以在线阅读文档或找一些书籍。但是 Python 为每个内置函数都有一个内置的文档函数。
请编写一个程序来打印一些 Python 内置函数的文档，例如 `abs()`, `int()`, `input()`。
并为自己的函数添加文档。

提示:
内置的文档方法是 `__doc__`。

解法:
```python
print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)

def square(num):
    '''Return the square value of the input number.
    
    The input number must be integer.
    '''
    return num ** 2

print(square(2))
print(square.__doc__)
```

### 问题 25
级别 1

问题:
定义一个类，它有一个类参数和一个同名的实例参数。

提示:
定义一个实例参数，需要将其添加到 `__init__` 方法中。
你可以通过构造参数初始化一个对象，或者稍后设置值。

解法:
```python
class Person:
    # 定义类参数 "name"
    name = "Person"
    
    def __init__(self, name = None):
        # self.name 是实例参数
        self.name = name

jeffrey = Person("Jeffrey")
print("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print("%s name is %s" % (Person.name, nico.name))
```

### 问题 26:
定义一个可以计算两个数之和的函数。

提示:
定义一个以两个数字为参数的函数。你可以在函数中计算和并返回值。

解法

```python
def SumFunction(number1, number2):
	return number1+number2

print(SumFunction(1,2))
```

### 问题 27
定义一个能将整数转换为字符串并在控制台中打印出来的函数。

提示:
使用 `str()` 将数字转换为字符串。

解法
```python
def printValue(n):
    print(str(n))

printValue(3)
```

### 问题 28
定义一个能将整数转换为字符串并在控制台中打印出来的函数。

提示:
使用 `str()` 将数字转换为字符串。

解法
```python
def printValue(n):
    print(str(n))

printValue(3)
```

### 问题 29
定义一个可以接收两个字符串形式的整数，计算它们的和，然后在控制台中打印出来的函数。

提示:
使用 `int()` 将字符串转换为整数。

解法
```python
def printValue(s1,s2):
    print(int(s1)+int(s2))

printValue("3","4")
```

### 问题 30
定义一个可以接受两个字符串作为输入，将它们连接起来，然后在控制台中打印出来的函数。

提示:
使用 `+` 来连接字符串。

解法
```python
def printValue(s1,s2):
    print(s1+s2)

printValue("3","4") #34
```

### 问题 31
定义一个可以接受两个字符串作为输入，并在控制台中打印出长度最大的字符串的函数。如果两个字符串长度相同，则函数应逐行打印所有字符串。

提示:
使用 `len()` 函数获取字符串的长度。

解法
```python
def printValue(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1>len2:
        print(s1)
    elif len2>len1:
        print(s2)
    else:
        print(s1)
        print(s2)
        
printValue("one","three")

```
### 问题 32
定义一个可以接受一个整数作为输入，如果数字是偶数则打印 "It is an even number"，否则打印 "It is an odd number" 的函数。

提示:
使用 `%` 运算符检查一个数是偶数还是奇数。

解法
```python
def checkValue(n):
    if n%2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")
        
checkValue(7)
```
### 问题 33
定义一个函数，可以打印一个字典，其中键是 1 到 3（含）之间的数字，值是键的平方。

提示:
使用 `dict[key]=value` 模式向字典中添加条目。
使用 `**` 运算符获取数字的幂。

解法
```python
def printDict():
    d=dict()
    d[1]=1
    d[2]=2**2
    d[3]=3**2
    print(d)
        
printDict()
```
### 问题 34
定义一个函数，可以打印一个字典，其中键是 1 到 20（含）之间的数字，值是键的平方。

提示:
使用 `dict[key]=value` 模式向字典中添加条目。
使用 `**` 运算符获取数字的幂。
使用 `range()` 进行循环。

解法
```python
def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	print(d)

printDict()
```

### 问题 35
定义一个函数，可以生成一个字典，其中键是 1 到 20（含）之间的数字，值是键的平方。该函数应只打印值。

提示:
使用 `dict[key]=value` 模式向字典中添加条目。
使用 `**` 运算符获取数字的幂。
使用 `range()` 进行循环。
使用 `keys()` 遍历字典中的键。我们也可以使用 `items()` 获取键/值对。

解法
```python
def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	for (k,v) in d.items():	
		print(v)

printDict()
```

### 问题 36
定义一个函数，可以生成一个字典，其中键是 1 到 20（含）之间的数字，值是键的平方。该函数应只打印键。

提示:
使用 `dict[key]=value` 模式向字典中添加条目。
使用 `**` 运算符获取数字的幂。
使用 `range()` 进行循环。
使用 `keys()` 遍历字典中的键。我们也可以使用 `items()` 获取键/值对。

解法
```python
def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	for k in d.keys():	
		print(k)

printDict()
```

### 问题 37
定义一个函数，可以生成并打印一个列表，其中值为 1 到 20（含）之间数字的平方。

提示:
使用 `**` 运算符获取数字的幂。
使用 `range()` 进行循环。
使用 `list.append()` 向列表中添加值。

解法
```python
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li)

printList()
```
### 问题 38
定义一个函数，可以生成一个列表，其中值为 1 到 20（含）之间数字的平方。然后该函数需要打印列表中的前 5 个元素。

提示:
使用 `**` 运算符获取数字的幂。
使用 `range()` 进行循环。
使用 `list.append()` 向列表中添加值。
使用 `[n1:n2]` 对列表进行切片。

解法
```python
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li[:5])

printList()
```

### 问题 39
定义一个函数，可以生成一个列表，其中值为 1 到 20（含）之间数字的平方。然后该函数需要打印列表中的后 5 个元素。

提示:
使用 `**` 运算符获取数字的幂。
使用 `range()` 进行循环。
使用 `list.append()` 向列表中添加值。
使用 `[n1:n2]` 对列表进行切片。

解法
```python
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li[-5:])

printList()
```
### 问题 40
定义一个函数，可以生成一个列表，其中值为 1 到 20（含）之间数字的平方。然后该函数需要打印列表中除了前 5 个元素之外的所有值。

提示:
使用 `**` 运算符获取数字的幂。
使用 `range()` 进行循环。
使用 `list.append()` 向列表中添加值。
使用 `[n1:n2]` 对列表进行切片。

解法
```python
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li[5:])

printList()
```

### 问题 41
定义一个函数，可以生成并打印一个元组，其中值为 1 到 20（含）之间数字的平方。

提示:
使用 `**` 运算符获取数字的幂。
使用 `range()` 进行循环。
使用 `list.append()` 向列表中添加值。
使用 `tuple()` 从列表获取元组。

解法
```python
def printTuple():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(tuple(li))
		
printTuple()
```
### 问题 42
给定一个元组 (1,2,3,4,5,6,7,8,9,10)，编写一个程序，在一行中打印前半部分的值，在另一行中打印后半部分的值。

提示:
使用 `[n1:n2]` 表示法从元组中获取切片。

解法
```python
tp=(1,2,3,4,5,6,7,8,9,10)
tp1=tp[:5]
tp2=tp[5:]
print(tp1)
print(tp2)
```

### 问题 43
编写一个程序，生成并打印另一个元组，其值为给定元组 (1,2,3,4,5,6,7,8,9,10) 中的偶数。

提示:
使用 "for" 循环遍历元组。
使用 `tuple()` 从列表生成元组。

解法
```python
tp=(1,2,3,4,5,6,7,8,9,10)
li=list()
for i in tp:
	if i%2==0:
		li.append(i)

tp2=tuple(li)
print(tp2)
```
### 问题 44
编写一个程序，接受一个字符串作为输入，如果字符串是 "yes" 或 "YES" 或 "Yes"，则打印 "Yes"，否则打印 "No"。

提示:
使用 `if` 语句来判断条件。

解法
```python
s= input()
if s=="yes" or s=="YES" or s=="Yes":
    print("Yes")
else:
    print("No")
```
### 问题 45
编写一个程序，使用 `filter` 函数过滤出列表中的偶数。该列表为: [1,2,3,4,5,6,7,8,9,10]。

提示:
使用 `filter()` 过滤列表中的一些元素。
使用 `lambda` 定义匿名函数。

解法
```python
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print(list(evenNumbers))
```

### 问题 46
编写一个程序，使用 `map()` 生成一个列表，其元素是 [1,2,3,4,5,6,7,8,9,10] 中元素的平方。

提示:
使用 `map()` 生成一个列表。
使用 `lambda` 定义匿名函数。

解法
```python
li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)
print(list(squaredNumbers))
```

### 问题 47
编写一个程序，使用 `map()` 和 `filter()` 生成一个列表，其元素是 [1,2,3,4,5,6,7,8,9,10] 中偶数的平方。

提示:
使用 `map()` 生成一个列表。
使用 `filter()` 过滤列表的元素。
使用 `lambda` 定义匿名函数。

解法
```python
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print(list(evenNumbers))
```
### 问题 48
编写一个程序，使用 `filter()` 生成一个列表，其元素是 1 到 20（含）之间的偶数。

提示:
使用 `filter()` 过滤列表的元素。
使用 `lambda` 定义匿名函数。

解法
```python
evenNumbers = filter(lambda x: x%2==0, range(1,21))
print(list(evenNumbers))
```

### 问题 49
编写一个程序，使用 `map()` 生成一个列表，其元素是 1 到 20（含）之间数字的平方。

提示:
使用 `map()` 生成一个列表。
使用 `lambda` 定义匿名函数。

解法
```python
squaredNumbers = map(lambda x: x**2, range(1,21))
print(list(squaredNumbers))
```

### 问题 50
定义一个名为 `American` 的类，它有一个名为 `printNationality` 的静态方法。

提示:
使用 `@staticmethod` 装饰器定义类静态方法。

解法
```python
class American(object):
    @staticmethod
    def printNationality():
        print("America")

anAmerican = American()
anAmerican.printNationality()
American.printNationality()
```

### 问题 51
定义一个名为 `American` 的类和它的子类 `NewYorker`。

提示:
使用 `class Subclass(ParentClass)` 来定义一个子类。

解法:
```python
class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print(anAmerican)
print(aNewYorker)
```

### 问题 52
定义一个名为 `Circle` 的类，可以通过一个半径来构造。`Circle` 类有一个可以计算面积的方法。

提示:
使用 `def methodName(self)` 定义一个方法。

解法:
```python
class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print(aCircle.area())
```

### 问题 53
定义一个名为 `Rectangle` 的类，可以通过长度和宽度来构造。`Rectangle` 类有一个可以计算面积的方法。

提示:
使用 `def methodName(self)` 定义一个方法。

解法:
```python
class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(2,10)
print(aRectangle.area())
```

### 问题 54
定义一个名为 `Shape` 的类和它的子类 `Square`。`Square` 类有一个 `init` 函数，它接受一个长度作为参数。两个类都有一个 `area` 函数，可以打印形状的面积，其中 `Shape` 的面积默认为 0。

提示:
要重写父类中的方法，我们可以在子类中定义一个同名的方法。

解法:
```python
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

aSquare= Square(3)
print(aSquare.area())
```

### 问题 55
请引发一个 `RuntimeError` 异常。

提示:
使用 `raise` 来引发一个异常。

解法:

```python
raise RuntimeError('something wrong')
```

### 问题 56
编写一个函数来计算 5/0，并使用 `try/except` 来捕获异常。

提示:
使用 `try/except` 来捕获异常。

解法:
```python
def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print("division by zero!")
except Exception as err:
    print('Caught an exception')
finally:
    print('In finally block for cleanup')
```

### 问题 57
定义一个自定义异常类，它接受一个字符串消息作为属性。

提示:
要定义一个自定义异常，我们需要定义一个继承自 `Exception` 的类。

解法:
```python
class MyError(Exception):
    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """
    
    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")
```

### 问题 58
假设我们有一些格式为 "username@companyname.com" 的电子邮件地址，请编写程序打印给定电子邮件地址的用户名。用户名和公司名都只由字母组成。

例如：
如果向程序提供以下电子邮件地址作为输入：

john@google.com

那么，程序的输出应该是：

john

如果问题提供了输入数据，应假定为控制台输入。

提示:
使用 `\w` 来匹配字母。

解法:
```python
import re
emailAddress = input()
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2,emailAddress)
print(r2.group(1))
```

### 问题 59
假设我们有一些格式为 "username@companyname.com" 的电子邮件地址，请编写程序打印给定电子邮件地址的公司名。用户名和公司名都只由字母组成。

例如：
如果向程序提供以下电子邮件地址作为输入：

john@google.com

那么，程序的输出应该是：

google

如果问题提供了输入数据，应假定为控制台输入。

提示:
使用 `\w` 来匹配字母。

解法:
```python
import re
emailAddress = input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print(r2.group(2))
```

### 问题 60
编写一个程序，接受一个以空格分隔的单词序列作为输入，以打印仅由数字组成的单词。

例如：
如果向程序提供以下单词作为输入：

2 cats and 3 dogs.

那么，程序的输出应该是：

['2', '3']

如果问题提供了输入数据，应假定为控制台输入。

提示:
使用 `re.findall()` 通过正则表达式查找所有子字符串。

解法:
```python
import re
s = input()
print(re.findall("\d+",s))
```

### 问题 61
打印一个 Unicode 字符串 "hello world"。

提示:
在 Python 3 中，字符串默认是 Unicode。

解法:
```python
unicodeString = "hello world!"
print(unicodeString)
```

### 问题 62
编写一个程序，读取一个字符串并将其转换为 UTF-8 编码的字节序列。

提示:
使用字符串的 `.encode()` 方法。

解法:
```python
s = input()
u = s.encode("utf-8")
print(u)
```

### 问题 63

编写一个特殊的注释来表明 Python 源代码文件是 Unicode 编码。

提示:

解法:
```python

# -*- coding: utf-8 -*-

#----------------------------------------#
```

### 问题 64

编写一个程序，用控制台给定的 n (n>0) 计算 1/2+2/3+3/4+...+n/n+1。

例如：
如果向程序提供以下 n 作为输入：

5

那么，程序的输出应该是：

3.55

如果问题提供了输入数据，应假定为控制台输入。

提示:
使用 `float()` 将整数转换为浮点数。

解法:
```python
n=int(input())
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print(sum)
```

### 问题 65

编写一个程序来计算：

f(n)=f(n-1)+100 当 n>0
且 f(0)=0

用控制台给定的 n (n>0)。

例如：
如果向程序提供以下 n 作为输入：

5

那么，程序的输出应该是：

500

如果问题提供了输入数据，应假定为控制台输入。

提示:
我们可以在 Python 中定义递归函数。

解法:
```python
def f(n):
    if n==0:
        return 0
    else:
        return f(n-1)+100

n=int(input())
print(f(n))
```

### 问题 66
斐波那契数列根据以下公式计算：

f(n)=0 如果 n=0
f(n)=1 如果 n=1
f(n)=f(n-1)+f(n-2) 如果 n>1

请编写一个程序，用控制台给定的 n 计算 f(n) 的值。

例如：
如果向程序提供以下 n 作为输入：

7

那么，程序的输出应该是：

13

如果问题提供了输入数据，应假定为控制台输入。

提示:
我们可以在 Python 中定义递归函数。


解法:
```python
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
print(f(n))
```

### 问题 67
斐波那契数列根据以下公式计算：

f(n)=0 如果 n=0
f(n)=1 如果 n=1
f(n)=f(n-1)+f(n-2) 如果 n>1

请编写一个程序，使用列表推导式以逗号分隔的形式打印斐波那契数列，n由控制台输入。

例如：
如果向程序提供以下 n 作为输入：

7

那么，程序的输出应该是：

0,1,1,2,3,5,8

（译者注：原文输出包含f(n+1)，此处修正为到f(n)为止）

提示:
我们可以在 Python 中定义递归函数。
使用列表推导式从现有列表生成列表。
使用 `string.join()` 连接字符串列表。
如果问题提供了输入数据，应假定为控制台输入。

解法:
```python
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
values = [str(f(x)) for x in range(0, n+1)]
print(",".join(values))
```

### 问题 68

请编写一个程序，使用生成器以逗号分隔的形式打印 0 到 n 之间的偶数，n由控制台输入。

例如：
如果向程序提供以下 n 作为输入：

10

那么，程序的输出应该是：

0,2,4,6,8,10

提示:
使用 `yield` 在生成器中产生下一个值。
如果问题提供了输入数据，应假定为控制台输入。

解法:
```python
def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


n=int(input())
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print(",".join(values))
```

### 问题 69
请编写一个程序，使用生成器以逗号分隔的形式打印 0 到 n 之间能被 5 和 7 整除的数字，n由控制台输入。

例如：
如果向程序提供以下 n 作为输入：

100

那么，程序的输出应该是：

0,35,70

提示:
使用 `yield` 在生成器中产生下一个值。
如果问题提供了输入数据，应假定为控制台输入。

解法:
```python
def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i

n=int(input())
values = []
for i in NumGenerator(n):
    values.append(str(i))

print(",".join(values))
```

### 问题 70
请编写 `assert` 语句来验证列表 `[2,4,6,8]` 中的每个数字都是偶数。

提示:
使用 `"assert expression"` 来进行断言。

解法:
```python
li = [2,4,6,8]
for i in li:
    assert i%2==0
```

### 问题 71
请编写一个程序，接受来自控制台的基本数学表达式并打印评估结果。

例如：
如果向程序提供以下字符串作为输入：

35+3

那么，程序的输出应该是：

38

提示:
使用 `eval()` 来评估一个表达式。


解法:
```python
expression = input()
print(eval(expression))
```

### 问题 72
请编写一个二分搜索函数，在已排序的列表中搜索一个项。该函数应返回要搜索的元素在列表中的索引。

提示:
使用 `if/elif` 来处理条件。

解法:
```python
import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print(bin_search(li,11))
print(bin_search(li,12))
```

### 问题 73
请编写一个二分搜索函数，在已排序的列表中搜索一个项。该函数应返回要搜索的元素在列表中的索引。

提示:
使用 `if/elif` 来处理条件。

解法:
```python
import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print(bin_search(li,11))
print(bin_search(li,12))
```

### 问题 74
请使用 Python `random` 模块生成一个介于 10 和 100 之间的随机浮点数。

提示:
使用 `random.uniform(a, b)`。

解法:
```python
import random
print(random.uniform(10,100))
```

### 问题 75
请使用 Python `random` 模块生成一个介于 5 和 95 之间的随机浮点数。

提示:
使用 `random.uniform(a, b)`。

解法:
```python
import random
print(random.uniform(5,95))
```

### 问题 76
请编写一个程序，使用 `random` 模块和列表推导式输出一个 0 到 10（含）之间的随机偶数。

提示:
使用 `random.choice()` 从列表中随机选择一个元素。

解法:
```python
import random
print(random.choice([i for i in range(11) if i%2==0]))
```

### 问题 77
请编写一个程序，使用 `random` 模块和列表推导式输出一个 0 到 200（含）之间能被 5 和 7 整除的随机数。

提示:
使用 `random.choice()` 从列表中随机选择一个元素。

解法:
```python
import random
print(random.choice([i for i in range(201) if i%5==0 and i%7==0]))
```

### 问题 78
请编写一个程序生成一个包含 5 个介于 100 和 200（含）之间的随机数的列表。

提示:
使用 `random.sample()` 生成一个随机值的列表。

解法:
```python
import random
print(random.sample(range(100, 201), 5))
```

### 问题 79
请编写一个程序随机生成一个包含 5 个介于 100 和 200（含）之间的偶数的列表。

提示:
使用 `random.sample()` 生成一个随机值的列表。

解法:
```python
import random
print(random.sample([i for i in range(100,201) if i%2==0], 5))
```

### 问题 80
请编写一个程序随机生成一个包含 5 个能被 5 和 7 整除、介于 1 和 1000（含）之间的数字的列表。

提示:
使用 `random.sample()` 生成一个随机值的列表。

解法:
```python
import random
print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5))
```

### 问题 81
请编写一个程序随机打印一个 7 到 15（含）之间的整数。

提示:
使用 `random.randrange()` 在给定范围内生成一个随机整数。

解法:
```python
import random
print(random.randrange(7,16))
```

### 问题 82
请编写一个程序来压缩和解压缩字符串 "hello world!hello world!hello world!hello world!"。

提示:
使用 `zlib.compress()` 和 `zlib.decompress()` 来压缩和解压缩字符串。

解法:
```python
import zlib
s = b'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))
```

### 问题 83
请编写一个程序来打印执行 100 次 "1+1" 的运行时间。

提示:
使用 `timeit()` 函数来测量运行时间。

解法:
```python
from timeit import Timer
t = Timer("for i in range(100):1+1")
print(t.timeit())
```

### 问题 84
请编写一个程序来打乱并打印列表 [3,6,7,8]。

提示:
使用 `shuffle()` 函数来打乱一个列表。

解法:
```python
from random import shuffle
li = [3,6,7,8]
shuffle(li)
print(li)
```

### 问题 85
请编写一个程序来打乱并打印列表 [3,6,7,8]。

提示:
使用 `shuffle()` 函数来打乱一个列表。

解法:
```python
from random import shuffle
li = [3,6,7,8]
shuffle(li)
print(li)
```

### 问题 86
请编写一个程序生成所有主语在 ["I", "You"]，动词在 ["Play", "Love"]，宾语在 ["Hockey","Football"] 中的句子。

提示:
使用 `list[index]` 表示法从列表中获取一个元素。

解法:
```python
subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
            print(sentence)
```

### 问题 87
请编写一个程序，在移除 [5,6,77,45,22,12,24] 中的偶数后打印列表。

提示:
使用列表推导式从列表中删除一批元素。

解法:
```python
li = [5,6,77,45,22,12,24]
li = [x for x in li if x%2!=0]
print(li)
```

### 问题 88
通过使用列表推导式，请编写一个程序，在移除 [12,24,35,70,88,120,155] 中能被 5 和 7 整除的数字后打印列表。

提示:
使用列表推导式从列表中删除一批元素。

解法:
```python
li = [12,24,35,70,88,120,155]
li = [x for x in li if x%5!=0 and x%7!=0]
print(li)
```

### 问题 89
通过使用列表推导式，请编写一个程序，在移除 [12,24,35,70,88,120,155] 中的第 0、2、4、6 个数字后打印列表。

提示:
使用列表推导式从列表中删除一批元素。
使用 `enumerate()` 获取 (index, value) 元组。

解法:
```python
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2!=0]
print(li)
```

### 问题 90
通过使用列表推导式，请编写一个程序生成一个 3*5*8 的三维数组，其每个元素都为 0。

提示:
使用列表推导式制作一个数组。

解法:
```python
array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)
```

### 问题 91
通过使用列表推导式，请编写一个程序，在移除 [12,24,35,70,88,120,155] 中的第 0、4、5 个数字后打印列表。

提示:
使用列表推导式从列表中删除一批元素。
使用 `enumerate()` 获取 (index, value) 元组。

解法:
```python
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
print(li)
```

### 问题 92
通过使用列表推导式，请编写一个程序，在移除 [12,24,35,24,88,120,155] 中的值 24 后打印列表。

提示:
使用列表推导式来删除一个值。

解法:
```python
li = [12,24,35,24,88,120,155]
li = [x for x in li if x!=24]
print(li)
```

### 问题 93
给定两个列表 [1,3,6,78,35,55] 和 [12,24,35,24,88,120,155]，编写一个程序，生成一个其元素为上述两个列表交集的列表。

提示:
使用 `set()` 和 `&` 运算符进行集合交集操作。

解法:
```python
set1=set([1,3,6,78,35,55])
set2=set([12,24,35,24,88,120,155])
set1.intersection_update(set2)
li=list(set1)
print(li)
```

### 问题 94
给定一个列表 [12,24,35,24,88,120,155,88,120,155]，编写一个程序，在移除所有重复值并保留原始顺序后打印此列表。

提示:
使用 `set()` 来存储不重复的值。

解法:
```python
def removeDuplicate( li ):
    newli=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)

    return newli

li=[12,24,35,24,88,120,155,88,120,155]
print(removeDuplicate(li))
```

### 问题 95
定义一个 `Person` 类和它的两个子类：`Male` 和 `Female`。所有类都有一个 `getGender` 方法，`Male` 类可以打印 "Male"，`Female` 类可以打印 "Female"。

提示:
使用 `Subclass(Parentclass)` 定义一个子类。

解法:
```python
class Person(object):
    def getGender( self ):
        return "Unknown"

class Male( Person ):
    def getGender( self ):
        return "Male"

class Female( Person ):
    def getGender( self ):
        return "Female"

aMale = Male()
aFemale= Female()
print(aMale.getGender())
print(aFemale.getGender())
```

### 问题 96
请编写一个程序，计算并打印由控制台输入的字符串中每个字符的数量。

例如：
如果向程序提供以下字符串作为输入：

abcdefgabc

那么，程序的输出应该是：

a,2
b,2
c,2
d,1
e,1
f,1
g,1

提示:
使用字典来存储键/值对。
使用 `dict.get()` 方法查找一个键并提供默认值。

解法:
```python
dic = {}
s=input()
for char in s:
    dic[char] = dic.get(char,0)+1
print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))
```

### 问题 97
请编写一个程序，接受来自控制台的字符串并按相反顺序打印。

例如：
如果向程序提供以下字符串作为输入：

rise to vote sir

那么，程序的输出应该是：

ris etov ot esir

提示:
使用 `list[::-1]` 以相反的顺序迭代列表。

解法:
```python
s=input()
s = s[::-1]
print(s)
```

### 问题 98
请编写一个程序，接受来自控制台的字符串并打印出具有偶数索引的字符。

例如：
如果向程序提供以下字符串作为输入：

H1e2l3l4o5w6o7r8l9d

那么，程序的输出应该是：

Helloworld

提示:
使用 `list[::2]` 以步长 2 迭代列表。

解法:
```python
s=input()
s = s[::2]
print(s)
```

### 问题 99
请编写一个程序，打印 [1,2,3] 的所有排列。

提示:
使用 `itertools.permutations()` 获取列表的排列。

解法:
```python
import itertools
print(list(itertools.permutations([1,2,3])))
```

### 问题 100
编写一个程序来解决一个经典的中国古代谜题：
我们数农场里的鸡和兔子，共有 35 个头和 94 条腿。我们有多少只兔子和多少只鸡？

提示:
使用 `for` 循环遍历所有可能的解。

解法:
```python
def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns

numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print(solutions)
```
