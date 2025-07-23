---
comments: true
---

# Bash 基础知识系列 #2：在 Bash 中使用变量

> 在本章的 Bash 基础知识系列中，学习在 Bash 脚本中使用变量。

在 Bash 基础知识系列的第一部分中，我简要提到了变量。现在是时候在本章中详细了解它们了。

如果你曾经进行过任何类型的编码，你一定熟悉术语“变量”。

如果没有，请将变量视为保存信息的盒子，并且该信息可以随着时间的推移而改变。

让我们看看如何使用它们。

## 在 Bash shell 中使用变量

打开终端并使用一个随机的数字 4 初始化变量：

```Bash
var=4
```

现在你有一个名为 `var` 的变量，它的值为 `4`。想验证一下吗？ **通过在变量名前添加 `$` 来访问变量的值**。这称为参数扩展。

```Bash

The value of var is 4
```

> 🚧 变量初始化时 `=` 前后不能有空格。

如果需要，你可以将该值更改为其他值：

![Using variables in shell](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/bashUsing-variables-in-shell.png)

在 Bash shell 中，变量可以是数字、字符或字符串（包括空格在内的字符）。

![Different variable types in Bash shell](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/bash-variables-types.png)

> 💡 与 Linux 中的其他事物一样，变量名称也区分大小写。它们可以由字母、数字和下划线 “`_`” 组成。


## 在 Bash 脚本中使用变量

你是否注意到我没有运行 shell 脚本来显示变量示例？ 你可以直接在 shell 中做很多事情.当你关闭终端时，你创建的那些变量将不再存在。

但是，你的发行版通常会添加全局变量，以便可以在所有脚本和 shell 中访问它们。

让我们再写一些脚本.你应该之前创建了脚本目录，但无论哪种情况，此命令都会处理该目录：

```Bash
mkdir -p bash_scripts && cd bash_scripts
```

基本上，如果 `bash_scripts` 目录尚不存在，它将创建它，然后切换到该目录。

这里让我们使用以下文本创建一个名为 `knock.sh` 的新脚本。

```Bash
#!/bin/bash

echo knock, knock
echo "Who's there?"
echo "It's me, $USER"
```

更改文件权限并运行脚本。你在上一章中已经学到了。

这是它为我生成的内容：

![Using global variable in Bahs script](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/using-global-variable-bash-script.png)

**你是否注意到它如何自动将我的名字添加到其中？** 这就是包含用户名的全局变量 `$USER` 的魔力。

你可能还注意到，我有时将 `"` 与 `echo` 一起使用，但其他时候则不使用。这是故意的。[bash 中的引号](https://linuxhandbook.com:443/quotes-in-bash/) 有特殊含义。它们可用于处理空格和其他特殊字符。让我展示一个例子。

## 处理变量中的空格

假设你必须使用一个名为 `greetings` 的变量，其值为 `hello and welcome`。

如果你尝试像这样初始化变量：

```Bash
greetings=Hello and Welcome
```

你会得到这样的错误：

```Bash
Command 'and' not found, but can be installed with:
sudo apt install and
```

这就是为什么你需要使用单引号或双引号：

```Bash
greetings="Hello and Welcome"
```

现在你可以根据需要使用该变量。

![Using spaces in variable names in bash](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/using-spaces-in-bash-variable.png)

## 将命令输出分配给变量

是的！你可以将命令的输出存储在变量中并在脚本中使用它们。这称为命令替换。

```Bash
var=$(command)
```

这是一个例子：

```Bash


Today's date is 06/19/23

```

![Command substitution in bash](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/command-substitue-bash-variable.png)

旧语法使用反引号而不是 `$()` 进行命令替换。虽然它可能仍然有效，但你应该使用新的推荐符号。

> 💡 变量会更改值，除非你声明一个“常量”变量，如下所示：`readonly pi=3.14`。在这种情况下，变量 `pi` 的值无法更改，因为它被声明为 `readlonly`。

## 🏋️ 练习时间

是时候练习你所学到的东西了。这里有一些练习来测试你的学习情况。

**练习 1**：编写一个 bash 脚本，以以下格式打印你的用户名、当前工作目录、主目录和默认 shell。

```Bash
Hello, there
My name is XYZ
My current location is XYZ
My home directory is XYZ
My default shell is XYZ
```

**提示**：使用全局变量 `$USER`、`$PWD`、`$HOME` 和 `$SHELL`。

**练习 2：** 编写一个 bash 脚本，声明一个名为 `price` 的变量.使用它来获取以下格式的输出：

```Bash
Today's price is $X
Tomorrow's price is $Y
```

其中 X 是变量 `price` 的初始值，并且明天价格翻倍。

**提示**：使用 `\` 转义特殊字符 `$`。

练习的答案可以在社区的这个专用帖子中讨论。

在 Bash 基础知识系列的下一章中，你将了解如何通过传递参数和接受用户输入来使 bash 脚本具有交互性。


--------------------------------------------------------------------------------
>
>via: https://itsfoss.com/bash-use-variables/
>
>作者：[Abhishek Prakash](https://itsfoss.com/author/abhishek/)
>
>选题：[lkxed](https://github.com/lkxed/)
>
>译者：[geekpi](https://github.com/geekpi)
>
>校对：[wxy](https://github.com/wxy)
>
>本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.net.cn/) 荣誉推出