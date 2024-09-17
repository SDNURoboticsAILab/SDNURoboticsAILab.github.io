# C++中的参数传递技术

在C++中，当调用函数时，必须将数据传递给函数以执行操作。这些数据称为参数或实参，C++中有多种参数传递方法，每种方法都有其优缺点。在本文中，我们将讨论C++中的各种参数传递技术。

### 基本术语

- ***\*函数参数:\****这些变量是指定在函数参数列表中的变量，表示函数在调用时期望接收的数据。
- ***\*实际参数:\**** 在函数调用期间传递的表达式或值。当函数被调用时，它接收这些值作为输入。
- 函数签名声明的参数。它们作为占位符，用于在函数被调用时提供的值。

## C++中的参数传递技术

有3种不同的方法可以在C++中将参数传递给函数。这些是：

按值传递

按引用传递

按指针传递

## **1. 按值传递**

在按值传递方法中，变量的实际值被复制并传递给函数，而不是原始变量。因此，函数内部对参数的任何更改都不会影响函数外部变量的原始值。尽管这种方法易于理解和实现，但对于大数据结构来说并不实用，因为它涉及复制值。

**示例**

```cpp
// C++ program to illustrate the pass by value 
#include <iostream> 
using namespace std; 
  
// function to swap variables 
void swap(int a, int b) 
{ 
    int temp = a; 
    a = b; 
    b = temp; 
} 
int main() 
{ 
    int x = 5; 
    int y = 10; 
  
    cout << "Before Swapping:\n"; 
    cout << "x = " << x << ", y = " << y << endl; 
  
    // Call the 'swap' function with pass-by-value 
    // parameters 
    swap(x, y); 
  
    // Print the values of 'x' and 'y' after the 
    // (ineffective) swap The values remain unchanged 
    // because the function works on copies. 
    cout << "After Swapping:\n"; 
    cout << "x = " << x << ", y = " << y << endl; 
  
    return 0; 
}
```

**输出**

```
Before Swapping:
x = 5, y = 10
After Swapping:
x = 5, y = 10
```

## 2. 按引用传递

在按引用传递方法中，我们不是传递参数本身，而是将参数的引用传递给函数。这允许函数更改原始参数的值。

我们在函数内部对参数所做的任何更改都会反映在原始参数中，因此在处理数据时必须小心。

**示例**

```
// C++ program to illustrate the use of pass by reference 
#include <iostream> 
using namespace std; 
  
// function to swap variables 
void swap(int& a, int& b) 
{ 
    int temp = a; 
    a = b; 
    b = temp; 
} 
  
// driver code 
int main() 
{ 
    int x = 5; 
    int y = 10; 
    cout << "Before swap:\n"; 
    cout << "x = " << x << ", "; 
    cout << "y = " << y << endl; 
  
    // Call the 'swap' function with pass-by-reference 
    // parameters Values of 'x' and 'y' are modified in the 
    // calling code because references are used. 
    swap(x, y); 
  
    cout << "After swap:\n"; 
    cout << "x = " << x << ", "; 
    cout << "y = " << y << endl; 
    return 0; 
}
```

**输出**

```
Before swap:
x = 5, y = 10
After swap:
x = 10, y = 5
```

## 3. 按指针传递

按指针传递与按引用传递方法非常相似。唯一的区别是我们传递原始指针而不是引用给函数。这意味着我们传递参数的地址给函数。

**示例**

```cpp
// C++ program to illustrate the pass by pointer method. 
#include <iostream> 
using` `namespace` `std; 
 
// function to swap variables 
void` `swap(``int``* a, ``int``* b) 
{ 
  ``int` `temp = *a; 
  ``*a = *b; 
  ``*b = temp; 
} 
 
// driver code 
int` `main() 
{ 
 
  ``int` `x = 5; 
  ``int` `y = 10; 
 
  ``// Print the values of 'x' and 'y' before the swap 
  ``cout << ``"Before swap:\n"``; 
  ``cout << ``"x = "` `<< x << ``" ,"``; 
  ``cout << ``"y = "` `<< y << endl; 
 
  ``// Call the 'swap' function with pass-by-pointer 
  ``// parameters 
  ``// Values of 'x' and 'y' are modified in the calling 
  ``// code because pointers are used. 
  ``swap(&x, &y); 
 
  ``// Print the values of 'x' and 'y' after the swap 
  ``cout << ``"After swap:\n"``; 
  ``cout << ``"x = "` `<< x << ``" ,"``; 
  ``cout << ``"y = "` `<< y << endl; 
 
  ``return` `0; 
}
```

**输出**

```
Before swap:
x = 5 ,y = 10
After swap:
x = 10 ,y = 5
```