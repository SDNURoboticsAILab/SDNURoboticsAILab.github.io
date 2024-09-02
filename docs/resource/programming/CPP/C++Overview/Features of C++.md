# C++的特点

C++是一种通用编程语言，它是在[C语言](https://www.geeksforgeeks.org/c-language-set-1-introduction/)的基础上发展起来的，加入了[面向对象的编程范式](https://www.geeksforgeeks.org/object-oriented-programming-in-cpp/)。它是一种命令式和**编译型**语言。C++具有以下特点：

- 面向对象编程
- 机器无关性
- 简单
- 高级语言
- 流行
- 区分大小写
- 基于编译器
- 动态内存分配
- 内存管理
- 多线程



- ## 1. 面向对象编程

  C++是一种面向对象编程语言，而C语言则是一种[过程式编程语言](https://www.geeksforgeeks.org/differences-between-procedural-and-object-oriented-programming/)。这是**C++**最重要的特点。它可以在编程过程中创建和销毁对象，并且可以创建对象的蓝图。我们在这篇[文章](https://www.geeksforgeeks.org/object-oriented-programming-in-cpp/)中讨论了C++中的面向对象编程概念。

  面向对象编程语言的概念：

  - [类](https://www.geeksforgeeks.org/c-classes-and-objects/)
  - 对象
  - [封装](https://www.geeksforgeeks.org/encapsulation-in-c/)
  - [多态](https://www.geeksforgeeks.org/polymorphism-in-c/)
  - [继承](https://www.geeksforgeeks.org/inheritance-in-c/)
  - [抽象](https://www.geeksforgeeks.org/abstraction-in-c/)

## 2. 机器无关性

C++的可执行文件不是[平台无关的](https://www.geeksforgeeks.org/writing-os-independent-code-cc/)（在Linux上编译的程序不能在Windows上运行），但它们是机器无关的。我们可以通过一个例子来理解这一特性。假设你写了一段代码，可以在Linux/Windows/Mac OS X上运行，这使得C++具有机器无关性，但C++的可执行文件不能在不同的操作系统上运行。

## 3. 简单

它是一种简单的语言，因为程序可以被分解成逻辑单元和部分，拥有丰富的库支持和多种数据类型。此外，C++ 的 Auto 关键字也使得编程更为方便。

### Auto 关键字

`auto` 关键字的理念是让 C++ 编译器在编译时自动推断数据类型，而不是每次都让你显式声明数据类型。需要注意的是，你不能在没有初始化器的情况下声明变量。编译器必须有某种方式来推断你的数据类型。

**Example:**

- C++

```
// C++ program to demonstrate
// working of auto keyword

#include <bits/stdc++.h>
using namespace std;

// Driver Code
int main() {
    // Variables
    auto an_int = 26;
    auto a_bool = false;
    auto a_float = 26.24;
    auto ptr = &a_float;

    // Print typeid
    cout << typeid(a_bool).name() << "\n";
    cout << typeid(an_int).name() << "\n";

    return 0;
}

```

**Output:**

```
b
i
```

 

- ## 4. 高级语言

  C++ 是一种 [高级语言](https://www.geeksforgeeks.org/difference-between-high-level-and-low-level-languages/)，而 C 是一种中级编程语言。由于 C++ 是高级语言，它与人类可理解的英语语言紧密相关，从而使得编程变得更容易。

  ## 5. 流行

  C++ 可以作为许多其他编程语言的基础，这些语言支持面向对象编程的特性。**Bjarne Stroustrup** 发现首个面向对象的语言 Simula 67 缺乏模拟功能，因此决定开发 C++。

  ## 6. 区分大小写

  C++ 是一种区分大小写的编程语言。例如，**cin** 用于从 [输入流](https://www.geeksforgeeks.org/basic-input-output-c/) 中读取输入。但 **“Cin”** 不会起作用。其他语言如 HTML 和 MySQL 是不区分大小写的语言。

  ## 7. 基于编译器

  C++ 是一种基于编译器的语言，与 Python 不同。即 C++ 程序需要被编译，其可执行文件用于运行程序。[C++ 比 Java 和 Python 更快](https://www.geeksforgeeks.org/c-vs-java-vs-python/)。

  ## 8. 动态内存分配

  在 C++ 中，当程序执行时，变量被分配到 [动态堆空间](https://www.geeksforgeeks.org/memory-layout-of-c-program/) 中。在函数内部，变量被分配到栈空间。很多时候，我们事先无法知道存储特定信息所需的内存量，因此内存的大小可以在运行时确定。

  ## 9. 内存管理

  - C++ 允许我们在运行时分配变量或数组的内存，这称为 [动态内存分配](https://www.geeksforgeeks.org/c-language-2-gq/dynamic-memory-allocation-gq/)。
  - 在其他编程语言如 [Java](https://www.geeksforgeeks.org/java/) 和 [Python](https://www.geeksforgeeks.org/python-programming-language/) 中，编译器自动管理分配给变量的内存。但在 C++ 中并非如此。
  - 在 C++ 中，必须在内存不再使用时手动释放动态分配的内存。
  - 内存的分配和释放可以分别使用 [new 和 delete 操作符](https://www.geeksforgeeks.org/new-and-delete-operators-in-cpp-for-dynamic-memory/) 来完成。

**Example:**

- C++

```
// C++ Program to implement memory management

#include <cstring>
#include <iostream>

using namespace std;

// Driver Code
int main() {
    int num = 5;
    float* ptr;

    // Memory allocation of num number of floats
    ptr = new float[num];

    for (int i = 0; i < num; ++i) {
        *(ptr + i) = i;
    }

    cout << "Display the GPA of students:" << endl;
    for (int i = 0; i < num; ++i) {
        cout << "Student " << i + 1 << ": " << *(ptr + i) << endl;
    }

    // Ptr memory is released
    delete[] ptr;

    return 0;
}

```

**Output:**

```
Display the GPA of students:
Student1: 0
Student2: 1
Student3: 2
Student4: 3
Student5: 4
```

 

- ## 10. 多线程

  - [多线程](https://www.geeksforgeeks.org/multithreading-c-2/) 是多任务的一种特殊形式，而多任务是允许系统同时执行两个或更多程序的功能。一般来说，多任务有两种形式：[基于进程和基于线程](https://www.geeksforgeeks.org/process-based-and-thread-based-multitasking/)。
  - 基于进程的多任务处理程序的并发执行，而基于线程的多任务则处理相同程序的多个部分的并发执行。
  - 多线程程序包含两个或更多可以并发运行的部分。每个部分被称为一个 [线程](https://www.geeksforgeeks.org/thread-in-operating-system/)，每个线程定义了一个独立的执行路径。
  - C++ 不包含对多线程应用的内建支持。相反，它完全依赖操作系统提供这一功能。

**Example:**

- C++

```
// C++ Program to implement the working of Multi-threading

#include <cstdlib>
#include <iostream>
#include <pthread.h>

using namespace std;

#define NUM_THREADS 5

// Function to print Hello with the thread id
void* PrintHello(void* threadid) {
    // Thread ID
    long tid;
    tid = (long)threadid;

    // Print the thread ID
    cout << "Hello World! Thread ID, " << tid << endl;

    pthread_exit(NULL);
}

// Driver Code
int main() {
    // Create thread
    pthread_t threads[NUM_THREADS];
    int rc;
    int i;

    for (i = 0; i < NUM_THREADS; i++) {
        cout << "main() : creating thread, " << i << endl;
        rc = pthread_create(&threads[i], NULL, PrintHello, (void*)&i);

        // If thread is not created
        if (rc) {
            cout << "Error: unable to create thread, " << rc << endl;
            exit(-1);
        }
    }

    pthread_exit(NULL);
}

```

**Output:**

![img](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20200910111517/Screenshot-from-2020-09-10-11-14-39.png)

 

