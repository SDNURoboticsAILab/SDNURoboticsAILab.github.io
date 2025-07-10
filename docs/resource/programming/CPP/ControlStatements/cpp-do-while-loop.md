---
comments: true
---
# C++ Do/While 循环

在需要重复执行一段代码时，可以使用 **循环**。与 **while 循环** 类似，**do-while 循环** 的执行也是基于一个测试条件。两者的主要区别在于，**do-while 循环** 是在循环体执行之后才进行条件判断，即 **do-while 循环** 是出口控制循环，而其他循环（如 for 和 while）是入口控制循环。

> **注意**: 在 **do-while 循环** 中，循环体至少会执行一次，无论测试条件是否为真。

![do-while loop in C++](https://media.geeksforgeeks.org/wp-content/uploads/20191118154342/do-while-Loop-GeeksforGeeks2.jpg)

**语法**

```
do
{
   // loop body

   update_expression;
} 
while (test_expression);
```

> **注意**: 请注意在循环结束时有分号 (";")。**

**do-while 循环的各个部分：**

1. **测试表达式 (Test Expression):** 判断条件是否成立。如果条件为真，执行循环体并更新循环变量；如果条件为假，退出循环。
2. **更新表达式 (Update Expression):** 每次循环执行后，增减循环变量的值。
3. **循环体 (Body):** 代码块，包含变量、函数等，用于执行操作，如打印输出、复杂算法或功能操作。

## do-while 循环的执行流程：

1. 控制流进入 do-while 循环。

2. 执行循环体中的语句。

3. 更新循环变量。

4. 流程跳转到条件判断部分。

5. 检查条件：

   ​	如果条件为真，跳转到步骤 2 继续循环。

   ​	如果条件为假，跳出循环。

6. 循环结束，控制流跳出循环。

## do-while 循环的流程图

![do while loop in C++](https://media.geeksforgeeks.org/wp-content/uploads/20221006152307/dowhileloopinc.png)

 

示例 1：打印 “Hello World”

- C++

```
// C++ program to illustrate do-while loop 

#include <iostream> 
using namespace std; 

int main() 
{ 
	// Initialization expression 
	int i = 2; 

	do { 
		// Loop body 
		cout << "Hello World\n"; 

		// Update expression 
		i++; 

	} 
	// Test expression 
	while (i < 1); 

	return 0; 
}

```

**输出**

```
Hello World
```

 

**示例 1 的逐步执行：**

1. 程序开始，变量 `i` 被初始化为 2。
2. 进入循环体，打印 "Hello World"。
3. 更新 `i = 3`。
4. 检查条件：`i < 1` 为假，跳出循环。

示例 2：从 1 递增到 5

- C++

```
// C++ program to illustrate do-while loop 

#include <iostream> 
using namespace std; 

int main() 
{ 
	// Initialization expression 
	int i = 1; 

	do { 
		// Loop body 
		cout << i << endl; 

		// Update expression 
		i++; 

	} 
	// Test expression 
	while (i <= 5); 

	return 0; 
}

```

**输出**

```
1
2
3
4
5
```