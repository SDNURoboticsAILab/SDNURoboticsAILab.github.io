# **cerr – C++中的标准错误流对象**

**标准输出流 (cout)：** `cout` 是 `ostream` 类的一个实例。`cout` 用于在标准输出设备上生成输出，通常是显示屏。需要在屏幕上显示的数据通过插入运算符（`<<`）插入到标准输出流 (`cout`) 中。

**标准错误流 (cerr)：** `cerr` 是用于输出错误的标准错误流。它也是 `ostream` 类的一个实例。由于 `cerr` 流是无缓冲的，因此当我们需要立即显示错误信息时使用它，它不会存储错误信息以便稍后显示。`cerr` 对象表示面向窄字符（即 `char` 类型）的标准错误流。它对应于 C 语言中的 `stderr` 流。

`cerr` 中的 "c" 指的是 "character"（字符），而 "err" 代表 "error"（错误），因此 `cerr` 代表 "character error"（字符错误）。使用 `cerr` 来显示错误信息是一种良好的实践。

下面是一个演示 `cerr` 的程序：

```
// C++程序演示 std::cerr

#include <iostream>
using namespace std;

// 驱动代码
int main()
{
    // 这将在错误窗口中打印 "Welcome to GfG"
    cerr << "Welcome to GfG! :: cerr";

    // 这将在输出窗口中打印 "Welcome to GfG"
    cout << "Welcome to GfG! :: cout";
    return 0;
}
```

在上述程序中，第11行的输出将在错误窗口中显示如下内容：

```
RunTime Error in CPP code:
```

```
Welcome to GfG! :: cerr
```