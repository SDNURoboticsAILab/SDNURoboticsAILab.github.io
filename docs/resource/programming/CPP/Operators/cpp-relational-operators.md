---
comments: true
---

C++ 关系运算符
=====

在 C++ 编程语言中，我们有时需要比较值和表达式。这种比较使我们能够确定关系、做出决策并控制我们的程序流程。C++ 中的关系运算符提供了比较值和评估条件的方法。

在本文中，我们将了解 C++ 关系运算符，并了解它们在代码中进行逻辑比较的重要性。

## C++ 中的关系运算符

C++ 关系运算符用于比较两个值或表达式，基于此比较，它返回一个布尔值（**true** 或 **false**）作为结果。通常 **false** 表示为 **0，true** 表示为任何**非零值**（大部分为 **1**）。



### 如何使用 Relational Operator？

所有 C++ 关系运算符都是与两个操作数一起使用的二元运算符，如下所示：

```C++
operand1   relational_operator  operand2
expression1   relational_operator  expression2
```

## C++ 关系运算符的类型

我们在 C++ 中有六个关系运算符，下面将通过示例进行解释。

| S. 编号 | 关系运算符 |   意义   |
| :-----: | :--------: | :------: |
|   1.    |     >      |   大于   |
|   2.    |     <      |   小于   |
|   3.    |     >=     | 大于等于 |
|   4.    |     <=     | 小于等于 |
|   5.    |     ==     |   等于   |
|   6.    |     !=     |  不等于  |

### 1.大于 （ > ）

**大于 （ > ）** 运算符检查左操作数是否大于右操作数。如果满足条件，则返回 true，否则返回 false。

**例**

```C++
29 > 21 // returns true
12 > 12 // return false
10 > 57 // return false
```

### 2. 小于 （ < ）

**小于 （ < ）** 运算符检查左操作数是否小于右操作数。如果满足条件，则返回 true，否则返回 false。

**例**

```C++
2 < 21 // returns true
12 < 12 // return false
12 < 5 // return false
```

### 3. 大于或等于 （ >= ）

**大于或等于 （ >= ）** 运算符检查左操作数是否大于或等于右操作数。如果满足条件，则返回 true，否则返回 false。

**例**

```C++
29 >= 21 // returns true 
12 >= 12 // return true 
10 >= 58 // return false
```

### 4. 小于或等于 （ <= ）

**小于或等于 （ <= ）** 运算符检查左操作数是否小于或等于右操作数。如果满足条件，则返回 true，否则返回 false。

**例**

```C++
2 <= 21 // returns true 
12 <= 12 // return true 
12 <= 5 // return false
```

### 5. 等于 （ == ）

**等于 （ == ）** 运算符检查两个值是否相等。如果值相等，则返回 true，否则返回 false。

**例**

```C++
9 == 9 // returns true 
19 == 12 // return false
```

### 6. 不等于 （ ！= ）

**不等于 （ ！= ）** 运算符检查两个值是否不相等。如果值不同，则返回 true，如果值相等，则返回 false。

**例**

```C++
12 != 21 // returns true
12 != 12 // return false
```

## C++ 关系运算符示例

在下面的代码中，我们定义了两个具有一些整数值的变量，并通过使用 C++ 中的关系运算符比较它们来打印输出。在输出中，我们得到 1、0、0、0 和 1，其中 **0 表示** false，1 **表示 true。**



```C++
// C++ Program to illustrate the relational operators 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
    // variables for comparison 
    int a = 10; 
    int b = 6; 
  
    // greater than 
    cout << "a > b = " << (a > b) << endl; 
    
    // less than 
    cout << "a < b = " << (a < b) << endl; 
    
    // equal to 
    cout << "a == b = " << (a == b) << endl; 
    
    // not equal to 
    cout << "a != b = " << (a != b) << endl; 
  
    return 0; 
}
```



**输出**

```C++
a > b = 1
a < b = 0
a == b = 0
a != b = 1
```



夏天来了，也是提高技能的时候了！超过 5,000 名学习者现在已经完成了从 **DSA 基础知识到高级开发计划**（如全栈、后端开发、数据科学）的旅程。

当我们的 [DSA to Development： Coding Guide](https://gfgcdn.com/tu/Q8V/) 将帮助您在几个月内掌握所有这些时，为什么还要去其他任何地方呢！现在就申请我们的[DSA发展计划](https://gfgcdn.com/tu/Q8V/)，我们的顾问将与您联系以获得进一步的指导和支持。
