# C++ 中的范围基 for 循环

自 C++ 11 以来，范围基 for 循环已经被引入。它用于在一组范围内执行 for 循环，是传统 for 循环在处理一组值（如容器中的所有元素）时更具可读性的替代方案。

#### **语法：**

```
for ( range_declaration : range_expression ) 
    loop_statement
```

**参数：**

- **range_declaration**: 一个声明变量，变量类型是由 `range_expression` 表示的序列元素类型，或对该类型的引用。通常使用 `auto` 关键字来自动推导类型。
- **range_expression**: 任意表达式，可以表示适合的序列或花括号初始化列表。
- **loop_statement**: 任意语句，通常是复合语句，作为循环的主体。

**C++ 实现示例：**

```
// Illustration of range-for loop
// using CPP code
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

// Driver
int main()
{
    // Iterating over whole array
    vector<int> v = { 0, 1, 2, 3, 4, 5 };
    for (auto i : v)
        cout << i << ' ';

    cout << '\n';

    // the initializer may be a braced-init-list
    for (int n : { 0, 1, 2, 3, 4, 5 })
        cout << n << ' ';

    cout << '\n';

    // Iterating over array
    int a[] = { 0, 1, 2, 3, 4, 5 };
    for (int n : a)
        cout << n << ' ';

    cout << '\n';

    // Just running a loop for every array
    // element
    for (int n : a)
        cout << "In loop" << ' ';

    cout << '\n';

    // Printing string characters
    string str = "Geeks";
    for (char c : str)
        cout << c << ' ';

    cout << '\n';

    // Printing keys and values of a map
    map<int, int> MAP({ { 1, 1 }, { 2, 2 }, { 3, 3 } });
    for (auto i : MAP)
        cout << '{' << i.first << ", " << i.second << "}\n";
}

```

**输出**

```
0 1 2 3 4 5 
0 1 2 3 4 5 
0 1 2 3 4 5 
In loop In loop In loop In loop In loop In loop 
G e e k s 
{1, 1}
{2, 2}
{3, 3}
```

**C++ 17 或更高版本：**

在 C++ 17 及更高版本中，范围基 for 循环还可以用在 `map` 容器上，如下所示：

```
for (auto& [key, value]: myMap) {
    cout << key << " has value " << value << std::endl;
}
```

在这里，`[key, value]` 类似于 `pair` 元素，允许我们直接访问 `key` 和 `value`，而不需要使用 `first` 或 `second` 关键字。

