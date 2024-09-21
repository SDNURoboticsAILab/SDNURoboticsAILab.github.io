# C++ if else 语句

条件判断在 C++ 中有助于根据某些条件执行特定代码块。

*if* 语句本身用于检查条件是否为真，如果条件为真，则执行代码块；如果条件为假，则不执行。但是，如果条件为假时我们希望执行其他操作，则可以使用 C++ 中的 **else 语句**。我们可以将 else 语句与 if 语句配合使用，在条件为假时执行特定的代码块。

![img](https://media.geeksforgeeks.org/wp-content/uploads/20191118180512/If-else-statement-GeeksforGeeks1.jpg)

## 语法

```
if (condition)
{
    // Executes this block if
    // condition is true
}
else
{
    // Executes this block if
    // condition is false
}
```

## if-else 语句的工作原理

1. 控制权进入 if 块。

2. 流程跳转到条件。

3. 条件被测试。

   ​	如果条件为真，跳转到步骤 4。

   ​	如果条件为假，跳转到步骤 5。

4. 执行 if 块中的代码。

5. 执行 else 块中的代码。

6. 流程退出 if-else 块。

## if-else 流程图

![img](https://media.geeksforgeeks.org/wp-content/uploads/20191119183412/C-Cpp-if-else.png)

## C++ 中 if else 语句的示例

### 示例 1：

下面的程序演示了 C++ 中 if else 语句的使用。

- C++

```cpp
// C++ program to illustrate if-else statement  
    
#include <iostream>  
using namespace std;  
    
int main()  
{  
    int i = 20;  
    
    // Check if i is 10  
    if (i == 10)  
        cout << "i is 10";  
    
    // Since is not 10  
    // Then execute the else statement  
    else
        cout << "i is 20\n";  
    
    cout << "Outside if-else block";  
    
    return 0;  
}  
```

**输出**

```
i is 20
Outside if-else block
```

**解释：**

- 程序开始。
- i 被初始化为 20。
- 检查 if 条件。i == 10，结果为假。
- 流程进入 else 块。
- 输出 "i is 20"。
- 输出 "Outside if-else block"。

### 示例 2：

# C++ if else 语句

条件判断在 C++ 中有助于根据某些条件执行特定代码块。

*if* 语句本身用于检查条件是否为真，如果条件为真，则执行代码块；如果条件为假，则不执行。但是，如果条件为假时我们希望执行其他操作，则可以使用 C++ 中的 **else 语句**。我们可以将 else 语句与 if 语句配合使用，在条件为假时执行特定的代码块。

![img](https://media.geeksforgeeks.org/wp-content/uploads/20191118180512/If-else-statement-GeeksforGeeks1.jpg)

## **语法**

```
arduino复制代码if (condition)
{
    // 当条件为真时执行该代码块
}
else
{
    // 当条件为假时执行该代码块
}
```

## **if-else 语句的工作原理**

1. 控制权进入 if 块。
2. 流程跳转到条件。
3. 条件被测试。
   1. 如果条件为真，跳转到步骤 4。
   2. 如果条件为假，跳转到步骤 5。
4. 执行 if 块中的代码。
5. 执行 else 块中的代码。
6. 流程退出 if-else 块。

## **if-else 流程图**

![img](https://media.geeksforgeeks.org/wp-content/uploads/20191119183412/C-Cpp-if-else.png)

## C++ 中 if else 语句的示例

### **示例 1：**

下面的程序演示了 C++ 中 if else 语句的使用。

```
cpp复制代码#include <iostream>
using namespace std;

int main() {
    int i = 20;

    // 检查 i 是否等于 10
    if (i == 10)
        cout << "i is 10";
    else
        cout << "i is 20\n";

    cout << "Outside if-else block";
    return 0;
}
```

**输出**

```
csharp复制代码i is 20
Outside if-else block
```

**解释：**

- 程序开始。
- i 被初始化为 20。
- 检查 if 条件。i == 10，结果为假。
- 流程进入 else 块。
- 输出 "i is 20"。
- 输出 "Outside if-else block"。

### **示例 2：**

另一个展示 C++ 中 if else 使用的程序。

- C++

```cpp
// C++ program to illustrate if-else statement  
    
#include <iostream>  
using namespace std;  
    
int main()  
{  
    int i = 25;  
    
    if (i > 15)  
        cout << "i is greater than 15";  
    else
        cout << "i is smaller than 15";  
    
    return 0;  
}
```

**输出**

```
i is greater than 15
```