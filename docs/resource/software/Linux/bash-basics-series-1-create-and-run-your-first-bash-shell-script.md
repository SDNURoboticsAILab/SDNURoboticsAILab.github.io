---
comments: true
---

Bash 基础知识系列 #1：创建并运行你的第一个 Bash Shell 脚本
======

> 这是一个新教程系列的开始。在这一篇中，你将熟悉 Bash 脚本。

本系列假定你对 Linux 终端比较熟悉。你不必精通，但了解基础知识会很好。我建议阅读终端基础知识系列。

## 这个系列适合谁？

任何想开始学习 Bash Shell 脚本的人。

如果你是一名将 Shell 脚本作为课程的一部分的学生，那么本系列适合你。

如果你是普通的桌面 Linux 用户，本系列将帮助你了解在探索各种软件和修复程序时遇到的大多数 Shell 脚本。你还可以使用它来自动执行一些常见的重复性任务。

到本 Bash 基础系列结束时，你应该能够编写简单到中等水平的 Bash 脚本。

该系列的所有章节都有示例练习，你可以边做边学。

> 🚧 你将在这里学习 Bash Shell 脚本。虽然还有语法基本相同的其他 Shell，但它们的行为在某些方面仍然存在差异。Bash 是最常见和通用的 Shell，因此学习 Shell 脚本从 Bash 开始吧。

## 你的第一个 Shell 脚本：Hello World！

打开一个终端。现在 [创建一个新目录](https://itsfoss.com/make-directories/) 来保存你将在本系列中创建的所有脚本：

```Bash
mkdir bash_scripts
```

现在 [切换到这个新创建的目录](https://itsfoss.com/change-directories/)：

```Bash
cd bash_scripts
```

让我们在这里 [创建一个新文件](https://itsfoss.com/create-files/)：

```Bash
touch hello_world.sh
```

现在，[编辑该文件](https://itsfoss.com/edit-files-linux/) 并向其中添加一行 `echo Hello World`。你可以使用 `cat` 命令的追加模式（使用 `>`）执行此操作：

```Bash

echo Hello World
^C
```

我更喜欢在使用 `cat` 命令添加文本时添加新行。

按 `Ctrl+C` 或 `Ctrl+D` 键退出 `cat` 命令的追加模式。现在，如果你查看脚本 `hellow_world.sh` 的内容，你应该只看到一行。

![Creating first shell script](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/bashbashchapter1create-first-shell-script.png)

关键时刻来了。你已经创建了第一个 Shell 脚本。是时候 [运行 Shell 脚本](https://itsfoss.com/run-shell-script-linux/) 了。

这样做：

```Bash
bash hello_world.sh
```

`echo` 命令只是显示提供给它的任何内容。在这种情况下，Shell 脚本应该在屏幕上输出 “Hello World”。

![Run first shell script](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/bashbashchapter1run-first-shell-script.png)

恭喜！ 你刚刚成功运行了第一个 Shell 脚本。多么酷啊！

以下是上述所有命令的重放，供你参考。

### 另一种运行 Shell 脚本的方法

大多数时候，你将以这种方式运行 Shell 脚本：

```Bash
./hello_world.sh
```

这将产生错误，因为作为脚本的文件还没有执行权限。

```Bash
bash: ./hello_world.sh: Permission denied
```

给脚本添加执行权限：

```Bash
chmod u+x hello-world.sh
```

现在，你可以像这样运行它：

```Bash
./hello_world.sh
```

![Run shell scripts](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/bashchapter1running-shell-scripts.png)

因此，你学习了两种运行 Shell 脚本的方法。是时候让我们将注意力转回 Bash 了。

## 把你的 Shell 脚本变成 Bash 脚本

感到困惑？ 实际上，Linux 中有几种可用的 Shell。Bash、Ksh、Csh、Zsh 等等。其中，Bash 是最受欢迎的，几乎所有发行版都默认安装了它。

Shell 是一个解释器。它接受并运行 Linux 命令。虽然大多数 Shell 的语法保持不变，但它们的行为在某些点上可能有所不同。例如，条件逻辑中括号的处理。

这就是为什么告诉系统使用哪个 Shell 来解释脚本很重要。

当你使用 `bash hello_world.sh` 时，你明确地使用了 Bash 解释器。

但是当你以这种方式运行 Shell 脚本时：

```Bash
./hello_world.sh
```

系统将使用你当前使用的任何 Shell 来运行脚本。

为避免由于不同的语法处理而导致不必要的意外，你应该明确告诉系统它是哪个 shell 脚本。

怎么做？ 使用释伴（`#!`）。通常，`#` 用于 Shell 脚本中的注释。但是，如果 `#!` 用作程序的第一行，它的特殊用途是告诉系统使用哪个 Shell。

因此，更改 `hello_world.sh` 的内容，使其看起来像这样：

```Bash
#!/bin/bash

echo Hello World
```

现在，你可以像往常一样运行 Shell 脚本，因为你知道系统将使用 Bash Shell 来运行脚本。

![Run bash shell script](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/bashchapter1run-bash-shell-script.png)

> 💡 如果你觉得在终端中编辑脚本文件不方便，作为桌面 Linux 用户，你可以使用 Gedit 或其他 GUI 文本编辑器编写脚本并在终端中运行。

## 🏋️ 练习时间

是时候练习你学到的东西了。以下是该级别的一些基本练习：

- 编写一个打印 “Hello Everyone” 的 Bash 脚本
- 编写一个显示当前工作目录的 Bash 脚本（提示：使用 `pwd` 命令）
- 编写一个 Shell 脚本，使用以下列方式打印你的用户名：“My name is XYZ”（提示：使用 `$USER`）

答案可以在社区论坛的 [这个专门的帖子](https://itsfoss.community:443/t/practice-exercise-in-bash-basics-series-1-create-and-run-your-first-bash-shell-script/10682) 中讨论。

最后一个练习使用 `$USER`。这是一个打印用户名的特殊变量。

这就引出了 Bash 基础系列下一章的主题：变量。

请继续关注下面的内容。


--------------------------------------------------------------------------------

>via: https://itsfoss.com/create-bash-script/
>
>作者：[Abhishek Prakash](https://itsfoss.com/author/abhishek/)
>
>选题：[lkxed](https://github.com/lkxed/)
>
>译者：[geekpi](https://github.com/geekpi)
>
>校对：[wxy](https://github.com/wxy)
>
>本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.net.cn/) 荣誉推出>