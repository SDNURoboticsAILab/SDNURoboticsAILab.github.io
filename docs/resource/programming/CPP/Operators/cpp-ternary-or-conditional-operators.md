---
comments: true
---

C++ 三元/条件运算符
=====

在 C++ 中，**三元** **或条件运算符 （ ？ ： ）** 是编写条件语句的最短形式。它可以用作内联条件语句来代替 if-else 来执行一些条件代码。

## 三元运算符 （ ？ ： ） 的语法

三元（或条件）运算符的语法为：

```C++
expression ? statement_1 : statement_2;
```

顾名思义，三元运算符适用于三个操作数，其中

- **expression：**要评估的条件。
- **statement_1**：表达式计算结果为 true 时将执行的语句。
- **statement_2：**表达式计算结果为 false 时要执行的代码。



// 图像

上述三元运算符的语句等效于下面给出的 if-else 语句：

```C++
if ( condition ) {
    statement1;
}
else {
    statement2;
}
```



## C++ 中的三元运算符示例

```C++
// C++ program to illustrate the use of ternary operator 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
  
    // creating a variable 
    int num, test = 40; 
  
    // assigning the value of num based on the value of test 
    // variable 
    num = test < 10 ? 10 : test + 10; 
  
    printf("Num - Test = %d", num - test); 
  
    return 0; 
}
```

**输出**

```C++
Num - Test = 10
```

在上面的代码中，我们使用了三元运算符， 根据另一个名为 test 的变量的值来分配变量 **num** 的值。

***注意：*** *三元运算符的优先级排名第三，因此我们需要使用这些表达式，以避免由于运算符优先级管理不当而导致的错误。*



## C++ 嵌套三元运算符

嵌套的三元运算符定义为在另一个三元运算符中使用一个三元运算符。与 if-else 语句一样，三元运算符也可以相互嵌套。

### 在 C++ 中嵌套三元运算符的示例

在下面的代码中，我们将使用嵌套的三元运算符找到三个数字中最大的一个。

```C++
// C++ program to find the largest of the three number using 
// ternary operator 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
  
    // Initialize variable 
    int A = 39, B = 10, C = 23; 
  
    // Evaluate largest of three using ternary operator 
    int maxNum 
        = (A > B) ? ((A > C) ? A : C) : ((B > C) ? B : C); 
  
    cout << "Largest number is " << maxNum << endl; 
  
    return 0; 
}
```

**输出**

```C++
Largest number is 39
```

正如我们所看到的，可以将三元运算符彼此嵌套，但代码变得难以阅读和理解。因此，通常避免使用嵌套的三元运算符。

此外，三元运算符只应用于短条件代码。对于较大的代码，应首选其他条件语句。



夏天来了，也是提高技能的时候了！超过 5,000 名学习者现在已经完成了从 **DSA 基础知识到高级开发计划**（如全栈、后端开发、数据科学）的旅程。

当我们的 [DSA to Development： Coding Guide](https://gfgcdn.com/tu/Q8V/) 将帮助您在几个月内掌握所有这些时，为什么还要去其他任何地方呢！现在就申请我们的[DSA发展计划](https://gfgcdn.com/tu/Q8V/)，我们的顾问将与您联系以获得进一步的指导和支持。
