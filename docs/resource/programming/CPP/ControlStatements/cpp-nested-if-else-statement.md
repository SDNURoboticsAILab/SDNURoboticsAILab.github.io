# C++ 嵌套 if-else 语句

在 C++ 中，有多种条件语句，例如 if、if-else、嵌套 if、嵌套 if-else 和 switch。在本文中，我们将学习嵌套 if-else 语句。

## 什么是嵌套 if-else 语句？

嵌套 if-else 语句是在一个 if-else 语句中包含另一个 if 语句。当我们希望实现多层条件判断（条件内包含条件，再包含条件，依此类推）时，就会使用嵌套 if-else 语句。C++ 允许任何级别的嵌套。

## 嵌套 if-else 的基本语法

```cpp
if(condition1)
{
    // Code to be executed 
    if(condition2)
    {
        // Code to be executed
    }
    else
    {
         // Code to be executed
    }
}
else
{
    // code to be executed
}
```

在上述嵌套 if-else 语句的语法中，只有当 `condition1` 为真时，内部的 if-else 语句才会被执行，否则执行 else 语句，内部的 if-else 语句同样适用这一规则。

## 嵌套 if-else 的流程图

![flow diagram of nested if-else](https://media.geeksforgeeks.org/wp-content/uploads/20230424102041/nested-if-else-flowchart.webp)

## 嵌套 if-else 示例

以下 C++ 程序演示了嵌套 if-else 语句的使用。

### 示例 1: 查找三个数中的最大值

在下面的示例中，我们将使用嵌套 if-else 语句找出三个给定数中的最大值。

#### **算法**

假设 a、b 和 c 是三个给定的数：

> 1. 如果 (a < b) 为真，
>
>    ​	如果 (c < b) 为真，则 b 是最大的。
>
>    ​	否则 c 是最大的。
>
> 2. 如果 (a < b) 为假，
>
>    ​	如果 (c < a) 为真，则 a 是最大的。
>
>    ​	否则 c 是最大的。

#### C++ 实现

```cpp
// C++ Program to evaluate largest of the three numbers
// using nested if else
#include <iostream>
using namespace std;

int main()
{
    // declaring three numbers
    int a = 10;
    int b = 2;
    int c = 6;

    // outermost if else
    if (a < b) {
        // nested if else
        if (c < b) {
            printf("%d is the greatest", b);
        }
        else {
            printf("%d is the greatest", c);
        }
    }
    else {
        // nested if else
        if (c < a) {
            printf("%d is the greatest", a);
        }
        else {
            printf("%d is the greatest", c);
        }
    }

    return 0;
}
```


**输出**

```
10 is the greatest
```

### 示例 2: 使用嵌套 if-else 检查闰年

一个年份是闰年如果它符合以下条件：**年份应能被 4 整除**，然后 **年份应能被 100 整除**，最后 **年份应能被 400 整除**，否则该年份不是闰年。

#### 算法

1. 如果年份能被 4 整除，

   ​	如果年份能被 100 整除，

   ​		如果年份能被 400 整除，该年份是闰年。

   ​		否则，该年份不是闰年。

   ​	否则，该年份是闰年。

2. 否则，该年份不是闰年。

#### C++ 实现

```cpp
// C++ program to check leap year using if-else
#include <iostream>
using namespace std;

int main()
{
    int year = 2023;

    if (year % 4 == 0) {
        // first nested if-else statement
        if (year % 100 == 0) {
            // second nested if-else statement
            if (year % 400 == 0) {
                cout << year << " is a leap year.";
            }
            else {
                cout << year << " is not a leap year.";
            }
        }
        else {
            cout << year << " is a leap year.";
        }
    }
    else {
        cout << year << " is not a leap year.";
    }

    return 0;
}
```


**输出**

```
2023 is not a leap year.
```