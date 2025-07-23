---
comments: true
---

Bash 脚本编程入门
=====

> 初学者们，让我们在这个大型的教程中来认识一下 Bash 脚本编程。

Shell 是 Linux 的核心部分，它允许你使用各种诸如 `cd`、`ls`、`cat` 等的命令与 Linux 内核进行交互。

Bash 是 Linux 上众多可用的 Shell 中的一个。这些 Shell 主要的语法基本相同，但并非完全一样。Bash 是目前最受欢迎的 Shell，并在大多数 Linux 发行版中被设为默认 Shell。

当你打开一个终端或 SSH 会话时，即使你无法真切地看到它，你其实已经在运行着一个 Shell。

当你输入一个命令，它会被 Shell 解释。如果命令和语法是正确的，它就会被执行，否则你会看到一个错误。

## 当你可以直接运行 Linux 命令时，为什么还需要 Bash 脚本？

你可以直接在终端输入命令，它们就会被执行。

```Bash
$ echo "hello world"
hello world
```

并且，同样的操作也可以在脚本中进行：

```Bash
$ cat >> script.sh
#!/bin/bash

echo "hello world"
$ bash script.sh
hello world
```

那么，为什么我们需要 Shell 脚本呢？因为你不必一遍又一遍地输入同一个命令，你只需运行 Shell 脚本即可。

此外，如果你的脚本中有复杂的逻辑，把所有的命令都输入到终端中可能并不是一个好主意。

例如，如果你输入下面的命令，它会奏效，但这并不容易理解。不断地输入相同的命令（甚至要在 Bash 历史记录中搜索）会造成困扰。

```Bash
if [ $(whoami) = 'root' ]; then echo "root"; else echo "not root"; fi
```

相反，你可以把命令放进 shell 脚本中，这样就更容易理解并且可以轻松运行了：

```Bash
#!/bin/bash

if [ $(whoami) = 'root' ]; then
    echo "You are root"
else
    echo "You are not root"
fi
```

这还是比较简单的情况。尝试想象一下，一个复杂的脚本可能有五十行或一百行！

## 你将会学到什么？

在这个 Bash 脚本教程中，有九个部分。你将会学到：

* 创建并运行你的第一个 Bash Shell 脚本
* 使用变量
* 在你的 Bash 脚本中传递参数和接受用户输入
* 进行数学计算
* 操作字符串
* 使用条件语句，例如 `if-else`
* 使用 `for`、`while` 和 `until` 循环
* 创建函数

> 💡 所有的部分都会给你一个简单的例子。如果你愿意，你可以通过访问每个部分的详细章节来更深入地学习。这些章节也都包含了实践练习。

## 这个教程的目标读者是谁？

这个教程适合任何想要开始学习 Bash Shell 脚本的人。

如果你是一名学生，而你的课程里包括了 Shell 脚本，那么这个系列就是为你准备的。

如果你是一个常规的桌面 Linux 用户，这个系列将会帮助你理解在探索各种软件和修复问题时遇到的大多数 Shell 脚本。你也可以使用它来自动化一些常见的、重复的任务。

在这个 Bash 脚本教程结束时，你应该可以编写简单的 Bash 脚本。

> 🚧 希望你已经拥有 Linux 命令行和编程语言的基础知识。

如果你对 Linux 命令行完全不熟悉，我建议你先掌握基础知识。

