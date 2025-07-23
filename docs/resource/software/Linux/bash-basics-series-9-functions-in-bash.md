---
comments: true
---

Bash 基础知识系列 #9：Bash 中的函数
======

> 在 Bash 基础系列的最后一章中学习函数的全部知识。

大多数编程语言都支持函数的概念。

函数帮助你避免在同一个程序中反复编写同一段代码。你只需将代码写为一个函数，然后在需要特定代码片段的地方使用这个函数。

在 Bash 基础知识系列的最后一章中，你将学习在 Bash 脚本中使用函数。

## Bash 中的函数

下面是声明 Bash 函数的通用语法：

```Bash
function_name() {
    commands
}
```

只有在 “调用函数” 的脚本中，函数内的命令才会被执行。

这里有一个伪代码来演示这个情况：

```Bash
function_name() {
    commands
}

some_other_commands

# 函数调用
function_name argument;
```

> 🚧 函数定义必须在你调用函数之前。

让我们通过一个简单的例子来看看这个：

```Bash
#!/bin/bash

fun() {
    echo "This is a function"
}

echo "This is a script"
fun
```

当你运行脚本时，你应该看到这样的输出：

```Bash
This is a script
This is a function
```

函数是在没有任何参数的情况下被调用的。接下来，让我们看看在 bash 中如何处理函数的参数。

## 向函数传递参数

向函数传递参数和向 Bash 脚本传递参数是一样的。你在调用函数时，可以在函数名旁边写上参数。

```Bash
function_name argument;
```

让我们用一个例子来看看这个：

```Bash
#!/bin/bash

sum() {
    sum=$(($1+$2))
    echo "The sum of $1 and $2 is: $sum"
}

echo "Let's use the sum function"
sum 1 5
```

如果你运行这个脚本，你会看到以下输出：

```Bash
Let's use the sum function
The sum of 1 and 5 is: 6
```

请记住，传递给脚本的参数和传递给函数的参数是不同的。

在下面的例子中，我在调用函数时交换了参数。

```Bash
#!/bin/bash

arg() {
    echo "1st argument to function is $1 and 2nd is $2"
}

echo "1st argument to script is $1 and 2nd is $2"
arg $2 $1
```

当你运行这个脚本时，你会看到这样的交换：

```Bash
$ ./function.sh abhi shek
1st argument to script is abhi and 2nd is shek
1st argument to function is shek and 2nd is abhi

```

## Bash 中的递归函数

一个递归函数会调用它自己。这就是递归的含义。

递归功能非常强大，可以帮助你编写复杂的程序。

让我们用一个计算阶乘的样本脚本来看看它的应用。如果你忘记了，阶乘的定义是这样的。

n 的阶乘：

```Bash
(n!) = 1 * 2 * 3 * 4 *...  * n
```

所以，5 的阶乘是 1 * 2 * 3 * 4 * 5，计算结果是 120。

这是我用递归计算给定数字的阶乘的脚本。

```Bash
#!/bin/bash

factorial() {

    if [ $1 -gt 1 ]; then
        echo $(( $1 * $(factorial $(( $1 -1 ))) ))
    else
        echo 1
    fi

}

echo -n "Factorial of $1 is: "
factorial $1
```

注意到 `echo $(( $1 * $(factorial $(( $1 -1 ))) ))`，代码使用比输入值小 1 的值调用了函数自身。这个过程会一直持续到值变为 1。所以，如果你运行脚本并输入参数 5，它最终会返回 5 * 4 * 3 * 2 *1 的结果。

```Bash
$ ./factorial.sh 5
Factorial of 5 is: 120
```

非常好。现在，让我们来做些练习吧。

## 🏋️ 练习时间

以下是一些示例编程挑战，用来帮助你实践你所学。

练习 1：写一个 Bash 脚本，使用一个名为 `is_even` 的函数来检查给定的数字是否是偶数。

练习 2：类似的练习，你需要编写一个脚本，该脚本具有一个名为 `is_prime` 的函数，并检查给定数字是否是质数。如果你还不知道，质数只能被 1 和它自身整除。

练习 3：编写一个生成给定数字的斐波那契序列的脚本。序列从 1 开始，脚本必须接受大于 3 的数字。

所以，如果你运行 `fibonacci.sh 5`，它应该输出 “1 1 2 3 5”。

就这些了，伙计们！这是 Bash 基础系列的最后一节。当然，你在这里学到的只是冰山一角；Bash 编程还有更多需要学习的内容。

但是现在，你应该对 Bash Shell 有了一定的理解。你应该能够理解大多数 Bash 脚本，并能编写简单的脚本，即便不能编写复杂的。

如果你想深入学习，没有什么比阅读 GNU Bash 手册更好的了。

> **[GNU Bash 手册](https://www.gnu.org/software/bash/manual/)**

🗨 希望你喜欢这个 Bash 基础知识系列。我们正在创建更多的教程系列，以给你提供更流畅的学习体验。请提供你的反馈，帮助我们帮助其他人学习 Linux。


--------------------------------------------------------------------------------

>via: https://itsfoss.com/bash-function/
>
>作者：[Abhishek Prakash](https://itsfoss.com/author/abhishek/)
>
>选题：[lujun9972](https://github.com/lujun9972)
>
>译者：ChatGPT
>
>校对：[wxy](https://github.com/wxy)
>
>本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.net.cn/) 荣誉推出