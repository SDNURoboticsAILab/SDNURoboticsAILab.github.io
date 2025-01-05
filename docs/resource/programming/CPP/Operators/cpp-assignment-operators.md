---
comments: true
---

C++ 赋值运算符
=====

在 C++ 中，赋值运算符通过执行简单的操作（例如为变量赋值）来构成许多算法和计算过程的支柱。它由**等号 （ = ）** 表示，并提供任何编程语言中最基本的操作之一，用于为 C++ 中的变量分配一些值，或者换句话说，它用于存储某种信息。

## 语法

```C++
variable = value;
```

右侧的**值**将分配给左侧的**变量**。变量和值应具有相同的数据类型。

该值可以是 Literal 或相同数据类型的其他变量。

**例**

```C++
// C++ program to illustrate the use of assignment operator 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
    // Declare an integer variable 
    int x; 
    // Assign the value 20 to variable x using assignment 
    // operator 
    x = 20; 
    cout << "The value of x is: " << x << endl; 
    return 0; 
}
```

**输出**

```C++
The value of x is: 20
```

## 复合赋值运算符

在 C++ 中，赋值运算符可以与一些其他运算符组合成一个运算符，以便在一个语句中执行两个操作的组合。这些运算符称为复合赋值运算符。C++ 中有 10 个复合赋值运算符：

1. 加法赋值运算符 （ += ）
2. 减法赋值运算符 （ -= ）
3. 乘法赋值运算符 （ *= ）
4. 除法赋值运算符 （ /= ）
5. 模数赋值运算符 （ %= ）
6. 按位 AND 赋值运算符 （ &= ）
7. 按位 OR 赋值运算符 （ |= ）
8. 按位 XOR 赋值运算符 （ ^= ）
9. 左移赋值运算符 （ <<= ）
10. 右移赋值运算符 （ >>= ）

让我们详细看看他们中的每一个。



### 1. 加法赋值运算符 （+=）

在 C++ 中，加法赋值运算符 （+=） 将加法运算与变量赋值相结合，允许您以简洁有效的方式通过指定的表达式递增变量的值。

**语法**

```C++
variable += value;
```

上述表达式等效于以下表达式：

```C++
variable = variable + value;
```

**例**

```C++
// C++ program to illustrate the addition assignment operator 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
    // Initialize a variable to the store the total 
    int total = 0; 
    total += 10; 
    total += 20; 
    total += 30; 
    total += 40; 
    total += 50; 
  
    // Display the final total 
    cout << "The total is: " << total << endl; 
    return 0; 
}
```

**输出**

```C++
The total is: 150
```



### 2. 减法赋值运算符 （-=）

C++ 中的减法赋值运算符 （-=） 使您能够通过从变量中减去另一个值来更新变量的值。当您需要执行减法并将结果存储回同一变量中时，此运算符特别有用。

**语法**

```C++
variable -= value;
```

上述表达式等效于以下表达式：

```C++
variable = variable - value;
```

**例**

```C++
// C++ program to illustrate the substraction assignment 
// operator 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
    int x = 20; 
    int y = 5; 
    
    // Using the subtraction assignment operator 
    x -= y; 
    cout << "After subtraction x is now: " << x << endl; 
    return 0; 
}
```

**输出**

```C++
After subtraction x is now: 15
```



### 3. 乘法赋值运算符 （*=）

在 C++ 中，乘法赋值运算符 （*=） 用于通过将变量与另一个值相乘来更新变量的值。

**语法**

```C++
variable *= value;
```

上述表达式等效于以下表达式：

```C+=
variable = variable * value;
```

**例**

```C++
#include <iostream> 
using namespace std; 
  
int main() { 
    int x = 7; // Initialize x to 7 
    x *= 4; 
    cout << "The updated value of x is: " << x << endl; 
    return 0; 
} 
```

**输出**

```C++
The updated value of x is: 28
```



### 4. 除法赋值运算符 （/=）

除法赋值运算符将左侧的变量除以右侧的值，并将结果分配给左侧的变量。

**语法**

```C++
variable /= value;
```

上述表达式等效于以下表达式：

```C++
variable = variable / value;
```

**例**

```C++
// C++ program to illustrate the use of divide assignment 
// operator 
#include <iostream> 
using namespace std; 
  
// driver code 
int main() 
{ 
    double x = 30.0; 
  
    // dividing x by 4 and assigning the value to x 
    x /= 4.0; 
  
    cout << "value : " << x << endl; 
  
    return 0; 
}
```

