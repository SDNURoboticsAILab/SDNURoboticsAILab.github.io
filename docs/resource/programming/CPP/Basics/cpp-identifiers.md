---
comments: true
---
# C++ 标识符

在 C++ 编程语言中，**标识符**是分配给变量、函数、类、结构体或程序中其他实体的唯一名称。例如，在以下语句中：

```
int num = 11;
```

**um** 是一个标识符。

## C++ 中标识符命名规则

我们可以使用任何单词作为标识符，只要它遵循以下规则：

1. 标识符可以由 **字母**（A-Z 或 a-z）、**数字**（0-9）和 **下划线 (_) ** 组成。特殊字符和空格是不允许的。
2. 标识符只能以 **字母或下划线** 开头。
3. C++ 有一些 **关键字** 是保留的，不能用作标识符，因为它们在语言中有预定义的意义。例如，**int** 不能作为标识符使用，因为它在 C++ 中已有预定义的含义。尝试使用这些关键字作为标识符会导致编译错误。
4. 标识符在其命名空间中必须 **唯一**。

此外，C++ 是区分大小写的语言，因此标识符如 **Num** 和 **num** 被视为不同的标识符。

以下图片展示了一些有效和无效的 C++ 标识符。

![examples of valid and invalid identifiers](https://media.geeksforgeeks.org/wp-content/uploads/20221202181520/Cvariables2.png)

### C++ 标识符示例

在这个示例中，我们按照指南使用了标识符，并用标识符命名了一个 [类](https://www.geeksforgeeks.org/c-classes-and-objects/)、函数、整数数据类型等。如果你对 C++ 中的 [函数](https://www.geeksforgeeks.org/functions-in-cpp/) 和 [类](https://www.geeksforgeeks.org/c-classes-and-objects/) 不太了解，别担心，你很快会学到它们。以下代码成功运行，这意味着我们正确地命名了它们。

- C++

```
// C++ 程序说明标识符
#include <iostream>
using namespace std;

// 这里的 Car_24 标识符用于引用下面的类
class Car_24 {
  string Brand;
  string model;
  int year;
};

// calculateSum 标识符用于调用下面的函数
void calculateSum(int a, int b) {
  int _sum = a + b;
  cout << "The sum is: " << _sum << endl;
}

int main() {
  // 标识符用作变量名
  int studentAge = 20;
  double accountBalance = 1000.50;
  string student_Name = "Karan";

  calculateSum(2, 10);

  return 0;
}
```

输出

```
The sum is: 12
```