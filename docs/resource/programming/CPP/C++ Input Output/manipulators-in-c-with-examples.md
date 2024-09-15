# C++中的操控符及示例

**最后更新：2022年6月12日**

**操控符** 是一些辅助函数，用于修改输入/输出流。它们并不会改变变量的值，而是通过插入（`<<`）和提取（`>>`）运算符来修改输入/输出流。

- 操控符是特殊函数，可以被包含在输入/输出语句中，以改变流的格式参数。
- 操控符是用于格式化数据展示的运算符。
- 要使用操控符，需要在程序中包含 `iomanip.h` 头文件。

例如，如果我们想要打印100的十六进制值，可以这样打印：

```
cout << setbase(16) << 100;
```

**操控符的类型** 操控符有多种类型：

1. **无参数的操控符**

   : 下面是 `IOStream` 库中定义的一些重要操控符。

   - **endl**: 在 `ostream` 中定义。用于换行，并在换行后刷新（即强制将所有输出写入屏幕或文件）输出流。
   - **ws**: 在 `istream` 中定义，用于忽略字符串序列中的空白字符。
   - **ends**: 也在 `ostream` 中定义，用于在输出流中插入一个空字符。通常与 `std::ostrstream` 一起使用，当相关的输出缓冲区需要以空字符终止以处理为 C 字符串时。
   - **flush**: 也在 `ostream` 中定义，用于刷新输出流，即强制将所有输出写入屏幕或文件。没有 `flush`，输出会相同，但可能不会实时显示。

**示例：**

- C++ 代码：

```
cpp#include <iostream>
#include <istream>
#include <sstream>
#include <string>
using namespace std;

int main()
{
    istringstream str("      Programmer");
    string line;
    // 忽略字符串中第一个单词前的所有空白字符
    getline(str >> std::ws, line);
    // 也可以写作 str >> ws
    // 打印输出后将自动换行
    cout << line << endl;
    // 没有 flush，输出会相同
    cout << "only a test" << flush;
    // 使用 ends 操控符
    cout << "\na";
    // 输出中将添加空字符
    cout << "b" << ends;
    cout << "c" << endl;
    return 0;
}
```

**输出：**

```
Programmer
only a test
abc
```

1. **有参数的操控符**

   一些操控符需要参数，如 `setw (20)`、`setfill ('*')` 等。这些操控符都在头文件中定义。如果要使用这些操控符，必须在程序中包含该头文件。例如，可以使用以下操控符来设置最小宽度并填充空白字符：`std::cout << std::setw(6) << std::setfill('*');`

   - **<iomanip>** 中的一些重要操控符：
     1. **setw(val):** 用于设置输出操作中的字段宽度。
     2. **setfill(c):** 用于在输出流中填充字符 `c`。
     3. **setprecision(val):** 设置浮点值的精度为 `val`。
     4. **setbase(val):** 设置数字值的进制值。
     5. **setiosflags(flag):** 设置由参数掩码指定的格式标志。
     6. **resetiosflags(m):** 重置由参数掩码指定的格式标志。
   - **<ios>** 中的一些重要操控符：
     1. **showpos:** 强制在正数上显示正号。
     2. **noshowpos:** 强制不在正数上显示正号。
     3. **showbase:** 指示数字值的进制。
     4. **uppercase:** 强制数字值使用大写字母。
     5. **nouppercase:** 强制数字值使用小写字母。
     6. **fixed:** 对浮点值使用十进制表示法。
     7. **scientific:** 使用科学计数法表示浮点值。
     8. **hex:** 读取和写入整数的十六进制值，效果等同于 `setbase(16)`。
     9. **dec:** 读取和写入整数的十进制值，即 `setbase(10)`。
     10. **oct:** 读取和写入整数的八进制值，即 `setbase(8)`。
     11. **left:** 将输出左对齐。
     12. **right:** 将输出右对齐。

操控符通常分为两种类型：

1. 带参数的
2. 不带参数的

- ### 1] 带参数的操控符：

  操控符        ->      含义
   setw (int n)         ->      设置字段宽度为 n
   setprecision (int p)   ->      精度设置为 p
   setfill (Char f)        ->      设置填充字符为 f
   setiosflags (long l)    ->      设置格式标志为 l
   resetiosflags (long l)  ->      移除标志 l
   setbase(int b)       ->      设置数字的进制为 b

  - **setw() 是 C++ 中的一个操控符函数：**

    `setw()` 函数是一个输出操控符，用于在两个变量之间插入空白。必须输入一个等于所需空白的整数值。
     **语法：**
     `setw(int n)`
     示例：

    ```
    cppint a = 15;  
    int b = 20;  
    cout << setw(10) << a << setw(10) << b << endl;  
    ```

  - **setfill() 是 C++ 中的一个操控符函数：**
     它用不同的字符替代 `setw()` 中的空白。与 `setw()` 类似，它用于操控输出，但只需要一个字符参数。
     **语法：**
     `setfill(char ch)`
     **示例：**

    ```
    cppint a, b;  
    a = 15;  
    b = 20;  
    cout << setfill('*') << endl;  
    cout << setw(5) << a << setw(5) << b << endl;  
    ```

  - **setprecision() 是 C++ 中的一个操控符函数：**
     它是一个输出操控符，用于控制浮点数的小数位数。
     **语法：**
     `setprecision(int p)`
     **示例：**

    ```
    cppfloat A = 1.34255;  
    cout << fixed << setprecision(3) << A << endl;  
    ```

  - **setbase() 是 C++ 中的一个操控符函数：**
     `setbase()` 操控符用于将数字的进制更改为不同的值。C++ 语言支持以下进制值：

    - hex（十六进制 = 16）
    - oct（八进制 = 8）
    - dec（十进制 = 10）

    操控符 `hex`、`oct` 和 `dec` 可以更改输入和输出数字的进制。

  - C++ 示例：

  ```
  cpp#include <iostream>
  #include <iomanip>
  using namespace std;
  
  int main() {
      int number = 100;
      cout << "Hex Value = " << " " << hex << number << endl;
      cout << "Octal Value = " << " " << oct << number << endl;
      cout << "Setbase Value = " << " " << setbase(8) << number << endl;
      cout << "Setbase Value = " << " " << setbase(16) << number << endl;
      return 0;
  }
  ```

  **输出**

  ```
  Hex Value = 64
  Octal Value = 144
  Setbase Value = 144
  Setbase Value = 64
  ```

  ### 2] 无参数的操控符

  示例包括 `endl`、`fixed`、`showpoint` 和 `flush`。

  - **endl** – 换行
  - **ends** – 在输出字符串末尾添加空字符
  - **flush** – 刷新缓冲区流
  - **ws** – 忽略在第一个字段之前的前导空白
  - **hex**、**oct**、**dec** – 以十六进制、八进制或十进制格式显示数字
  - C++ 示例：

  ```
  cpp#include <iostream>
  using namespace std;
  
  int main() {
      char name[125];
      cout << "Enter your name" << endl;
      cin >> ws;
      cin.getline(name, 125);
      cout << name << endl;
      return 0;
  }
  ```

  **输出**

  ```
  Enter your name
  ram
  ram
  ```

  **参考资料：**

  - [C++ iomanip 参考](http://www.cplusplus.com/reference/iomanip/)
  - [C++ basic_ios 参考](http://www.cplusplus.com/reference/ios/basic_ios/)
  - [C++ ios 参考](http://www.cplusplus.com/reference/ios/)