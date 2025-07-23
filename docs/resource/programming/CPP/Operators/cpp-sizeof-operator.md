---
comments: true
---

# C++ sizeof 运算符

sizeof 运算符是一个一元编译时运算符，用于在编译时确定变量、数据类型和常量的大小（以字节为单位）。它还可以确定类、结构和联合的大小。

**语法**：

```C++
 sizeof （数据类型）
     
 或
     
 sizeof （表达式）
```



### 示例 1：不同数据类型占用的字节数。

下面是 C++ 程序，用于实现 sizeof 运算符来确定不同数据类型所占用的字节数：

```C++
// C++ program to implement sizeof 
// to determine the number of bytes 
// taken by different data types 
#include <bits/stdc++.h> 
using namespace std; 
  
// Driver code 
int main()  
{   
  cout << "No of Bytes taken up by char is " << 
           sizeof(char) << endl; 
  cout << "No of Bytes taken up by int is " <<  
           sizeof(int) << endl; 
  cout << "No of Bytes taken up by float is " << 
           sizeof(float) << endl; 
  cout << "No of Bytes taken up by double is " << 
           sizeof(double) << endl; 
  cout << "No of Bytes taken up by long is " <<  
           sizeof(long) << endl; 
}
```

**输出**

```C++
No of Bytes taken up by char is 1
No of Bytes taken up by int is 4
No of Bytes taken up by float is 4
No of Bytes taken up by double is 8
No of Bytes taken up by long is 8
```



### 示例 2：不同数据类型的变量占用的字节数。

下面是实现 sizeof 的 C++ 程序，用于确定不同数据类型的变量所占用的字节数：

```C++
// C++ program to implement sizeof 
// to determine the number of bytes  
// taken by variables of different 
// data types 
#include <bits/stdc++.h> 
using namespace std; 
  
// Driver code 
int main()  
{ 
  int a; 
  float b; 
  char g; 
  cout << "No of Bytes taken up by a is " << 
           sizeof(a) << endl; 
  cout << "No of Bytes taken up by b is " <<  
           sizeof(b) << endl; 
  cout << "No of Bytes taken up by g is " <<  
           sizeof(g) << endl; 
  return 0; 
}
```

**输出**

```C++
No of Bytes taken up by a is 4
No of Bytes taken up by b is 4
No of Bytes taken up by g is 1
```



### 示例 3：表达式占用的字节数。

下面是实现 sizeof 以确定表达式占用的字节数的 C++ 程序：

```C++
// C++ program to implement sizeof  
// to determine the number of bytes  
// taken by an expression: 
#include <bits/stdc++.h> 
using namespace std; 
  
// Driver code 
int main()  
{ 
  int a = 5; 
  long x = 9; 
  double p = 10.2; 
  float g = 2.5; 
        
  cout << "No of Bytes taken up by (a+g) is " << 
           sizeof(a + g) << endl; 
  cout << "No of Bytes taken up by (a+x) is " <<  
           sizeof(a + x) << endl; 
  cout << "No of Bytes taken up by (a+p) is " <<  
           sizeof(a + p) << endl; 
  cout << "No of Bytes taken up by (x+p) is " <<  
           sizeof(x + p) << endl; 
  return 0; 
}
```

**输出**

```C++
No of Bytes taken up by (a+g) is 4
No of Bytes taken up by (a+x) is 8
No of Bytes taken up by (a+p) is 8
No of Bytes taken up by (x+p) is 8
```



### **示例 4：使用 sizeof（） 查找数组的大小。**

下面是实现 sizeof 来确定数组大小的 C++ 程序：

```C++
// C++ program to implement sizeof  
// to determine the size of an array 
#include <bits/stdc++.h> 
using namespace std; 
  
// Driver code 
int main()  
{ 
  int x[] = {1, 2, 3, 5, 6, 7, 8, 9}; 
  int length = sizeof(x) / sizeof(x[0]); 
  cout << "Length of the array is " << 
           length << endl; 
  return 0; 
}
```

