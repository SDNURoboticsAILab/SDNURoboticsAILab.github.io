# C++ 中的函数

[函数](https://www.geeksforgeeks.org/types-of-functions/)是一组接受输入、进行特定计算并产生输出的语句。我们的想法是将一些常用或重复执行的任务组合在一起，形成一个函数，这样我们就可以调用这个函数，而不必为不同的输入重复编写相同的代码。
简单来说，函数是一个代码块，只有在被调用时才会运行。

语法：![Syntax of Function](https://media.geeksforgeeks.org/wp-content/uploads/20220719131329/syntaxofFunction-660x214.png)

**示例:**

```cpp
// C++ Program to demonstrate working of a function
#include <iostream>
using namespace std;

// Following function that takes two parameters 'x' and 'y'
// as input and returns max of two input numbers
int max(int x, int y)
{
    if (x > y)
        return x;
    else
        return y;
}

// main function that doesn't receive any parameter and
// returns integer
int main()
{
    int a = 10, b = 20;

    // Calling above function to find max of 'a' and 'b'
    int m = max(a, b);

    cout << "m is " << m;
    return 0;
}
```

**输出:**

```
m is 20
```

**时间复杂度:** O(1)

**空间复杂度:** O(1)

## 为什么需要函数？

- 函数可以帮助我们减少代码冗余。如果功能在软件中的多个地方执行，那么与其反复编写相同的代码，不如创建一个函数并在所有地方调用它。这也有助于维护，因为如果我们将来要更改功能，只需在一个地方进行更改即可。
- 函数使代码模块化。考虑一下一个有许多行代码的大文件。如果将代码分成若干函数，阅读和使用代码就会变得非常简单。
- 函数提供了抽象性。例如，我们可以使用库函数，而不必担心它们的内部工作。

## ***Function Declaration***

函数声明会告诉编译器函数的参数个数、参数数据类型和返回类型。在函数声明中写入参数名是可选项，但必须在定义中写入参数名。下面是函数声明的示例。(以下声明中不包含参数名） 

![Function Declaration in C++](https://media.geeksforgeeks.org/wp-content/uploads/20220719123136/FunctionPrototypeincppmin-660x330.png)

**示例:**

```cpp
// C++ Program to show function that takes
// two integers as parameters and returns
// an integer
int max(int, int);

// A function that takes an int
// pointer and an int variable
// as parameters and returns
// a pointer of type int
int* swap(int*, int);

// A function that takes
// a char as parameter and
// returns a reference variable
char* call(char b);

// A function that takes a
// char and an int as parameters
// and returns an integer
int fun(char, int);
```

## 功能类型

![Types of Function in C++](https://media.geeksforgeeks.org/wp-content/uploads/20220719123505/Typesoffunction-660x248.png)

## 用户自定义功能

用户自定义函数是用户/客户自定义的代码块，专门用于降低大型程序的复杂性。它们通常也被称为 **“定制函数”**，仅用于满足用户面临问题的条件，同时降低整个程序的复杂性。

## 库函数

库函数也称为 **“内置函数”**。这些函数是已定义的编译器软件包的一部分，由具有特殊和不同含义的特殊函数组成。内置函数给我们带来了优势，因为我们可以直接使用它们而无需定义它们，而在用户自定义函数中，我们必须在使用它们之前声明和定义一个函数。
**例如：**sqrt()、setw()、strcat()等。

## 函数参数传递

传递给函数的参数称为**实际参数**。例如，在下面的程序中，5 和 10 是实际参数。
函数接收到的参数称为**形参**。例如，在上述程序中，x 和 y 是形参。

![Formal Parameter and Actual Parameter in C++](https://media.geeksforgeeks.org/wp-content/uploads/20220719161856/Actualparameterandformalparameter-660x337.png)

<center>*Formal Parameter and Actual Parameter*</center>

有两种最常用的参数传递方式：

1.**按值传递：**在这种参数传递方法中，实际参数的值被复制到函数的形参中。实际参数和形参存储在不同的内存位置，因此函数中进行的任何更改都不会反映在调用者的实际参数中。

2.**引用传递：** 实际参数和形式参数都引用相同的位置，因此函数内部的任何更改都会反映在调用者的实际参数中。

## 函数定义

**按值传递**用于在函数fun()中不修改x的值的情况。

```cpp
// C++ Program to demonstrate function definition
#include <iostream>
using namespace std;

void fun(int x)
{
    // definition of
    // function
    x = 30;
}

int main()
{
    int x = 20;
    fun(x);
    cout << "x = " << x;
    return 0;
}
```

**输出**

```cpp
// C++ Program to demonstrate function definition
#include <iostream>
using namespace std;

void fun(int x)
{
    // definition of
    // function
    x = 30;
}

int main()
{
    int x = 20;
    fun(x);
    cout << "x = " << x;
    return 0;
}
```

**时间复杂度:** O(1)

**空间复杂度:** O(1)

## 使用指针的函数

函数 fun() 需要一个指向整数（或整数地址）的指针 ptr。它修改 ptr 地址处的值。取消引用操作符 * 用于访问地址处的值。在语句 “*ptr = 30 ”中，地址 ptr 上的值被改为 30。地址操作符 & 用于获取任意数据类型变量的地址。在函数调用语句 “fun(&x) ”中，传递了 x 的地址，这样就可以使用其地址修改 x。

```cpp
// C++ Program to demonstrate working of
// function using pointers
#include <iostream>
using namespace std;

void fun(int* ptr) { *ptr = 30; }

int main()
{
    int x = 20;
    fun(&x);
    cout << "x = " << x;

    return 0;
}
```

**输出**

```
x = 30
```

***时间复杂度:*** O(1)

***空间复杂度:*** O(1)

## 将字符串作为参数传递：

在 C++ 中，我们可以通过多种方式将字符串作为参数传递

1.通过值传递
2.通过引用传递
3.通过指针传递

### 1. 按值传递

在这种情况下，当你传递一个字符串值时，它会复制一个字符串值。

```cpp
#include <iostream>
#include <string>

void printString(std::string str) {
    std::cout << str << std::endl;
}

int main() {
    std::string myString = "Hello, GFG!";
    printString(myString);
    return 0;
}
```

**输出**

```
Hello, GFG!
```

### 2. 引用传递

使用“&”运算符可以实现这一功能

```cpp
#include <iostream>
#include <string>

void printString(const std::string& str) { // Note the 'const' to prevent modification
    std::cout << str << std::endl;
}

int main() {
    std::string myString = "welcome to gfg";
    printString(myString);
    return 0;
}
```

**输出**

```
welcome to gfg
```

### 3. 指针传递

这可以通过使用 * 操作符来实现

```cpp
#include <iostream>
#include <string>

void printString(const std::string* str) { // Note the 'const' to prevent modification
    std::cout << *str << std::endl;
}

int main() {
    std::string myString = "This is Pss by pointer";
    printString(&myString);
    return 0;
}

```

**输出**

```
This is Pss by pointer
```

## 从函数中返回字符串：

这可以通过使用函数 “std::string ”来实现

```cpp
#include <iostream>
#include <string>

std::string getGreeting() {
    return "This is  C++";
}

int main() {
    std::string greeting = getGreeting();
    std::cout << greeting << std::endl;
    return 0;
}
```

**输出**

```
This is  C++
```

## 从函数返回指针

我们需要创建一个函数，返回指向整数数组的指针。

```cpp
#include <iostream>

int* createArray(int size) {
    int* arr = new int[size]; // Dynamically allocate memory for an array
    for (int i = 0; i < size; ++i) {
        arr[i] = i * 10; // Initialize array elements
    }
    return arr; // Return the pointer to the array
}

int main() {
    int size = 10;
    int* myArray = createArray(size); // Function returns a pointer to the array
    
    // Print the array
    for (int i = 0; i < size; ++i) {
        std::cout << myArray[i] << " ";
    }
    std::cout << std::endl;

    delete[] myArray; // Don't forget to free the allocated memory
    return 0;
}
```

**输出**

```
0 10 20 30 40 50 60 70 80 90 
```

## 回调函数（作为参数传递给其他函数的函数）

回调函数是作为参数传递给另一个函数的函数

```cpp
#include <iostream>

// Define a callback function type
typedef void (*CallbackFunction)();

// Function that takes a callback function as an argument
void performAction(CallbackFunction callback) {
    std::cout << "Performing some action...\n";
    // Call the callback function
    callback();
}

// Example callback function
void myCallback() {
    std::cout << "Callback function \n";
}

int main() {
    // Pass the callback function to performAction
    performAction(myCallback);
    return 0;
}
```

**输出**

```
Performing some action...
Callback function 
```

## 函数指针数组及其元素的访问方式

这里有一个C++示例，用于从数组中访问元素

```cpp
#include <iostream>

// Function declarations
int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int multiply(int a, int b) {
    return a * b;
}

int main() {
    // Declare and initialize an array of function pointers
    int (*funcArray[3])(int, int) = { add, subtract, multiply };

    // Variables to use as function parameters
    int x = 2, y = 3;

    // Access and call the functions using the array of function pointers
    std::cout << "Add: " << funcArray[0](x, y) << std::endl;       // Calls add(10, 5)
    std::cout << "Subtract: " << funcArray[1](x, y) << std::endl;  // Calls subtract(10, 5)
    std::cout << "Multiply: " << funcArray[2](x, y) << std::endl;  // Calls multiply(10, 5)

    return 0;
}
```

**输出**

 ```
 Add: 5
 Subtract: -1
 Multiply: 6
 ```

## C++中按值调用和按引用调用的区别

|                 按值调用                 |                 按引用调用                 |
| :--------------------------------------: | :----------------------------------------: |
|           将值的副本传递给函数           |            将值的地址传递给函数            |
| 在函数内部所做的更改不会反映在其他函数中 |    在函数内部所做的更改会反映在函数外部    |
| 实际参数和形式参数将在不同的内存位置创建 | 实际参数和形式参数将在相同的内存位置创建。 |

## 关于C++函数的要点

1. 大多数C++程序都有一个名为main()的函数，当用户运行程序时，操作系统会调用该函数。
2. 每个函数都有一个返回类型。如果函数不返回任何值，则使用void作为返回类型。此外，如果函数的返回类型是void，我们仍然可以在函数定义的主体中使用return语句，而不指定任何常量、变量等，只需提及‘return;’语句，这表示函数的终止，如下所示：

```cpp
void function name(int a)
{
    ....... // Function Body
        return; // Function execution would get terminated
}
```

3. 要声明一个只能在没有参数的情况下调用的函数，我们应该使用“void fun(void)”。顺便提一下，在C++中，空列表意味着函数只能在没有参数的情况下调用。在C++中，void fun()和void fun(void)是相同的。

## 主函数

主函数是一个特殊的函数。每个C++程序都必须包含一个名为main的函数。它作为程序的入口点。计算机将从主函数的开头开始运行代码。

主函数的类型

1. 无参数：

```cpp
// Without Parameters
int main() { ... return 0; }
```

2.带参数：

```cpp
// With Parameters
int main(int argc, char* const argv[]) { ... return 0; }
```

为main函数提供参数选项的原因是为了允许从命令行输入。当你使用带参数的main函数时，它会将程序名称后的每一组字符（由空格分隔）保存为名为argv的数组中的元素。
由于main函数具有int返回类型，程序员必须在代码中始终包含一个return语句。返回的数字用于通知调用程序程序执行的结果。返回0表示没有问题。

## C++递归

当函数在同一个函数中被调用时，称为C++中的递归。调用自身的函数称为递归函数。
一个调用自身并且不在函数调用后执行任何任务的函数称为尾递归。在尾递归中，我们通常使用return语句调用相同的函数。
语法：

我们有直接递归和间接递归

1. **直接递归：**
   当函数调用自身时，可以进行直接递归

```cpp
#include <iostream>
using namespace std;

void directRecursion(int n) {
    if (n > 0) {
        cout << n << " ";
        directRecursion(n - 1); // Function calls itself
    }
}

int main() {
    directRecursion(10);
    return 0;
}
```

**输出**

```
5 4 3 2 1 
```

2. **间接递归**
在这种情况下，一个函数调用另一个函数。

```cpp
#include <iostream>
using namespace std;

void indirectRecursionB(int n); // Forward declaration

void indirectRecursionA(int n) {
    if (n > 0) {
        cout << n << " ";
        indirectRecursionB(n - 1); // Function A calls Function B
    }
}

void indirectRecursionB(int n) {
    if (n > 1) {
        cout << n << " ";
        indirectRecursionA(n / 2); // Function B calls Function A
    }
}

int main() {
    indirectRecursionA(10);
    return 0;
}
```

**输出**

```
10 9 4 3 1 
```

## 尾递归和非尾递归：

**1. Tail Recursion:**

尾递归发生在函数在其最后操作中进行递归调用时，

```cpp
#include <iostream>
using namespace std;

void tailRecursion(int n) {
    if (n > 0) {
        cout << n << " ";
        tailRecursion(n - 1); // Recursive call is the last operation
    }
}

int main() {
    tailRecursion(15);
    return 0;
}
```

**输出**

```
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 
```

**2. Non-Tail Recursion**

非尾递归发生在函数在递归调用后执行某些操作时。

```cpp
#include <iostream>
using namespace std;

int nonTailRecursion(int n) {
    if (n > 0) {
        return n + nonTailRecursion(n - 1); // Recursive call is not the last operation
    } else {
        return 0;
    }
}

int main() {
    int result = nonTailRecursion(20);
    cout << "Result: " << result << endl;
    return 0;
}
```

**输出**

```
Result: 210
```

要了解更多信息，请参阅[这篇文章](https://www.geeksforgeeks.org/recursion/)。

## C++传递数组给函数

在C++中，为了重用数组逻辑，我们可以创建一个函数。要将数组传递给C++中的函数，我们只需要提供数组名称。

```
function_name(array_name[]); //passing array to function
```

**示例：打印给定数组中的最小数字。**

```cpp
#include <iostream>
using namespace std;
void printMin(int arr[5]);
int main()
{
    int ar[5] = { 30, 10, 20, 40, 50 };
    printMin(ar); // passing array to function
}
void printMin(int arr[5])
{
    int min = arr[0];
    for (int i = 0; i < 5; i++) {
        if (min > arr[i]) {
            min = arr[i];
        }
    }
    cout << "Minimum element is: " << min << "\n";
}

// Code submitted by Susobhan Akhuli
```

**输出**

```
Minimum element is: 10
```

**时间复杂度：**O(n)，其中n是数组的大小
**空间复杂度：**O(n)，其中n是数组的大小。

## C++重载（函数）

如果我们创建两个或更多成员具有相同的名称但参数的数量或类型不同，这被称为C++重载。在C++中，我们可以重载：

- 方法，

- 构造函数和

- 索引属性
  **C++中的重载类型有：**

- 函数重载

- 运算符重载

  **C++函数重载**
  函数重载被定义为具有相同名称但参数不同的两个或多个函数的过程。在函数重载中，函数通过使用不同类型或数量的参数来重新定义。只有通过这些差异，编译器才能区分这些函数。
  函数重载的优点是它增加了程序的可读性，因为你不需要为相同的操作使用不同的名称。

**示例：更改add()方法的参数数量**

```cpp
// program of function overloading when number of arguments
// vary
#include <iostream>
using namespace std;
class Cal {
public:
    static int add(int a, int b) { return a + b; }
    static int add(int a, int b, int c)
    {
        return a + b + c;
    }
};
int main(void)
{
    Cal C; // class object declaration.
    cout << C.add(10, 20) << endl;
    cout << C.add(12, 20, 23);
    return 0;
}

// Code Submitted By Susobhan Akhuli
```

**输出**

```
30
55
```

**时间复杂度：**O(1)
**空间复杂度：**O(1)

**示例：当参数的类型不同时。**

```cpp
// Program of function overloading with different types of
// arguments.
#include <iostream>
using namespace std;
int mul(int, int);
float mul(float, int);

int mul(int a, int b) { return a * b; }
float mul(double x, int y) { return x * y; }
int main()
{
    int r1 = mul(6, 7);
    float r2 = mul(0.2, 3);
    cout << "r1 is : " << r1 << endl;
    cout << "r2 is : " << r2 << endl;
    return 0;
}

// Code Submitted By Susobhan Akhuli
```

**输出**

```
r1 is : 42
r2 is : 0.6
```

**时间复杂度：**O(1)
**空间复杂度：**O(1)

## 函数重载和歧义

当编译器无法决定在重载函数中调用哪个函数时，这种情况称为函数重载歧义。
当编译器显示歧义错误时，编译器不会运行程序。

**歧义的原因：**

- 类型转换。

- 带有默认参数的函数。

- 通过引用传递的函数。

  **类型转换：-**

```cpp
#include <iostream>
using namespace std;
void fun(int);
void fun(float);
void fun(int i) { cout << "Value of i is : " << i << endl; }
void fun(float j)
{
    cout << "Value of j is : " << j << endl;
}
int main()
{
    fun(12);
    fun(1.2);
    return 0;
}

// Code Submitted By Susobhan Akhuli
```

上例显示了 “调用重载的 ‘fun(double)’ 有歧义 ”的错误。fun(10) 将调用第一个函数。根据我们的预测，fun(1.2) 将调用第二个函数。但是，这并不是指任何函数，因为在 C++ 中，所有浮点常量都被视为 double 而不是 float。如果我们将 float 替换为 double，程序就能正常运行。因此，这是从 float 到 double 的类型转换。

**带默认参数的函数：-**

```cpp
#include <iostream>
using namespace std;
void fun(int);
void fun(int, int);
void fun(int i) { cout << "Value of i is : " << i << endl; }
void fun(int a, int b = 9)
{
    cout << "Value of a is : " << a << endl;
    cout << "Value of b is : " << b << endl;
}
int main()
{
    fun(12);

    return 0;
}

// Code Submitted By Susobhan Akhuli
```

上例显示错误 “调用重载的 ‘fun(int)’ 有歧义”。fun(int a, int b=9)有两种调用方式：一种是调用带有一个参数的函数，即 fun(12)；另一种是调用带有两个参数的函数，即 fun(4,5)。fun(int i) 函数只调用一个参数。因此，编译器无法在 fun(int i) 和 fun(int a,int b=9) 中进行选择。

**带引用传递的函数：-**

```cpp
#include <iostream>
using namespace std;
void fun(int);
void fun(int&);
int main()
{
    int a = 10;
    fun(a); // error, which fun()?
    return 0;
}
void fun(int x) { cout << "Value of x is : " << x << endl; }
void fun(int& b)
{
    cout << "Value of b is : " << b << endl;
}

// Code Submitted By Susobhan Akhuli
```

上例显示了一个错误 “调用重载的 ‘fun(int&)’ 有歧义”。第一个函数接收一个整数参数，第二个函数接收一个引用参数作为参数。在这种情况下，编译器不知道用户需要哪个函数，因为 fun(int) 和 fun(int&) 在语法上没有区别。

**友元函数**

- 友元函数是C++中的一种特殊函数，尽管它不是类的成员函数，但它有权访问类的私有和受保护数据。
- 友元函数是一个类的非成员函数或普通函数，通过在类内部使用关键字“friend”来声明。通过将函数声明为友元，所有访问权限都授予该函数。
- 关键字“friend”仅放置在函数声明中，而不是函数定义中。
- 当调用友元函数时，既不使用对象的名称也不使用点运算符。然而，它可能接受对象作为参数，以便访问其值。
- 友元函数可以在类的任何部分声明，即公共、私有或受保护部分。
  **C++中友元函数的声明**
  **语法：**

```
class <class_name> {    
           friend  <return_type>  <function_name>(argument/s);
};
```

示例_1：使用友元函数找出两个数中的最大值

```cpp
#include <iostream>
using namespace std;
class Largest {
    int a, b, m;

public:
    void set_data();
    friend void find_max(Largest);
};

void Largest::set_data()
{
    cout << "Enter the first number : ";
    cin >> a;
    cout << "\nEnter the second number : ";
    cin >> b;
}

void find_max(Largest t)
{
    if (t.a > t.b)
        t.m = t.a;
    else
        t.m = t.b;

    cout << "\nLargest number is " << t.m;
}

int main()
{
    Largest l;
    l.set_data();
    find_max(l);
    return 0;
}
```

**输出**

```
Enter the first number : 789
Enter the second number : 982
Largest number is 982
```

