# 编写第一个 C++ 程序 – Hello World 示例

C++ 是一种广泛使用的面向对象编程语言，相对容易理解。“Hello World” 程序是学习任何编程语言的第一步，也是你将学习的最简单的程序之一。

C++ 中的 Hello World 程序是一个基本程序，用于演示编码过程的工作原理。你只需要在控制台屏幕上显示“Hello World”消息。

要编写和运行 C++ 程序，你需要在计算机上设置本地环境。请参阅完整的文章 [设置 C++ 开发环境](https://www.geeksforgeeks.org/setting-c-development-environment/)。如果你不想在计算机上设置本地环境，也可以使用 [在线 IDE](https://ide.geeksforgeeks.org/) 编写和运行你的 C++ 程序。

## C++ Hello World 程序

下面是一个 C++ 程序，用于打印 Hello World。

- C++

```
cpp// C++ 程序显示 "Hello World"
// 输入输出函数的头文件
#include <iostream>

// 使用标准命名空间
using namespace std;

// 主函数：程序的执行从这里开始
int main() {
    // 打印 hello world
    cout << "Hello World";
    return 0;
}
```

**输出**

```
Hello World
```

## C++ 中 Hello World 程序的工作原理

让我们了解上面程序中的每一行和术语。

### 1. // C++ 程序显示 “Hello World”

这一行是注释行。注释用于显示有关程序的额外信息。注释不包含任何编程逻辑。

当编译器遇到注释时，编译器会跳过该行代码。在 C++ 中，任何以 ‘//’ 开头的行（不包括引号）或在 /*…*/ 之间的内容都是注释。点击了解 [更多关于注释的信息](https://www.geeksforgeeks.org/comments-in-c-c/)

### 2. #include

这是一个预处理指令。***#include*** 指令告诉编译器将文件的内容包含到源代码中。

例如，***#include<iostream>*** 告诉编译器包含标准 iostream 文件，该文件包含所有标准输入/输出库函数的声明。点击了解 [更多关于预处理器的信息](https://www.geeksforgeeks.org/cc-preprocessors/)

### 3. using namespace std

这用于将 std 命名空间的实体导入当前程序的命名空间。使用 namespace std 的语句通常被认为是一种不良实践。当我们导入一个命名空间时，实际上是将所有类型定义引入当前作用域。

std 命名空间非常庞大。替代方案是每次声明类型时，使用作用域运算符 (::) 指定标识符所属的命名空间。例如，std::cout。点击了解 [更多关于使用 namespace std 的信息](https://www.geeksforgeeks.org/using-namespace-std-considered-bad-practice/)

### 4. int main() { }

函数是一组旨在执行特定任务的语句。main() 函数是每个 C++ 程序的入口点，无论函数在程序中的位置如何。

开括号 ‘{’ 表示 main 函数的开始，闭括号 ‘}’ 表示 main 函数的结束。点击了解 [更多关于 main() 函数的信息](https://www.geeksforgeeks.org/executing-main-in-c-behind-the-scene/)

### 5. cout << “Hello World”;

std::cout 是 std::ostream 类的一个实例，用于在屏幕上显示输出。所有跟随字符 << 的内容会显示在输出设备上。语句末尾的分号表示语句在此结束。点击了解 [更多关于输入/输出的信息](https://www.geeksforgeeks.org/basic-input-output-c/)

### 6. return 0

此语句用于从函数中返回一个值，并表示函数的结束。此语句基本上用于函数中，以返回函数执行操作的结果。

### 7. 缩进

如你所见，cout 和 return 语句已缩进或移动到右侧。这是为了使代码更具可读性。我们必须始终使用缩进和注释来提高代码的可读性。必须阅读 [关于编程风格的常见问题解答](https://www.geeksforgeeks.org/facts-and-question-related-to-style-of-writing-programs-in-c-c/)

## 重要点

1. 始终包括必要的头文件，以确保函数的顺利执行。例如，***<iostream>*** 必须包含以使用 ***std::cin*** 和 ***std::cout***。
2. 代码的执行从 ***main()*** 函数开始。
3. 使用 ***缩进*** 和 ***注释*** 来提高程序的可理解性是一个好习惯。
4. ***cout*** 用于打印语句，***cin*** 用于获取输入。