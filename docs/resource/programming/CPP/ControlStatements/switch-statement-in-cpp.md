---
comments: true
---
# C++ 中的 Switch 语句

C++ 中的 Switch case 语句会根据给定表达式的值（匹配某个条件）执行与该值关联的语句。它是较长的 if-else-if 语句的替代方案，提供了一种简便的方法，根据表达式的值将执行转发到代码的不同部分。

## 什么是 C++ 中的 switch 语句？

C++ 中的 switch 语句是一种流程控制语句，用于根据给定表达式的值执行不同的语句块。我们可以为 switch 表达式的不同值创建不同的 case。我们可以在 switch 语句中指定任意数量的 case，但***case 值***只能是***int***或***char***类型。

## switch 语句的语法

```cpp
switch (expression) {
    case value_1:
        // statements_1;
        break;
    case value_2:
        // statements_2;
        break;
    .....
    .....
    default:
        // default_statements;
        break;
}
```

下面的示例展示了如何在 C++ 中使用 switch 语句的语法。

## 示例：演示 switch 语句语法的 C++ 程序

```cpp
// C++ program to demonstrate syntax of switch
#include <iostream>
using namespace std;

// Driver Code
int main()
{
    // switch variable
    char x = 'A';

    // switch statements
    switch (x) {
    case 'A':
        cout << "Choice is A";
        break;
    case 'B':
        cout << "Choice is B";
        break;
    case 'C':
        cout << "Choice is C";
        break;
    default:
        cout << "Choice other than A, B and C";
        break;
    }
    return 0;
}
```


**输出**

```
Choice is A
```

## C++ 中 switch case 语句的规则

使用 C++ 的 switch 语句时需要遵循以下规则：

1. case 值必须是 int 或 char 类型。
2. 可以有任意数量的 case。
3. 不允许重复的 case 值。
4. 每个 case 语句可以包含 break 语句，但它是可选的。
5. default 语句也是可选的。

## C++ 中 switch 语句的流程图

