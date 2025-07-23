---
comments: true
---

# Bash 基础知识系列 #6：处理字符串操作

在大多数编程语言中，你都会找到字符串数据类型。字符串基本上是一组字符。

但 Bash shell 有所不同。字符串没有单独的数据类型。这里一切都是变量。

但这并不意味着你不能像在 C 和其他编程语言中那样处理字符串。

在 Bash Shell 中可以查找子字符串、替换子字符串、连接字符串以及更多字符串操作。

在 Bash 基础知识系列的这一部分中，你将学习基本的字符串操作。

## 在 Bash 中获取字符串长度

让我们从最简单的选项开始。也就是获取字符串的长度。这很简单：

```Bash
${#string}
```

让我们在示例中使用它。

![Example of getting string length in bash](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/bash-string-length-example.png)

正如你所看到的，第二个示例中有两个单词，但由于它用引号引起来，因此它被视为单个单词。连空格都算作一个字符。

## 在 Bash 中连接字符串

用技术术语来说是字符串 <ruby>连接<rt>concatenation</rt></ruby>，这是 Bash 中最简单的字符串操作之一。

你只需像这样一个接一个地使用字符串变量：

```Bash
str3=$str1$str2
```

还能比这更简单吗？我觉得不能。

让我们看一个例子。这是我的示例脚本，名为 `join.sh`：

```Bash
#!/bin/bash

read -p "Enter first string: " str1
read -p "Enter second string: " str2

joined=$str1$str2

echo "The joined string is: $joined"
```

以下是该脚本的运行示例：

![Join two strings in bash](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/join-strings-bash.png)

## 在 Bash 中提取子字符串

假设你有一个包含多个字符的大字符串，并且你想要提取其中的一部分。

要提取子字符串，需要指定主字符串、子字符串的起始位置和子字符串的长度，如下所示：

```Bash
${string:$pos:$len}
```

> 💡 和数组一样，字符串中的定位也是从 0 开始。

这是一个例子：

![Extracting substring in bash](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/extract-substring-bash.png)

即使你指定的子字符串长度大于字符串长度，它也只会到达字符串末尾。

## 替换 Bash 中的子字符串

假设你有一个大字符串，并且你想用另一个字符串替换其中的一部分。

在这种情况下，你可以使用这种语法：

```Bash
${string/substr1/substr2}
```

> ✋ 只有第一次出现的子字符串才会以这种方式替换。如果要替换所有出现的地方，请使用 `${string//substr1/substr2}`

这是一个例子：

![Replace substring in bash](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/replace-substring-bash.png)

正如你在上面看到的，“good” 一词被替换为 “best”。我将替换的字符串保存到同一字符串中以更改原始字符串。

> 💡 如果未找到子字符串，则不会替换任何内容。它不会导致错误。

## 在 Bash 中删除子字符串

我们来谈谈删除子字符串。假设你要删除字符串的一部分。在这种情况下，只需将子字符串提供给主字符串，如下所示：

```Bash
${string/substring}
```

> ✋ 通过这种方式，仅删除第一次出现的子字符串。如果要删除所有出现的内容，请使用 `${string//substr}`

如果找到子字符串，则将从字符串中删除它。

让我们通过一个例子来看看。

![Delete substring in bash](https://itsfoss.com/content/images/2023/07/bash-delete-substring.png)

不用说，如果没有找到子字符串，则不会删除它。它不会导致错误。

## 🏋️ 练习时间

现在是你通过简单练习来实践字符串操作的时候了。

**练习 1**：声明一个字符串 “I am all wet”。现在通过用 “set” 替换单词 “wet” 来更改此字符串。

**练习 2**：创建一个字符串，以 `112-123-1234` 格式保存电话号码。现在，你必须删除所有 `-`。

这应该会给你一些在 Bash 中使用字符串的不错的练习。在下一章中，你将学习如何在 Bash 中使用 `if-else` 语句。敬请关注。


--------------------------------------------------------------------------------

>via: https://itsfoss.com/bash-strings/
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