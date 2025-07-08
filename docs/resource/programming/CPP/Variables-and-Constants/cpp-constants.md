# C++中的常量

在C++中，常量是指在程序执行过程中保持不变的值。本文将讨论在C++中定义和使用常量的各种方法。

## C++中的常量

C++中的常量指的是具有固定值的变量，这些值不能被更改。一旦在程序中定义了常量，它们在程序的整个执行过程中保持不变。常量通常以只读标记的形式存储在程序的代码段内存中。它们可以是C++中任何可用的数据类型，例如int、char、string等。

## 如何在C++中定义常量？

我们可以通过三种方式在C++中定义常量：

1. 使用 `const` 关键字
2. 使用 `constexpr` 关键字
3. 使用 `#define` 预处理器

下面我们详细讨论这些方法。

### 1. 使用 `const` 关键字定义常量

使用 `const` 关键字定义常量是C++从C语言继承下来的较老方法。在这种方法中，我们在变量定义中添加 `const` 关键字，如下所示：

`const` 关键字的语法：

```
const 数据类型 变量名 = 值;
```

> 首先使用 `const` 关键字以确保变量是常量，然后是常量变量的数据类型，接着是常量变量的名称，最后给常量变量赋予适当的值。
>
> 注意：我们必须在声明时初始化常量变量，因为程序中后续无法修改其值。

![How to declare constants](https://media.geeksforgeeks.org/wp-content/uploads/20230306220005/how-to-declare-constants-in-c.png)

 

### **`const` 关键字示例**

- C++

```
// C++程序演示如何使用const关键字
#include <iostream>
using namespace std;

int main()
{
    // 声明一个变量
    int var = 10;

    // 声明一个常量变量
    const int cons = 24;

    cout << "初始值:" << endl;
    cout << "var: " << var << endl;
    cout << "cons: " << cons << endl;

    // 尝试更改两个常量的值
    var = 24;
    cons = 0; // 这将导致错误

    cout << "最终值:" << endl;
    cout << "var: " << var << endl;
    cout << "cons: " << cons << endl;

    return 0;
}
```

**Output**

```
./Solution.cpp: 在函数'int main()':
./Solution.cpp:19:10: 错误: 只读变量'cons'的赋值
     cons = 0;
```

### 2. 使用 `constexpr` 关键字定义常量

`constexpr` 关键字类似于 `const` 关键字，也用于声明常量。但主要的区别在于 `constexpr` 常量在编译时初始化，这意味着其值必须在编译时已知。另一方面，`const` 关键字的常量可以在运行时或编译时初始化。

`constexpr` 关键字的语法：

```
constexpr 数据类型 变量名 = 值;
```

首先使用 `constexpr` 关键字以确保变量是常量，然后是常量变量的数据类型，接着是常量变量的名称，最后给常量变量赋予适当的值。

### **`constexpr` 关键字示例**

- C++

```
// C++程序演示constexpr关键字的使用
#include <iostream>
using namespace std;

int main()
{
    // 定义常量
    int constexpr hoursIn_day = 24;

    // 打印值
    cout << "一天的总小时数: " << hoursIn_day;
}
```

**Output**

```
一天的总小时数: 24
```

上面的代码片段使用 `const` 和 `constexpr` 关键字定义了一天中的小时数常量（`hoursIn_day`）。

### 3. 使用 `#define` 预处理器定义常量

我们也可以使用 `#define` 定义常量。通过 `#define` 预处理器创建的常量称为“宏常量”。与其他方法不同，使用这种方法定义的常量仅作为其值的别名，在预处理期间进行替换。

由于缺乏类型安全，这种方法在C++中定义常量的优先级较低。

语法：

```
#define 宏名称 替代值
```

- 我们使用 `#define` 指令创建宏。首先以 `#define` 指令开始，然后是我们希望赋予宏的名称。接着，为宏提供一个替代值。每当预处理器在代码中遇到这个宏时，它会用指定的值替换宏。

  **示例**

- C++

```
// C++程序演示如何使用#define创建常量
#include <iostream>
using namespace std;

// 使用#define创建宏
#define Side 5

int main()
{
    // 使用常量
    const double area = Side * Side;

    cout << "边长为5的正方形的面积是 ";
    cout << area;

    return 0;
}
```

输出

```
边长为5的正方形的面积是 25
```

- **解释：**

  我们定义了宏常量 `Side` 的值为5。然后用它来计算正方形的面积。宏常量 `Side` 是全局的，意味着它不局限于单个函数。还需注意的是，我们不能为宏常量获取用户输入。

## 关于常量的重要点

  本文讨论的C++常量的一些主要特性：

  - 常量是具有固定值的变量。
  - 我们必须在声明时初始化常量，且在程序中不能更改其值。
  - `const` 和 `constexpr` 可以用来定义常量。
  - `#define` 也用于定义宏常量。