---
comments: true
---

C++ 算术运算符
=====

C++ 中的算术运算符用于对操作数执行算术或数学运算。例如，'**+**' 用于加法，'**–**' 用于减法，'*****' 用于乘法，等等。简单来说，算术运算符用于对变量和数据执行算术运算;它们遵循运算符和操作数之间的相同关系。

**C++ 算术运算符有 2 种类型：**

1. **一元算术运算符**
2. **二元算术运算符**

### 1. 二元算术运算符

这些运算符操作或使用两个操作数。C++ 提供了 **5** 个二进制*算术运算符*来执行算术函数：

| 算子  | 运算符名称 |                操作                | 实现 |
| :---: | :--------: | :--------------------------------: | :--: |
| **+** |    加法    |      用于计算两个操作数的加法      | x+y  |
| **–** |    减法    |      用于计算两个操作数的减法      | x-y  |
| ***** |    乘法    |      用于计算两个操作数的乘法      | x*y  |
| **/** |    取商    |      用于计算两个操作数的除法      | x/y  |
| **%** |    取余    | 用于计算两个操作数后计算 Remainder | x%y  |

**例**

```cpp
// C++ program to execute all 5 
// arithmetic function 
#include <iostream> 
using namespace std; 
 
int main() 
{ 
  int GFG1, GFG2; 
  GFG1 = 10; 
  GFG2 = 3; 
 
  // printing the sum of GFG1 and GFG2 
  cout<< "GFG1 + GFG2= " << (GFG1 + GFG2) << endl; 
 
  // printing the difference of GFG1 and GFG2 
  cout << "GFG1 - GFG2 = " << (GFG1 - GFG2) << endl; 
 
  // printing the product of GFG1 and GFG2 
  cout << "GFG1 * GFG2 = " << (GFG1 * GFG2) << endl; 
 
  // printing the division of GFG1 by GFG2 
  cout << "GFG1 / GFG2 = " << (GFG1 / GFG2) << endl; 
 
  // printing the modulo of GFG1 by GFG2 
  cout << "GFG1 % GFG2 = " << (GFG1 % GFG2) << endl; 
 
  return 0; 
}
```

**输出**

```
GFG1 + GFG2= 13
GFG1 - GFG2 = 7
GFG1 * GFG2 = 30
GFG1 / GFG2 = 3
GFG1 % GFG2 = 1
```



### 2. 一元运算符

这些运算符操作或使用单个操作数。


|    算子    | 象征 |         操作         |    实现    |
| :--------: | :--: | :------------------: | :--------: |
| 递减运算符 |  —   | 将变量的整数值减少 1 | –x 或 x —  |
| 递增运算符 |  ++  | 将变量的整数值增加 1 | ++x 或 x++ |

**例**

```cpp
// C++ Program to demonstrate the 
// increment and decrement operators 
#include <iostream> 
using namespace std; 
 
int main() 
{ 
  int x = 5; 
 
  // This statement Incremented 1 
  cout << "x++ is " << x++ << endl; 
 
  // This statement Incremented 1 
  // from already Incremented 
  // statement resulting in 
  // Incrementing of 2 
  cout << "++x is " << ++x << endl; 
 
  int y = 10; 
  
  // This statement Decremented 1 
  cout << "y-- is " << y-- << endl; 
 
  // This statement Decremented 1 
  // from already Decremented 
  // statement resulting in 
  // Decrementing of 2 
  cout << "--y is " << --y << endl; 
 
  return 0; 
}
```

**输出**

```
x++ is 5
++x is 7
y-- is 10
--y is 8
```



*在 **++x** 中，变量的值首先增加/递增，然后再在程序中使用。*

*在 **x++** 中，变量的值在增加/递增之前被分配。*

*递减运算符也会发生类似情况。*



夏天来了，也是提高技能的时候了！超过 5,000 名学习者现在已经完成了从 **DSA 基础知识到高级开发计划**（如全栈、后端开发、数据科学）的旅程。

当我们的 [DSA to Development： Coding Guide](https://gfgcdn.com/tu/Q8V/) 将帮助您在几个月内掌握所有这些时，为什么还要去其他任何地方呢！现在就申请我们的[DSA发展计划](https://gfgcdn.com/tu/Q8V/)，我们的顾问将与您联系以获得进一步的指导和支持。

