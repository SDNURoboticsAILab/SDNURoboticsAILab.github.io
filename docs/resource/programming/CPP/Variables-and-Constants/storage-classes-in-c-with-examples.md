---
comments: true
---
# C++ 存储类及示例

**C++ 存储类** 用于描述变量/函数的特性。它决定了变量的生命周期、可见性、默认值和存储位置，帮助我们在程序运行时跟踪特定变量的存在。存储类说明符用于指定变量的存储类。

### 语法

要指定变量的存储类，需遵循以下语法：

```
storage_class var_data_type var_name;
```

1. C++ 使用 6 种存储类，如下所示：
   1. auto 存储类
   2. register 存储类
   3. extern 存储类
   4. static 存储类
   5. mutable 存储类
   6. thread_local 存储类

![c++ storage classes](https://media.geeksforgeeks.org/wp-content/uploads/20230419110456/Cpp-Storage-Class.webp)

Below is a detailed explanation of each storage class:

以下是每种存储类的详细解释：

## 1. auto 存储类

**auto 存储类** 是在代码块内声明的所有变量的默认存储类。auto 表示自动，所有在代码块内声明的局部变量自动属于此类。

### auto 存储类对象的特性

- **作用域：** 局部
- **默认值：** 垃圾值
- **内存位置：** RAM
- **生命周期：** 直到作用域结束

### auto 存储类示例

C++



```cpp
// C++ 程序演示 auto 存储类
#include <iostream>
using namespace std;

void autoStorageClass()
{
    cout << "Demonstrating auto class\n";

    // 声明一个 auto 变量
    int a = 32;
    float b = 3.2;
    char* c = "GeeksforGeeks";
    char d = 'G';

    // 打印 auto 变量
    cout << a << " \n";
    cout << b << " \n";
    cout << c << " \n";
    cout << d << " \n";
}

int main()
{
    // 演示 auto 存储类
    autoStorageClass();

    return 0;
}
```

输出

```
Demonstrating auto class
32 
3.2 
GeeksforGeeks 
G 
```

> **注意：** 在早期的 C++ 中，我们可以使用 `auto` 关键字显式声明 auto 变量，但从 C++11 起，`auto` 关键字的含义发生了变化，不能再用于定义 auto 变量。

## 2. extern 存储类

**extern 存储类** 简单地告诉我们该变量在其他地方定义，而不是在使用它的同一个块内（即外部链接）。基本上，它的值在不同的块中分配，也可以在不同的块中被覆盖/修改。extern 变量实际上是一个全局变量，在声明时初始化了合法的值，以便在其他地方使用。

普通的全局变量也可以通过在任何函数/块中的声明/定义前加上 `extern` 关键字来变成 extern。使用 extern 变量的主要目的是它们可以在大型程序的不同文件之间访问。

### extern 存储类对象的特性

- **作用域：** 全局
- **默认值：** 零
- **内存位置：** RAM
- **生命周期：** 直到程序结束

### extern 存储类示例

C++



```cpp
// C++ 程序演示 extern 存储类
#include <iostream>
using namespace std;

// 声明一个变量，使其成为 extern，初始值可以
// 也可以初始化为 x
int x;

void externStorageClass()
{
    cout << "Demonstrating extern class\n";

    // 告诉编译器变量 x 是一个 extern 变量
    // 并且已在其他地方定义（main 函数之前）
    extern int x;

    // 打印 extern 变量 'x'
    cout << "Value of the variable 'x'"
         << " declared as extern: " << x << "\n";

    // 修改 extern 变量 x 的值
    x = 2;

    // 打印修改后的 extern 变量 'x'
    cout << "Modified value of the variable 'x'"
         << " declared as extern: \n"
         << x;
}

int main()
{
    // 演示 extern 存储类
    externStorageClass();

    return 0;
}
```

输出

```
Demonstrating extern class
Value of the variable 'x' declared as extern: 0
Modified value of the variable 'x' declared as extern: 
2
```

有关 extern 变量的更多信息，请查看 [链接](https://www.geeksforgeeks.org/understanding-extern-keyword-in-c/)。

## 3. static 存储类

**static 存储类** 用于声明静态变量，这些变量在 C++ 编程中广泛使用。静态变量具有在其作用域结束后仍保持其值的特性！因此，静态变量保留其上次使用的值。

我们可以说，静态变量只初始化一次，并且存在直到程序终止。因此，不会分配新的内存，因为它们不会被重新声明。全局静态变量可以在程序的任何地方访问。

### static 存储类对象的特性

- **作用域：** 局部
- **默认值：** 零
- **内存位置：** RAM
- **生命周期：** 直到程序结束

> **注意：** 全局静态变量可以在任何函数中访问。

### static 存储类示例

C++



```cpp
// C++ 程序演示 static 存储类
#include <iostream>
using namespace std;

// 包含静态变量的函数
// 在执行期间内存被保留
int staticFun()
{
    cout << "For static variables: ";
    static int count = 0;
    count++;
    return count;
}

// 包含非静态变量的函数
// 内存被销毁
int nonStaticFun()
{
    cout << "For Non-Static variables: ";

    int count = 0;
    count++;
    return count;
}

int main()
{
    // 调用静态部分
    cout << staticFun() << "\n";
    cout << staticFun() << "\n";

    // 调用非静态部分
    cout << nonStaticFun() << "\n";
    cout << nonStaticFun() << "\n";
    
    return 0;
}

```

输出

```
For static variables: 1
For static variables: 2
For Non-Static variables: 1
For Non-Static variables: 1

```

## 4. register 存储类

**register 存储类** 使用 `register` 关键字声明寄存器变量，功能与 auto 变量相同。唯一的区别是，编译器会尽量将这些变量存储在微处理器的寄存器中（如果有空闲寄存器）。这使得寄存器变量的使用速度比存储在内存中的变量要快得多。如果没有空闲寄存器，这些变量将存储在内存中。

一个重要的注意点是，我们不能使用指针获取寄存器变量的地址。

### register 存储类对象的特性

- **作用域：** 局部
- **默认值：** 垃圾值
- **内存位置：** CPU 寄存器或 RAM
- **生命周期：** 直到作用域结束

### register 存储类示例

C++



```cpp
// C++ 程序演示寄存器变量的使用
#include <iostream>
using namespace std;

void registerStorageClass()
{
    cout << "Demonstrating register class\n";

    // 声明一个寄存器变量
    register char b = 'G';

    // 打印寄存器变量 'b'
    cout << "Value of the variable 'b'"
         << " declared as register: " << b;
}

int main()
{
    // 演示 register 存储类
    registerStorageClass();
    return 0;
}

```

输出

```
Demonstrating register class
Value of the variable 'b' declared as register: G
```

> **注意：** 从 C++17 起，`register` 关键字已被弃用。

## 5. mutable 存储类

有时需要通过 const 函数修改类/结构体中的一个或多个数据成员，即使你不希望函数更新类/结构体的其他成员。这可以通过使用 `mutable` 关键字轻松实现。`mutable` 关键字主要用于允许 const 对象的特定数据成员被修改。

当我们将函数声明为 const 时，传递给函数的指针变为 const。为变量添加 `mutable` 允许 const 指针修改成员。

### mutable 存储类的特性

`mutable` 说明符不影响对象的链接性或生命周期。它与在该位置声明的普通对象相同。

### mutable 存储类示例

C++



```cpp
// C++ 程序演示 mutable 存储类说明符的使用
#include <iostream>
using std::cout;

class Test {
public:
    int x;

    // 定义 mutable 变量 y
    // 现在它可以被修改
    mutable int y;

    Test()
    {
        x = 4;
        y = 10;
    }
};

int main()
{
    // t1 被设置为常量
    const Test t1;

    // 尝试改变值
    t1.y = 20;
    cout << t1.y;

    // 取消注释以下行
    // 将会报错
    // t1.x = 8;
    // cout << t1.x;
    return 0;
}

```

输出

```
20
```

## 6. thread_local 存储类

`thread_local` 存储类是 C++11 中新增的存储类。我们可以使用 `thread_local` 存储类说明符将对象定义为线程本地。`thread_local` 变量可以与其他存储说明符（如 static 或 extern）组合使用，`thread_local` 对象的属性会相应地变化。

### thread_local 存储类的特性

- **内存位置：** RAM
- **生命周期：** 直到线程结束

### thread_local 存储类示例

C++



```cpp
// C++ 程序演示使用 thread_local 存储说明符
#include <iostream>
#include <mutex>
#include <thread>

using namespace std;

// 定义线程本地变量
thread_local int value = 10;
// 用于同步的互斥锁
mutex mtx;

int main()
{
    // 创建 3 个线程
    // 在线程 1 中修改值
    thread th1([]() {
        value += 18;
        lock_guard<mutex> lock(mtx);
        cout << "Thread 1 value: " << value << '\n';
    });

    thread th2([]() {
        // 在线程 2 中修改值
        value += 7;
        lock_guard<mutex> lock(mtx);
        cout << "Thread 2 value: " << value << '\n';
    });

    thread th3([]() {
        // 在线程 3 中修改值
        value += 13;
        lock_guard<mutex> lock(mtx);
        cout << "Thread 3 value: " << value << '\n';
    });

    // 等待所有线程完成
    th1.join();
    th2.join();
    th3.join();

    // 打印主线程中的 value 值
    cout << "Main thread value: " << value << '\n';

    return 0;
}

```

**Output**

```
Thread 1 value: 28
Thread 2 value: 17
Thread 3 value: 23
Main thread value: 10
```

如我们所见，每个线程都有自己的 `thread_local` 变量副本，并且只分配了其调用中指定的值。