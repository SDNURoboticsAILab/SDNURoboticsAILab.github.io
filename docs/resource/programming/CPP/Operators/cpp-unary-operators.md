---
comments: true
---

# C++ 一元运算符

C++ 中的一元运算符是那些作用于单个值（操作数）的运算符。它们执行更改值的符号、将其递增或递减 1 或获取其地址等操作。示例包括 ++ 表示增量，— 表示递减，+ 表示正值，– 表示负值，！用于逻辑否定，以及 & 用于检索内存地址。在本文中，我们将讨论 C++ 中可用的各种一元运算符。

## C++ 中的一元运算符类型

C++ 共有 8 个一元运算符，如下所示：

1. **自增运算符 （++）**
2. **自减运算符 （–）**
3. **一元加号运算符 （+）**
4. **一元减号运算符 （-）**
5. **逻辑 否 运算符 （！）**
6. **按位 否 运算符 （~）**
7. **取址 运算符 （&）**
8. **间接寻址运算符 （\*）**
9. **sizeof 运算符**

### **1. 递增运算符 （++）**

increment 运算符用于将其操作数的值增加 1。它适用于数字操作数，并用作操作数的前缀和后缀

**语法**

```C++
++ operand
```

或

```C++
operand ++
```

**例**

```C++
#include <iostream> 
  
using namespace std; 
  
int main() 
{ 
    int x = 5; 
  
    // Increment Operator (++) 
    cout << "Initial value of x: " << x << endl; 
    x++; // Increment x by 1 
    cout << "After x++, x is now: " << x << endl; 
  
    // Prefix and Postfix Increment/Decrement 
    int a = 10; 
    int b, c; 
  
    b = ++a; // Prefix increment: first, increment a, then 
             // assign to b 
    c = a++; // Postfix increment: first, assign a to c, 
             // then increment a 
  
    cout << "a: " << a << ", b: " << b << ", c: " << c 
         << endl; 
  
    return 0; 
}
```

**输出**

```C++
Initial value of x: 5
After x++, x is now: 6
a: 12, b: 11, c: 11
```



### **2. 递减运算符 （–）**

递减运算符用于将值递减 1。就像 increment 运算符一样，它可以用作 pre-decrement 和 post-decrement。它适用于数值。

**语法**

```C++
operand --
```

或

```C++
-- operand
```

**例**

```C++
// C++ program to illustrate the decrement operator 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
  
    int var = 10; 
    cout << "Value before decrement: " << var << endl; 
    var--; 
    cout << "Value after decrement: " << var; 
    return 0; 
}
```

**输出**

```C++
Value before decrement: 10
Value after decrement: 9
```

