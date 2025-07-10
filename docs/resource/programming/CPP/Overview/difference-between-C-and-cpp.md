---
comments: true
---
# C和C++的不同之处

***C*** 和 ***C++*** 之间的相似点：

- 两种语言的语法相似。
- 两种语言的代码结构相同。
- 两种语言的编译过程类似。
- 它们共享相同的基本语法。几乎所有C的运算符和关键字在C++中也存在，并且作用相同。
- C++的语法相比C稍微扩展，但基本语法相同。
- 两者的基本内存模型都非常接近硬件。
- 两种语言中都存在相同的堆栈、堆、文件作用域和静态变量的概念。

***C*** 和 ***C++*** 之间的不同点：

- C++通常被视为C的超集。C++也被称为“带类的C”。这一点在C++最初创建时几乎是正确的，但随着时间的推移，两种语言都发生了变化，C添加了许多在当时的C++版本中找不到的特性，或者仍未出现在任何版本的C++中。尽管如此，C++仍然主要是C的超集，增加了[面向对象编程](https://www.geeksforgeeks.org/object-oriented-programming-in-cpp/)、[异常处理](https://www.geeksforgeeks.org/exception-handling-c/)、模板编程和更广泛的标准库。

以下是C和C++之间一些更明显和一般的区别的表格。语言及其版本之间还有许多更微妙的差异。

|                              C                               |                             C++                              |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|  C由Dennis Ritchie于1969年至1973年间在AT&T Bell Labs开发。   |             C++由Bjarne Stroustrup于1979年开发。             |
|    C不支持多态、封装和继承，这意味着C不支持面向对象编程。    | C++支持[多态](https://www.geeksforgeeks.org/polymorphism-in-c/)、[封装](https://www.geeksforgeeks.org/encapsulation-in-c/)和[继承](https://www.geeksforgeeks.org/inheritance-in-c/)，因为它是一种面向对象编程语言。 |
|                    C（主要）是C++的子集。                    |                    C++（主要）是C的超集。                    |
| C中的[关键字](https://www.geeksforgeeks.org/variables-and-keywords-in-c/)数量： * C90: 32 * C99: 37 * C11: 44 * C23: 59 | C++中的[关键字](https://www.geeksforgeeks.org/cc-tokens/)数量： * C++98: 63 * C++11: 73 * C++17: 73 * C++20: 81 |
| C支持[过程式编程](https://www.geeksforgeeks.org/introduction-of-programming-paradigms/)。 | C++被称为混合语言，因为C++支持[过程式](https://www.geeksforgeeks.org/introduction-of-programming-paradigms/)和[面向对象编程范式](https://www.geeksforgeeks.org/introduction-of-programming-paradigms/)。 |
|    数据和函数在C中是分开的，因为它是一种过程式编程语言。     |              数据和函数在C++中被封装在对象中。               |
|                      C不支持信息隐藏。                       |   数据通过封装进行隐藏，以确保数据结构和操作符按预期使用。   |
|                     C支持内置数据类型。                      |              C++支持内置和用户定义的数据类型。               |
|      C是一种函数驱动的语言，因为C是一种过程式编程语言。      |      C++是一种面向对象的语言，因为它是面向对象编程的。       |
|                  C不支持函数和运算符重载。                   |                  C++支持函数和运算符重载。                   |
|                   C是一种函数驱动的语言。                    |                  C++是一种面向对象的语言。                   |
|               C中的函数不能定义在结构体内部。                |              C++中的函数可以在结构体内部使用。               |
|                    C中没有命名空间功能。                     | C++使用[命名空间](https://www.geeksforgeeks.org/namespace-in-c/)来避免名称冲突。 |
| 标准输入输出头文件是[stdio.h](https://www.geeksforgeeks.org/whats-difference-between-and/)。 | 标准输入输出头文件是[iostream.h](https://www.geeksforgeeks.org/basic-input-output-c/)。 |
|                      C不支持引用变量。                       |                      C++支持引用变量。                       |
|                  C不支持虚函数和友元函数。                   | C++支持[虚函数](https://www.geeksforgeeks.org/virtual-function-cpp/)和[友元函数](https://www.geeksforgeeks.org/friend-class-function-cpp/)。 |
|                        C不支持继承。                         |                        C++支持继承。                         |
|              C关注的是方法或过程，而不是数据。               |             C++关注的是数据，而不是方法或过程。              |
| C提供了[malloc()](https://www.geeksforgeeks.org/dynamic-memory-allocation-in-c-using-malloc-calloc-free-and-realloc/)和[calloc()](https://www.geeksforgeeks.org/dynamic-memory-allocation-in-c-using-malloc-calloc-free-and-realloc/)函数用于[动态内存分配](https://www.geeksforgeeks.org/dynamic-memory-allocation-in-c-using-malloc-calloc-free-and-realloc/)，并使用[free()](https://www.geeksforgeeks.org/dynamic-memory-allocation-in-c-using-malloc-calloc-free-and-realloc/)进行内存释放。 | C++提供了[new操作符](https://www.geeksforgeeks.org/new-and-delete-operators-in-cpp-for-dynamic-memory/)用于内存分配，并提供了[delete操作符](https://www.geeksforgeeks.org/new-and-delete-operators-in-cpp-for-dynamic-memory/)用于内存释放。 |
|                    C不直接支持异常处理。                     | C++支持[异常处理](https://www.geeksforgeeks.org/exception-handling-c/)。 |
| [scanf()](https://www.geeksforgeeks.org/scanf-and-fscanf-in-c-simple-yet-poweful/)和printf()函数用于C中的输入/输出。 | [cin和cout](https://www.geeksforgeeks.org/basic-input-output-c/)用于C++中的[输入/输出](https://www.geeksforgeeks.org/basic-input-output-c/)。 |
|                   C结构体没有访问修饰符。                    |                   C++结构体有访问修饰符。                    |
|               C编程语言中没有严格的类型检查。                | C++中进行严格的类型检查。因此，许多在C编译器中运行良好的程序在C++编译器中会产生许多警告和错误。 |
|                        C不支持重载。                         |                        C++支持重载。                         |
|         C99及以后的版本允许使用联合体进行类型混淆。          | 类型混淆使用联合体在C++中是未定义行为（除非在非常特定的情况下）。 |
|                  命名初始化器可以无序出现。                  |           命名初始化器必须与结构体的数据布局匹配。           |
|                      文件扩展名是“.c”。                      |         文件扩展名是“.cpp”或“.c++”或“.cc”或“.cxx”。          |
|                   元编程：宏 + _Generic()                    |          元编程：模板（宏仍然受支持但不推荐使用）。          |
|                      C中有32个关键字。                       |                     C++中有97个关键字。                      |