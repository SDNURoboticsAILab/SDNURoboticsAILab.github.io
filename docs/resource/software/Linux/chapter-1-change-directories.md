---
comments: true
---

# 终端基础：Linux 终端中的目录切换

> 本篇文章作为终端基础教程系列的一部分，介绍如何在 Linux 命令行中，利用绝对路径和相对路径实现目录切换。

Linux 的 [`cd` 命令](https://linux.net.cn/article-15967-1.html) 让你可以轻松切换文件夹（即目录）。只需提供你要切换到的文件夹路径即可。

```Bash
cd path_to_directory
```

然而对于 Linux 新人来说，可能会在路径的指定上有所困扰。

首先，让我们解决这个问题。

## 理解 Linux 中的路径

在 Linux 文件系统中，路径是用来追踪文件位置的信息。所有的路径都从根目录开始，然后向下延伸。

你可以通过下面的方式查看当前所在的位置：

```Bash
pwd
```

结果可能是类似于 `/home/username` 的输出。注意，这里的 `username` 将会是你自己的用户名。

你可以注意到，路径是由 `/` 符号和目录名组成的。比如路径 `/home/abhishek/scripts`， 表示 `scripts` 是在文件夹 `abhishek` 之内，而文件夹 `abhishek` 在 `home` 文件夹之内。要注意，第一个 '/' 是指根目录（即文件系统的开始处），后面的 '/' 则作为目录的分隔符。

![Path in Linux](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter1path-linux.webp)

!!! note "🖥️"

    在终端中键入 `ls /`，然后按回车。你将会看到根目录下的所有内容，试试看！

接下来，让我们学习两种常见的路径指定方式：绝对路径和相对路径。

**绝对路径**：这种路径从根开始，然后一直扩展到你需要的位置。如果一个路径是以 `/` 开头，那就说明它是一个绝对路径。

**相对路径**：这是相对于你文件系统中当前位置的路径。如果我当前位置在 `/home/abhishek`，并且我需要去 `/home/abhishek/Documents`， 我只需要简单地切换到 `Documents`，而不需要指定整个绝对路径 `/home/abhishek/Documents`。

在我演示这两种路径的区别之前，有必要先熟悉两个特殊的目录标识：

- `.` （单点）表示当前目录。
- `..` （双点）表示上一级目录，也就是当前目录的母目录。

这里有一张图形化的表示。

![Absolute path vs relative path](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter1relative-path-cd.png)

想要了解更多关于Linux路径的信息吗？这篇文章将对你有所帮助。

[Linux 中的绝对路径与相对路径：有何区别？](https://cn.linux-console.net/?p=19897)

## 利用 cd 命令变更目录

在你已对路径概念有所了解之后，我们来了解如何切换目录。

!!! note "🖥️"

    如果你**仅键入 `cd` 并按回车键**，无论当前位置在哪，系统都会将你带回主目录。试一试吧。

敲入以下命令，你就能看到主目录里的所有文件夹：

```Bash
ls
```

这是我看到的情况：

```Bash
abhishek@ituxedo:~$ ls
Desktop    Downloads  Pictures  Templates  VirtualBoxVMs
Documents  Music      Public    Videos
```

你的情况可能与此类似，但未必完全一样。

假如你希望跳转到 `Documents` 文件夹。由于它就在当前目录下，这里使用相对路径会比较方便：

```Bash
cd Documents
```

!!! question "💡"

    注意，大部分 Linux 发行版预设的终端模拟器会在提示符本身显示出当前所在的位置。因此你不必频繁使用 `pwd` 指令来确认自己的位置。

![Most Linux terminal prompts show the current location](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter1linux-terminal-prompt.png)

*大多数Linux终端提示符会显示当前位置*

假如你希望切换到位于主目录里的 `Templates` 文件夹。

你可以使用相对路径 `../Templates`（`..` 会让你返回到上层目录，即 `/home/username`，然后你就可以进入 `Templates` 文件夹了）。

但这次我们尝试使用绝对路径。请把下面的 `abhishek` 替换成你的用户名。

```Bash
cd /home/abhishek/Templates
```

此刻你已经在 `Templates` 文件夹里了。如何前往 `Downloads` 文件夹呢？这次我们再使用相对路径：

```Bash
cd ../Downloads
```

下面的图片会回顾一下你刚才学到的所有或有关目录切换的范例。

![cd command example](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter1cd-command-example.svg)

*观看上述 cd 命令示例的重播*

!!! question "💡"

    别忘了你还可以使用终端的 `tab` 键自动补全功能。只需要键入命令或者文件夹名称的前几个字母，然后敲击 `tab` 键，系统就会尝试自动地补全命令或文件夹名称，或者给你显示出所有可能的选项。

## 故障解决

在 Linux 终端操作切换目录的过程中，你可能会遇到一些常见的错误。

### 文件或目录不存在

如果在你尝试切换目录时，出现类似下面的错误信息：

> bash: cd: directory_name: No such file or directory

那么你可能在路径或目录名称上犯了误解。这里有几点你需要注意的：

- 请确定你输入的目录名中没有拼写错误。
- Linux 系统对大小写敏感，因此，`Downloads` 和 `downloads` 会被识别为不同的目录。
- 你可能未正确指定路径。可能你所在的位置与你预期的不同？或者你遗漏了绝对路径中的开头的 `/` 字符？

![Common examples of "no such file or directory" error](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter1common-errors-with-cd.png)

*常见的“无此文件或目录”错误示例。*

### 非目录错误

如果你看到像下面这样的错误提示：

> bash: cd: filename: Not a directory

这表示你尝试使用 `cd` 命令对一个文件进行操作，而不是一个目录（文件夹）。很明显，你不能像进入文件夹那样“进入”一个文件，因此会出现这样的错误。

![Not a directory error with the cd command](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter1not-a-directory-error-linux.png)

### 参数过多

这是 Linux 新手常犯的另一个错误：

> bash: cd: too many arguments

`cd` 命令只接受一个参数。也就是说，你只能对命令指定一个目录。

如果你指定了超过一个的参数，或者在路径中误加了空格，你就会看到这个错误。

![Too many arguments error in Linux terminal](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter1too-many-arguments.png)

*cd 命令只接受一个参数*

!!! question "🏋🏻"

    如果你输入 `cd -`，它将会把你带到前一个目录。当你在两个相隔较远的地方切换时非常方便，可以避免再次输入长路径。

## 特殊目录符号

在结束这个教程之前，我想快速告诉你关于特殊符号 `~`。在 Linux 中，`~` 是用户主目录的捷径。

如果用户 `abhi` 运行它，`~` 就会代表 `/home/abhi`，如果用户 `prakash` 运行，`~` 就意味着 `/home/prakash`。

总结一下你在这个基础教程系列中学到的所有特殊目录标识：

| 符号 | 描述       |
| :--- | :--------- |
| `.`  | 当前目录   |
| `..` | 上级目录   |
| `~`  | 主目录     |
| `-`  | 前一个目录 |

## 📝测试你的知识

下面是一些简单的练习，用来测试你刚刚学到的关于路径和 `cd` 命令的知识。

移动到你的主目录，并使用这个命令创建一个嵌套的目录结构：

```Bash
mkdir -p sample/dir1/dir2/dir3
```

然后，一步步来试试这个：

- 使用绝对路径或相对路径进入 `dir3`
- 使用相对路径移动到 `dir1`
- 使用你能想象到的最短路径进入 `dir2`
- 使用绝对路径切换到 `sample` 目录
- 返回你的主目录

> 🔑 想知道你是否全都做对了吗？欢迎分享你的答案。

现在你知道如何切换目录，是不是应该学习一下如何创建目录呢？本系列的下一章将对此进行讨论。

当然，我们也非常欢迎您对这一新系列的反馈。为了改进本教程，我能做些什么呢？

--------------------------------------------------------------------------------

>via: [https://linux.net.cn/article-16304-1.html](https://linux.net.cn/article-16304-1.html)
>
>source: [https://itsfoss.com/change-directories/](https://itsfoss.com/change-directories/)
>
>作者：[Abhishek Prakash](https://itsfoss.com/author/abhishek/)
>
>选题：[lkxed](https://github.com/lkxed/)
>
>译者：[ChatGPT](https://linux.net.cn/lctt/ChatGPT)
>
>校对：[wxy](https://github.com/wxy)
>
>本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.net.cn/) 荣誉推出