![switch case in cpp](https://media.geeksforgeeks.org/wp-content/uploads/20230224161406/switch-case-in-c.png)

## C++ 中 switch 语句的工作原理

C 语言中 switch 语句的工作原理如下：

1. ***步骤 1:*** 计算 switch 表达式。
2. ***步骤 2:*** 将计算结果与各个 case 值进行匹配。
3. ***步骤 3A:*** 如果找到匹配的 case 值，则执行该 case 语句块。
4. ***步骤 3B:*** 如果没有找到匹配的 case 值，并且存在 default 语句块，则执行该块。
5. ***步骤 4A:*** 如果在语句块中出现了 break 关键字，则程序控制退出 switch 语句。
6. ***步骤 4B:*** 如果没有 break 关键字，则所有匹配 case 之后的 case 语句也会被执行。
7. ***步骤 5:*** 执行 switch 语句后的语句。

## 关于 switch case 语句的重要事项

### 1. Switch 表达式应当产生***常量值***

如果 switch 语句中的表达式没有产生常量值，它将无效。以下是一些有效的 switch case 表达式：

```cpp
// 允许常量表达式
switch(1+2+23)
switch(1*2+3%4)

// 允许变量表达式，前提是它们已分配固定值
switch(a*b+c*d)
switch(a+b+c)
```

### 2. 表达式必须仅计算 int 或 char 类型的值

Switch 语句只能计算整数或字符值。因此，switch 表达式应仅返回 int 或 char 类型的值。

### 3.  Switch case 中的 break

break 关键字用于在遇到匹配 case 时跳出 switch 语句。它通常放在每个 case 语句块的末尾，以确保程序控制在执行匹配 case 后退出循环。

***break 语句是可选的***。如果省略，则匹配 case 之后的所有 case 语句也会被执行。

### 示例：不带 break 语句的 switch 语句

```c
// C Program to demonstrate the behaviour of switch case without break
#include <stdio.h>

int main() {
    int var = 2;

    // switch case without break
    switch (var) {
    case 1:
        printf("Case 1 is executed.\n");
    case 2:
        printf("Case 2 is executed.\n");
    case 3:
        printf("Case 3 is executed.\n");
    case 4:
        printf("Case 4 is executed.");
    }
    return 0;
}
```


**输出**

```
Case 2 is executed.
Case 3 is executed.
Case 4 is executed.
```

### 4.Switch case 中的 default

default 关键字用于定义一个默认 case，当没有 case 值匹配时将执行该 case。它也是可选的，即使省略了，switch case 语句也能正常运行。

### 5. 不允许重复的 Case 值

C 语言的 switch 语句中，不允许出现重复的 case 值。所有 case 值必须是唯一的。

### 6. 嵌套的 Switch 语句

在 C++ 中，我们可以在一个 switch 语句中嵌套另一个 switch 语句。尽管这在大多数情况下是可以避免的，因为它会使程序更复杂且难以阅读。

#### 嵌套 Switch 语句示例

```c
// C program to illustrate the use of nested switch
#include <iostream>
using namespace std;

int main() {
    int var1 = 1;
    int var2 = 0;

    // outer switch
    switch (var1) {
    case 0:
        cout << "Outer Switch Case 0\n";
        break;
    case 1:
        cout << "Outer Switch Case 1\n";

        // inner switch
        switch (var2) {
        case 0:
            cout << "Inner Switch Case 0\n";
            break;
        }
        break;
    default:
        cout << "Default Case of Outer Loop";
        break;
    }
    return 0;
}

```


**输出**

```
Outer Switch Case 1
Inner Switch Case 0
```

### 7. Default Case 的位置无关紧要

无论 default case 的位置在哪里，只有当没有其他 case 条件满足时，才会执行它。因此，将它放在开头、中间或末尾不会改变核心逻辑（除非使用了一种较不常见的技术，称为“fall-through”）。

***示例：*** 下面的例子中，我们将通过 (1-7) 数字来识别工作日。

```cpp
// C++ program to demonstrate the placement of default anywhere
#include <iostream>
using namespace std;

int main() {
    int day;

    cout << "Enter a day number (1-7): ";
    cin >> day;

    switch (day) {
    default: // Default placed first for demonstration
        cout << "Not a valid weekday." << endl;
        break;
    case 1:
        cout << "It's Monday!" << endl;
        break;
    case 2:
        cout << "It's Tuesday!" << endl;
        break;
    case 3:
        cout << "It's Wednesday!" << endl;
        break;
    case 4:
        cout << "It's Thursday!" << endl;
        break;
    case 5:
        cout << "It's Friday!" << endl;
        break;
    case 6:
        cout << "It's Saturday!" << endl;
        break;
    case 7:
        cout << "It's Sunday!" << endl;
        break;
    }
    return 0;
}

```


**输出**

```
Enter a day number (1-7): 8
Not a valid weekday.
```

## C++ 中 switch 语句的示例

### 示例 1：使用 switch 制作一个简单计算器的 C++ 程序

```cpp
// C Program to create a simple calculator using switch statement
#include <iostream>
#include <stdlib.h>
using namespace std;

int main() {
    // switch variable
    char choice;
    // operands
    int x, y;

    while (1) {
        cout << "Enter the Operator (+,-,*,/)\nEnter x to exit\n";
        cin >> choice;

        // for exit
        if (choice == 'x') {
            exit(0);
        }

        cout << "Enter the two numbers: ";
        cin >> x >> y;

        // switch case with operation for each operator
        switch (choice) {
        case '+':
            cout << x << " + " << y << " = " << x + y << endl;
            break;

        case '-':
            cout << x << " - " << y << " = " << x - y << endl;
            break;

        case '*':
            cout << x << " * " << y << " = " << x * y << endl;
            break;

        case '/':
            cout << x << " / " << y << " = " << x / y << endl;
            break;

        default:
            cout << "Invalid Operator\n";
            break;
        }
    }
    return 0;
}

```


**输出**

```
Enter the operator (+, -, *, /)

Enter x to exit

+
Enter the two numbers: 100 + 200
100 + 200 = 300
```

### 示例 2: 使用 switch 语句输出星期的 C++ 程序

```cpp
// C++ program to returns day based on the numeric value.
#include <iostream>
using namespace std;

class Day {
private:
    int day = 3;

public:
    void set_data()
    {
        cout << "Enter no of day you want to display: ";
        cin >> day;
    }

    void display_day()
    {
        switch (day) {
        case 1:
            cout << "MONDAY";
            break;

        case 2:
            cout << "TUESDAY";
            break;

        case 3:
            cout << "WEDNESDAY";
            break;

        case 4:
            cout << "THURSDAY";
            break;

        case 5:
            cout << "FRIDAY";
            break;

        case 6:
            cout << "SATURDAY";
            break;

        case 7:
            cout << "SUNDAY";
            break;

        default:
            cout << "INVALID INPUT";
            break;
        }
    }
};

main()
{
    Day d1;

    d1.display_day();

    return 0;
}
```


**输出**

```
WEDNESDAY
```

### 示例 3: 使用枚举值和类输出不同选择的 C++ 程序

```cpp
// C++ Program to print different choices using enum values
// and class

#include <iostream>
#include <map>
#include <string>
using namespace std;

// Define an enum class for the choices
enum class Choice { A, B, C };

// Create a map to associate strings with the enum values
map<std::string, Choice> stringToEnumMap
    = { { "A", Choice::A },
        { "B", Choice::B },
        { "C", Choice::C } };

int main()
{
    // The input string
    string x = "A";

    // Convert the string to the corresponding enum using
    // the map
    Choice choice = stringToEnumMap[x];

    // Use a switch statement on the enum
    switch (choice) {
    case Choice::A:
        cout << "Choice is A";
        break;
    case Choice::B:
        cout << "Choice is B";
        break;
    case Choice::C:
        cout << "Choice is C";
        break;
    default:
        cout << "Choice other than A, B and C";
        break;
    }

    return 0;
}

/* The enum class can be used for choice sets
from different projects or programs,
hence improving modularity*/
```


**输出**

```
Choice is A
```

## C++ 中 switch 语句的优点

1. 对于大量条件更容易调试和维护。
2. 相比 if else if 更易于阅读。

## C++ 中 switch 语句的缺点

1. switch 语句只能对 int 或 char 类型的值进行判断。
2. 不支持逻辑表达式。
3. 需要注意在每个 case 中添加 break。

## 总结

本文讨论了 switch 语句以及如何使用它替换复杂的 if else if 语句结构。我们还讨论了如何在 C++ 程序中使用 switch 语句提高效率。

## C++ 中的 switch 语句 - 常见问题

### 什么是 C++ 中的 switch？

> switch 是一种条件判断语句，它可以根据指定表达式的值执行不同的代码块。

### 在 C++ 的 switch 中哪些语句是可选的？

> default 和 break 在 C++ 中的 switch 语句中是可选的。

### C++ 中 switch 与 if else if 有什么区别？

> 以下是 C++ 中 switch 和 if else if 的主要区别：

|                  switch                   |             if else if             |
| :---------------------------------------: | :--------------------------------: |
|  它根据 switch 变量的值执行不同的 case。  | 它根据指定的条件执行不同的代码块。 |
| 只能对 int 或 char 类型的表达式进行判断。 |     可以判断任何类型的表达式。     |
|      在大量条件时更快且更容易阅读。       | 当条件很多时，代码可能会变得混乱。 |

