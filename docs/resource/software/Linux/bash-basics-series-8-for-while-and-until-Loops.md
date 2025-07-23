---
comments: true
---

Bash 基础知识系列 #8：For、While 和 Until 循环
======

> 在 Bash 基础知识系列的倒数第二章节，学习 `for`、`while` 和 `until` 循环。

循环是任何编程语言中的一个强大功能。如果你还不知道，循环其实是一种根据某些条件重复代码的方式。

例如，想象一下你需要打印从 1 到 10 的数字。你可以使用 `echo` 命令写十次，但那太原始了。你使用一个循环，在 3 到 4 行代码内，就能完成。

这是我能想到的最简单的例子。我将在讨论 Bash 循环时，分享一些实际有用的例子。

在 Bash 中有三种类型的循环：

  * `for`
  * `while`
  * `until`

我将在教程中展示所有三种类型的循环。让我们从最常见的一种开始。

## Bash 中的 For 循环

以下是 Bash 中的 `for` 循环语法：

```Bash
for arg in LIST; do
    commands
done
```

这里的 `LIST` 可能是一个数组或者一个项目列表。[括号扩展](https://linuxhandbook.com/brace-expansion/?ref=itsfoss.com) 也是进行循环的常用手段。

考虑一下我在开始提到的最简单的场景。让我们使用 `for` 循环打印从 1 到 10 的数字：

```Bash
#!/bin/bash

for num in {1..10}; do
    echo $num
done
```

如果你运行它，你应该会看到像这样的输出：

```Bash
$ ./for-loop.sh
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

你也可以使用 `for num in 1 2 3 4 5 6 7 8 9 10; do` ，但是使用括号扩展使得代码看起来更短且更智能。

`{..}` 是用于扩展模式的。你使用 `{d..h}` ，它等同于 `d e f g h` 。关于括号扩展的更多信息，可以在这篇文章中找到。

> **[在 Bash 中使用括号扩展](https://linuxhandbook.com/brace-expansion/?ref=itsfoss.com)**

> 💡 如果你熟悉 C 语言编程，你可能会喜欢在 bash 中使用 C 风格的 for 循环：
>
> ```Bash
> for ((i = 0 ; i < 10 ; i++)); do
>   echo $i
> done
> ```

让我们看另一个例子，显示 [Bash 数组](https://itsfoss.com/bash-arrays/) 的所有内容：

```Bash
#!/bin/bash

distros=(Ubuntu Fedora Debian Alpine)

for i in "${distros[@]}"; do
    echo $i
done
```

如果你运行脚本，它将显示数组中定义的所有发行版：

```Bash
Ubuntu
Fedora
Debian
Alpine
```

## Bash 中的 While 循环

`while` 循环测试一个条件，然后只要条件为真，就继续循环。

```Bash
while [ condition ]; do
    commands
done
```

如果你考虑前一个例子，它可以使用 `while` 循环进行重写：

```Bash
#!/bin/bash

num=1
while [ $num -le 10 ]; do
    echo $num
    num=$(($num+1))
done
```

如你所见，你首先需要将变量 `num` 定义为 1，然后在循环体内，你增加 `num` 的值。只要 `num` 小于或等于 10，while 循环就会检查条件并运行脚本。

因此，现在运行脚本将会显示出和之前 `for` 循环中看到的完全相同的结果。

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

让我们看另一个例子。这是一个 [Bash 脚本，它接受一个数字作为参数](https://itsfoss.com/bash-pass-arguments/) 并显示该表。

```Bash
#!/bin/bash

echo "Table for $1 is:"
index=1
while [ $index -le 10 ]; do
    echo $(($1*$index))
    index=$(($index+1))
done
```

如果你对 `$1` 的使用感到困惑，它代表传递给脚本的第一个参数。更多的细节可以参考这个系列的 [第三章](https://itsfoss.com/bash-pass-arguments/)。

如果你运行这个脚本，它应该会显示以下的输出：

```Bash
$ ./table.sh 2
Table for 2 is:
2
4
6
8
10
12
14
16
18
20
```

## Bash 中的 Until 循环

这是一个使用较少的循环格式。它的行为和 `while` 循环类似。这里的区别是，循环运行直到它检查的条件为真为止。意味着为了在循环中执行代码，`[ ]` 中的条件必须为假。

我马上会解释一下。让我们先看一下它的语法。

```Bash
until [ condition ]; do
    commands
done
```

现在，如果我要使用相同的示例，即使用 `until` 循环打印从 1 到 10 的数字，它看起来会是这样：

```Bash
#!/bin/bash

num=1
until [ $num -gt 10 ]; do
    echo $num
    num=$(($num+1))
done
```

区别在于条件；其余部分保持不变。

  * 当变量 `num` 小于或等于 10 时，while 循环就会运行。`[ ]` 中的条件必须为真，循环才会执行。
  * 知道变量 `num` 变得大于 10 时，until 循环才会运行。`[ ]` 中的条件必须为假，循环才会执行。

这都是做同样事情的两种不同方式。`while` 更受欢迎，因为你会在大多数编程语言中找到类似 `while` 的循环语法。

## 🏋️ 练习时间

那是有趣的。现在是做一些练习的时候了。

**练习 1**：编写一个脚本，该脚本接受一个数字作为参数并打印其表格。如果脚本在没有参数的情况下运行，你的脚本还应显示一个消息。

**预期输出**：

```Bash
$: ./table.sh
You forgot to enter a number

$: ./table.sh 3
3
6
9
12
15
18
21
24
27
30
```

**练习 2** : 编写一个脚本，列出目录 `/var` 中的所有文件。

**提示** : 对于循环，使用 `/var/*` 作为 “列表”。

Bash 基础知识系列即将结束。作为该系列的最后一章，你将在下周学习在 Bash 脚本中使用函数。敬请期待。


--------------------------------------------------------------------------------

>via: https://itsfoss.com/bash-loops/
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