**输出**

```C++
value : 7.5
```



### 5. 模数赋值运算符 （%=）

当左侧的变量除以右侧的值或变量时，模赋值运算符计算余数，并将结果分配给左侧的变量。

**语法**

```C++
variable %= value;
```

上述表达式等效于以下表达式：

```C++
variable = variable % value;
```

**例**

```C++
// C++ program to illustrate the use of modulus assignment 
// operator 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
    int a = 15; 
  
    // finding the remainder when a is divided by 15 and 
    // assigning it to a again 
    a %= 5; 
  
    cout << "value : " << a << endl; 
    return 0; 
}
```

**输出**

```C++
value : 0
```



### 6. 按位 AND 赋值运算符 （&=）

此运算符在左侧的变量和右侧的值之间执行按位 AND，并将结果分配给左侧的变量。

**语法**

```C++
variable &= value;
```

上述表达式等效于以下表达式：

```C++
variable = variable & value;
```

**例**

```C++
// C++ program to illustrate the use of Bitwise AND 
// Assignment Operator 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
    int a = 9; 
  
    // using Bitwise AND Assignment Operator 
    a &= 3; 
    cout << "value : " << a << endl; 
    return 0; 
}
```

**输出**

```C++
value : 1
```



### 7. 按位 OR 赋值运算符 （|=）

按位 OR 赋值运算符在左侧的变量和右侧的值或变量之间执行按位 OR，并将结果分配给左侧的变量。

**语法**

```C++
variable |= value;
```

上述表达式等效于以下表达式：

```C++
variable = variable | value;
```

**例**

```C++
// C++ program to illustrate the use of Bitwise OR 
// Assignment Operator 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
    int a = 5; // 0101 in binary 
  
    // using Bitwise OR Assignment Operator 
    a |= 2; 
    cout << "value : " << a << endl; 
    return 0; 
}
```

**输出**

```C++
value : 7
```



### 8. 按位 XOR 赋值运算符 （^=）

按位 XOR 赋值运算符在左侧的变量和右侧的值或变量之间执行按位 XOR，并将结果分配给左侧的变量。

**语法**

```C++
variable ^= value;
```

上述表达式等效于以下表达式：

```C++
variable = variable ^ value;
```

**例**

```C++
// C++ program to illustrate the use of Bitwise XOR 
// Assignment Operator 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
    int a = 7; 
  
    // using Bitwise XOR Assignment Operator 
    a ^= 3; 
    cout << "value : " << a << endl; 
    return 0; 
}
```

**输出**

```C++
value : 4
```



### 9. 左移赋值运算符 （<<=）

左移赋值运算符将左侧变量的位向左移动右侧指定的位置数，并将结果分配给左侧的变量。

**语法**

```C++
variable <<= value;
```

上述表达式等效于以下表达式：

```C++
variable = variable << value;
```

**例**

```C++
// C++ program to illustrate the use of Left Shift 
// Assignment Operator 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
    int a = 9; 
  
    // using Left Shift Assignment Operator 
    a <<= 4; 
    cout << "value : " << a << endl; 
    return 0; 
}
```

**输出**

```C++
value : 144
```



### 10. 右移赋值运算符 （>>=）

右移赋值运算符将左侧变量的位向右移动右侧指定的位数，并将结果分配给左侧的变量。

**语法**

```C++
variable >>= value;
```

上述表达式等效于以下表达式：

```C++
variable = variable >> value;
```

**例**

```C++
// C++ program to illustrate the use of Right Shift 
// Assignment Operator 
#include <iostream> 
using namespace std; 
  
int main() 
{ 
    int a = 19; 
  
    // using Right Shift Assignment Operator 
    a >>= 4; 
    cout << "value : " << a << endl; 
    return 0; 
}
```

**输出**

```C++
value : 1
```

另外，需要注意的是，上述所有运算符都可以重载，以便使用用户定义的数据类型进行自定义操作，以执行我们想要的操作。



夏天来了，也是提高技能的时候了！超过 5,000 名学习者现在已经完成了从 **DSA 基础知识到高级开发计划**（如全栈、后端开发、数据科学）的旅程。

当我们的 [DSA to Development： Coding Guide](https://gfgcdn.com/tu/Q8V/) 将帮助您在几个月内掌握所有这些时，为什么还要去其他任何地方呢！现在就申请我们的[DSA发展计划](https://gfgcdn.com/tu/Q8V/)，我们的顾问将与您联系以获得进一步的指导和支持。
