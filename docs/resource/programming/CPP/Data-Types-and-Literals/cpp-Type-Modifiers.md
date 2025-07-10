---
comments: true
---
# C++类型修饰符

修饰符在C++中被用来改变或赋予已有数据类型额外的含义。它作为前缀添加到基本数据类型上以改变其含义。修饰符用于改变基本类型的含义，使其更好地符合不同情况下的需求。

以下是C++数据类型修饰符：

1. **signed（有符号）**
2. **unsigned（无符号）**
3. **short（短）**
4. **long（长）**

![ModifiersInC](.\asset\ModifiersInC.png)

这些修饰符可以与以下内置数据类型一起使用。

### 1.有符号修饰符

有符号变量可以存储正整数、负整数和零。

**样例**

```
signed int a = 45;
signed int b = -67;
signed int c = 0;
```

这里，

- **‘a’ **是一个正整数值。
- **‘b’ **是一个负整数值。
- **‘c’ **是一个零值整数。

**样例**

```
// C++程序，演示有符号修饰符
#include <iostream>
using namespace std;

// 驱动代码
int main()
{
    cout << "Size of signed int : " << 
             sizeof(signed int) << 
             " bytes" << endl;
    cout << "Size of signed char : " << 
             sizeof(signed char) << 
             " bytes" << endl;

    return 0;
}
```

**输出**

```
Size of signed int : 4 bytes
Size of signed char : 1 bytes
```

> [!CAUTION]
>
> int 数据类型默认就是有符号的。因此，可以直接使用 int 而不是 signed int。

### 2.无符号修饰符

无符号变量只能存储非负整数值。

**样例**

```
unsigned int a = 9;
unsigned int b = 0;
```

这里，

- **‘a’** 是一个正整数值。
- **‘b’ **是一个零值整数。

**样例**

```
// C++程序，演示符号修饰符
#include <iostream>
using namespace std;

// 驱动代码
int main()
{
    cout << "Size of unsigned int : " << 
             sizeof(unsigned int) << 
             " bytes" << endl;
    cout << "Size of unsigned char : " << 
             sizeof(unsigned char) << 
             " bytes" << endl;
    return 0;
}

```

**输出**

```
Size of signed int : 4 bytes
Size of signed char : 1 bytes
```

有符号和无符号修饰符之间的区别
有符号变量的有符号值存储在分配的内存中。然而，无符号变量不存储有符号值。
有符号整数使用一位来表示符号（正或负），而无符号整数使用所有位来表示非负值。
无符号类型的值范围从0开始。例如，对于unsigned int，值范围是从0到4,294,967,295。然而，对于signed int，值范围是从-2,147,483,648到2,147,483,647。

> [!CAUTION]
>
> 有符号和无符号修饰符只能用于int和char数据类型。

### 3.短修饰符

short关键字修改了数据类型可以容纳的最小值。它用于范围在−32,767到+32,767之间的小整数。

**样例**

```
short int x = 4590;
```

**样例**

```
// C++程序，演示有符号修饰符
#include <iostream>
using namespace std;

int main()
{
    cout << "Size of short int : " << 
             sizeof(short int) << 
             " bytes" << endl;
    return 0;
}
```

**输出**

```
Size of short int : 2 bytes
```

> [!CAUTION]
>
> short int 可以简写为 short，它们是等价的。



### 长修饰符

long关键字修改了数据类型可以容纳的最大值。它用于范围在-2147483647到2147483647之间的大整数。

**样例**

```
long int y = 26936;
```

**样例**

```
// C++程序，演示有符号修饰符
#include <iostream>
using namespace std;

int main()
{
    cout << "Size of long int : " << 
             sizeof(long int) << 
             " bytes" << endl;
    cout << "Size of long double : " << 
             sizeof(long double) << 
             " bytes" << endl;
    return 0;
}
```

**输出**

```
Size of long int : 8 bytes
Size of long double : 16 bytes
```

> [!CAUTION]
>
> long int可以写成long，它们是等价的。

### 关于数据类型修饰符的重要点

**1.数据类型的修饰符可以组合使用。**
例如，signed/unsigned 可以与 long/short 修饰符一起使用。以下是C++程序，用于演示上述概念。

**样例**

```
// C++程序演示
// 修饰符可以组合在一起
#include <iostream>
using namespace std;

int main()
{
    cout << "Size of signed long int : " << 
             sizeof(signed long int) << 
             " bytes" << endl;
    cout << "Size of unsigned short int : " << 
             sizeof(unsigned short int) << 
             " bytes" << endl;
    return 0;
}
```

**输出**

```
Size of signed long int : 8 bytes
Size of unsigned short int : 2 bytes
```

**1.long 修饰符可以连续使用两次，即 long long，来表示更长的整型。**
它用于比long更大的数字。然而，long long类型修饰符只能与int一起使用。以下是演示上述概念的C++程序。

**样例**