**输出**

```C++
Length of the array is 8
```



### 示例 5：查找类的大小。

下面是实现 sizeof 以查找类大小的 C++ 程序：

```C++
// C++ program to implement sizeof  
// to find the size of the class 
#include <bits/stdc++.h> 
using namespace std; 
  
class GFG 
{   
  int x;   
}; 
  
// Driver code 
int main()   
{   
  GFG g;   
  cout << "Size of class gfg is in bytes  : " << 
           sizeof(g) << endl;   
  return 0;   
}
```

**输出**

```C++
Size of class gfg is in bytes  : 4
```



### **示例 6：查找指针的大小。**

下面是 C++ 程序实现 sizeof 来查找指针的大小：

```C++
// C++ program to implement sizeof  
// to find the size of pointers 
#include <bits/stdc++.h> 
using namespace std; 
    
// Driver code 
int main()   
{   
  int *a = new int(10); 
  char *g = new char('g'); 
  double *d = new double(7.5); 
  cout << "size of pointer a is " <<  
           sizeof(a) << endl; 
  cout << "size of pointer *a is " << 
           sizeof(*a) << endl; 
  cout << "size of pointer g is " <<  
           sizeof(g) << endl; 
  cout << "size of pointer *g is " <<  
           sizeof(*g) << endl; 
  cout << "size of pointer d is " <<  
           sizeof(d) << endl; 
  cout << "size of pointer *d is " <<  
           sizeof(*d) << endl; 
  return 0;   
}
```

**输出**

```C++
size of pointer a is 8
size of pointer *a is 4
size of pointer g is 8
size of pointer *g is 1
size of pointer d is 8
size of pointer *d is 8
```



### 示例 7：sizeof（） 运算符的嵌套。

下面是显示 sizeof 运算符嵌套的 C++ 程序：

```C++
// C++ program to show the  
// nesting of sizeof operator 
#include <bits/stdc++.h> 
using namespace std; 
  
// Driver code 
int main()  
{ 
  int x; 
  double y; 
  cout << "Nesting of sizeof operator is implemented " <<  
          "as sizeof(x*sizeof(y)) :" <<  
           sizeof(x * sizeof(y)) << endl; 
  return 0; 
}
```

**输出**

```C++
Nesting of sizeof operator is implemented as sizeof(x*sizeof(y)) :8
```



### 示例 8：查找结构体的大小。

下面是 C++ 程序实现 sizeof 运算符来查找结构体的大小：

```C++
// C++ program to implement the  
// sizeof operator to find the  
// size of structure 
#include <bits/stdc++.h> 
using namespace std; 
  
struct gfg 
{ 
  int z; 
  float d; 
  char s[20]; 
}g; 
  
// Driver code 
int main()  
{ 
  cout << "size of structure is " <<  
           sizeof(g) << endl; 
  return 0; 
}
```

**输出**

```C++
size of structure is 28
```



### 示例 9：查找联合体的大小。

下面是 C++ 程序实现 sizeof 运算符来查找联合体的大小：

```C++
// C++ program to implement the  
// sizeof operator to find the  
// size of the union 
#include <bits/stdc++.h> 
using namespace std; 
  
union gfg 
{ 
  int z; 
  double d; 
}g; 
  
// Driver code 
int main()  
{ 
  cout << "size of union is " << 
           sizeof(g) << endl; 
  return 0; 
}
```

**输出**

```C++
size of union is 8
```



夏天来了，也是提高技能的时候了！超过 5,000 名学习者现在已经完成了从 **DSA 基础知识到高级开发计划**（如全栈、后端开发、数据科学）的旅程。

当我们的 [DSA to Development： Coding Guide](https://gfgcdn.com/tu/Q8V/) 将帮助您在几个月内掌握所有这些时，为什么还要去其他任何地方呢！现在就申请我们的[DSA发展计划](https://gfgcdn.com/tu/Q8V/)，我们的顾问将与您联系以获得进一步的指导和支持。