> **[19 个你应该知道的基础而重要的 Linux 终端技巧](https://itsfoss.com/basic-terminal-tips-ubuntu/)**

你应该了解如何在命令行中进入特定的位置。为了做到这一点，你需要理解 Linux 文件系统中的路径是如何工作的。

> **[Linux 中的绝对路径和相对路径有什么不同](https://linuxhandbook.com/absolute-vs-relative-path/)**

接下来，这个教程系列会给你介绍目录导航和文件操作的基本知识。

> **[终端基础：Linux 终端入门](https://linux.net.cn/article-16104-1.html)**

## 1、编写你的第一个 Bash Shell 脚本

创建一个名为 `hello.sh` 的新文件：

```Bash
nano hello.sh
```

这将在终端中打开 nano 编辑器。在其中输入以下几行代码：

```Bash
#!/bin/bash
echo "Hello World"
```

通过按 `Ctrl+X` 键可以保存并退出 nano 编辑器。

现在，你可以以以下方式运行 Bash Shell 脚本：

```Bash
bash hello.sh
```

你应该可以看到以下的输出：

```Bash
Hello World
```

另一种方式是首先赋予脚本执行权限：

```Bash
chmod u+x hello.sh
```

然后这样运行它：

```Bash
./hello.sh
```

> 💡 你也可以使用基于图形用户界面的文本编辑器来编写脚本。这可能更适合编写较长的脚本。然而，你需要切换到保存脚本的目录中才能运行它。

恭喜！你刚刚运行了你的第一个 Bash 脚本。

> **[Bash 基础知识系列 #1：创建并运行你的第一个 Bash Shell 脚本](https://linux.net.cn/article-15921-1.html)**

## 2、在 Bash 脚本中使用变量

变量的声明方式如下：

```Bash
var=some_value
```

然后可以像这样访问变量：

```Bash
$var
```

> 🚧 在声明变量时，等号（`=`）前后不能有空格。

我们通过添加一个变量来修改前面的脚本。

```Bash
#!/bin/bash
message="Hello World"
echo $message
```

如果运行这个脚本，输出仍然会保持不变。

```Bash
Hello World
```

> **[Bash 基础知识系列 #2：在 Bash 中使用变量](https://linux.net.cn/article-15991-1.html)**

## 3、向 Bash 脚本传递参数

你可以在运行 Bash 脚本时以以下方式传递参数：

```Bash
./my_script.sh arg1 arg2
```

在脚本中，你可以使用 `$1` 来代表第 1 个参数，用 `$2` 来代表第 2 个参数，以此类推。`$0` 是一个特殊变量，它代表正在运行的脚本的名字。

现在，创建一个新的 shell 脚本，命名为 `arguments.sh`，并向其中添加以下几行代码：

```Bash
#!/bin/bash

echo "Script name is: $0"
echo "First argument is: $1"
echo "Second argument is: $2"
```

使其可执行并像这样运行它：

```Bash
$ ./argument.sh abhishek prakash
Script name is: ./argument.sh
First argument is: abhishek
Second argument is: prakash
```

让我们快速看一下特殊变量：

特殊变量 | 描述
---|---
`$0` | 脚本名称
`$1`、`$2`...`$9` | 脚本参数
`${n}` | 10 到 255 的脚本参数
`$#` | 参数数量
`$@` | 所有参数一起
`$$` | 当前 shell 的进程 id
`$!` | 最后执行命令的进程 id
`$?` | 最后执行命令的退出状态

你也可以通过接受键盘输入使你的 Bash 脚本变得交互式。

为此，你必须使用 `read` 命令。你还可以使用 `read -p` 命令提示用户进行键盘输入，而不需要 `echo` 命令。

```Bash
#!/bin/bash

echo "What is your name, stranger?"
read name
read -p "What's your full name, $name? " full_name
echo "Welcome, $full_name"
```

现在，如果你运行这个脚本，当系统提示你输入“参数”时，你必须输入。

```Bash
$ ./argument.sh
What is your name, stranger?
abhishek
What's your full name, abhishek? abhishek prakash
Welcome, abhishek prakash
```

> **[Bash 基础知识系列 #3：传递参数和接受用户输入](https://linux.net.cn/article-16001-1.html)**

## 4、执行算术运算

在 Bash Shell 中执行算术运算的语法是这样的：

```Bash
$((arithmetic_operation))
```

下面是你可以在 Bash 中执行的算术运算的列表：

操作符 | 描述
---|---
`+` | 加法
`-` | 减法
`*` | 乘法
`/` | 整数除法（没有小数）
`%` | 模运算（只余）
`**` | 指数（a 的 b 次方）

以下是在 Bash 脚本中进行加法和减法的示例：

```Bash
#!/bin/bash

read -p "Enter first number: " num1
read -p "Enter second number: " num2

sum=$(($num1+$num2))
sub=$(($num1-$num2))
echo "The summation of $num1 and $num2 is $sum"
echo "The substraction of $num2 from $num1 is $sub"
```

你可以执行 Shell 脚本，使用你选择的任意数字作为参数。

如果你尝试除法，会出现一个大问题。Bash 只使用整数。默认情况下，它没有小数的概念。因此，你会得到 10/3 的结果为3，而不是 3.333。

对于浮点数运算，你需要这样使用 `bc` 命令：

```Bash
#!/bin/bash

num1=50
num2=6

result=$(echo "$num1/$num2" | bc -l)

echo "The result is $result"
```

这个时候，你将看到准确的结果。

```Bash

    The result is 8.33333333333333333333

```

> **[Bash 基础知识系列 #4：算术运算](https://linux.net.cn/article-16006-1.html)**

## 5、在 Bash 脚本中使用数组

你可以使用 Bash 中的数组来存储同一类别的值，而不是使用多个变量。

你可以像这样声明一个数组：

```Bash
distros=(Ubuntu Fedora SUSE "Arch Linux" Nix)
```

要访问一个元素，使用：

```Bash
${array_name[N]}
```

像大多数其他的编程语言一样，数组的索引从 0 开始。

你可以像这样显示数组的所有元素：

```Bash
${array[*]}
```

这样获取数组长度：

```Bash
${#array_name[@]}
```

> **[Bash 基础知识系列 #5：在 Bash 中使用数组](https://linux.net.cn/article-16016-1.html)**

## 6、Bash 中的基础字符串操作

Bash 能够执行许多字符串操作。

你可以使用这种方式获取字符串长度：

```Bash
${#string}
```

连接两个字符串：

```Bash
str3=$str1$str2
```

提供子字符串的起始位置和长度来提取子字符串：

```Bash
${string:$pos:$len}
```

你也可以替换给定字符串的一部分：

```Bash

${string/substr1/substr2}

```

并且你也可以从给定字符串中删除一个子字符串：
```Bash

    ${string/substring}

```

> **[Bash 基础知识系列 #6：处理字符串操作](https://linux.net.cn/article-16047-1.html)**

## 7、在 Bash 中使用条件语句

你可以通过使用 `if` 或 `if-else` 语句为你的 Bash 脚本添加条件逻辑。这些语句以 `fi` 结束。

单个 `if` 语句的语法是：

```Bash
if [ condition ]; then
  your code
fi
```

注意使用 `[ ... ];` 和 `then` 。

`if-else` 语句的语法是：

```Bash
if [ expression ]; then
    # execute this block if condition is true else go to next
elif [ expression ]; then
    # execute this block if condition is true else go to next
else
    # if none of the above conditions are true, execute this block
fi
```

这里有一个使用 `if-else` 语句的 Bash 脚本示例：

```Bash
#!/bin/bash

read -p "Enter the number: " num
mod=$(($num%2))

if [ $mod -eq 0 ]; then
    echo "Number $num is even"
else
    echo "Number $num is odd"
fi
```

`-eq` 被称为测试条件或条件操作符。有许多这样的操作符可以给你不同类型的比较：

这些是你可以用来进行数值比较的测试条件操作符：

条件 | 当...时，等同于 true
---|---
`$a -lt $b` | `$a < $b` （`$a` 是小于 `$b`） 
`$a -gt $b` | `$a > $b` （`$a` 是大于 `$b`）
`$a -le $b` | `$a <= $b` （`$a` 是小于或等于 `$b`） 
`$a -ge $b` | `$a >= $b` （`$a` 是大于或等于 `$b`）
`$a -eq $b` | `$a == $b` （`$a` 等于 `$b`）
`$a -ne $b` | `$a != $b` （`$a` 不等于 `$b`）

如果你在进行字符串比较，你可以使用以下这些测试条件：

条件 | 当...时，等同于 true
---|---
`"$a" = "$b"` | `$a` 等同于 `$b`
`"$a" == "$b"` | `$a` 等同于 `$b`
`"$a" != "$b"` | `$a` 不同于 `$b`
`-z "$a"` | `$a` 是空的

还有些条件用于检查文件类型：

条件 | 当...时，等同于 true
---|---
`-f $a` | `$a` 是一个文件
`-d $a` | `$a` 是一个目录
`-L $a` | `$a` 是一个链接

> 🚧 要特别注意空格。开括号和闭括号、条件之间必须有空格。同样地，条件操作符（`-le`、`==` 等）之前和之后必须有空格。

> **[Bash 基础知识系列 #7：If-Else 语句](https://linux.net.cn/article-16083-1.html)**

## 8、使用 Bash 脚本中的循环

Bash 支持三种类型的循环：`for`、`while` 和 `until`。

这是 `for` 循环的一个例子：

```Bash
#!/bin/bash

for num in {1..10}; do
    echo $num
done
```

运行它，你将看到以下输出：
```Bash
1
2
3
4
5
6
7
8
9
10
```

如果你选择使用上面的示例，可以使用 `while` 循环这样重写：

```Bash
#!/bin/bash

num=1
while [ $num -le 10 ]; do
    echo $num
    num=$(($num+1))
done
```

同样，可以使用 `until` 循环来重写：

```Bash
#!/bin/bash

num=1
until [ $num -gt 10 ]; do
    echo $num
    num=$(($num+1))
done
```

> 💡 `while` 循环和 `until` 循环非常相似。区别在于：`while` 循环在条件为真时运行，而 `until` 循环在条件为假时运行。

> **[Bash 基础知识系列 #8：For、While 和 Until 循环](https://linux.net.cn/article-16114-1.html)**

## 9、在 Bash 脚本中使用函数

Bash Shell 支持使用函数，这样你不必反复编写相同的代码片段。

这是声明 Bash 函数的通用语法：

```Bash
function_name() {
  commands
}
```

这是一个使用带参数的函数的 Bash 脚本样例：

```Bash
#!/bin/bash

sum() {
    sum=$(($1+$2))
    echo "The sum of $1 and $2 is: $sum"
}

echo "Let's use the sum function"
sum 1 5
```

如果你运行该脚本，你将看到以下输出：

```Bash
Let's use the sum function
The sum of 1 and 5 is: 6
```

> **[Bash 基础知识系列 #9：Bash 中的函数](https://linux.net.cn/article-16116-1.html)**

## 接下来呢？

这只是一个初窥。这个 Bash 脚本教程只是一篇引言。Bash 脚本的内容还有很多，你可以慢慢地、逐渐地探索。

GNU Bash 参考是一份优秀的在线资源，可以解答你的 Bash 疑问。

> **[GNU Bash 参考](https://www.gnu.org/software/bash/manual/bash.html)**

除此之外，你可以下载这本免费书籍来学习更多在此未涵盖的 Bash 内容：

> **[下载 Bash 初学者指南](https://tldp.org/LDP/Bash-Beginners-Guide/Bash-Beginners-Guide.pdf)**

一旦你具有足够的 Bash 基础知识，你可以通过这本免费书籍来学习高级 Bash 脚本：

> **[下载高级 Bash 编程指南](https://tldp.org/LDP/abs/abs-guide.pdf)**

这两本书至少都有十年的历史，但你仍然可以使用它们来学习 Bash。

💬 希望你喜欢这个作为学习 Bash 脚本起点的教程。请在评论区提供你的反馈。


--------------------------------------------------------------------------------
>
>via: https://itsfoss.com/bash-scripting-tutorial/
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