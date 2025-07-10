---
comments: true
---
# **C++中的cin**

C++中的`cin`对象是`iostream`类的一个实例。它用于从标准输入设备（即键盘）接收输入。它与标准C输入流`stdin`相关联。提取运算符（`>>`）与`cin`对象一起使用来读取输入。提取运算符从`cin`对象中提取通过键盘输入的数据。

**程序1：**

下面是一个实现`cin`对象的C++程序

C++

```cpp
// C++程序演示多个输入
#include <iostream>
using namespace std;

// 驱动代码
int main()
{
    string name;
    int age;

    // 使用cin获取多个输入
    cin >> name >> age;

    // 打印输出
    cout << "Name : " << name << endl;
    cout << "Age : " << age << endl;

    return 0;
}
```

 
 

**Input:** 

![img](https://media.geeksforgeeks.org/wp-content/uploads/20210125212825/cin1.PNG)


 

**Output:**

![img](https://media.geeksforgeeks.org/wp-content/uploads/20210125212912/cin2.PNG)

**程序2：**

使用提取运算符（`>>`）进行多个输入。下面是一个C++程序来获取多个用户输入： 

C++

```cpp
// C++程序演示多个输入
#include <iostream>
using namespace std;

// 驱动代码
int main()
{
    string name;
    int age;

    // 使用cin获取多个输入
    cin >> name >> age;

    // 打印输出
    cout << "Name : " << name << endl;
    cout << "Age : " << age << endl;

    return 0;
}
```

 
 

**Input:**

![img](https://media.geeksforgeeks.org/wp-content/uploads/20210125213319/cin3.PNG)


 

**Output:**

![img](https://media.geeksforgeeks.org/wp-content/uploads/20210125213405/cin4.PNG)

**cin还可以与一些成员函数一起使用，如下所示：**

- **cin.getline(char \*buffer, int N):** 它将长度为N的字符流读取到字符串缓冲区中。当读取到（N-1）个字符、遇到文件结束或换行符（`\n`）时停止。下面是实现`cin.getline()`的C++程序：

 

C++

```cpp
// C++程序演示cin.getline的使用
#include <iostream>
using namespace std;

// 驱动代码
int main()
{
    char name[5];

    // 读取3个字符的流
    cin.getline(name, 3);

    // 打印输出
    cout << name << endl;

    return 0;
}
```

**Input:**
 

![img](https://media.geeksforgeeks.org/wp-content/uploads/20210125214045/cin5.PNG)


 

**Output:**

![img](https://media.geeksforgeeks.org/wp-content/uploads/20210125214122/cin6.PNG)


 

**cin.get(char& var):** 它读取一个输入字符并将其存储在一个变量中。下面是实现`cin.get()`的C++程序:

C++

```cpp
// C++程序演示cin.get()的使用
#include <iostream>
using namespace std;

// 驱动代码
int main()
{
    char ch[30];
    cin.get(ch, 25);

    // 打印ch
    cout << ch;
}
```

**Input:**

![img](https://media.geeksforgeeks.org/wp-content/uploads/20210125215557/cin7.PNG)

**Output:**

![img](https://media.geeksforgeeks.org/wp-content/uploads/20210125215645/cin8.PNG)


 

**cin.read(char \*buffer, int N):** 读取长度为N的字符流。下面是实现`cin.read()`的C++程序：

C++

```cpp
// C++程序演示cin.read()的使用
#include <iostream>
using namespace std;

// 驱动代码
int main()
{
    char gfg[20];

    // 读取字符流
    cin.read(gfg, 10);

    // 打印输出
    cout << gfg << endl;

    return 0;
}
```

**Input:**


 

![img](https://media.geeksforgeeks.org/wp-content/uploads/20210125225445/cin11.PNG)


 

**Output:**


 

![img](https://media.geeksforgeeks.org/wp-content/uploads/20210125225705/cin12.PNG)


 

**cin.ignore():** 它忽略或清除输入缓冲区中的一个或多个字符。下面是实现`cin.ignore()`的C++程序：

C++

```cpp
// C++程序演示cin.ignore()的使用
#include <iostream>
#include <ios>
#include <limits>
using namespace std;

// 驱动代码
int main()
{
    int x;
    char str[80];
    cout << "Enter a number and string:\n";
    cin >> x;

    // 在输入新行前清除缓冲区
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    // 输入字符串
    cin.getline(str, 80);
    cout << "You have entered:\n";
    cout << x << endl;
    cout << str << endl;

    return 0;
}
```

 
 

**Input:**

![img](https://media.geeksforgeeks.org/wp-content/uploads/20210125223339/cin9.PNG)


 

**Output:**


 

![img](https://media.geeksforgeeks.org/wp-content/uploads/20210125223459/cin10.PNG)


 

**解释：** 在上述程序中，如果没有使用`cin.ignore()`，则在输入数字后按回车键输入字符串时，输出将只包含输入的数字。程序将不会接受字符串输入。为了避免这个问题，使用`cin.ignore()`，它将忽略换行符。