要了解有关递增和递减运算符的更多信息，请参阅文章 –[ C++ 递增和递减运算符](https://www.geeksforgeeks.org/cpp-increment-and-decrement-operators/)



### 3. 一元加运算符 （+）

符号 （+） 表示 C++ 中的一元加号运算符，它显式指定其操作数的正值。如果 a 已经是正数，它不会改变 a 的符号，但它可以用于表达式的清晰度。

– 是一元减号运算符，它将其操作数的符号更改为负数。

解释：

- 一元减号 （-） 更改值的符号。如果 a 为正数，则 -a 为负数。
- 一元加号 （+） 用于显式指定正值。

**语法**

```C++
+ operand
```

**例**

```C++
// C++ program to illustrate the unary plus operator 
#include <iostream> 
  
using namespace std; 
  
int main() 
{ 
    int a = 10; 
    int c = +a; // Unary Plus: Explicitly specifies 'a' as 
                // positive 
  
    cout << "Original value of a: " << a << endl; 
    cout << "After using unary plus (+a): " << c << endl; 
  
    return 0; 
}
```

**输出**

```C++
Original value of a: 10
After using unary plus (+a): 10
```



### 4. 一元减号 （-） 运算符

符号 （+） 表示 C++ 中的一元加号运算符，该运算符将其操作数的符号更改为负数。如果操作数为负数，则此运算符将使其为正数，反之亦然。

**语法**

```C++
- operand
```

**例**

```C++
// C++ program to illustrate the unary minus operator 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
    int var = 20; 
    cout << "Initial Value: " << var << endl; 
    cout << "Value with (-): " << -var; 
    
    return 0; 
}
```

**输出**

```C++
Initial Value: 20
Value with (-): -20
```



### 5. 逻辑 NOT 运算符 （！）

逻辑 NOT 运算符 （！） 用于否定布尔表达式的值。如果操作数为 false，则返回 true，如果操作数为 true，则返回 false。

> **注意：**在 C++ 中，零被视为 false，任何非零值都被视为 true。

**语法**

```C++
! operand
```

**例**

```C++
// C++ program to illustrate the use of logical NOT operator 
#include <iomanip> 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
    bool isTrue = true; 
    // Logical NOT: Negates the value of 'isTrue' 
    bool isFalse = !isTrue; 
  
    // print string correspoinding to true and false 
    cout << boolalpha; 
  
    cout << "Value of isTrue: " << isTrue << endl; 
    cout << "Value of isFalse (!isTrue): " << isFalse 
         << endl; 
  
    return 0; 
}
```

**输出**

```C++
Value of isTrue: true
Value of isFalse (!isTrue): false
```



### 6. 按位 NOT 运算符 （~）

C++ 中的按位 NOT 运算符 ~ 对整数等整型数据类型执行按位求反运算。它反转操作数的每个位，将每个 0 位更改为 1，将每个 1 位更改为 0'。

**语法**

```C++
~ operand
```

**例**

```C++


// C++ program to illustrate the use of first complement 
// operator 
#include <iostream> 
  
using namespace std; 
  
int main() 
{ 
    // Binary: 0000 0101 
    unsigned int a = 5; 
    // Bitwise NOT: Inverts each bit of 'a' 
    unsigned int b = ~a; 
  
    cout << "Original value of a: " << a 
         << " (Binary: 0000 0101)" << endl; 
    cout << "Value of b after ~a: " << b 
         << " (Binary: 1111 1010)" << endl; 
  
    return 0; 
}
```

**输出**

```C++
Original value of a: 5 (Binary: 0000 0101)
Value of b after ~a: 4294967290 (Binary: 1111 1010)
```



### 7. Addressof 运算符 （&）

addressof 运算符 （&） 检索变量的内存地址。它返回变量在计算机内存中存储的内存位置。

**语法**

```C++
& operand
```

**例**

```C++
// C++ program to illustrate the use of addressof operator 
#include <iostream> 
  
using namespace std; 
  
int main() 
{ 
    int number = 42; 
    // Pointer 'ptr' stores the address of 'number' 
    int* ptr = &number; 
  
    cout << "Value of number: " << number << endl; 
    cout << "Address of number: " << &number << endl; 
  
    return 0; 
}
```

**输出**

```C++
Value of number: 42
Address of number: 0x7fff5785a304
```



### 8. 取消引用运算符 （*）

取消引用运算符 （*） 用于访问存储在指针中的特定内存地址处的值。它 “指向” 存储在该 Sddress 中的值。

**语法**

```C++
* operand
```

**例**

```C++
// C++ program to illustrate the dereferencing operator 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
    int var = 10; 
    int* ptr = &var; 
  
    cout << "var = " << var << endl; 
    cout << "*ptr = " << *ptr; 
    return 0; 
}
```

**输出**

```C++
var = 10
*ptr = 10
```



### 9. sizeof 运算符

sizeof 运算符是 C++ 中的一个特殊一元运算符，它返回其操作数的大小 it 字节。其操作数可以是任何数据类型或变量。

**语法**

```C++
sizeof (operand)
```

**例**

```C++
// C++ program to illustrate the use of sizeof operator 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
    // integer array with 10 elements 
    int arr[10]; 
  
    // finding size of integer 
    cout << "Integer Size: " << sizeof(int) << endl; 
    cout << "Size of Integer Array with Elements: "
         << sizeof(arr); 
    return 0; 
}
```

**输出**

```C++
Integer Size: 4
Size of Integer Array with Elements: 40
```



## C++ 中一元运算符的优先级和结合性

### **一元运算符的优先级**

一元运算符通常比大多数二元运算符具有更高的优先级。在大多数二进制操作之前，它们具有固定的执行顺序。

### **一元运算符的结合性**

一元运算符是右结合的，这意味着如果将多个一元运算符应用于同一操作数，则会从右到左计算它们。

**例**

- int a = 5;： 使用值 5 初始化变量 'a'。
- int b = -++a;： 在此表达式中：
- ++a 是前缀增量，它将 'a' 的值增加 1。
- – 是一元减号运算符，它更改从 ++a 获得的值的符号。
- 然后在应用一元运算符后显示 'a' 的初始值和 'b' 的值。

```C++
// C++ program to illustrate the precedence and 
// associativity of the unary operators 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
    int a = 5; 
  
    // Demonstration of unary operators' precedence and 
    // associativity 
    int b = -++a; 
  
    cout << "Initial value of a: " << a << endl; 
    cout << "Value of b (-++a): " << b << endl; 
  
    return 0; 
}
```

**输出**

```C++
Initial value of a: 6
Value of b (-++a): -6
```



夏天来了，也是提高技能的时候了！超过 5,000 名学习者现在已经完成了从 **DSA 基础知识到高级开发计划**（如全栈、后端开发、数据科学）的旅程。

当我们的 [DSA to Development： Coding Guide](https://gfgcdn.com/tu/Q8V/) 将帮助您在几个月内掌握所有这些时，为什么还要去其他任何地方呢！现在就申请我们的[DSA发展计划](https://gfgcdn.com/tu/Q8V/)，我们的顾问将与您联系以获得进一步的指导和支持。
