---
comments: true
---

终端基础：在 Linux 中删除文件和文件夹
======

> 在终端基础知识系列的这一部分中，学习如何在 Linux 中使用命令行复制文件和目录。

复制文件是你经常执行的最基本但最重要的任务之一。

Linux 有一个专门的 `cp` 命令用于复制文件和目录（文件夹）。

在终端基础知识系列的这一部分中，你将学习在终端中复制文件和文件夹。

> 📋 回想一下，以下是你迄今为止在本终端基础知识系列中所学到的内容：
> - [更改目录][2]
> - [创建新目录][3]
> - [列出目录内容][4]
> - [创建文件][5]
> - [读取文件][6]
> - [删除文件和目录][7]

让我们继续该系列的第七章。

## 在 Linux 命令行中复制文件

让我向你展示一些复制文件的示例。

### 将文件复制到另一个目录

要将一个文件复制到另一目录，你所要做的就是遵循给定的命令语法：

```Bash
cp 源文件 目标目录
```

例如，在这里，我将名为 `Hello.txt` 的文件复制到名为 `Tux` 的目录中：

![copy file to another directory in linux command line][8]

正如你所看到的，文件已成功复制到 `Tux` 目录中。

### 复制文件但重命名

你可以选择在复制文件时重命名该文件。只需为“目标文件”指定一个不同的名称即可。

```Bash
cp 源文件 改名的文件
```

作为参考，在这里，我将名为 `Hello.txt` 的文件复制到同一目录，并将其重命名为 `Renamed_Hello.txt`：

![rename a file while copying in a same directory in linux terminal][9]

为什么要这么做？ 比如说，你必须编辑配置文件。一个好的做法是在编辑配置文件之前在同一位置对其进行备份。这样，如果事情没有按计划进行，你可以恢复到旧配置。

### 将多个文件复制到另一个位置

要将多个文件复制到另一个目录，请按以下方式执行命令：

```Bash
cp File1 File2 File3 FileN Target_directory
```

在这里，我将多个文件复制到新位置。

![copy multiple files using the cp command in linux][10]

> 📋 当你复制多个文件时，仅使用 `cp` 命令无法重命名它们。

### 复制时处理重复文件

默认情况下，如果目标目录中存在同名文件，`cp` 命令将覆盖该文件。

为了避免覆盖，你可以在 cp 命令中使用 `-n` 选项，它不会覆盖现有文件：

```Bash
cp -n 源文件 目标目录
```

例如，在这里，我尝试复制目标目录中已有的两个文件，并使用 `-v` 选项来展示该命令正在执行的操作：

```Bash
cp -n -v itsFOSS.txt LHB.txt LU.txt ~/Tux
```

![how not to override files while copying in linux using the cp command][11]

### 交互式复制文件

但是，当你想要覆盖某些文件，而某些文件应该保持不变时该怎么办？

好吧，你可以使用 `-i` 选项在交互模式下使用 `cp` 命令，它每次都会询问你是否应该覆盖该文件：

```Bash
cp -i 源文件 目标目录
```

![how to use cp command in interactive mode][12]

> 🖥️ 自己练习上述所有示例。你已经了解如何创建文件和文件夹，因此请重新创建所有内容。

## 在 Linux 命令行中复制目录

`mkdir` 命令用于创建新目录，`rmdir` 命令用于删除（空）目录。但没有用于复制目录的 `cpdir` 命令。

你必须使用相同的 `cp` 命令，但使用递归选项 `-r` 将目录及其所有内容复制到另一个位置：

```Bash
cp -r 源目录 目标目录
```

例如，在这里，我将名为 `IF` 的目录复制到 `LHB`：

![how to copy a directory in linux command line][13]

但它复制了整个目录。🤨

那么，当你只想复制目录内容而不是目录本身时该怎么办？

你可以执行以下操作：

### 仅复制目录的内容（不是目录）

要仅复制目录的内容，而不复制目录本身，请在源目录名称的末尾附加 `/.`：

```Bash
cp -r 源目录/. 目标目录
```

在这里，我想复制名为 `IF` 的目录的内容，其中包含以下三个文件：

![check the file contents of directory using the tree command][14]

我将执行以下命令将 `IF` 目录的文件内容复制到 `LHB`：

```Bash
cp -r IF/. LHB
```

![copy the file contents of directory not a directory itself in linux command line][15]

你还可以在此处使用 `源目录/*` 。

### 复制多个目录

要复制多个目录，你必须按以下方式执行命令：

```Bash
cp -r 目录1 目录2 目录3 目录N 目标目录
```

例如，在这里，我将两个名为 `IF` 和 `LU` 的目录复制到 `LHB`：

```Bash
cp -r IF LU ~/LHB
```

![copy multiple directories using the cp command in linux command line][16]

当你想要从多个目录复制文件但不复制目录本身时，你可以执行相同的操作：

```Bash
cp -r 目录1/. 目录2/. 目录3/. 目录N/. 目标目录
```

![copy files from multiple directories but not directories their self using the cp command][17]

> 🖥️ 你还可以像重命名文件一样重命名目录。

## 测试你的知识

现在，让我们看看你对到目前为止所学到的知识还记得多少。

- 创建一个名为 `copy_practice` 的目录。
- 将文件 `/etc/services` 复制到这个新创建的文件夹。
- 在此目录下创建一个名为 `secrets` 的文件夹，并将文件 `/etc/passwd` 和 `/etc/services` 复制到其中。
- 将 `copy_practice` 中的 `services` 文件复制到 `secrets` 文件夹中，但不要覆盖它。
- 将 `secrets` 文件夹复制到你的主目录。
- 删除 `secrets` 和 `copy_practice` 目录。

这会给你一些练习。

到目前为止进展顺利。你已经学到了很多东西。在下一章中，你将了解如何使用 `mv` 命令移动文件和文件夹。

--------------------------------------------------------------------------------

via: https://itsfoss.com/copy-files-directory-linux/

作者：[Sagar Sharma][a]
选题：[lkxed][b]
译者：[geekpi](https://github.com/geekpi)
校对：[wxy](https://github.com/wxy)

本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出