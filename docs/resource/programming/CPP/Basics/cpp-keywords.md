# C++ 关键字

C++ 是一种强大的语言。在 [C++](https://www.geeksforgeeks.org/c-plus-plus/) 中，我们可以编写结构化程序和 [面向对象的程序](https://www.geeksforgeeks.org/oops-object-oriented-design/)。C++ 是 [C](https://www.geeksforgeeks.org/c-programming-language/) 的超集，因此大多数 C 的结构在 C++ 中是合法的，其含义不变。然而，也有一些例外和新增内容。

## ***标记***

当编译器处理 C++ 程序的源代码时，每组由空格分隔的字符被称为 [标记](https://www.geeksforgeeks.org/cc-tokens/)。标记是程序中最小的独立单位。C++ 程序是通过使用标记来编写的。它包括以下标记：

- 关键字
- 标识符
- [常量](https://www.geeksforgeeks.org/constants-in-c-cpp/)
- [字符串](https://www.geeksforgeeks.org/strings-in-c/)
- [运算符](https://www.geeksforgeeks.org/operators-in-cpp/)





- ![C++ Tokens](https://media.geeksforgeeks.org/wp-content/uploads/20210507151607/token2.png)

## ***关键字***

关键字（也称为 ***保留字***）对 [C++ 编译器](https://www.geeksforgeeks.org/compiling-with-g-plus-plus/) 有特殊的含义，并且总是以小写字母书写。关键字是语言用于特定目的的词汇，如 ***void***、***int***、***public*** 等。它不能用作变量名、函数名或任何其他标识符。总共有 95 个保留关键字。以下是一些常用 C++ 关键字的表格。

| **C++ Keyword** |                                                              |           |                                                              |
| :-------------------: | ------------------------------------------------------------ | --------- | ------------------------------------------------------------ |
|          asm          | double                                                       | new       | [switch](https://www.geeksforgeeks.org/switch-statement-cc/) |
|         auto          | else                                                         | operator  | template                                                     |
|         break         | enum                                                         | private   | this                                                         |
|         case          | extern                                                       | protected | throw                                                        |
|         catch         | float                                                        | public    | try                                                          |
|         char          | for                                                          | register  | typedef                                                      |
|         class         | friend                                                       | return    | union                                                        |
|         const         | goto                                                         | short     | unsigned                                                     |
|       continue        | [if](https://www.geeksforgeeks.org/check-if-given-number-is-perfect-square-in-cpp/) | signed    | virtual                                                      |
|        default        | inline                                                       | sizeof    | void                                                         |
|        delete         | int                                                          | static    | volatile                                                     |
|          do           | long                                                         | struct    | while                                                        |

> ***注释：*** 在 ANSI C 中没有的关键字以粗体显示。

- ***asm***: 用于声明一段代码块将传递给汇编器。
- ***auto***: 存储类说明符，用于在块中定义对象。
- ***break***: 终止 switch 语句或循环。
- ***case***: 在 switch 语句中用于指定匹配语句表达式的情况。
- ***catch***: 指定异常发生时采取的动作。
- ***char***: 基本数据类型，用于定义字符对象。
- ***class***: 用于声明一个用户定义的类型，封装数据成员和操作或成员函数。
- ***const***: 用于定义在程序执行过程中值不会改变的对象。
- ***continue***: 将控制转移到循环的开始。
- ***default***: 处理 switch 语句中未被 case 处理的表达式值。
- ***delete***: 内存释放操作符。
- ***do***: 表示 do-while 语句的开始，其中子语句重复执行，直到表达式的值为逻辑假。
- ***double***: 基本数据类型，用于定义浮点数。
- ***else***: 在 if-else 语句中使用。
- ***enum***: 用于声明用户定义的枚举数据类型。
- ***extern***: 作为 extern 指定的标识符具有外部链接到块的特性。
- ***float***: 基本数据类型，用于定义浮点数。
- ***for***: 表示开始一个语句以实现重复控制。
- ***friend***: 一个类或操作，其实现可以访问类的私有数据成员。
- ***goto***: 将控制转移到指定标签。
- ***if***: 表示 if 语句的开始，以实现选择控制。
- ***inline***: 函数说明符，指示编译器优选内联替换函数体，而不是通常的函数调用实现。
- ***int***: 基本数据类型，用于定义整数对象。
- ***long***: 数据类型修饰符，定义 32 位整数或扩展的 double。
- ***new***: 内存分配操作符。
- ***operator***: 用于重载 C++ 运算符的新声明。
- ***private***: 声明类成员在类外不可见。
- ***protected***: 声明类成员对派生类可见，其他类不可见。
- ***public***: 声明类成员在类外可见。
- ***register***: 存储类说明符，是 auto 说明符的一种，但还指示编译器对象将被频繁使用，因此应保存在寄存器中。
- ***return***: 将对象返回给函数的调用者。
- ***short***: 数据类型修饰符，定义 16 位整数。
- ***signed***: 数据类型修饰符，指示对象的符号存储在高位。
- ***sizeof***: 返回对象的字节大小。
- ***static***: 定义的静态对象的生命周期贯穿整个程序执行。
- ***struct***: 用于声明封装数据和成员函数的新类型。
- ***switch***: 用于“switch 语句”。
- ***template***: 参数化或泛型类型。
- ***this***: 指向类的对象或实例的类指针。
- ***throw***: 生成一个异常。
- ***try***: 表示异常处理程序块的开始。
- ***typedef***: 另一个基本或用户定义类型的同义词。
- ***union***: 类似于结构体，能够存储不同类型的数据，但一次只能存储一个成员。
- ***unsigned***: 数据类型修饰符，指示高位用于对象。
- ***virtual***: 函数说明符，声明一个成员函数，该函数将由派生类重新定义。
- ***void***: 没有类型或函数参数列表。
- ***volatile***: 定义一个值可能以编译器无法检测的方式变化的对象。
- ***while***: while 语句的开始和 do-while 语句的结束。

### 什么是标识符？

标识符指程序员创建的变量、函数、数组、类等的名称。它们是任何语言的基本要求。

***标识符命名规则：***

- 标识符名称不能以数字或任何特殊字符开头。
- 关键字不能用作标识符名称。
- 仅允许字母字符、数字和下划线。
- 大写字母和小写字母是区分的，即 A 和 a 在 C++ 中是不同的。
- 有效的标识符有 GFG、gfg 和 geeks_for_geeks。

***良好与不良标识符的示例***

| 无效标识符 | 不良标识符 | 良好标识符 |
| ---------- | ---------- | ---------- |
| Cash prize | C_prize    | cashprize  |
| catch      | catch_1    | catch1     |
| 1list      | list_1     | list1      |

**示例：**

- C++

```
// C++ 程序示例：演示标识符的使用
#include <iostream>
using namespace std;

// 驱动代码
int main() {
    // 使用下划线 (_) 符号
    // 在变量声明中
    int geeks_for_geeks = 1;
    
    cout << "标识符结果是: " << geeks_for_geeks;
    return 0;
}
```

**Output**

```
标识符结果是: 1
```

### 关键词和标识符的区别

关键词和标识符之间有几个主要的区别:

| **关键词**                               | **标识符**                                                   |
| ---------------------------------------- | ------------------------------------------------------------ |
| 关键词是预定义的/保留的字词              | 标识符是用来定义不同编程项（如变量、整数、结构体、联合体）的值 |
| 关键词总是以小写字母开头                 | 标识符可以以大写字母或小写字母开头                           |
| 关键词定义了实体的类型                   | 标识符用来标识实体的名称                                     |
| 关键词只包含字母字符                     | 标识符可以包含字母字符、数字和下划线                         |
| 关键词应为小写字母                       | 标识符可以是大写或小写字母                                   |
| 关键词和标识符中不使用特殊符号或标点符号 | 关键词和标识符中不使用特殊符号或标点符号。标识符中只能使用下划线 |
| 关键词举例：int, char, while, do         | 标识符举例：Geeks_for_Geeks, GFG, Gfg1                       |

**示例：** 以下是一个演示如何在程序中使用不同关键词的示例：

- C++

```
// C++ 程序：演示关键词的使用
#include <iostream>
using namespace std;

// 驱动代码
int main() {
    // 变量声明和初始化
    int n = 2;
    
    // switch-case 语句
    switch (n) {
        case 1:
            cout << "计算机网络" << endl;
            break;
        case 2:
            cout << "C++" << endl;
            break;
        case 3:
            cout << "数据库管理系统" << endl;
            break;
        case 4:
            cout << "数据结构" << endl;
            break;
        case 5:
            cout << "操作系统" << endl;
            break;
        default:
            cout << "请输入有效的数字" << endl;
    }
    
    // return 关键词返回对象给函数的调用者
    return 0;
}
```

**Output**

```
C++
```