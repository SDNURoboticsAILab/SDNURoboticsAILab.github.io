# C++中的派生数据类型

**数据类型**是用来识别数据种类及其相关操作处理方式的方法。数据类型主要分为三种：

1. 预定义数据类型
2. 派生数据类型
3. 用户定义数据类型![DatatypesInC](.\asset\DatatypesInC.png)

在这篇文章中，将解释派生数据类型：

### C++中的派生数据类型

派生数据类型是从基本或内置数据类型衍生出来的。它们主要可以分为四种类型：

1. 函数
2. 数组
3. 指针
4. 引用

让我们简要了解以下每种派生数据类型：

### 1.函数 

函数是一段被定义用来执行特定明确任务的代码块或程序段。函数通常被定义以避免用户对相同的输入重复编写相同的代码行。所有代码行被集中放置在一个函数内，这样可以在任何需要的地方调用。在C++的每个程序中，main() 是一个默认定义的函数。

**语法**

```
FunctionType FunctionName(parameters)
```

**样例**

下面的示例演示了C++中函数的使用。

```
// C++程序演示
// 函数派生类型

#include <iostream>
using namespace std;

// max here is a function derived type
int max(int x, int y)
{
    if (x > y)
        return x;
    else
        return y;
}

// main is the default function derived type
int main()
{
    int a = 10, b = 20;

    // Calling above function to
    // find max of 'a' and 'b'
    int m = max(a, b);

    cout << "m is " << m;
    return 0;
}
```

**输出**

```
m is 20
```

**解释：**上述程序演示了函数派生类型的使用。它定义了一个名为“max”的函数，该函数返回作为输入提供的两个整数中的最大值。在main函数中，调用max函数以找到变量“a”和“b”的最大值并将其存储在m中，最后打印m（最大数）。

### 2.数组

数组是一系列存储在连续内存位置的项目集合。数组的理念是用一个变量表示多个实例。

**语法**

```
DataType ArrayName[size_of_array];
```

**样例**

下面的示例演示了C++中数组的使用。

```
// C++程序演示
// 数组派生类型

#include <iostream>
using namespace std;
int main()
{

    // Array Derived Type
    int arr[5];
    arr[0] = 5;
    arr[2] = -10;

    // this is same as arr[1] = 2
    arr[3 / 2] = 2;

    arr[3] = arr[0];

    cout << arr[0] << " " << arr[1] << " " << arr[2] << " "
         << arr[3];

    return 0;
}
```

**输出**

```
5 2 -10 5
```

**解释：**上述程序展示了数组派生类型的使用。它创建了一个整数数组“arr”，并使用索引赋值。然后打印所有数组元素。

### 3.指针 

指针是地址的符号表示。它们使程序能够模拟按引用调用，以及创建和操作动态数据结构。它在C/C++中的一般声明格式为：

**语法**

```
datatype *var_name;
```

例如：`int *ptr;` （ptr指向一个存储整型数据的地址）。

**样例**

下面的示例演示了C++中指针的使用。

```
// C++程序演示
// 指针派生类型

#include <iostream>
using namespace std;

void geeks()
{
    int var = 20;

    // Pointers Derived Type
    // declare pointer variable
    int* ptr;

    // note that data type of ptr
    // and var must be same
    ptr = &var;

    // assign the address of a variable
    // to a pointer
    cout << "Value at ptr = " << ptr << "\n";
    cout << "Value at var = " << var << "\n";
    cout << "Value at *ptr = " << *ptr << "\n";
}

// Driver program
int main() { geeks(); }
```

**输出**

```
Value at ptr = 0x7ffc04f3f894
Value at var = 20
Value at *ptr = 20
```

**解释：**上述程序展示了指针作为派生类型的使用。它声明了一个指针变量 ‘ptr’，并将变量 ‘var’ 的地址赋值给它。然后，它打印出指针的值、变量的值，以及解引用指针的值，展示了C++中指针使用的基础知识。

### 4.引用

当一个变量被声明为引用时，它成为现有变量的替代名称。通过在声明中放置“&”，可以将变量声明为引用。

**语法**

```
data_type &ref = variable;
```

**样例**

下面的示例演示了C++中引用的使用。

```
// C++程序演示
// 引用派生类型

#include <iostream>
using namespace std;

int main()
{
    int x = 10;

    // Reference Derived Type
    // ref is a reference to x.
    int& ref = x;

    // Value of x is now changed to 20
    ref = 20;
    cout << "x = " << x << endl;

    // Value of x is now changed to 30
    x = 30;
    cout << "ref = " << ref << endl;

    return 0;
}
```

**输出**

```
x = 20
ref = 30
```

**解释：**上述程序演示了引用派生类型的使用。创建了一个整数变量“x”的引用“ref”。如果“ref”的值改变，“x”的值也会改变，反之亦然。

### 总结

C++中的派生数据类型是函数、数组、指针和引用，提供了许多有用的工具来处理数据。函数让我们编写可重用的代码。数组帮助高效地管理多个项和数据。指针允许灵活的内存使用和引用。引用提供了一种创建别名和更简单地处理变量的方法。总的来说，这些派生数据类型使C++编码更加系统和有效。