# C++中的return语句示例

**先决条件：**[C++中的函数](https://www.geeksforgeeks.org/functions-in-c/)

**return语句**将执行流程返回到调用它的[函数](https://www.geeksforgeeks.org/functions-in-c/)。此语句不需要任何条件语句。一旦执行该语句，**程序流程立即停止**，并从调用它的地方返回控制。对于void函数，return语句可能不返回任何内容，但对于非void函数，必须返回一个返回值。

**语法：**

```
return[expression];
```

![return statement in C++](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20191128194949/CPP-return-statement.png)

有多种使用return语句的方式。以下是一些示例：

### **1.不返回值的方法**

在C++中，当方法具有返回类型时，不能跳过return语句。只有对于void类型，才能跳过return语句。

### **在void返回类型函数中不使用return语句**

当函数不返回任何内容时，使用void返回类型。因此，如果函数定义中有void返回类型，那么该函数内部通常不会有return语句。

**语法：**

```
void func()
{
    .
    .
    .
}
```

**示例：**

```cpp
// C++ code to show not using return 
// statement in void return type function 
#include <iostream> 
using namespace std; 
  
// void method 
void Print() 
{ 
    cout << "Welcome to GeeksforGeeks"; 
} 
  
// Driver method 
int main() 
{ 
  
    // Calling print 
    Print(); 
  
    return 0; 
} 
```

**输出**

```
Welcome to GeeksforGeeks
```

#### 在void返回类型函数中使用return语句

现在的问题是，如果在void返回类型函数中有return语句会怎样？我们知道，如果函数定义中有void返回类型，那么该函数内部通常不会有return语句。但如果其中有return语句，只要语法正确，也不会有问题：

**语法：**

```
void func()
{
    return;
}
```

此语法在函数中用作跳转语句，以中断函数的流程并跳出函数。可以将其视为在函数中使用的“[break语句](https://www.geeksforgeeks.org/break-statement-cc/)”的替代方案。

**示例：**

```cpp
// C++ code to show using return 
// statement in void return type function 
#include <iostream> 
using namespace std; 
  
// void method 
void Print() 
{ 
    cout << "Welcome to GeekforGeeks"; 
  
    // void method using the return statement 
    return; 
} 
  
// Driver method 
int main() 
{ 
  
    // Calling print 
    Print(); 
    return 0; 
} 
```

**输出**

```
Welcome to GeekforGeeks
```

但如果return语句试图在void返回类型函数中返回一个值，这将导致错误。

**错误语法：**

```
void func()
{
    return value;
}
```

**示例：**

```cpp
// C++ code to show using return statement 
// with a value in void return type function 
#include <iostream> 
using namespace std; 
  
// void method 
void Print() 
{ 
    cout << "Welcome to GeeksforGeeks"; 
  
    // void method using the return 
    // statement to return a value 
    return 10; 
} 
  
// Driver method 
int main() 
{ 
  
    // Calling print 
    Print(); 
  
    return 0; 
} 
```

**输出**

```
warning: 'return' with a value, in function returning void
```

### 2. 返回值的方法：

对于定义了返回类型的方法，return语句必须紧随该指定返回类型的返回值。

**语法：**

```
return-type func()
{
    return value;
}
```

**示例：**

```cpp
// C++ code to illustrate Methods returning 
// a value using return statement 
#include <iostream> 
using namespace std; 
  
// non-void return type 
// function to calculate sum 
int SUM(int a, int b) 
{ 
    int s1 = a + b; 
  
    // method using the return 
    // statement to return a value 
    return s1; 
} 
  
// Driver method 
int main() 
{ 
    int num1 = 10; 
    int num2 = 10; 
    int sum_of = SUM(num1, num2); 
    cout << "The sum is " << sum_of; 
    return 0; 
}
```

**输出：**

```
The sum is 20
```

**注意：** *我们只能使用return语句从函数中返回一个值。要返回多个值，我们可以使用指针、结构、类等。要了解更多信息，请点击* [这里。](https://www.geeksforgeeks.org/how-to-return-multiple-values-from-a-function-in-c-or-cpp/)