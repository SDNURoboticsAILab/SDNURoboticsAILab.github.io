---
comments: true
---
# C++中的用户定义数据类型

**数据类型**是用于标识数据类型及其相关处理操作的手段。在C++中，数据类型用于声明变量。有三种数据类型：

1. 预定义数据类型
2. 派生数据类型
3. 用户定义数据类型![DatatypesInC](.\asset\DatatypesInC.png)

在本文中，解释了用户定义数据类型：

### 用户定义数据类型 

由用户定义的数据类型被称为派生数据类型或用户定义派生数据类型。这些类型包括：

1. 类（Class）
2. 结构体（Structure）
3. 联合体（Union）
4. 枚举（Enumeration）
5. 类型定义（Typedef）

下面是对以上类型的详细描述：

### 1.类 

类是C++中面向对象编程的基础构建块。它是一种用户定义的数据类型，拥有自己的数据成员和成员函数，可以通过创建该类的实例来访问和使用。类就像是对象的蓝图。

**语法**

![Classes-and-Objects-in-C](.\asset\Classes-and-Objects-in-C.png)

**样例**

下面的示例演示了C++中类的使用。

```c++
// C++程序演示
// 类 
  
#include <bits/stdc++.h> 
using namespace std; 
  
class Geeks { 
    // 访问说明符 
public: 
    // 数据成员 
    string geekname; 
  
    // 成员函数() 
    void printname() 
    { 
        cout << "Geekname is: " << geekname; 
    } 
}; 
  
int main() 
{ 
  
    // 声明一个类geeks的对象 
    Geeks obj1; 
  
    // 访问数据成员 
    obj1.geekname = "GeeksForGeeks"; 
  
    // 访问成员函数 
    obj1.printname(); 
  
    return 0; 
}
```

**输出**

```
Geekname is: GeeksForGeeks
```

**解释：**上述程序定义了一个名为“Geeks”的类，其中包含一个geekname属性和一个printname()函数，用于打印geek的名称。在main函数中，它创建了一个名为obj1的对象，将geekname设置为“GeeksforGeeks”，并调用printname()函数来显示它。

### 2.结构体

结构体是C/C++中的用户定义数据类型。结构体创建了一种数据类型，可以用来将可能不同类型的项组合成单一类型。

**语法**

```
struct structName{     
char  varName[size];        
int varName; 
};
```

**样例**

下面的示例演示了C++中结构体的使用。

```c++
// C++程序演示
// 结构体
  
#include <iostream> 
using namespace std; 
  
// 声明结构体
struct Point { 
    int x, y; 
}; 
  
int main() 
{ 
    // 创建结构体数组
    struct Point arr[10]; 
  
    // 访问数组成员
    arr[0].x = 10; 
    arr[0].y = 20; 
  
    cout << arr[0].x << ", " << arr[0].y; 
  
    return 0; 
}
```

**输出**

```
10, 20
```

**解释：**上述程序通过定义一个名为 “Points” 的结构体，它具有 x 和 y 坐标，展示了结构体的使用。在 main 函数中，它创建了一个这些结构体的数组，设置了它们的值，并打印出来。

### 3.联合体

与结构体一样，联合体（Union）也是一种用户定义的数据类型。在联合体中，所有成员共享同一块内存位置。例如，在下面的C程序中，x 和 y 共享同一位置。如果我们改变 x，我们可以在 y 中看到相应的变化。

**语法**

```
Union_Name 
{
  // Declaration of data members
}; union_variables;
```



**样例**

下面的示例演示了C++中联合体的使用。

```c++
#include <iostream> 
using namespace std; 
 
// 联合的声明与结构相同
union test { 
    int x, y; 
}; 
  
int main() 
{ 
    // 一个联合变量t
    union test t; 
  
    // t.y也得到值2
    t.x = 2; 
  
    cout << "After making x = 2:" << endl 
         << "x = " << t.x << ", y = " << t.y << endl; 
  
    // t.x也更新为10
    t.y = 10; 
  
    cout << "After making Y = 10:" << endl 
         << "x = " << t.x << ", y = " << t.y << endl; 
  
    return 0; 
}
```

**输出**

```
After making x = 2:
x = 2, y = 2
After making Y = 10:
x = 10, y = 10
```

**解释：**上述程序展示了联合体的使用。定义了一个名为 “test” 的联合体，它有两个整型成员 x 和 y，在这里 x 和 y 共享同一块内存空间。在 main 函数中，将 x 的值设置为 2 并打印出来。随后，将 y 更新为 10，x 的值也被更新为 10，这展示了联合体共享内存的特性。

### 4.枚举 

枚举（Enumeration 或 enum）是C语言中的一种用户定义数据类型。它主要用于给整型常量分配名称，这些名称使得程序易于阅读和维护。

**语法**

```
enum  nameOfEnum {
varName1 = 1, varName2 = 0
}; 
```

**样例**

下面的示例演示了C++中枚举的使用。

```c++
// 程序演示工作
// C++中的枚举
  
#include <iostream> 
using namespace std; 
  
enum week { Mon, Tue, Wed, Thur, Fri, Sat, Sun }; 
  
int main() 
{ 
    enum week day; 
  
    day = Wed; 
  
    cout << day; 
  
    return 0; 
}
```

**输出**

```
2
```

### 5.类型定义

C++允许您使用关键字 `typedef` 明确地定义新的数据类型名称。使用 `typedef` 并不是创建一个新的数据类，而是为现有类型定义一个新名称。这可以提高程序的可移植性（即程序在不同类型的机器上使用的能力，例如迷你机、大型机、微型机等，而无需对代码进行大量更改），因为只需更改 `typedef` 声明。使用 `typedef`，人们还可以通过为标准数据类型提供描述性名称来自我记录代码。

**语法**

```
typedef typeName;
```

其中typeName是任何C++数据类型，name是此数据类型的新名称。这为C++的标准类型定义了另一个名称。

**样例**

下面的示例演示了C++中类型定义的使用。

```c++
// C++程序演示typedef
#include <iostream> 
using namespace std; 
  
// 在此行之后，BYTE可以代替unsigned char使用
typedef unsigned char BYTE; 
  
int main() 
{ 
    BYTE b1, b2; 
    b1 = 'c'; 
    cout << " " << b1; 
    return 0; 
}
```

**输出**

```
 c
```

### 总结

总之，C++有用户定义的数据类型，如类、结构、联合、枚举和typedef。这些用户定义的数据类型允许程序员轻松组织和自定义他们的代码，并编写模块化、高效和可读的代码。因此，用户定义的数据类型提高了C++程序的灵活性和结构，以更好地组织代码。