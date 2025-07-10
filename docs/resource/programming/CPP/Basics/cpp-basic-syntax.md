---
comments: true
---
# C++ 基本语法

语法指的是在编程语言中编写语句的规则和规定。它们也可以被看作是定义编程语言结构的语法规则。

[**C++ 语言**](https://www.geeksforgeeks.org/c-plus-plus/) 也有其自身功能所对应的语法。不同的语句有不同的语法来规定其用法，但 C++ 程序也有一些贯穿所有程序的基本语法规则。

## C++ 语法

我们可以通过下面的程序来学习 **C++ 基本语法**。

```cpp
#include <iostream>

// 标准命名空间
using namespace std;

// 主函数
int main() {

    // 声明变量
    int num1 = 24;
    int num2 = 34;

    int result = num1 + num2;

    // 输出
    cout << result << endl;

    // 返回语句
    return 0;
}
```

**输出**

```
58
```

上面的程序展示了一个包含头文件、主函数、命名空间声明等基本元素的 C++ 程序。让我们逐一理解它们。

### 1. 头文件

[头文件](https://www.geeksforgeeks.org/header-files-in-c-c-with-examples/) 包含了我们在程序中使用的函数和宏的定义。在 **第 1 行**，我们使用 **#include  <iostream>** 语句告诉编译器包含 **iostream** 头文件库，该库存储了我们用于输入和输出的 `cin` 和 `cout` 标准输入/输出流的定义。**#include** 是一个预处理器指令，我们用它来导入头文件。

### 2. 命名空间

C++ 中的[命名空间](https://www.geeksforgeeks.org/namespace-in-c/)用于提供一个作用域或一个区域，在其中我们可以定义标识符。在 **第 2 行**，我们使用了 **using namespace std** 语句，用以指定我们将使用标准命名空间，所有标准库函数都在该命名空间中定义。

### 3. 主函数

在 **第 3 行**，我们将主函数定义为 **int main()**。[函数](https://www.geeksforgeeks.org/functions-in-cpp/)是任何 C++ 程序中最重要的部分。程序的执行总是从 `main` 函数开始。所有其他函数都由 `main` 函数调用。在 C++ 中，`main` 函数需要返回一个值来表示执行状态。

### 4. 代码块

代码块是被 **{ }** 大括号括起来的一组语句。`main` 函数的主体是从 **第 4 行** 到 **第 9 行**，被 **{ }** 括起来的部分。

### 5. 分号

你可能已经注意到，上面代码中的每条语句后面都有一个 ( **;** ) 分号符号。它用于终止程序中的每一行语句。

### 6. 标识符

我们使用[标识符](https://www.geeksforgeeks.org/c-identifiers/)来命名[**变量**](https://www.geeksforgeeks.org/cpp-variables/)、函数和其他用户定义的数据类型。标识符可以由大写和小写字母、下划线和数字组成。第一个字符必须是下划线或字母。

### 7. 关键字

在 C++ 编程语言中，有一些保留字在 C++ 程序中具有特殊的含义。它们不能用作标识符。例如，我们程序中使用的 **int**、**return** 和 **using** 就是一些[关键字](https://www.geeksforgeeks.org/keywords-in-c/)。

### 8. 基本输出 cout

在第 7 行，我们使用了 [`cout`](https://www.geeksforgeeks.org/cout-in-c/) 流对象（在 [`` 头文件](https://www.geeksforgeeks.org/basic-input-output-c/)中声明）将两个数的和打印到标准输出流（stdout）。

### 9. 注释

你可以在代码中看到带有两个正斜杠 (//) 和一些文本的内容，这在 C++ 程序中被称为[**注释**](https://www.geeksforgeeks.org/cpp-comments/)。注释提供了关于代码或特定代码行的信息，以提高可读性。

## C++ 中的面向对象编程

C++ 编程语言同时支持面向过程编程和面向对象编程。上面的例子是基于面向过程编程范式的。所以让我们用另一个例子来讨论 [C++ 中的面向对象编程](https://www.geeksforgeeks.org/object-oriented-programming-in-cpp/)。

```cpp
#include <iostream>
using namespace std;

class Calculate {

    // 访问修饰符
public:

    // 数据成员
    int num1 = 50;
    int num2 = 30;

    // 成员函数
    void addition() {
        int result = num1 + num2;
        cout << result << endl;
    }
};

int main() {

    // 对象声明
    Calculate add;
    
    // 调用成员函数
    add.addition();

    return 0;
}
```

**输出**

```
80
```

### 1. 类

[类](https://www.geeksforgeeks.org/c-classes-and-objects/)是一种用户定义的数据类型。一个类有它自己的属性（数据成员）和行为（成员函数）。在 **第 3 行**，我们声明了一个名为 **Calculate** 的类，它的主体从 **第 3 行** 扩展到 **第 7 行**。

### 2. 类成员

类中的属性或数据由数据成员定义，而操作这些数据成员的函数被称为成员函数。

在上面的例子中，`num1` 和 `num2` 是数据成员，而 `addition()` 是一个操作这两个数据成员的成员函数。这里有一个关键字 **public**，它是一个**访问修饰符**。[访问修饰符](https://www.geeksforgeeks.org/access-modifiers-in-c/)决定了谁可以访问这些数据成员和成员函数。

### 3. 对象

[对象](https://www.geeksforgeeks.org/c-classes-and-objects/)是类的一个实例。类本身只是一个模板，不会被分配任何内存。要使用类中定义的数据和方法，我们必须创建该类的一个对象。