---
comments: true
---
# C语言中按值调用和按引用调用的区别

函数可以通过两种方式调用：**按值调用**或**按引用调用**。这两种方式通常通过传递给它们的参数类型来区分。

传递给函数的参数称为实际参数，而函数接收的参数称为形式参数。

## C语言中的按值调用

在按值传递参数的方法中，实际参数的值被复制到函数的形参中。

- 有两个参数的副本存储在不同的内存位置。
- 一个是原始副本，另一个是函数副本。
- 函数内部所做的任何更改都不会反映在调用者的实际参数中。

### 按值调用的示例

以下示例演示了按值传递参数的方法

```c
// C program to illustrate call by value
#include <stdio.h>

// Function Prototype
void swapx(int x, int y);

// Main function
int main()
{
    int a = 10, b = 20;

    // Pass by Values
    swapx(a, b); // Actual Parameters

    printf("In the Caller:\na = %d b = %d\n", a, b);

    return 0;
}

// Swap functions that swaps
// two values
void swapx(int x, int y) // Formal Parameters
{
    int t;

    t = x;
    x = y;
    y = t;

    printf("Inside Function:\nx = %d y = %d\n", x, y);
}
```

**输出**

```
Inside Function:
x = 20 y = 10
In the Caller:
a = 10 b = 20
```

因此，即使在函数中交换了x和y的值，a和b的实际值仍然保持不变。

## C语言中的按引用调用

在按引用传递参数的方法中，实际参数的地址作为形参传递给函数。在C语言中，我们使用指针来实现按引用调用。

- 实际参数和形参引用相同的位置。
- 函数内部所做的任何更改实际上会反映在调用者的实际参数中。

### 按引用调用的示例

以下C程序是按引用传递方法的示例。

```c
// C program to illustrate Call by Reference
#include <stdio.h>

// Function Prototype
void swapx(int*, int*);

// Main function
int main()
{
    int a = 10, b = 20;

    // Pass reference
    swapx(&a, &b); // Actual Parameters

    printf("Inside the Caller:\na = %d b = %d\n", a, b);

    return 0;
}

// Function to swap two variables
// by references
void swapx(int* x, int* y) // Formal Parameters
{
    int t;

    t = *x;
    *x = *y;
    *y = t;

    printf("Inside the Function:\nx = %d y = %d\n", *x, *y);
}
```

输出

```
Inside the Function:
x = 20 y = 10
Inside the Caller:
a = 20 b = 10
```

因此，在交换x和y的值后，a和b的实际值发生了变化。

## C语言中按值调用和按引用调用的区别

下表列出了按值传递参数和按引用传递参数方法之间的区别。

|                           按值调用                           |                          按引用调用                          |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|  在调用函数时，我们传递变量的值。这样的函数称为“按值调用”。  | 在调用函数时，我们不传递变量的值，而是传递变量的地址（变量的位置）给函数，这称为“按引用调用”。 |
| 在这种方法中，调用函数中每个变量的值被复制到被调用函数的相应虚拟变量中。 | 在这种方法中，调用函数中实际变量的地址被复制到被调用函数的虚拟变量中。 |
| 使用这种方法，在被调用函数中对虚拟变量所做的更改不会影响调用函数中实际变量的值。 | 使用这种方法，通过地址我们可以访问实际变量，因此我们可以操作它们。 |
|    在按值调用中，我们不能通过函数调用来改变实际变量的值。    |     在按引用调用中，我们可以通过函数调用来改变变量的值。     |
|                  变量的值通过简单技术传递。                  |             需要定义指针变量来存储变量的地址值。             |
|      当我们要传递一些不应更改的小值时，这种方法是首选。      |        当我们要向函数传递大量数据时，这种方法是首选。        |
|         按值调用被认为更安全，因为原始数据得以保留。         |        按引用调用有风险，因为它允许直接修改原始数据。        |

注意：在C语言中，我们使用指针来实现按引用调用。在C++中，我们可以使用指针或[引用](https://www.geeksforgeeks.org/references-in-c/)来实现按引用传递。在Java中，[基本类型按值传递，非基本类型总是按引用传递](https://www.geeksforgeeks.org/g-fact-31-java-is-strictly-pass-by-value/)。

## 结论

总之，按值调用意味着将值作为副本传递给函数，因此原始数据得以保留，函数内部所做的任何更改都不会反映在原始数据中，而按引用调用意味着传递变量的内存位置的引用（在C语言中，我们传递指针来实现按引用调用），因此函数内部所做的更改会直接修改原始值。两者之间的选择完全取决于程序的具体需求和考虑。