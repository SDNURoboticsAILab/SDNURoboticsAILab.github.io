---
comments: true
---

# C++ 运算符

**运算符**是对值进行操作以执行特定数学或逻辑计算的符号。它们构成了任何编程语言的基础。在 C++ 中，我们有内置的运算符来提供所需的功能。

运算符操作**操作数**。例如

```cpp
int c = a + b;
```

这里，'+' 是加法运算符。'a' 和 'b' 是被 '添加' 的操作数。

**C++ 中的运算符可分为 6 种类型：**

1.算术运算符
2.关系运算符
3.逻辑运算符
4.按位运算符
5.赋值运算符
6.三元运算符或条件运算符

![C++ 中的运算符](https://media.geeksforgeeks.org/wp-content/uploads/20220527101351/OperatorsinCPP.png)

### 1） 算术运算符

 这些运算符用于对操作数执行算术或数学运算。例如，'+' 用于加法，'-' 用于减法，'*' 用于乘法，等等。

 **算术运算符可分为 2 种类型：**

 **A） 一元运算符：**这些运算符操作或使用单个操作数。例如：Increment（++） 和 Decrement（–） 运算符。

|    名字    | 象征 |         描述         |           例            |
| :--------: | :--: | :------------------: | :---------------------: |
| 递增运算符 |  ++  | 将变量的整数值增加 1 | int a = 5;一个++;返回 6 |
| 递减运算符 |  --  | 将变量的整数值减少 1 | int a = 5;一个–;返回 4  |

**例：**

描述



**输出**

 ```C++
 a++ is 10
 ++a is 12
 b-- is 15
 --b is 13
 ```

**时间复杂度: O(1)**
**辅助空间: O(1)**


***注意：*** *++a 和 a++ 都是递增运算符，但是，两者略有不同。*

*在 ++a 中，变量的值首先递增，然后在程序中使用它。在 a++ 中，首先分配变量的值，然后递>增。递减运算符也会发生类似情况。*



**B） 二元运算符：**这些运算符操作或处理两个操作数。例如：Addition（+）、Subtraction（-） 等。


| 名字 | 象征 |          描述          |             例             |
| :------------: | :------------: | :------------------------------: | :----------------------------------: |
|      加法      |       +        |          添加两个操作数          | int a = 3， b = 6;int c = a+b;c = 9  |
|      减法      |       –        | 从第一个操作数中减去第二个操作数 | int a = 9， b = 6;int c = a-b;c = 3  |
|      乘法      |       *        |          两个操作数相乘          | int a = 3， b = 6;int c = a*b;c = 18 |
|      划分      |       /        |  将第一个操作数除以第二个操作数  | int a = 12， b = 6;int c = a/b;c = 2 |
|     模运算     |       %        |       返回余数 - 整数除法        | int a = 8， b = 6;int c = a%b;c = 2  |

***注意：*** *模运算符 （%） 运算符只能与整数一起使用。*



**例**

```C++
// CPP Program to demonstrate the Binary Operators
#include <iostream>
using namespace std;

int main()
{
    int a = 8, b = 3;

    // Addition operator
    cout << "a + b = " << (a + b) << endl;
  
    // Subtraction operator
    cout << "a - b = " << (a - b) << endl;
  
    // Multiplication operator
    cout << "a * b = " << (a * b) << endl;
  
    // Division operator
    cout << "a / b = " << (a / b) << endl;
  
    // Modulo operator
    cout << "a % b = " << (a % b) << endl;

    return 0;
}
```

**输出**

```C++
a + b = 11
a - b = 5
a * b = 24
a / b = 2
a % b = 2
```

**时间复杂度: O(1)**
**辅助空间: O(1)**



### 2） 关系运算符

这些运算符用于比较两个操作数的值。例如，'>' 检查一个操作数是否大于另一个操作数，等等。结果返回一个布尔值，即 **true** 或 **false。**

| 名字 | 象征 |              描述               |           例            |
| :------------: | :------------: | :----------------------------------------: | :-------------------------------: |
|      等于      |       ==       |           检查两个操作数是否相等           | int a = 3， b = 6;a==b;返回 false |
|      大于      |       >        |    检查第一个操作数是否大于第二个操作数    | int a = 3， b = 6;a>b;返回 false  |
|   大于或等于   |       >=       | 检查第一个操作数是否大于或等于第二个操作数 | int a = 3， b = 6;a>=b;返回 false |
|      小于      |       <        |    检查第一个操作数是否小于第二个操作数    |  int a = 3， b = 6;a<b;返回 true  |
|   小于或等于   |       <=       | 检查第一个操作数是否小于或等于第二个操作数 | int a = 3， b = 6;a<=b;返回 true  |
|     不等于     |       !=       |          检查两个操作数是否不相等          | int a = 3， b = 6;a！=b;返回 true |

**例**

```C++
// CPP Program to demonstrate the Relational Operators
#include <iostream>
using namespace std;

int main()
{
    int a = 6, b = 4;

    // Equal to operator
    cout << "a == b is " << (a == b) << endl;
  
    // Greater than operator
    cout << "a > b is " << (a > b) << endl;
  
    // Greater than or Equal to operator
    cout << "a >= b is " << (a >= b) << endl;
  
    //  Lesser than operator
    cout << "a < b is " << (a < b) << endl;
  
    // Lesser than or Equal to operator
    cout << "a <= b is " << (a <= b) << endl;
  
    // true
    cout << "a != b is " << (a != b) << endl;

    return 0;
}
```


**输出**

```C++
a == b is 0
a > b is 1
a >= b is 1
a < b is 0
a <= b is 0
a != b is 1
```
**时间复杂度: O(1)**
**辅助空间: O(1)**

这里， **0** 表示 **false **， **1 ** 表示**true **。要了解更多信息，请参阅文章 – [关系运算符](https://www.geeksforgeeks.org/relational-operators-in-c/)。



### 3） 逻辑运算符

这些运算符用于组合两个或多个条件或约束，或补充对所考虑的原始条件的评估。结果返回一个布尔值，即 **true** 或 **false **。

|   名字   | 象征 |                     描述                      |                  例                   |
| :------: | :--: | :-------------------------------------------: | :-----------------------------------: |
| 逻辑 AND |  &&  | 仅当所有操作数均为 true 或非零时，才返回 true |   int a = 3， b = 6;A&&B;返回 true    |
| 逻辑 OR  | \|\| |   如果任一操作数为 true 或非零，则返回 true   | int a = 3， b = 6;一个\|\|b;返回 true |
| 逻辑 NOT |  !   |     如果操作数为 false 或零，则返回 true      |      int a = 3;！一个;返回 false      |

**例**

```c++
// CPP Program to demonstrate the Logical Operators
#include <iostream>
using namespace std;

int main()
{
    int a = 6, b = 4;

    // Logical AND operator
    cout << "a && b is " << (a && b) << endl;
  
    // Logical OR operator
    cout << "a || b is " << (a || b) << endl;
  
    // Logical NOT operator
    cout << "!b is " << (!b) << endl;

    return 0;
}
```

**输出**

```C++
a && b is 1
a ! b is 1
!b is 0
```

**时间复杂度: O(1)**
**辅助空间: O(1)**

这里， **0** 表示 **false **， **1 ** 表示 **true **。要了解更多信息，请参阅文章 – [逻辑运算符](https://www.geeksforgeeks.org/operators-in-c-set-2-relational-and-logical-operators)。



### 4） 按位运算符

这些运算符用于对操作数执行 bit-level 操作。运算符首先转换为位级，然后对操作数执行计算。可以在位级别执行加法、减法、乘法等数学运算，以加快处理速度。

|     名字     | 象征 |                             描述                             |                  例                   |
| :----------: | :--: | :----------------------------------------------------------: | :-----------------------------------: |
|  二进制 AND  |  &   |      如果两个操作数中都存在 bit，则向计算结果复制一个位      |  int a = 2， b = 3;（a & b）;返回 2   |
|  二进制 OR   |  \|  |    如果计算结果存在于任何操作数中，则向计算结果复制一个位    | int a = 2， b = 3;（一 \| 二）;返回 3 |
|  二进制 XOR  |  ^   | 如果该位存在于任一操作数中，但不是同时存在于两个操作数中，则将其复制到计算结果中 |  int a = 2， b = 3;（a ^ b）;返回 1   |
|     左移     |  <<  |               将值向左移动右操作数指定的位数。               |  int a = 2， b = 3;（a << 1）;返回 4  |
|     右移     |  >>  |               将值向右移动右操作数指定的位数。               | int a = 2， b = 3;（第 1 >>）;返回 1  |
| 一个人的补充 |  ~   |            将二进制数字 1 更改为 0，将 0 更改为 1            |       int b = 3;（~b）;返回 -4        |

***注：*** *只有* ***char*** *和* ***int*** *数据类型可以与按位运算符一起使用。*



**例**

```C++
// CPP Program to demonstrate the Bitwise Operators
#include <iostream>
using namespace std;

int main()
{
    int a = 6, b = 4;

    // Binary AND operator
    cout << "a & b is " << (a & b) << endl;

    // Binary OR operator
    cout << "a | b is " << (a | b) << endl;

    // Binary XOR operator
    cout << "a ^ b is " << (a ^ b) << endl;

    // Left Shift operator
    cout << "a<<1 is " << (a << 1) << endl;

    // Right Shift operator
    cout << "a>>1 is " << (a >> 1) << endl;

    // One’s Complement operator
    cout << "~(a) is " << ~(a) << endl;

    return 0;
}
```

**输出**

```
a & b is 4
a | b is 6
a ^ b is 2
a<<1 is 12
a>>1 is 3
~(a) is -7
```

**时间复杂度: O(1)**
**辅助空间: O(1)**

要了解更多信息，请参阅文章 – [按位运算符](https://www.geeksforgeeks.org/bitwise-operators-in-c-cpp)。



### 5） 赋值运算符

这些运算符用于为变量赋值。赋值运算符的左侧操作数是变量，赋值运算符的右侧操作数是值。右侧的值必须与左侧的变量具有相同的数据类型，否则编译器将引发错误。

|       名字       | 象征 |                             描述                             |              例               |
| :--------------: | :--: | :----------------------------------------------------------: | :---------------------------: |
|    赋值运算符    |  =   |                  将右侧的值分配给左侧的变量                  |        int a = 2;a = 2        |
| 加法和赋值运算符 |  +=  | 首先将左侧变量的当前值与右侧的值相加，然后将结果分配给左侧的变量 | int a = 2， b = 4;a+=b;a = 6  |
| 减法和赋值运算符 |  -=  | 首先从左侧变量的当前值中减去右侧的值，然后将结果分配给左侧的变量 | int a = 2， b = 4;a-=b;a = -2 |
| 乘法和赋值运算符 |  *=  | 首先将左侧变量的当前值乘以右侧的值，然后将结果分配给左侧的变量 | int a = 2， b = 4;a*=b;a = 8  |
| 除法和赋值运算符 |  /=  | 首先将左侧变量的当前值除以右侧的值，然后将结果分配给左侧的变量 | int a = 4， b = 2;a /=b;a = 2 |

**例**

```C++
// CPP Program to demonstrate the Assignment Operators
#include <iostream>
using namespace std;

int main()
{
    int a = 6, b = 4;

    // Assignment Operator
    cout << "a = " << a << endl;
  
    //  Add and Assignment Operator
    cout << "a += b is " << (a += b) << endl;
  
    // Subtract and Assignment Operator
    cout << "a -= b is " << (a -= b) << endl;
  
    //  Multiply and Assignment Operator
    cout << "a *= b is " << (a *= b) << endl;
  
    //  Divide and Assignment Operator
    cout << "a /= b is " << (a /= b) << endl;

    return 0;
}
```

**输出**

```
a = 6
a += b is 10
a -= b is 6
a *= b is 24
a /= b is 6
```

**时间复杂度: O(1)**
**辅助空间: O(1)**



### 6） 三元或条件运算符 （？:)

此运算符根据条件返回值。

```
Expression1? Expression2: Expression3
```

三元运算符 **？**根据 **Expression1 ** 的计算确定答案。如果为 **true **，则计算 **Expression2 ** 并将其用作表达式的答案。如果 **Expression1 ** 为 **false **，则计算 **Expression3 ** 并将其用作表达式的答案。

这个运算符需要**三个操作数**，因此它被称为三元运算符。

**例**

```C++
// CPP Program to demonstrate the Conditional Operators
#include <iostream>
using namespace std;

int main()
{
    int a = 3, b = 4;

    // Conditional Operator
    int result = (a < b) ? b : a;
    cout << "The greatest number is " << result << endl;

    return 0;
}
```

**输出**

```C++
The greatest number is 4
```

**时间复杂度: O(1)**
**辅助空间: O(1)**



**7）** 除了上面讨论的运算符之外，C++ 中还有一些其他常见的运算符。以下是详细讨论的这些运算符的列表：

**A） sizeof 运算符：**此一元运算符用于计算其操作数或变量的大小。

```C++
sizeof(char); // returns 1
```

**B） 逗号运算符（，）：**此二元运算符（由标记表示）用于计算其第一个操作数并丢弃结果，然后计算第二个操作数并返回此值（和类型）。它用于将各种表达式组合在一起。

```C++
int a = 6;
int b = (a+1, a-2, a+5); // b = 11
```

**C） -> 运算符：**此运算符用于访问类或结构体的变量。

```C++
cout<<emp->first_name;
```

**D） Cast 运算符：**此一元运算符用于将一种数据类型转换为另一种数据类型。

```C++
float a = 11.567;
int c = (int) a; // returns 11
```

**E） 点运算符（.）：**此运算符用于访问 C++ 中结构变量或类对象的成员。

```C++
cout<<emp.first_name;
```

**F） & 运算符：**这是一个指针运算符，用于表示操作数的内存地址。

**G） \* 运算符：**这是一个间接运算符

```c++
// CPP Program to demonstrate the & and * Operators
#include <iostream>
using namespace std;

int main()
{
    int a = 6;
    int* b;
    int c;
    //  & Operator
    b = &a;

    // * Operator
    c = *b;
    cout << " a = " << a << endl;
    cout << " b = " << b << endl;
    cout << " c = " << c << endl;

    return 0;
}
```

**输出**

```C++
 a = 6
 b = 0x7ffe8e8681bc
 c = 6
```

**H） <<运算符：**称为插入运算符。它与 cout 一起使用以打印输出。

**I） >>运算符：**称为提取运算符。它与 cin 一起使用以获取输入。

```C++
int a;
cin>>a;
cout<<a;
```

**时间复杂度: O(1)**
**辅助空间: O(1)**



### 运算符优先级图

<table><thead><tr><th><span _msttexthash="4006600" _msthash="1661">优先权</span></th><th><span _msttexthash="5310253" _msthash="1662">运算符</span></th><th><span _msttexthash="6157333" _msthash="1663">描述</span></th><th><span _msttexthash="8194004" _msthash="1664">关联性</span></th></tr></thead><tbody><tr><td rowspan="5"><span _msttexthash="9243" _msthash="1665">1.</span></td><td><span>()</span></td><td><span _msttexthash="41163408" _msthash="1666">括号（函数调用）</span></td><td><span _msttexthash="9591296" _msthash="1667">从左到右</span></td></tr><tr><td><span>[]</span></td><td><span _msttexthash="45736366" _msthash="1668">方括号 （数组下标）</span></td><td><span>&nbsp;</span></td></tr><tr><td><span _msttexthash="4186" _msthash="1669">.</span></td><td><span _msttexthash="42784495" _msthash="1670">通过对象名称选择成员</span></td><td><span>&nbsp;</span></td></tr><tr><td><span>-&gt;</span></td><td><span _msttexthash="32489340" _msthash="1671">通过指针选择成员</span></td><td><span>&nbsp;</span></td></tr><tr><td><span _msttexthash="1081314" _msthash="1672">++/–</span></td><td><span _msttexthash="21903440" _msthash="1673">后缀递增/递减</span></td><td><span>&nbsp;</span></td></tr><tr><td rowspan="7"><span _msttexthash="9334" _msthash="1674">2.</span></td><td><span _msttexthash="1081314" _msthash="1675">++/–</span></td><td><span _msttexthash="21862581" _msthash="1676">前缀递增/递减</span></td><td><span _msttexthash="9657518" _msthash="1677">从右到左</span></td></tr><tr><td><span>+/-</span></td><td><span _msttexthash="9456343" _msthash="1678">一元加/减</span></td><td><span>&nbsp;</span></td></tr><tr><td><span _msttexthash="16107" _msthash="1679">!~</span></td><td><span _msttexthash="32951880" _msthash="1680">逻辑求反/按位补码</span></td><td><span>&nbsp;</span></td></tr><tr><td><span _msttexthash="20365033" _msthash="1681">（类型）</span></td><td><span _msttexthash="89843780" _msthash="1682">Cast （将值转换为类型的临时值）</span></td><td><span>&nbsp;</span></td></tr><tr><td><span>*</span></td><td><span _msttexthash="5334199" _msthash="1683">引用</span></td><td><span>&nbsp;</span></td></tr><tr><td><span>&amp;</span></td><td><span _msttexthash="33337447" _msthash="1684">地址（操作数）</span></td><td><span>&nbsp;</span></td></tr><tr><td><span _msttexthash="4387409" _msthash="1685">size的</span></td><td><span _msttexthash="93249871" _msthash="1686">确定此实现的大小（以字节为单位）</span></td><td><span>&nbsp;</span></td></tr><tr><td><span _msttexthash="9425" _msthash="1687">3.</span></td><td><span _msttexthash="24908" _msthash="1688">*,/,%</span></td><td><span _msttexthash="23042331" _msthash="1689">乘法/除法/模数</span></td><td><span _msttexthash="9591296" _msthash="1690">从左到右</span></td></tr><tr><td><span _msttexthash="9516" _msthash="1691">4.</span></td><td><span>+/-</span></td><td><span _msttexthash="11534588" _msthash="1692">加法/减法</span></td><td><span _msttexthash="9591296" _msthash="1693">从左到右</span></td></tr><tr><td><span _msttexthash="9607" _msthash="1694">5.</span></td><td><span _msttexthash="33774" _msthash="1695">&lt;&lt; , &gt;&gt;</span></td><td><span _msttexthash="38016953" _msthash="1696">左按位移，右按位移</span></td><td><span _msttexthash="9591296" _msthash="1697">从左到右</span></td></tr><tr><td rowspan="2"><span _msttexthash="9698" _msthash="1698">6.</span></td><td><span _msttexthash="24986" _msthash="1699">&lt; , &lt;=</span></td><td><span _msttexthash="32585618" _msthash="1700">关系 小于/小于或等于</span></td><td><span _msttexthash="9591296" _msthash="1701">从左到右</span></td></tr><tr><td><span _msttexthash="25402" _msthash="1702">&gt; , &gt;=</span></td><td><span _msttexthash="32382506" _msthash="1703">关系大于/大于或等于</span></td><td><span _msttexthash="9591296" _msthash="1704">从左到右</span></td></tr><tr><td><span _msttexthash="9789" _msthash="1705">7.</span></td><td><span _msttexthash="30056" _msthash="1706">== , !=</span></td><td><span _msttexthash="23649444" _msthash="1707">关系等于/不等于</span></td><td><span _msttexthash="9591296" _msthash="1708">从左到右</span></td></tr><tr><td><span _msttexthash="9880" _msthash="1709">8.</span></td><td><span>&amp;</span></td><td><span _msttexthash="4445896" _msthash="1710">按位 AND</span></td><td><span _msttexthash="9591296" _msthash="1711">从左到右</span></td></tr><tr><td><span _msttexthash="9971" _msthash="1712">9.</span></td><td><span>^</span></td><td><span _msttexthash="10528401" _msthash="1713">按位异或</span></td><td><span _msttexthash="9591296" _msthash="1714">从左到右</span></td></tr><tr><td><span _msttexthash="14833" _msthash="1715">10.</span></td><td><span _msttexthash="11284" _msthash="1716">|</span></td><td><span _msttexthash="25916163" _msthash="1717">按位（含 OR）</span></td><td><span _msttexthash="9591296" _msthash="1718">从左到右</span></td></tr><tr><td><span _msttexthash="14937" _msthash="1719">11.</span></td><td><span>&amp;&amp;</span></td><td><span _msttexthash="7209774" _msthash="1720">逻辑 AND</span></td><td><span _msttexthash="9591296" _msthash="1721">从左到右</span></td></tr><tr><td><span _msttexthash="15041" _msthash="1722">12.</span></td><td><span _msttexthash="24180" _msthash="1723">||</span></td><td><span _msttexthash="7202208" _msthash="1724">逻辑 OR</span></td><td><span _msttexthash="9591296" _msthash="1725">从左到右</span></td></tr><tr><td><span _msttexthash="15145" _msthash="1726">13.</span></td><td><span _msttexthash="11765" _msthash="1727">?:</span></td><td><span _msttexthash="9705644" _msthash="1728">三元条件</span></td><td><span _msttexthash="9657518" _msthash="1729">从右到左</span></td></tr><tr><td rowspan="6"><span _msttexthash="15249" _msthash="1730">14.</span></td><td><span>=</span></td><td><span _msttexthash="5779306" _msthash="1731">分配</span></td><td><span _msttexthash="9657518" _msthash="1732">从右到左</span></td></tr><tr><td><span _msttexthash="29978" _msthash="1733">+= , -=</span></td><td><span _msttexthash="20648524" _msthash="1734">加法/减法赋值</span></td><td><span>&nbsp;</span></td></tr><tr><td><span _msttexthash="30147" _msthash="1735">*= , /=</span></td><td><span _msttexthash="22831198" _msthash="1736">乘法/除法赋值</span></td><td><span>&nbsp;</span></td></tr><tr><td><span _msttexthash="28522" _msthash="1737">%= , &amp;=</span></td><td><span _msttexthash="22738846" _msthash="1738">模数/按位 AND 赋值</span></td><td><span>&nbsp;</span></td></tr><tr><td><span _msttexthash="44889" _msthash="1739">^= , |=</span></td><td><span _msttexthash="37895416" _msthash="1740">按位互斥/非独占 OR 赋值</span></td><td><span>&nbsp;</span></td></tr><tr><td><span>&lt;&gt;=</span></td><td><span _msttexthash="19872177" _msthash="1741">按位左/右分配</span></td><td><span>&nbsp;</span></td></tr><tr><td><span _msttexthash="15353" _msthash="1742">15.</span></td><td><span _msttexthash="4004" _msthash="1743">,</span></td><td><span _msttexthash="23012067" _msthash="1744">表达式分隔符</span></td><td><span _msttexthash="9591296" _msthash="1745">从左到右</span></td></tr></tbody></table>



夏天来了，也是提高技能的时候了！超过 5,000 名学习者现在已经完成了从 **DSA 基础知识到高级开发计划**（如全栈、后端开发、数据科学）的旅程。

当我们的 [DSA to Development： Coding Guide](https://gfgcdn.com/tu/Q8V/) 将帮助您在几个月内掌握所有这些时，为什么还要去其他任何地方呢！现在就申请我们的[DSA发展计划](https://gfgcdn.com/tu/Q8V/)，我们的顾问将与您联系以获得进一步的指导和支持。