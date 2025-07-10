---
comments: true
---
## C++ 中的 static 关键字

**前提知识：C 中的静态变量**

`static` 关键字在不同类型中具有不同的含义。我们可以在以下情况下使用 `static` 关键字：

- **静态变量：** 函数中的变量，类中的变量
- **类的静态成员：** 类中的对象和函数

现在让我们详细了解这些 `static` 的用法。

### 静态变量

**函数中的静态变量：** 当一个变量被声明为 `static` 时，它的空间会被分配到程序的整个生命周期中。即使函数被多次调用，静态变量的空间只会分配一次，并且上一次调用中的变量值会保留到下一次函数调用中。这在实现 C/C++ 中的协程或需要存储函数先前状态的应用程序中非常有用。

C++

```cpp
// C++ 程序演示函数中静态变量的使用
#include <iostream>
#include <string>
using namespace std;

void demo()
{
    // 静态变量
    static int count = 0;
    cout << count << " ";

    // 值被更新，并
    // 会被传递到下一个
    // 函数调用
    count++;
}

int main()
{
    for (int i = 0; i < 5; i++)
        demo();
    return 0;
}
```

**Output**

```
0 1 2 3 4 
```

在上述程序中，变量 `count` 被声明为静态。因此，它的值会在函数调用之间保留。变量 `count` 并不会在每次函数调用时被重新初始化。作为旁注，Java 不允许函数中的静态局部变量。

**类中的静态变量：** 由于静态变量只初始化一次，并且它们在独立的静态存储中分配空间，因此类中的静态变量是由对象共享的。相同的静态变量不会为不同的对象创建多个副本。因此，静态变量不能通过构造函数进行初始化。

**C++ 示例**

```cpp
// C++ 程序演示类中的静态变量
#include <iostream>
using namespace std;

class GfG {
public:
    static int i;

    GfG(){
        // 不做任何操作
    };
};

int main()
{
    GfG obj1;
    GfG obj2;
    obj1.i = 2;
    obj2.i = 3;

    // 打印 i 的值
    cout << obj1.i << " " << obj2.i;
}
```


**Output**

```
undefined reference to `GfG::i'
collect2: error: ld returned 1 exit status
```

在上述程序中，我们尝试为多个对象创建静态变量 `i` 的多个副本。但这并没有发生。因此，类中的静态变量应通过类名和作用域解析运算符在类外部显式初始化，如下所示：

C++

```cpp
// C++ 程序演示类中的静态变量
#include <iostream>
using namespace std;

class GfG {
public:
    static int i;

    GfG(){
        // 不做任何操作
    };
};

// 类外部初始化静态变量
int GfG::i = 1;

int main()
{
    GfG obj;
    // 打印 i 的值
    cout << obj.i;
}
```

**Output**

```
1
```

### 类的静态成员

**类对象作为静态：** 就像变量一样，当对象被声明为静态时，它的作用域持续到程序的整个生命周期。考虑以下程序，其中对象是非静态的。

**C++ 示例**

```cpp
// CPP program to illustrate
// when not using static keyword
#include <iostream>
using namespace std;

class GfG {
    int i;

public:
    GfG()
    {
        i = 0;
        cout << "Inside Constructor\n";
    }
    ~GfG() { cout << "Inside Destructor\n"; }
};

int main()
{
    int x = 0;
    if (x == 0) {
        GfG obj;
    }
    cout << "End of main\n";
}
```

**Output**

```
Inside Constructor
Inside Destructor
End of main
```

在上述程序中，对象在 `if` 块内被声明为非静态。因此，变量的作用域仅限于 `if` 块内。当对象创建时，构造函数被调用，而当 `if` 块的控制结束时，析构函数被调用，因为对象的作用域仅限于 `if` 块内。让我们看看如果将对象声明为静态时输出的变化。

C++

```cpp
// C++ 程序演示类对象作为静态的情况
#include <iostream>
using namespace std;

class GfG {
    int i = 0;

public:
    GfG()
    {
        i = 0;
        cout << "Inside Constructor\n";
    }

    ~GfG() { cout << "Inside Destructor\n"; }
};

int main()
{
    int x = 0;
    if (x == 0) {
        static GfG obj;
    }
    cout << "End of main\n";
}
```

**Output**

```
Inside Constructor
End of main
Inside Destructor
```

你可以清楚地看到输出的变化。现在析构函数在 `main` 函数结束后被调用。这是因为静态对象的作用域是整个程序的生命周期。

### 类中的静态函数

**静态成员函数：** 与静态数据成员或类中的静态变量类似，静态成员函数也不依赖于类的对象。我们可以使用对象和 `.` 运算符调用静态成员函数，但推荐使用类名和作用域解析运算符调用静态成员。静态成员函数只能访问静态数据成员或其他静态成员函数，不能访问类的非静态数据成员或成员函数。

C++

```cpp
// C++ 程序演示类中的静态成员函数
#include <iostream>
using namespace std;

class GfG {
public:
    // 静态成员函数
    static void printMsg() { cout << "Welcome to GfG!"; }
};

// 主函数
int main()
{
    // 调用静态成员函数
    GfG::printMsg();
}
```

**Output**

```
Welcome to GfG!
```

### 相关文章

- 关于静态关键字的测验
- C++ 中的静态数据成员
- 静态对象何时被销毁？
- 静态成员函数的有趣事实
- 静态函数可以是虚拟函数吗？
- C++ 和 Java 中的静态关键字比较
- C 中的静态函数

