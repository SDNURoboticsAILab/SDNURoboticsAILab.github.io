---
comments: true
---
# C++ While 循环

**While 循环** 在 C++ 中用于未知确切迭代次数的情况。循环的执行依据测试条件来终止。当我们学习 C++ 中的 **for 循环** 时，可以看到 for 循环用于已知迭代次数的情况。而 while 循环则适合迭代次数不确定的情形。

![while loop in C++](https://media.geeksforgeeks.org/wp-content/uploads/20191118170432/While-Loop-GeeksforGeeks1.jpg)

**语法**

```
while (test_expression)
{
   // statements
 
  update_expression;
}
```

**While 循环的各个部分：**

1. **测试表达式 (Test Expression):** 该表达式用于判断条件。如果条件为真，继续执行循环体并更新表达式；如果为假，则退出循环。
2. **更新表达式 (Update Expression):** 每次循环执行完后，此表达式会对循环变量进行增量或减量操作。
3. **循环体 (Body):** 一组包含变量、函数等的语句。在 while 循环中，可以执行打印、算法操作或函数调用。

## While 循环的执行流程：

1. 控制进入 while 循环。

2. 条件表达式被检查。

   ​	如果条件为真，执行循环体，然后进行更新。

   ​	如果条件为假，跳出循环。

3. 执行循环体中的语句。

4. 更新循环变量。

5. 返回步骤 2，继续检查条件。

6. 循环结束后，控制流跳出循环。

## While 循环的流程图

![while loop in C++](https://media.geeksforgeeks.org/wp-content/uploads/20220927171802/WhileloopinC2.png)

 

**示例 1：**打印 “Hello World” 5 次

- C++

```
// C++ program to illustrate while loop 

#include <iostream> 
using namespace std; 

int main() 
{ 
	// initialization expression 
	int i = 1; 

	// test expression 
	while (i < 6) { 
		cout << "Hello World\n"; 

		// update expression 
		i++; 
	} 

	return 0; 
}

```

**输出**

```
Hello World
Hello World
Hello World
Hello World
Hello World
```

**示例 1 的逐步执行**：

```
程序开始，变量 i 被初始化为 1。
检查条件：1 < 6 为真，打印第 1 次 "Hello World"，更新 i = 2。
检查条件：2 < 6 为真，打印第 2 次，更新 i = 3。
检查条件：3 < 6 为真，打印第 3 次，更新 i = 4。
检查条件：4 < 6 为真，打印第 4 次，更新 i = 5。
检查条件：5 < 6 为真，打印第 5 次，更新 i = 6。
检查条件：6 < 6 为假，跳出循环，程序结束。
```

**示例2**

- C++

```
// C++ program to illustrate while loop 

#include <iostream> 
using namespace std; 

int main() 
{ 
	// initialization expression 
	int i = 1; 

	// test expression 
	while (i > -5) { 
		cout << i << "\n"; 

		// update expression 
		i--; 
	} 

	return 0; 
} 

```

**输出**

```
1
0
-1
-2
-3
-4
```