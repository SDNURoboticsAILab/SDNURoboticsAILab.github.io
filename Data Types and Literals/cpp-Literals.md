## C++中的字面量

在C++编程语言中，我们使用字面量来表示固定的值。C++支持各种类型的字面量，包括整数字面量、浮点字面量、字符字面量和字符串字面量。在这篇文章中，我们将讨论C++字面量的所有必要信息及其使用。

![Cpp-literals](.\asset\Cpp-literals.png)

### C++中的字面量是什么？

字面量是用于表示C++编程语言中使用的常量值的基本元素。这些常量可以包括数字、字符、字符串等。理解和使用字面量在C++中对于数据赋值、计算和数据表示是必不可少的。它们通常作为赋值操作中的右操作数出现。

### C++中的字面量类型

C++中有五种字面量类型，分别是：

1. 整数字面量
2. 浮点数字面量
3. 字符字面量
4. 字符串字面量
5. 布尔字面量



1. **整数字面量**

C++中的整数字面量是表示没有小数部分的整数的常量。它们可以是正数或负数，并且可以有不同的进制，如十进制、八进制或十六进制。

**样例：**

```c++
 int integerLiteral = 42;
```

**实现：**

```c++
// C++程序演示整数字面量的使用
#include <iostream>
using namespace std;
 
int main()
{
 
    int age = 35; // An integer literal
    cout << "Age: " << age << endl;
    return 0;
}
```

**输出**

```c++
Age: 35
```

在C++中，整型字面量可以根据它们的进制被分为不同的类型。

**1. 十进制字面量（无前缀）**

十进制字面量表示一个无前缀的十进制整数。

**样例**

```c++
int decimal = 42;
```

**2. 八进制字面量（前缀：0）**

八进制字面量表示进制为8的整数，并以0前缀开头。

**样例**

```c++
int octal = 052; // 十进制为42
```

**3. 十六进制字面量（前缀：0x或0X）**

十六进制字面量表示一个十六进制的整数，并且以0x或0X作为前缀。

**样例**

```
int hexadecimal = 0x2A; //  十进制为42
```

**4. 二进制字面量（后缀：b或B）**

二进制字面量表示一个二进制的整数，并且可以有一个b或B的后缀。

**样例**

```
int binary = 0b101010; // 十进制为42
```

**5. 长整数字面量（后缀：l或L）**

长整型字面量可以通过添加l或L后缀来表示它是一个长整型（long int）。

**样例**

```
long int longInteger = 42L;
```

**6. 无符号整数字面量（后缀：u或U）**
无符号整型字面量可以通过添加u或U后缀来表示它是一个无符号整型（unsigned int）。

**样例**

```
unsigned int unsignedInt = 42U;
```

**7. 长长整数字面量（后缀：ll或LL）**

长长整型字面量可以通过添加ll或LL后缀来表示它是一个长长整型（long long int）。

**样例**

```
long long int longLongInteger = 42LL;
```

​    2.**浮点数字面量**

C++中的浮点数字面量是表示带有小数部分的数字的常量。这些可以是单精度或双精度值。

与整数字面量类似，浮点数字面量也可以通过使用后缀（无后缀）和f分别定义为double或float。默认情况下，C++编译器将所有小数视为double类型。

**样例**

```
double floatLiteral = 3.14;
```

**实现**

```
// 这是一个C++程序的示例，用于展示如何使用浮点数字面量。
#include <iostream>
using namespace std;
 
int main()
{
    // float literal
    float e = 2.7f;
 
    // double literal
    double pi = 3.14;
 
    // long double literal
    long double g = 9.8L;
 
    cout << "The Value of pi: " << pi << endl;
    cout << "The value of e: " << e << endl;
    cout << "The value of g: " << g << endl;
    return 0;
}
```

**输出**

```
The Value of pi: 3.14
The value of e: 2.7
The value of g: 9.8
```

   3.**字符字面量**

C++中的字符字面量是表示单个字符或转义序列的常量。它们用单引号括起来，您可以使用它们来表示单个字符。

**样例**

```
char charLiteral = 'A';
```

**实现**

```
// 这是一个C++程序的示例，用于展示如何使用字符字面量。
#include <iostream>
using namespace std;
 
int main()
{
    char grade = 'A';
 
    cout << "Grade: " << grade << endl;
    return 0;
}
```

**输出**

```
Grade: A
```

4. **字符串字面量**

C++中的字符串字面量是表示字符序列的常量。它们用双引号括起来，您可以使用它们来表示文本或字符序列。

**样例**

```
const char* stringLiteral = "Hello, World!";
```

**实现**

```
// 这是一个C++程序的示例，用于展示如何使用字符串字面量。
#include <iostream>
using namespace std;
 
int main()
{
    const char* message = "Hello, GeeksforGeeks!";
    cout << "Message: " << message << endl;
    return 0;
}
```

**输出**

```
Message: Hello, GeeksforGeeks!
```

> [!CAUTION]
>
> 字符串字面量是唯一不是右值的字面量。

5. **布尔字面量**

布尔字面量表示真值，只有两个可能的值：true和false。这些值用于布尔表达式和逻辑操作。

**样例**

```
// 这是一个C++程序的示例，用于展示如何使用布尔字面量。
#include <iostream>
using namespace std;
 
int main()
{
  // using boolean literals
    bool isTrue = true;
    bool isFalse = false;
   
    if (isTrue) {
        cout << "isTrue is true" << endl;
    }
    else {
        cout << "isTrue is false" << endl;
    }
 
    if (isFalse) {
        cout << "isFalse is true" << endl;
    }
    else {
        cout << "isFalse is false" << endl;
    }
    return 0;
}
```

**输出**

```
isTrue is true
isFalse is false
```

