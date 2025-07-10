---
comments: true
---
### C++ 数据类型

在声明[变量](https://www.geeksforgeeks.org/variables-in-c/)时，所有变量都使用数据类型来限制存储的数据类型。因此，我们可以说数据类型用于告诉变量它们可以存储的数据类型。每当在C++中定义一个变量时，编译器会根据声明时使用的数据类型为该变量分配一定的内存。每种数据类型所需的内存量是不同的。

C++支持多种数据类型，程序员可以根据应用程序的需求选择合适的数据类型。数据类型指定了要存储的值的大小和类型。然而，尽管C++指令在所有机器上都是相同的，存储表示和操作每种数据类型的机器指令也会因机器而异。

**C++支持以下数据类型：**

1. **基本数据类型或内置数据类型或基本数据类型**
2. **派生数据类型**
3. **用户定义数据类型**

![DatatypesInC](.\asset\DatatypesInC.png)

### C++中的数据类型主要分为三种：

**1.基本数据类型：**这些数据类型是内置或预定义的数据类型，用户可以直接使用它们来声明变量。例如：int、char、float、bool等。C++中可用的基本数据类型包括：

- 整数
- 字符
- 布尔
- 浮点数
- 双精度浮点数
- 无值或空
- 宽字符

**2.派生数据类型：**[派生数据类型](https://www.geeksforgeeks.org/derived-data-types-in-c/)是从基本数据类型或内置数据类型派生出来的，被称为派生数据类型，可以分为以下四种：

- 函数
- 数组
- 指针
- 引用

**3.抽象或用户定义数据类型：**[抽象或用户定义数据类型](https://www.geeksforgeeks.org/cpp-data-types/?ref=shm)由用户自己定义。例如，在C++中定义一个类或结构。C++提供了以下用户定义数据类型：

- 类
- 结构
- 联合
- 枚举
- typedef定义的数据类型

### 基本数据类型

- **整数(Integer)**：用于整数数据类型的关键字是**int**。整数通常需要4字节的内存空间，范围从-2147483648到2147483647。
- **字符(Character)**：字符数据类型用于存储字符。用于字符数据类型的关键字是**char**。字符通常需要1字节的内存空间，范围从-128到127或0到255。
- **布尔(Boolean)**：布尔数据类型用于存储布尔值或逻辑值。布尔变量可以存储 true（真）或 false（假）。布尔数据类型的关键字是 **bool**。
- **浮点数(Floating Point)**：浮点数数据类型用于存储单精度浮点值或十进制值。用于浮点数数据类型的关键字是**float**。浮点变量通常需要4字节的内存空间。
- **双精度浮点数(Double Floating Point)**：双精度浮点数数据类型用于存储双精度浮点值或十进制值。用于双精度浮点数数据类型的关键字是**double**。双精度变量通常需要8字节的内存空间。
- **空(void)**：空意味着没有任何值。**void**数据类型表示一个无值的实体。void数据类型用于那些不返回值的函数。
- **宽字符(Wide Character)**：[宽字符数据类型](https://www.geeksforgeeks.org/wide-char-and-library-functions-in-c/)也是一种字符数据类型，但这个数据类型的大小超过了普通的 8 位数据类型。用 `wchar_t` 表示。它通常是 2 或 4 字节长。
- **sizeof() 运算符(sizeof() operator)**：[sizeof() 运算符](https://www.geeksforgeeks.org/sizeof-operator-c/)用于找出变量/数据类型在计算机内存中占用的字节数。

**样例**

```c++
int m , x[50];     

cout<<sizeof(m); //返回 4，这是整数变量 "m" 占用的字节数。

cout<<sizeof(x); //返回 200，这是整数数组变量 "x" 占用的字节数。 
```

变量的大小可能因编译器和您使用的计算机而异，可能与上述显示的数值不同。

```c++
// C++ 程序，演示您计算机上各种数据类型的正确大小。
#include <iostream>
using namespace std;
 
int main()
{
    cout << "Size of char : " << sizeof(char) << endl;
    cout << "Size of int : " << sizeof(int) << endl;
 
    cout << "Size of long : " << sizeof(long) << endl;
    cout << "Size of float : " << sizeof(float) << endl;
 
    cout << "Size of double : " << sizeof(double) << endl;
 
    return 0;
}
```

**输出**

```c++
Size of char : 1
Size of int : 4
Size of long : 8
Size of float : 4
Size of double : 8
```

**时间复杂度：**O(1)

**空间复杂度：**O(1)

### 数据类型修饰符

顾名思义，数据类型修饰符与内置数据类型一起使用，以修改特定数据类型可以容纳的数据长度。

![ModifiersInC](.\asset\ModifiersInC.png)

C++中可用的数据类型修饰符包括：

- **有符号(Signed)**
- **无符号(Unsigned)**
- **短(Short)**
- **长(Long)**

下表总结了当与类型修饰符结合使用时，内置数据类型修改后的大小和范围：

<table class="GFGEditorTheme__table">
<colgroup>
<col>
<col>
<col></colgroup>
<thead>
<tr>
<th class="GFGEditorTheme__tableCell GFGEditorTheme__tableCellHeader">
<p style="text-align: center;" dir="ltr"><span>Data Type</span></p>
</th>
<th class="GFGEditorTheme__tableCell GFGEditorTheme__tableCellHeader">
<p style="text-align: center;" dir="ltr"><span>大小 (以字节为单位)</span></p>
</th>
<th class="GFGEditorTheme__tableCell GFGEditorTheme__tableCellHeader">
<p style="text-align: center;" dir="ltr"><span>范围</span></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>short int</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;"><span>2</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>-32,768 到 32,767</span></p>
</td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>unsigned short int</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;"><span>2</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>0 到 65,535</span></p>
</td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>unsigned int</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;"><span>4</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>0 到 4,294,967,295</span></p>
</td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>int</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;"><span>4</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>-2,147,483,648 到 2,147,483,647</span></p>
</td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>long int</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;"><span>4</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>-2,147,483,648 到 2,147,483,647</span></p>
</td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>unsigned long int</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;"><span>4</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>0 到 4,294,967,295</span></p>
</td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>long long int</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;"><span>8</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>-(2^63) 到 (2^63)-1</span></p>
</td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>unsigned long long int</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;"><span>8</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>0 到 18,446,744,073,709,551,615</span></p>
</td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>signed char</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;"><span>1</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>-128 到 127</span></p>
</td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>unsigned char</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;"><span>1</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>0 到 255</span></p>
</td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>float</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;"><span>4</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>-3.4×10^38 到 3.4×10^38</span></p>
</td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>double</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;"><span>8</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>-1.7×10^308 到1.7×10^308</span></p>
</td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>long double</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;"><span>12</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>-1.1×10^4932 到1.1×10^4932</span></p>
</td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>wchar_t</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>2 或者 4</span></p>
</td>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>1个宽字符</span></p>
</td>
</tr>
</tbody>
</table>

> [!CAUTION]
>
> 以上数值可能因编译器而异。在上面的例子中，我们使用的是 GCC 32 位编译器。
> 我们可以通过使用 sizeof() 运算符并将数据类型的关键字作为参数传递给这个函数，如下所示来显示所有数据类型的大小：

现在，为了获取数据类型的范围，请参考以下图表。

> [!CAUTION]
>
> **<limits.h>头文件**定义了查找基本数据类型范围的宏常量。无符号修饰符的最小值为零。因此，没有为无符号最小值定义宏常量。

### 宏常量

<table class="GFGEditorTheme__table">
<colgroup>
<col>
<col></colgroup>
<thead>
<tr>
<th class="GFGEditorTheme__tableCell GFGEditorTheme__tableCellHeader">
<p style="text-align: center;" dir="ltr"><span>名称</span></p>
</th>
<th class="GFGEditorTheme__tableCell GFGEditorTheme__tableCellHeader">
<p style="text-align: center;" dir="ltr"><span>表达</span></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>CHAR_MIN</span></p>
</td>
<td class="GFGEditorTheme__tableCell"><span>类型为char的对象的最小值</span></td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>CHAR_MAX</span></p>
</td>
<td class="GFGEditorTheme__tableCell"><span>类型为char的对象的最大值</span></td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>SCHAR_MIN</span></p>
</td>
<td class="GFGEditorTheme__tableCell"><span>类型为Signed char的对象的最小值</span></td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>SCHAR_MAX</span></p>
</td>
<td class="GFGEditorTheme__tableCell"><span>类型为Signed char的对象的最大值</span></td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>UCHAR_MAX</span></p>
</td>
<td class="GFGEditorTheme__tableCell"><span>类型为Unsigned char的对象的最大值</span></td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>CHAR_BIT</span></p>
</td>
<td class="GFGEditorTheme__tableCell"><span>一个 char 对象中的位数。
</span></td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>MB_LEN_MAX</span></p>
</td>
<td class="GFGEditorTheme__tableCell"><span>多字节字符中的最大字节数。
</span></td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>SHRT_MIN</span></p>
</td>
<td class="GFGEditorTheme__tableCell"><span>类型为short int的对象的最小值</span></td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>SHRT_MAX</span></p>
</td>
<td class="GFGEditorTheme__tableCell"><span>类型为short int的对象的最大值</span></td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>USHRT_MAX</span></p>
</td>
<td class="GFGEditorTheme__tableCell"><span>类型为Unsigned short int的对象的最大值</span></td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>INT_MIN</span></p>
</td>
<td class="GFGEditorTheme__tableCell"><span>类型为int的对象的最小值</span></td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>INT_MAX</span></p>
</td>
<td class="GFGEditorTheme__tableCell"><span>类型为int的对象的最大值</span></td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>UINT_MAX</span></p>
</td>
<td class="GFGEditorTheme__tableCell"><span>类型为Unsigned int的对象的最大值</span></td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>LONG_MIN</span></p>
</td>
<td class="GFGEditorTheme__tableCell"><span>类型为long int的对象的最小值</span></td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>LONG_MAX</span></p>
</td>
<td class="GFGEditorTheme__tableCell"><span>类型为long int的对象的最大值</span></td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>ULONG_MAX</span></p>
</td>
<td class="GFGEditorTheme__tableCell"><span>类型为Unsigned long int的对象的最大值</span></td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>LLONG_MIN&nbsp;</span></p>
</td>
<td class="GFGEditorTheme__tableCell"><span>类型为long long int的对象的最小值</span></td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>LLONG_MAX</span></p>
</td>
<td class="GFGEditorTheme__tableCell"><span>类型为long long int的对象的最大值</span></td>
</tr>
<tr>
<td class="GFGEditorTheme__tableCell">
<p style="text-align: center;" dir="ltr"><span>ULLONG_MAX</span></p>
</td>
<td class="GFGEditorTheme__tableCell"><span>类型为Unsigned long long int的对象的最大值</span></td>
</tr>
</tbody>
</table>

实际值取决于特定的系统和库实现，但应反映目标平台上这些类型的限制。LLONG_MIN、LLONG_MAX和ULLONG_MAX是为符合1999年或更高版本C标准的库定义的（这仅包括自2011年以来的C++标准：C++11）。

C++程序使用宏常量查找数据类型的范围

**样例**

```C++
// C++程序演示数据类型的大小
#include <iostream>
#include <limits.h>
using namespace std;
 
int main()
{
    cout << "Size of char : " << sizeof(char) << " byte"
         << endl;
 
    cout << "char minimum value: " << CHAR_MIN << endl;
 
    cout << "char maximum value: " << CHAR_MAX << endl;
 
    cout << "Size of int : " << sizeof(int) << " bytes"
         << endl;
 
    cout << "Size of short int : " << sizeof(short int)
         << " bytes" << endl;
 
    cout << "Size of long int : " << sizeof(long int)
         << " bytes" << endl;
 
    cout << "Size of signed long int : "
         << sizeof(signed long int) << " bytes" << endl;
 
    cout << "Size of unsigned long int : "
         << sizeof(unsigned long int) << " bytes" << endl;
 
    cout << "Size of float : " << sizeof(float) << " bytes"
         << endl;
 
    cout << "Size of double : " << sizeof(double)
         << " bytes" << endl;
 
    cout << "Size of wchar_t : " << sizeof(wchar_t)
         << " bytes" << endl;
 
    return 0;
}
```

**输出**

```
Size of char : 1 byte
char minimum value: -128
char maximum value: 127
Size of int : 4 bytes
Size of short int : 2 bytes
Size of long int : 8 bytes
Size of signed long int : 8 bytes
Size of unsigned long int : 8 bytes
Size of float : 4 bytes
Size of double : 8 bytes
Size of wchar_t : 4 bytes
```

**时间复杂度：O(1)**

**空间复杂度：O(1)**

```c++
#include <iostream>
#include <string>
using namespace std;
 
int main() {
  // 整数数据类型
  int a = 10;
  short b = 20;
  long c = 30;
  long long d = 40;
  cout << "Integer data types: " << endl;
  cout << "int: " << a << endl;
  cout << "short: " << b << endl;
  cout << "long: " << c << endl;
  cout << "long long: " << d << endl;
   
  // 浮点数据类型
  float e = 3.14f;
  double f = 3.141592;
  long double g = 3.14159265358979L;
  cout << "Floating-point data types: " << endl;
  cout << "float: " << e << endl;
  cout << "double: " << f << endl;
  cout << "long double: " << g << endl;
   
  // 字符数据类型
  char h = 'a';
  wchar_t i = L'b';
  char16_t j = u'c';
  char32_t k = U'd';
  cout << "Character data types: " << endl;
  cout << "char: " << h << endl;
  wcout << "wchar_t: " << i << endl;
  cout << "char16_t: " << j << endl;
  cout << "char32_t: " << k << endl;
   
  // 布尔数据类型
  bool l = true;
  bool m = false;
  cout << "Boolean data type: " << endl;
  cout << "true: " << l << endl;
  cout << "false: " << m << endl;
   
  // 字符串数据类型
  string n = "Hello, world!";
  cout << "String data type: " << endl;
  cout << n << endl;
   
  return 0;
}
```

**输出**

```
Integer data types: 
int: 10
short: 20
long: 30
long long: 40
Floating-point data types: 
float: 3.14
double: 3.14159
long double: 3.14159
Character data types: 
char: a
wchar_t: b
char16_t: 99
char32_t: 100
Boolean data type: 
true: 1
false: 0
String data type: 
Hello, world!
```

这个程序声明了各种数据类型的变量，为它们赋值，然后打印出它们的值。

整数数据类型包括int、short、long和long long。这些数据类型表示不同大小的整数。

浮点数据类型包括float、double和long double。这些数据类型表示具有不同精度级别的实数。

字符数据类型包括char、wchar_t、char16_t和char32_t。这些数据类型表示不同大小的单个字符。

布尔数据类型是一个简单的数据类型，只能有两个值之一：true或false。

字符串数据类型是字符序列。在这个程序中，我们使用string类声明一个字符串变量并为其赋值。

**优点**

数据类型为程序中的数据提供了一种分类和组织的方式，使其更容易理解和维护。
每种数据类型都有一个特定的值范围，可以容纳，从而实现对存储数据的更精确控制。
数据类型通过强制执行关于如何使用和操作数据的严格规则，帮助防止程序中的错误和漏洞。
C++提供了广泛的数据类型，允许开发人员为特定任务选择最佳类型。

**缺点**

使用错误的数据类型可能会导致程序出现意外的行为和错误。
一些数据类型，如长双精度浮点数（long double）或字符数组（char），如果过度使用，可能会占用大量内存并影响性能。
C++ 的复杂类型系统可能会使初学者难以有效地学习和使用该语言。
数据类型的使用可能会增加程序的复杂性和冗长，使其更难以阅读和理解。