```
// C++程序演示 long long 修饰符
#include <iostream>
using namespace std;

// Driver Code
int main()
{
    cout << "Size of long long int : " << 
             sizeof(long long int) << 
             " bytes" << endl;
    return 0;
}
```

**输出**

```
Size of long long int : 8 bytes
```

### 各种带有修饰符的数据类型及其字节大小

**1.字符数据类型（char）**

字符数据类型只允许 signed 和 unsigned 修饰符。当只使用 char 而不是 signed char 或 unsigned char 时，这种类型被称为普通 char。在进行数值计算时，建议使用 signed char 或 unsigned char 而不是普通 char。字符值应该只作为普通 char 存储。

<table><thead><tr><th><b><strong>编号</strong></b></th><th><p dir="ltr" style="text-align: center;"><span>修饰符</span></p>
</th><th><p dir="ltr" style="text-align: center;"><span>大小（以字节为单位）</span></p>
</th></tr></thead><tbody><tr><td>
<p><span>1.</span></p>
</td><td><p dir="ltr"><span>char</span></p>
</td><td>
<p><span>1</span></p>
</td></tr><tr><td>
<p><span>2.</span></p>
</td><td><p dir="ltr"><span>signed char</span></p>
</td><td>
<p><span>1</span></p>
</td></tr><tr><td>
<p><span>3.</span></p>
</td><td><p dir="ltr"><span>unsigned char</span></p>
</td><td>
<p><span>1</span></p>
</td></tr></tbody></table>

**2.整数数据类型（int）**

<table><thead><tr><th><b><strong>编号</strong></b></th><th><p dir="ltr" style="text-align: center;"><span>修饰符</span></p>
</th><th><p dir="ltr" style="text-align: center;"><span>大小（以字节为单位）</span></p>
</th></tr></thead><tbody><tr><td>
<p><span>1.</span></p>
</td><td><p dir="ltr"><span>int</span></p>
</td><td>
<p><span>4</span></p>
</td></tr><tr><td>
<p><span>2.</span></p>
</td><td><p dir="ltr"><span>signed int</span></p>
</td><td>
<p><span>4</span></p>
</td></tr><tr><td>
<p><span>3.</span></p>
</td><td><p dir="ltr"><span>unsigned int</span></p>
</td><td>
<p><span>4</span></p>
</td></tr><tr><td>
<p><span>4.</span></p>
</td><td><p dir="ltr"><span>short</span></p>
</td><td>
<p><span>2</span></p>
</td></tr><tr><td>
<p><span>5.</span></p>
</td><td><p dir="ltr"><span>signed short</span></p>
</td><td>
<p><span>2</span></p>
</td></tr><tr><td>
<p><span>6.</span></p>
</td><td><p dir="ltr"><span>unsigned short</span></p>
</td><td>
<p><span>2</span></p>
</td></tr><tr><td>
<p><span>7.</span></p>
</td><td><p dir="ltr"><span>long</span></p>
</td><td>
<p><span>8</span></p>
</td></tr><tr><td>
<p><span>8.</span></p>
</td><td><p dir="ltr"><span>signed long&nbsp;</span></p>
</td><td>
<p><span>8</span></p>
</td></tr><tr><td>
<p><span>9.</span></p>
</td><td><p dir="ltr"><span>unsigned long</span></p>
</td><td>
<p><span>8</span></p>
</td></tr></tbody></table>

**浮点数（float）和双精度浮点数（double）**
double类型可以与long修饰符一起使用。

<table><thead><tr><th><p dir="ltr"><span>编号</span></p>
</th><th><p dir="ltr" style="text-align: center;"><span>修饰符</span></p>
</th><th><p dir="ltr" style="text-align: center;"><span>大小（以字节为单位）</span></p>
</th></tr></thead><tbody><tr><td>
<p><span>1.</span></p>
</td><td><p dir="ltr"><span>float</span></p>
</td><td>
<p><span>4</span></p>
</td></tr><tr><td>
<p><span>2.</span></p>
</td><td><p dir="ltr"><span>double</span></p>
</td><td>
<p><span>8</span></p>
</td></tr><tr><td>
<p><span>3.</span></p>
</td><td><p dir="ltr"><span>long double</span></p>
</td><td>
<p><span>16</span></p>
</td></tr></tbody></table>

### C++中的类型限定符：

类型限定符用于在提供有关值的更多信息的同时，确保数据被正确使用。

1. **const：**const类型的对象在执行期间不能被更改。在程序运行时，const对象不能被程序修改。
2. **volatile：**volatile修饰符告诉编译器，变量的值可以通过程序未明确定义的方式更改。volatile修饰符通知编译器，变量的值可能会以程序中未明确说明的方式更改。
3. **restrict：**由restrict限定的指针最初是访问它所指向的对象的唯一方式。对象限制只能通过最初由它限定的指针访问的链接。restrict是一种新的限定符，仅在C99中添加。