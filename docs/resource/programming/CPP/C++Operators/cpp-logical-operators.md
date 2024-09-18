---
comments: true
---

C++ 逻辑运算符
=====

在 C++ 编程语言中，逻辑运算符是允许您组合或修改条件以进行逻辑计算的符号。它们用于对布尔值（**true** 或 **false**）执行逻辑运算。

在 C++ 中，有三个逻辑运算符：

1. **逻辑 AND （ & & ） 运算符**
2. **逻辑 OR （ || ）运算符**
3. **逻辑 NOT （ ！）运算符**

让我们详细讨论每个运算符。

## 1. 逻辑 AND 运算符 （ & & ）

C++ **逻辑 AND 运算符 （&&）** 是一个二元运算符，如果其两个操作数均为 true，则返回 true。否则，它将返回 false。下面是 AND 运算符的真值表：

| 操作数 1 | 操作数 2 |     结果     |
| :------: | :------: | :----------: |
|    真    |    真    | **真** |
|    真    |    假    | **假** |
|    假    |    真    | **假** |
|    假    |    假    | **假** |

***注意：*** *在 C 语言中，false 表示为 0，而 true 表示为任何非零值，通常为 1。*



### 逻辑 AND 的语法

```C++
expression1  &&  expression2
```

### C++ 中的逻辑 AND 示例

```C++
// C++ Program to illustrate the logical AND Operator 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
  
    // initialize variables 
    int age = 25; 
    bool isStudent = true; 
  
    // Using AND operator in if condition 
    if (age > 18 && isStudent) { 
        cout << "You are eligible for a student discount."
             << endl; 
    } 
    else { 
        cout << "You are not eligible for a student "
                "discount."
             << endl; 
  
        return 0; 
    }
```

**输出**

```C++
You are eligible for a student discount.
```

**说明：**在上面的代码中，我们在 if 条件中使用了 **AND** 运算符来检查年龄是否大于 18 岁，该人是否为检查。如果两个条件都成立，则将打印消息“您有资格享受学生折扣”。否则，将执行 else 语句。



## 2. 逻辑 OR 运算符 （ || ）

C++ **逻辑 OR 运算符 （ || ）** 是一个二元运算符，如果其至少有一个操作数为 true，则返回 true。仅当两个操作数均为 false 时，它才返回 false。下面是 OR 运算符的真值表：

| 操作数 1 | 操作数 2 |     结果     |
| :------: | :------: | :----------: |
|    真    |    真    | **真** |
|    真    |    假    | **真** |
|    假    |    真    | **真** |
|    假    |    假    | **假** |

### 逻辑 OR 的语法

```C++
expression1  ||  expression2
```

### C++ 中的逻辑 OR 示例

```C++
// C++ program to demonstrate the logical or operator 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
  
    int num = 7; 
  
    // using logical or for conditional statement 
    if (num <= 0 || num >= 10) { 
        cout 
            << "The number is outside the range of 0 to 10."
            << endl; 
    } 
    else { 
        cout << "The number is between 0 to 10." << endl; 
    } 
  
    return 0; 
}
```

**输出**

```C++
The number is between 0 to 10.
```

**说明：**在上面的代码中，条件 **num < 0 || num > 10** 检查数字是小于等于 0 **还是**大于等于 10。如果这些条件中的任何一个为 true，则将打印消息 “The number is outside the range of 0 to 10..” 否则打印 else 语句。



## 3. 逻辑 NOT 运算符 （ ！ ）

C++ **逻辑 NOT 运算符 （ ！** ） 是用于否定 condition 值的一元运算符。如果条件为 false，则返回 true，如果条件为 true，则返回 false。下面是 NOT 运算符的真值表：

| 操作数 1 |     结果     |
| :------: | :----------: |
|    真    | **假** |
|    假    | **真** |

### 逻辑 NOT 的语法

```C++
! expression
```

### C++ 中的逻辑 NOT 示例

```C++
// C++ program to illustrate the logical not operator 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
  
    bool isLoggedIn = false; 
  
    // using logical not operator 
    if (!isLoggedIn) { 
        cout << "Please log in to access this feature."
             << endl; 
    } 
    else { 
        cout << "Welcome to GeeksforGeeks!" << endl; 
    } 
  
    return 0; 
}
```

**输出**

```C++
Please log in to access this feature.
```

**说明：**在上面的代码中，条件 **'！isLoggedIn'** 检查用户是否未登录。如果条件为 true（即用户未登录），则将显示消息 “Please log in to access this feature.”，否则将打印 else 语句。



## 结论

使用 C++ 中的逻辑运算符，可以组合条件并创建富有表现力的逻辑。在代码中处理决策和分支时，它们非常宝贵。通过掌握这些逻辑运算符，您可以编写更健壮、更灵活的程序。

夏天来了，也是提高技能的时候了！超过 5,000 名学习者现在已经完成了从 **DSA 基础知识到高级开发计划**（如全栈、后端开发、数据科学）的旅程。

当我们的 [DSA to Development： Coding Guide](https://gfgcdn.com/tu/Q8V/) 将帮助您在几个月内掌握所有这些时，为什么还要去其他任何地方呢！现在就申请我们的[DSA发展计划](https://gfgcdn.com/tu/Q8V/)，我们的顾问将与您联系以获得进一步的指导和支持。

