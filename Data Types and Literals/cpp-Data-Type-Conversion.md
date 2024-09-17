# C++ 中的类型转换

类型转换基本上是从一种类型转换为另一种类型。C++ 中有两种类型转换：
1.**隐式类型转换** 也称为“自动类型转换”。

- 由编译器自行完成，无需用户的外部触发。
- 通常在表达式中有多个数据类型存在时发生。在这种情况下，为了避免数据丢失，会发生类型转换（类型提升）。
- 所有变量的数据类型都会升级为具有最大数据类型的变量的数据类型。

```
bool -> char -> short int -> int -> 

unsigned int -> long -> unsigned -> 

long long -> float -> double -> long double
```

隐式转换可能会丢失信息，可能会丢失符号（当有符号类型隐式转换为无符号类型时），并且可能会发生溢出（当 `long long` 隐式转换为 `float` 时）。

**隐式类型转换的示例：**

```
// 以下是一个 C++ 中隐式类型转换的例子：
  
#include <iostream> 
using namespace std; 
  
int main() 
{ 
    int x = 10; // 整型数x
    char y = 'a'; // 字符型y
  
    // 字符 'a' 隐式转换为 int 时，其 ASCII 值为 97。
    x = x + y; 
  
    // 变量 x 隐式转换为 float。 
    float z = x + 1.0; 
  
    cout << "x = " << x << endl 
         << "y = " << y << endl 
         << "z = " << z << endl; 
  
    return 0; 
} 
```

**输出**

```
x = 107
y = a
z = 108
```

2.**显式类型转换：**这个过程也称为类型转换，是用户定义的。用户可以在这里将结果类型转换为特定的数据类型。

在 C++ 中，可以通过两种方式进行显式类型转换：

- **通过赋值转换**：这是通过在表达式前用括号明确指定所需类型来完成的。这也可以被认为是强制转换。

  **语法**

  ```
  (type) expression
  ```

  其中 type 表示最终结果将被转换成的数据类型。

  **样例**

  ```
  // C++程序演示显式类型转换
    
  #include <iostream> 
  using namespace std; 
    
  int main() 
  { 
      double x = 1.2; 
    
      // 从 double 到 int 的显式转换
      int sum = (int)x + 1; 
    
      cout << "Sum = " << sum; 
    
      return 0; 
  } 
  ```

  **输出**

  ```
  Sum = 2
  ```

- **使用类型转换运算符进行转换：**类型转换运算符是一种**一元运算符**，它强制将一种数据类型转换为另一种数据类型。

  C++ 支持四种类型转换：

  1. **静态转换（Static Cast）**
  2. **动态转换（Dynamic Cast）**
  3. **常量转换（Const Cast）**
  4. **重解释转换（Reinterpret Cast）**

  **样例**

  ```
  #include <iostream> 
  using namespace std; 
  int main() 
  { 
      float f = 3.5; 
    
      // 使用类型转换运算符 
      int b = static_cast<int>(f); 
    
      cout << b; 
  } 
  ```

  ### 类型转换的优势：
  1.这可以利用类型层次结构或类型表示的某些特性。
  2.它有助于计算包含不同数据类型变量的表达式。



