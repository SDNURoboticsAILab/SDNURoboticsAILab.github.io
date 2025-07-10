---
comments: true
---
# **基本输入/输出在C++中的使用**

- C++ 提供了许多用于执行输入和输出的库。在 C++ 中，输入和输出以字节序列的形式进行，通常被称为流（streams）。

  **输入流：** 如果字节流的方向是从设备（例如，键盘）到主存储器，则这个过程称为输入。

  **输出流：** 如果字节流的方向相反，即从主存储器到设备（显示屏），则这个过程称为输出。

![Basic Input / Output in C++](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20191113125616/C-basic-input-output.png)


在 C++ 中，用于输入/输出操作的头文件包括：

1. **iostream**：`iostream` 代表标准输入输出流。这个头文件包含了像 `cin`、`cout`、`cerr` 等对象的定义。
2. **iomanip**：`iomanip` 代表输入输出操控符。这个文件中声明的方法用于操作流。文件中包含了 `setw`、`setprecision` 等定义。
3. **fstream**：这个头文件主要描述了文件流。这个头文件用于处理从文件读取的数据作为输入或写入到文件的数据作为输出。
4. **bits/stdc++**：这个头文件包含了所有标准库。在编程竞赛中，使用这个文件是一个好主意，尤其是在时间敏感的情况下，可以减少处理时间。有关更多信息，请参阅本文。

在 C++ 中，头文件之后，我们通常使用 `using namespace std;`。原因在于所有的标准库定义都在 `std` 命名空间中。由于库函数不是在全局范围内定义的，因此为了使用它们，我们使用 `std` 命名空间。这样，我们就不需要在每一行前面都写 `std::`（例如 `std::cout` 等）。要了解更多信息，请参阅本文。

C++ 中的两个实例 `cout` 和 `cin` 分别来自 `iostream` 类，通常用于输出和输入。这两个是 C++ 中最基本的输入和输出方法。要使用 `cin` 和 `cout`，必须在程序中包含 `iostream` 头文件。

本文主要讨论了 `iostream` 头文件中定义的对象，如 `cin` 和 `cout`。

**标准输出流（cout）：** 通常，标准输出设备是显示屏。C++ 的 `cout` 语句是 `ostream` 类的实例。它用于在标准输出设备（通常是显示屏）上生成输出。需要显示在屏幕上的数据通过插入运算符 `<<` 插入到标准输出流（`cout`）中。

C++



```cpp
#include <iostream>

using namespace std;

int main()
{
    char sample[] = "GeeksforGeeks";

    cout << sample << " - A computer science portal for geeks";

    return 0;
}
```

**Output:** 

```
GeeksforGeeks - A computer science portal for geeks
```

- 在上述程序中，插入运算符 `<<` 将字符串变量 `sample` 的值以及字符串 "A computer science portal for geeks" 插入到标准输出流 `cout` 中，然后显示在屏幕上。

  **标准输入流（cin）：** 通常，计算机的输入设备是键盘。C++ 的 `cin` 语句是 `istream` 类的实例，用于从标准输入设备（通常是键盘）读取输入。提取运算符 `>>` 与 `cin` 对象一起使用来读取输入。提取运算符从通过键盘输入的 `cin` 对象中提取数据。

C++



```cpp
#include <iostream>
using namespace std;

int main()
{
    int age;

    cout << "Enter your age:";
    cin >> age;
    cout << "\nYour age is: " << age;

    return 0;
}
```

**Input :** 

```
18
```

**Output:** 

```
Enter your age:
Your age is: 18
```

- 上述程序要求用户输入年龄。对象 `cin` 连接到输入设备。用户输入的年龄通过提取运算符 `>>` 从 `cin` 中提取，然后存储在提取运算符右侧的变量 `age` 中。

  **无缓冲标准错误流（cerr）：** C++ 的 `cerr` 是标准错误流，用于输出错误信息。它也是 `iostream` 类的一个实例。由于 `cerr` 在 C++ 中是无缓冲的，因此在需要立即显示错误信息时使用。它没有缓冲区来存储错误信息并在以后显示。

  `cerr` 和 `cout` 之间的主要区别在于，当你想通过“cout”重定向输出到文件时，如果使用 `cerr`，错误不会被存储到文件中。（这就是无缓冲的意思——它不能存储消息）

C++



```cpp
#include <iostream>

using namespace std;

int main()
{
    cerr << "An error occurred";
    return 0;
}
```

**Output:** 

```
An error occurred
```



- **缓冲标准错误流（clog）：** 这也是 `ostream` 类的一个实例，用于显示错误信息，但与 `cerr` 不同，错误信息首先被插入到缓冲区中，直到缓冲区被填满或缓冲区被显式刷新（使用 `flush()`）。错误信息也会显示在屏幕上。

C++



```cpp
#include <iostream>

using namespace std;

int main()
{
    clog << "An error occurred";

    return 0;
}
```

**Output:** 

```
An error occurred
```

- **相关文章：**
  - `cout << endl` 与 `cout << "\n"` 在 C++ 中的区别
  - 当 `fgets()/gets()/scanf()` 后面有 `scanf()` 的问题
  - 如何在 C++ 中使用 `getline()` 处理输入中的空行？
  - `Cin-Cout` 与 `Scanf-Printf` 的比较