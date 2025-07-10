---
comments: true
---
# C++ 中的 for 循环

在 C++ 中，for 循环是一种**入口控制循环**，用于对指定范围内的值重复执行一段代码。基本上，for 循环允许你在特定次数内重复执行一组指令。

当迭代次数预先已知时，for 循环通常优于 while 和 do-while 循环。

## for 循环的语法

C++ 中 for 循环的语法如下：

```
for ( initialization; test condition; updation)
{ 
     // body of for loop
}
```

![syntax breakdown of for loop in cpp](https://media.geeksforgeeks.org/wp-content/uploads/20231221155254/cpp-for-loop.png)

for 循环的各个部分：

#### 1. 初始化表达式

在此表达式中，需要将循环变量初始化为某个值。

#### 2. 测试条件

在此表达式中，需要测试循环条件。如果条件为真，则执行循环体并继续到更新表达式；否则，退出 for 循环。

#### 3. 更新表达式

在执行循环体后，该表达式将循环变量增加或减少一定的值。

## for 循环的流程图

![flowchart of for loop in C++](https://media.geeksforgeeks.org/wp-content/uploads/20221220175422/for_loop_in_cpp.png)

# C++ 中的 for 循环

在 C++ 中，for 循环是一种**入口控制循环**，用于对指定范围内的值重复执行一段代码。基本上，for 循环允许你在特定次数内重复执行一组指令。

当迭代次数预先已知时，for 循环通常优于 while 和 do-while 循环。

## **for 循环的语法**

C++ 中 for 循环的语法如下：

```cpp
for ( initialization; test condition; updation) 
{ 
     // for 循环体
}
```

![C++ for 循环语法的分解](https://media.geeksforgeeks.org/wp-content/uploads/20231221155254/cpp-for-loop.png)

### for 循环的各个部分：

#### 1. 初始化表达式

在此表达式中，需要将循环变量初始化为某个值。

#### 2. 测试条件

在此表达式中，需要测试循环条件。如果条件为真，则执行循环体并继续到更新表达式；否则，退出 for 循环。

#### 3. 更新表达式

在执行循环体后，该表达式将循环变量增加或减少一定的值。

## **for 循环的流程图**

![C++ 中 for 循环的流程图](https://media.geeksforgeeks.org/wp-content/uploads/20221220175422/for_loop_in_cpp.png)

### for 循环的执行流程：

- 控制权进入 for 循环，进行初始化。

- 流程跳转到条件部分。

- 测试条件：

  ​	如果条件为真，流程进入循环体。

  ​	如果条件为假，流程跳出循环。

- 执行循环体内的语句。

- 流程跳转到更新部分。

- 更新循环变量并重复步骤 3。

- 当循环结束，流程跳出循环。

## C++ for 循环示例

### 示例 1

以下示例展示了在 C++ 程序中使用 for 循环打印从 1 到 n 的数字。

- C++

```
// C++ program to illustrate for loop to print numbers from 
// 1 to n 

#include <iostream> 
using namespace std; 

int main() 
{ 
	// initializing n (value upto which you want to print 
	// numbers 
	int n = 5; 
	int i; // initialization of loop variable 
	for (i = 1; i <= n; i++) { 
		cout << i << " "; 
	} 

	return 0; 
}

```

**输出**

```
1 2 3 4 5 
```

**解释**

该程序使用 for 循环打印从 1 到 n（这里 n=5）。循环变量 i 从 1 迭代到 n，每次迭代时都会检查条件（i <= n），如果为真，则打印 i 的值并递增 i。当条件为假时，循环终止。

### 示例 2

该示例展示了如何使用 for 循环以逆序打印从 n 到 1 的数字。

- C++

```
// C++ program to illustrate for loop to print numbers from 
// n to 1 (reverse counting). 

#include <iostream> 
using namespace std; 

int main() 
{ 
	// initializing n (value upto which you want to print 
	// numbers 
	int n = 5; 
	int i; // initialization of loop variable 
	for (i = n; i >= 1; i--) { 
		cout << i << " "; 
	} 

	return 0; 
}

```

**输出**

```
5 4 3 2 1 
```

**解释**
该程序使用 for 循环从 n 到 1（这里 n=5）打印数字。循环变量 i 从 n 递减到 1，每次迭代时检查条件（i >= 1），如果为真，则打印 i 的值并递减 i。当条件为假时，循环终止。

## C++ 嵌套 for 循环

嵌套 for 循环是指一个循环嵌套在另一个循环内。每次外部循环执行时，内部循环都会完整执行一次。

### 嵌套 for 循环示例

以下示例展示了如何在 C++ 程序中使用嵌套 for 循环。

- C++

```
// C++ program to demonstrate the use of Nested for loop. 

#include <iostream> 
using namespace std; 

int main() 
{ 
	// Outer loop 
	for (int i = 0; i < 4; i++) { 

		// Inner loop 
		for (int j = 0; j < 4; j++) { 

			// Printing the value of i and j 
			cout << "*"
				<< " "; 
		} 
		cout << endl; 
	} 
}

```

**输出**

```
* * * * 
* * * * 
* * * * 
* * * * 
```

**解释**

该程序使用嵌套 for 循环打印一个 4x4 的星号矩阵。外部循环迭代行数，内部循环迭代列数。每次内部循环打印一个星号和一个空格，外部循环每次迭代后打印换行符。

## 在 for 循环中使用多个变量

在 for 循环中，我们可以同时初始化、测试和更新多个变量。

### 使用多个变量的 for 循环示例

以下示例演示了如何在 C++ 程序中使用多个变量的 for 循环。

- C++

```
// C++ program to demonstrate the use of multiple variables 
// in for loops 

#include <iostream> 
using namespace std; 

int main() 
{ 
	// initializing loop variable 
	int m, n; 

	// loop having multiple variable and updations 
	for (m = 1, n = 1; m <= 5; m += 1, n += 2) { 
		cout << "iteration " << m << endl; 
		cout << "m is: " << m << endl; 
		cout << "j is: " << n << endl; 
	} 

	return 0; 
}

```

**输出**

```
iteration 1
m is: 1
j is: 1
iteration 2
m is: 2
j is: 3
iteration 3
m is: 3
j is: 5
iteration 4
m is: 4
j is: 7
iteration 5
m is: 5
j is: 9
```

**解释**
上面的程序使用了 for 循环中的多个变量（这里是 m 和 n）。每次迭代时，循环会同时更新两个变量，并输出它们的当前值。

## C++ 无限 for 循环

当 for 循环没有给定任何参数时，它会因为缺少输入条件而不断重复，形成一种无限循环。

### 无限 for 循环的示例

以下示例演示了如何在 C++ 程序中实现无限循环。

- C++

```
// C++ Program to demonstrate infinite loop 

#include <iostream> 
using namespace std; 

int main() 
{ 
	// skip Initialization, test and update conditions 
	for (;;) { 
		cout << "gfg" << endl; 
	} 
	// Return statement to show program compiles 
	// successfully safely 
	return 0; 
}

```

**Output**

```
gfg
gfg
.
.
.
infinite times
```

## C++ 中的范围基 for 循环

C++ 中的[**范围基**](https://www.geeksforgeeks.org/range-based-loop-c/) for 循环在一组范围内执行循环，例如遍历容器中的所有元素，比传统的 for 循环更具可读性。

**语法：**

```
for ( range_declaration : range_expression )     {        
// loop_statements here
  }
```

- **range_declaration**：声明一个变量，该变量将获取给定范围表达式中的每个元素的值。
- **range_expression**：表示循环要遍历的范围。

### 范围基 for 循环示例

以下示例演示了如何在 C++ 程序中使用范围基 for 循环。

- C++

```
// C++ Program to demonstrate the use of range based for 
// loop in C++ 
#include <iostream> 
#include <vector> 
using namespace std; 

int main() 
{ 
	int arr[] = { 10, 20, 30, 40, 50 }; 

	cout << "Printing array elements: " << endl; 
	// range based for loop 
	for (int& val : arr) { 
		cout << val << " "; 
	} 
	cout << endl; 

	cout << "Printing vector elements: " << endl; 
	vector<int> v = { 10, 20, 30, 40, 50 }; 

	// range-based for loop for vector 
	for (auto& it : v) { 
		cout << it << " "; 
	} 
	cout << endl; 

	return 0; 
}

```

**输出**

```
Printing array elements: 
10 20 30 40 50 
Printing vector elements: 
10 20 30 40 50 
```

**解释**
上述程序展示了范围基 for 循环的使用。它遍历数组（arr）和向量（v）中的每个元素，并打印它们的值。

## 在 for 循环中使用多个变量

在 for 循环中，我们可以同时初始化、测试和更新多个变量。

### 使用多个变量的 for 循环示例

以下示例演示了如何在 C++ 程序中使用多个变量的 for 循环。

- C++

```cpp
// 演示在 for 循环中使用多个变量
#include <iostream>
using namespace std;

int main() {
  // 初始化循环变量
  int m, n;

  // for 循环中同时初始化多个变量并更新它们
  for (m = 1, n = 1; m <= 5; m += 1, n += 2) {
    cout << "iteration " << m << endl;
    cout << "m is: " << m << endl;
    cout << "n is: " << n << endl;
  }
  return 0;
}
```

**输出**

```
iteration 1
m is: 1
n is: 1
iteration 2
m is: 2
n is: 3
iteration 3
m is: 3
n is: 5
iteration 4
m is: 4
n is: 7
iteration 5
m is: 5
n is: 9
```

**解释** 上面的程序使用了 for 循环中的多个变量（这里是 m 和 n）。每次迭代时，循环会同时更新两个变量，并输出它们的当前值。

------

## C++ 无限 for 循环

当 for 循环没有给定任何参数时，它会因为缺少输入条件而不断重复，形成一种无限循环。

### 无限 for 循环的示例

以下示例演示了如何在 C++ 程序中实现无限循环。

- C++

```cpp
// 演示无限循环的 C++ 程序
#include <iostream>
using namespace std;

int main() {
  // 跳过初始化、测试和更新条件
  for (;;) {
    cout << "gfg" << endl;
  }

  // 返回语句以确保程序编译成功
  return 0;
}
```

**输出**

```
gfg
gfg
.
.
.
无限次
```

------

## C++ 中的范围基 for 循环

C++ 中的[**范围基**](https://www.geeksforgeeks.org/range-based-loop-c/) for 循环在一组范围内执行循环，例如遍历容器中的所有元素，比传统的 for 循环更具可读性。

**语法：**

```cpp
for ( range_declaration : range_expression ) {
  // 在此处编写循环语句
}
```

- **range_declaration**：声明一个变量，该变量将获取给定范围表达式中的每个元素的值。
- **range_expression**：表示循环要遍历的范围。

### 范围基 for 循环示例

以下示例演示了如何在 C++ 程序中使用范围基 for 循环。

- C++

```cpp
// 演示 C++ 中范围基 for 循环的程序
#include <iostream>
#include <vector>
using namespace std;

int main() {
  int arr[] = { 10, 20, 30, 40, 50 };
  cout << "打印数组元素：" << endl;
  
  // 范围基 for 循环
  for (int& val : arr) {
    cout << val << " ";
  }
  cout << endl;

  cout << "打印向量元素：" << endl;
  vector<int> v = { 10, 20, 30, 40, 50 };

  // 向量的范围基 for 循环
  for (auto& it : v) {
    cout << it << " ";
  }
  cout << endl;

  return 0;
}
```

**输出**

```
打印数组元素： 
10 20 30 40 50 
打印向量元素： 
10 20 30 40 50 
```

**解释：** 上述程序展示了范围基 for 循环的使用。它遍历数组（arr）和向量（v）中的每个元素，并打印它们的值。

------

## C++ 中的 for_each 循环

C++ 中的 [**for_each**](https://www.geeksforgeeks.org/for_each-loop-c/) 循环接受一个函数，并对每个容器元素执行该函数。

这个循环定义在头文件 **<algorithm>** 中，因此需要包含该头文件才能成功使用该循环。

### for_each 循环的语法

```
for_each ( InputIterator start_iter, InputIterator last_iter, Function fnc);
```

### **参数**

- **start_iter**：迭代器，指向函数操作的开始位置。
- **last_iter**：迭代器，指向函数操作的结束位置。
- **fnc**：第三个参数是一个函数或函数对象，该函数将对每个元素执行操作。

### for_each 循环的示例

以下示例演示了如何在 C++ 程序中使用 for_each 循环。

- C++

```
// C++ Program to show use of for_each loop 

#include <bits/stdc++.h> 
using namespace std; 

// function to print values passed as parameter in loop 
void printValues(int i) { cout << i << " " << endl; } 

int main() 
{ 
	// initializing vector 
	vector<int> v = { 1, 2, 3, 4, 5 }; 

	// iterating using for_each loop 
	for_each(v.begin(), v.end(), printValues); 

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

**解释**
该程序使用 for_each 循环遍历向量中的每个元素，并调用 `printValues` 函数来打印每个元素。每次迭代的输出显示在新的一行。