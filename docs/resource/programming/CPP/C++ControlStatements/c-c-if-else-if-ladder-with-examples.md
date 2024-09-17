# C++ if-else if 梯级语句

条件判断在 C++ 中帮助根据某些条件执行特定的代码块。

在 C++ 中，**if-else-if 梯级语句** 允许用户在多个选项中进行选择。C++ 中的 if 语句从上到下执行。一旦某个条件为真，便会执行与该 if 语句相关的代码，且剩余的 else-if 结构将被跳过。如果所有条件都不为真，则最终的 else 语句将会被执行。

![img](https://media.geeksforgeeks.org/wp-content/uploads/20191114112014/If-else-if-ladder-GeeksforGeeks-1.jpg)

## 语法

```
if (condition)
    statement 1;
else if (condition)
    statement 2;
.
.
else
    statement;
```

## 梯级 if-else-if 的工作原理

1. 控制权进入 if 块。

2. 流程跳转到条件 1。

3. 条件被测试。

   ​	如果条件为真，跳转到步骤 4。

   ​	如果条件为假，跳转到步骤 5。

4. 当前的代码块被执行，跳转到步骤 7。

5. 流程跳转到条件 2。

   ​	如果条件为真，跳转到步骤 4。

   ​	如果条件为假，跳转到步骤 6。

6. 流程跳转到条件 3。

   ​	如果条件为真，跳转到步骤 4。

   ​	如果条件为假，执行 else 代码块并跳转到步骤 7。

7. 退出 if-else-if 结构。

# C++ if else if Ladder

条件判断在 C++ 中帮助根据某些条件执行特定的代码块。

在 C++ 中，**if-else-if ladder** 允许用户在多个选项中进行选择。C++ 中的 if 语句从上到下执行。一旦某个条件为真，便会执行与该 if 语句相关的代码，且剩余的 else-if ladder 将被跳过。如果所有条件都不为真，则最终的 else 语句将会被执行。

![img](https://media.geeksforgeeks.org/wp-content/uploads/20191114112014/If-else-if-ladder-GeeksforGeeks-1.jpg)

## **语法**

```cpp
if (condition)
    statement 1;
else if (condition)
    statement 2;
.
.
else
    statement;
```

## **if-else-if ladder 的工作原理**

1. 控制权进入 if 块。
2. 流程跳转到条件 1。
3. 条件被测试。
   1. 如果条件为真，跳转到步骤 4。
   2. 如果条件为假，跳转到步骤 5。
4. 当前的代码块被执行，跳转到步骤 7。
5. 流程跳转到条件 2。
   1. 如果条件为真，跳转到步骤 4。
   2. 如果条件为假，跳转到步骤 6。
6. 流程跳转到条件 3。
   1. 如果条件为真，跳转到步骤 4。
   2. 如果条件为假，执行 else 代码块并跳转到步骤 7。
7. 退出 if-else-if 结构。

## **if-else-if ladder 流程图**

![if-else-if-ladder](https://media.geeksforgeeks.org/wp-content/uploads/decision-making-c-4.png)

## 梯级 if-else-if 的示例

### 示例 1：

以下程序演示了 C++ 中 if-else-if ladder 的使用。

- C++

```cpp
// C++ program to illustrate if-else-if ladder  
#include <iostream>  
using namespace std;  
    
int main()  
{  
    int i = 20;  
    
    // Check if i is 10  
    if (i == 10)  
        cout << "i is 10";  
    
    // Since i is not 10  
    // Check if i is 15  
    else if (i == 15)  
        cout << "i is 15";  
    
    // Since i is not 15  
    // Check if i is 20  
    else if (i == 20)  
        cout << "i is 20";  
    
    // If none of the above conditions is true  
    // Then execute the else statement  
    else
        cout << "i is not present";  
    
    return 0;  
}
```

**输出**

```
i is 20
```

**解释：**

- 程序开始。
- i 被初始化为 20。
- 检查条件 1：20 == 10，结果为假。
- 检查条件 2：20 == 15，结果为假。
- 检查条件 3：20 == 20，结果为真，因此输出 "i is 20"。
- 程序结束。

### 示例 2：

另一个演示 C++ 中 if-else-if ladder 的示例。

- C++

```cpp
// C++ program to illustrate if-else-if ladder 
  
#include <iostream> 
using namespace std; 
  
int main() 
{ 
    int i = 25; 
  
    // Check if i is between 0 and 10 
    if (i >= 0 && i <= 10) 
        cout << "i is between 0 and 10" << endl; 
  
    // Since i is not between 0 and 10 
    // Check if i is between 11 and 15 
    else if (i >= 11 && i <= 15) 
        cout << "i is between 11 and 15" << endl; 
  
    // Since i is not between 11 and 15 
    // Check if i is between 16 and 20 
    else if (i >= 16 && i <= 20) 
        cout << "i is between 16 and 20" << endl; 
  
    // Since i is not between 0 and 20 
    // It means i is greater than 20 
    else
        cout << "i is greater than 20" << endl; 
}
```

**输出**

```
i is greater than 20
```