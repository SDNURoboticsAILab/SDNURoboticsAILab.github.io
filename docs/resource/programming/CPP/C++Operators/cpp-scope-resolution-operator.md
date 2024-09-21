---
comments: true
---

C++ 范围解析运算符
=====

在 C++ 中，范围解析运算符为 **::** 。它用于以下目的。

**1） 要在存在同名的局部变量时访问全局变量： **

```C++
// C++ program to show that we can access a global variable
// using scope resolution operator :: when there is a local 
// variable with same name 
#include<iostream> 
using namespace std;

int x; // Global x

int main()
{
int x = 10; // Local x
cout << "Value of global x is " << ::x;
cout << "\nValue of local x is " << x; 
return 0;
}
```

**输出**

```C++
Value of global x is 0
Value of local x is 10
```

**2） 在类外部定义函数:**

```C++
// C++ program to show that scope resolution operator :: is
// used to define a function outside a class
#include <iostream>
using namespace std;

class A {
public:
    // Only declaration
    void fun();
};

// Definition outside class using ::
void A::fun() { cout << "fun() called"; }

int main()
{
    A a;
    a.fun();
    return 0;
}
```

**输出**

```C++
fun() called
```



**3） 访问类的静态变量:**

```C++
// C++ program to show that :: can be used to access static
// members when there is a local variable with same name
#include<iostream>
using namespace std;

class Test
{
    static int x; 
public:
    static int y; 

    // Local parameter 'x' hides class member
    // 'x', but we can access it using ::
    void func(int x) 
    { 
    // We can access class's static variable
    // even if there is a local variable
    cout << "Value of static x is " << Test::x;

    cout << "\nValue of local x is " << x; 
    }
};

// In C++, static members must be explicitly defined 
// like this
int Test::x = 1;
int Test::y = 2;

int main()
{
    Test obj;
    int x = 3 ;
    obj.func(x);

    cout << "\nTest::y = " << Test::y;

    return 0;
}
```

**输出**

```C++
Value of static x is 1
Value of local x is 3
Test::y = 2
```



**4） 在多重继承的情况下：** 如果两个祖先类中存在相同的变量名，我们可以使用范围解析运算符来区分。

```C++
// Use of scope resolution operator in multiple inheritance.
#include<iostream>
using namespace std;

class A
{
protected:
    int x;
public:
    A() { x = 10; }
};

class B
{
protected:
    int x;
public:
    B() { x = 20; }
};

class C: public A, public B
{
public:
void fun()
{
    cout << "A's x is " << A::x;
    cout << "\nB's x is " << B::x;
}
};

int main()
{
    C c;
    c.fun();
    return 0;
}
```

**输出**

```C++
A's x is 10
B's x is 20
```



**5） 对于命名空间**：如果两个命名空间中存在具有相同名称的类，我们可以将命名空间名称与范围解析运算符一起使用来引用该类，而不会发生任何冲突

```C++
#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define nline "\n"

// Global Declarations

string name1 = "GFG";
string favlang = "python";
string companyName = "GFG_2.0";

// You can also do the same thing in classes as we did in
// our struct example

class Developer {
public:
    string name = "krishna";
    string favLang = "c++";
    string company = "GFG";

    // Accessing Global Declarations

    Developer(string favlang, string company)
        : favLang(favlang)
        , company(companyName)
    {
    }
};

int main()
{
    Developer obj = Developer("python", "GFG");
    cout << "favourite Language : " << obj.favLang << endl;
    cout << "company Name : " << obj.company << nline;
}
```

**输出**

```C++
favourite Language : python
company Name : GFG_2.0
```



**6） 在另一个类中引用一个类：**如果一个类存在于另一个类中，我们可以使用嵌套类，通过范围解析运算符来引用嵌套的类

```C++
// Use of scope resolution class inside another class.
#include <iostream>
using namespace std;

class outside {
public:
    int x;
    class inside {
    public:
        int x;
        static int y;
        int foo();
    };
};
int outside::inside::y = 5;

int main()
{
    outside A;
    outside::inside B;
}
```



**7） 在派生对象中引用基类的成员：**在基类和派生类中具有相同的方法的情况下，我们可以通过范围解析运算符来引用每个，如下所示。

```C++
// Refer to a member of the base class in the derived object.
#include <iostream>

class Base {
public:
    void func()
    {
        std::cout << "This is Base class" << std::endl;
    }
};

class Derived : public Base {
public:
    void func()
    {
        std::cout << "This is Derived class" << std::endl;
    }
};

int main()
{
    Derived obj;
    obj.Base::func();
    obj.func();
    return 0;
}
```

**输出**

```C++
This is Base class
This is Derived class
```



夏天来了，也是提高技能的时候了！超过 5,000 名学习者现在已经完成了从 **DSA 基础知识到高级开发计划**（如全栈、后端开发、数据科学）的旅程。

当我们的 [DSA to Development： Coding Guide](https://gfgcdn.com/tu/Q8V/) 将帮助您在几个月内掌握所有这些时，为什么还要去其他任何地方呢！现在就申请我们的[DSA发展计划](https://gfgcdn.com/tu/Q8V/)，我们的顾问将与您联系以获得进一步的指导和支持。
