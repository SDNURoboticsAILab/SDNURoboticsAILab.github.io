---
comments: true
---

# 终端基础：在 Linux 中创建文件

到目前为止，在这个终端基础系列中，你已经学会了：

- [更改目录](https://linux.net.cn/article-16304-1.html)
- [创建新目录](https://linux.net.cn/article-15595-1.html)
- [列出目录内容](https://cn.linux-console.net/?p=17707)

现在让我们学习如何在 Linux 命令行中创建文件。我将简要讨论向文件添加内容。但是，稍后将介绍有关编辑文本文件的详细信息。


## 使用 touch 命令创建一个新的空文件

使用 `touch` 命令非常简单。

```Bash
touch filename
```

切换到你的主目录并创建一个名为 `practice_files` 的新目录，然后切换到该目录：

```Bash
mkdir practice_files && cd practice_files
```

!!! question "💡"

    `&&` 是一种组合两个命令的方法。只有当第一个命令执行成功时，第二个命令才会运行。


现在，创建一个名为 `new_file` 的新文件：

```Bash
touch new_file
```

就是这样。你刚刚创建了一个新的空文件。

列出目录内容并使用 `ls -l` 命令检查文件的属性。

![](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter4-touch-example.svg)
*使用 touch 命令创建新文件*

!!! question "💡"

    `touch` 命令的最初目的是“触摸”文件并更改其时间戳。如果提供的文件不存在，它会创建一个具有该名称的新文件。

## 使用 echo 命令创建一个新文件

很久以前我就应该向你介绍 `echo` 命令。迟到总比不到好。`echo` 命令显示你提供给它的任何内容。因此得名“回声”。

```Bash
echo Hello World
```

你可以使用重定向并将输出路由到文件。因此在此过程中创建一个新文件：

```Bash
echo "Hello World" >> other_new_file
```

这样，你将创建一个名为 `other_new_file` 的新文件，其中包含文本 `Hello World`。

![](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter4-echo-example.svg)
*使用 echo 命令创建文件*

请记住，如果提供的文件已经存在，使用 `>>` 重定向，你将向文件添加一个新行。你也可以使用 `>` 重定向，但它会替换文件的现有内容。

更多关于重定向的信息可以在下面的教程中找到。

**[解释：Linux 中的输入、输出和错误重定向](https://www.51cto.com/article/722462.html)**

## 使用 cat 命令创建新文件

`cat` 命令的最初目的是连接文件。但是，它主要用于显示文件的内容。

它还可以使用选项创建新文件并添加内容。为此，你可以使用相同的 `>` 和 `>>` 重定向。

```Bash
cat >> another_file
```

但是这个将创建一个新文件并允许你向其中添加一些文本。添加文本是可选的。**你可以使用 `Ctrl+d` 键退出 `cat` 输入模式。**

![](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter4-cat-example.svg)
*使用 cat 命令创建新文件*

同样，附加模式 `>>` 在文件内容的末尾添加新文本，而覆盖模式 `>` 用新内容替换现有内容。



!!! question "🏋️"

    使用 `ls -l` 长列表显示并注意时间戳。使用 `touch` 创建文件，你看到时间戳的区别了吗？

```Bash
touch other_new_file
```

## 📝测试你的知识

你已经了解了如何创建新文件。这里有一些简单的练习来练习你刚刚学到的东西。它也包括前几章的一些内容。

- 使用 `touch` 命令创建三个新文件，分别命名为 `file1`、`file2` 和 `file3`。提示：你不需要运行 `touch` 三次。
- 创建一个名为 `files` 的目录，并在其中创建一个名为 `my_file` 的文件。
- 使用 `cat` 命令创建一个名为 `your_file` 的文件，并在其中添加以下文本 “This is your file”。
- 使用 `echo` 命令将新行 “This is our file” 添加到 `your_file`。
- 以相反的时间顺序显示所有文件（请参阅第 3 篇）。现在使用 `touch` 命令修改 `file2` 和 `file3` 的时间戳。现在再次按时间倒序显示内容。

这很有趣。你正在取得很好的进步。你已在本章中学会了创建新文件。接下来，你将学习如何查看文件的内容。

--------------------------------------------------------------------------------

>via: [https://linux.net.cn/article-15643-1.html](https://linux.net.cn/article-15643-1.html)
>
>source: [https://itsfoss.com/create-files/](https://itsfoss.com/create-files/)
>
>作者：[Abhishek Prakash][a]
>选题：[lkxed][b]
>译者：[geekpi](https://github.com/geekpi)
>校对：[wxy](https://github.com/wxy)
>
>本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.net.cn/) 荣誉推出