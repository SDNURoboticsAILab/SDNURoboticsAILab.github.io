# C++中的默认参数

默认参数是在函数声明中提供的一个值，如果调用函数没有为该参数提供值，编译器会自动分配该值。如果传递了任何值，默认值将被覆盖。

1）以下是一个简单的C++示例，演示了默认参数的使用。在这里，我们不需要编写3个求和函数；只需使用默认值为第3个和第4个参数的一个函数即可。

```c
// CPP Program to demonstrate Default Arguments
#include <iostream>
using namespace std;
 
// A function with default arguments,
// it can be called with
// 2 arguments or 3 arguments or 4 arguments.
int sum(int x, int y, int z = 0, int w = 0) //assigning default values to z,w as 0
{
    return (x + y + z + w);
}
 
// Driver Code
int main()
{
    // Statement 1
    cout << sum(10, 15) << endl;
   
    // Statement 2
    cout << sum(10, 15, 25) << endl;
   
    // Statement 3
    cout << sum(10, 15, 25, 30) << endl;
    return 0;
}
```

**输出**

```
25
50
80
```

**时间复杂度:** O(1)

**空间复杂度:** O(1)

**解释：**在语句1中，只传递了两个值，因此变量z和w取默认值0。在语句2中，传递了三个值，因此z的值被25覆盖。在语句3中，传递了四个值，因此z和w的值分别被25和30覆盖。

**2）**如果函数重载包含默认参数，我们需要确保它不会让编译器产生歧义，否则它会抛出错误。以下是上述程序的修改版本：

```cpp
// CPP Program to demonstrate Function overloading in
// Default Arguments
#include <iostream>
using namespace std;
 
// A function with default arguments, it can be called with
// 2 arguments or 3 arguments or 4 arguments.
int sum(int x, int y, int z = 0, int w = 0)
{
    return (x + y + z + w);
}
int sum(int x, int y, float z = 0, float w = 0)
{
    return (x + y + z + w);
}
// Driver Code
int main()
{
    cout << sum(10, 15) << endl;
    cout << sum(10, 15, 25) << endl;
    cout << sum(10, 15, 25, 30) << endl;
    return 0;
}
```

**错误：**

```
prog.cpp: In function 'int main()':
prog.cpp:17:20: error: call of overloaded 
'sum(int, int)' is ambiguous
  cout << sum(10, 15) << endl; 
                    ^
prog.cpp:6:5: note: candidate: 
int sum(int, int, int, int)
 int sum(int x, int y, int z=0, int w=0) 
     ^
prog.cpp:10:5: note: candidate: 
int sum(int, int, float, float)
 int sum(int x, int y, float z=0, float w=0) 
     ^
```

**3）**构造函数也可以包含默认参数。默认构造函数可以没有参数，也可以有带默认参数的参数。

```cpp
// CPP code to demonstrate use of default arguments in
// Constructors
 
#include <iostream>
using namespace std;
 
class A {
    private:
        int var = 0;
    public:
        A(int x = 0): var(x){}; // default constructor with one argument
                                  // Note that var(x) is the syntax in c++ to do : "var = x"
        void setVar(int s){
            var = s; // OR => this->var = s;
            return;
        }
        int getVar(){
            return var; // OR => return this->var;
        }
};
int main(){
    A a(1);
 
    a.setVar(2);
 
    cout << "var = " << a.getVar() << endl;
     
    /* ANOTHER APPROACH:
    A *a = new A(1);
 
    a->setVar(2);
 
    cout << "var = " << a->getVar() << endl;
    */
}
 
// contributed by Francisco Vargas #pt
```

**解释：**在这里，我们看到一个没有参数的默认构造函数和一个带有一个默认参数的默认构造函数。带参数的默认构造函数的参数x被赋值为0。

**关键点:** 

- 默认参数不同于常量参数，因为常量参数不能更改，而默认参数可以根据需要被覆盖。
- 如果调用函数为它们提供值，默认参数将被覆盖。例如，调用函数sum(10, 15, 25, 30)将z和w的值分别覆盖为25和30。
- 当调用函数时，参数从调用函数按从左到右的顺序复制到被调用函数。因此，sum(10, 15, 25)将分别将10、15和25赋值给x、y和z，这意味着只使用w的默认值。
- 一旦在函数定义中为参数使用了默认值，所有后续参数也必须有默认值。也可以说默认参数是从右到左分配的。例如，以下函数定义是无效的，因为默认变量z的后续参数不是默认的。

```
// Invalid because z has default value, but w after it doesn't have a default value
int sum(int x, int y, int z = 0, int w).
```

**默认参数的优点:**

- 默认参数在希望增加现有函数的功能时非常有用，因为只需向函数添加另一个默认参数即可。
- 它有助于减少程序的大小。
- 它提供了一种简单而有效的编程方法。
- 默认参数提高了程序的一致性。

**默认参数的缺点**

- 它增加了执行时间，因为编译器需要在函数调用中将省略的参数替换为其默认值。