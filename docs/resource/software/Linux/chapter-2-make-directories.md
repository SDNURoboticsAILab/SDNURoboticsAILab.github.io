---
comments: true
---

# 终端基础第二章：在 Linux 终端中创建目录

在终端基础系列的上一章中，你学到了在 Linux 命令行中改变文件夹的知识。

我在最后给出了一个练习，简单地提到了创建目录。

在本系列的这一部分，我将讨论如何使用 `mkdir` 命令在 Linux 命令行中建立新的文件夹。

```
mkdir dir_name
```

`mkdir` 是 “<ruby>创建目录<rt>make directories</rt></ruby>” 的简称。让我们来看看这个命令的使用情况。

!!! note "📋"

    如果你不知道，文件夹在 Linux 中被称为目录。

## 在 Linux 中创建一个新目录

你现在应该已经熟悉了 Linux 中绝对路径和相对路径的概念。如果没有，请参考 [本教程](https://cn.linux-console.net/?p=19897)。

如果你的系统还没有打开终端，请打开它。通常情况下，你从主目录（`/home/username`）开始。但为了本教程和回忆一些事情，我假定你不在你的主目录中。

所以，先换到你的主目录：

```
cd
```

是的，如果你简单地输入 `cd`，没有任何选项和参数，它就会把你带到你的主目录。你也可以使用 `cd ~` 等方法。

在这里，建立一个新的目录，叫做 `practice`。

```
mkdir practice
```

你能切换到这个新建立的 `practice` 目录吗？

```
cd practice
```

很好！现在你有了一个专门的文件夹，你将在这里练习本系列中的 Linux 命令行教程。

![](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter2-make-directory-example.svg)

## 创建多个新目录

你刚刚创建了一个新的目录。如果你要创建不止一个呢？比方说，有三个。

你可以对每个目录连续使用三次 `mkdir` 命令。这将会起作用。然而，这并不是真的需要。你可以像这样同时创建多个目录来节省时间和精力：

```
mkdir dir1 dir2 dir3
```

请继续这样做吧。你可以列出 `practice` 目录的内容，查看所有新创建的目录。以后会有更多关于 `ls` 命令的内容。

![](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter2-create-multiple-directories-linux.png)

!!! question "💡"

    你不能在同一地方有两个同名的文件夹或文件。

## 创建多个嵌套的子目录

你现在知道了一次创建多个目录的方法。

但是，如果你要创建一个嵌套的目录结构呢？比方说，你需要在 `dir1` 里面的 `subdir1` 里面创建一个目录 `subdir2`。

```
dir1/subdir1/subdir2
```

这里的问题是 `subdir1` 并不存在。所以如果你尝试 `mkdir dir1/subdir1/subdir32`，你会得到一个错误：

```
abhishek@itsfoss:~/practice$ mkdir dir1/subdir1/subdir2
mkdir: cannot create directory ‘dir1/subdir1/subdir2’: No such file or directory
```

如果你不知道的话，你会选择 `mkdir dir1/subdir1`，然后运行 `mkdir dir1/subdir2`。这将会起作用。然而，有一个更好的方法。

你使用 `-p` 选项，它会在需要时创建父目录。如果你运行下面的命令：

```
mkdir -p dir1/subdir1/subdir2
```

它将创建 `subdir1`，然后在 `subdir1` 里面创建 `subdir2`。

!!! question "💡"

    不是命名惯例，但最好在文件和目录名中避免空格。使用下划线或破折号代替，因为处理文件/目录名中的空格需要额外精力。

## 测试你的知识

这是一个相当简短的教程，因为 `mkdir` 命令只有几个选项。

现在，让我给你一些实践练习，以利用你先前创建的 `practice` 目录。

- 不进入 `dir2` 目录，在其中创建两个新的子目录。
- 不进入 `dir3` 目录，创建两级嵌套子目录（`subdir1/subdir2`）
- 进入 dir2 目录。在这里，在你的主目录下创建一个名为 `temp_stuff` 的目录。不要担心，我们将在本系列教程的后面删除它。
- 回到父目录 `practice`，尝试创建一个名为 `dir3` 的目录。你看到一个错误。你能用 `-p` 选项使它消失吗？

你可以 [在社区论坛讨论这个练习](https://itsfoss.community/t/exercise-in-making-directories-in-linux-terminal/10227)。

在终端基础系列的下一章中，你将学习如何用 `ls` 命令列出一个目录的内容。

如果你有问题或建议，请告诉我。

--------------------------------------------------------------------------------

>via: https://itsfoss.com/make-directories/
>
>source: https://itsfoss.com/linux-terminal-basics/
>
>作者：[Abhishek Prakash](https://itsfoss.com/author/abhishek/)
>选题：[lkxed](https://github.com/lkxed/)
>译者：[geekpi](https://github.com/geekpi)
>校对：[wxy](https://github.com/wxy)
>
>本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出