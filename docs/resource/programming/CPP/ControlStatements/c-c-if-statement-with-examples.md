---
comments: true
---
# C++ if 语句

条件判断在 C++ 中有助于编写基于特定条件执行特定代码块的语句。

C++ 中的 ***if 语句*** 是最简单的条件判断语句。它用于根据某种条件决定某条语句或语句块是否执行。

![img](https://media.geeksforgeeks.org/wp-content/uploads/20191118171408/If-statement-GeeksforGeeks1.jpg)

## 语法

```
if(condition) 
{
   // Statements to execute if
   // condition is true
}
```

## if 语句在 C++ 中的工作原理

1. 控制进入 if 块。

2. 流程跳转到条件。

3. 条件被测试。

   如果条件为真，跳转到步骤 4。

   如果条件为假，跳转到步骤 5。

   

4. 执行 if 块内的代码。

5. 流程退出 if 块。

## 流程图

![img](https://media.geeksforgeeks.org/wp-content/uploads/20191119173402/C-Cpp-if.png)

如果我们在 `if( condition )` 后没有提供大括号 `{}`，那么 if 语句默认会将其后的第一条语句视为它的代码块。

**例如:**

```
if(condition)    
statement1;    
statement2;  // Here if the condition is true if block will consider only statement1 to be inside  its block.
```

## if 语句的示例

### 示例 1

下面的程序演示了 C++ 中 if 语句的使用。

- C++

```cpp
// C++ program to illustrate If statement  
    
#include <iostream>  
using namespace std;  
    
int main()  
{  
    int i = 10;  
    
    if (i < 15) {  
        cout << "10 is less than 15 \n";  
    }  
    
    cout << "I am Not in if";  
}
```

**输出**

```
10 is less than 15 
I am Not in if
```

**解释:**

- 程序开始。
- 变量 i 被初始化为 10。
- 检查 if 条件，10 < 15，条件为真。
- 输出 "10 is less than 15"。
- if 条件结束，输出 "I am Not in if"。

### 示例 2

下面的程序演示了 C++ 中 if 语句的另一个例子。

- C++

```cpp
// C++ program to illustrate If statement 
  
#include <iostream> 
using namespace std; 
  
int main() 
{ 
    int i = 10; 
  
    if (i > 15) { 
        cout << "10 is greater than 15 \n"; 
    } 
  
    cout << "I am Not in if"; 
}
```

**输出**

```
I am Not in if
```