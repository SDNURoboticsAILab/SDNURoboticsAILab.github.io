---
comments: true
---

Bash 基础知识系列 #5：在 Bash 中使用数组
======

> 本章将介绍如何在 Bash Shell 脚本中使用数组。学习添加元素、删除元素和获取数组长度。

在本系列的前面部分中，你了解了变量。变量中可以有单个值。

数组内部可以有多个值。当你必须一次处理多个变量时，这会使事情变得更容易。你不必将各个值存储在新变量中。

因此，不要像这样声明五个变量：

```Bash
distro1=Ubuntu
distro2=Fedora
distro3=SUSE
distro4=Arch Linux
distro5=Nix
```

你可以在单个数组中初始化它们所有：

```Bash
distros=(Ubuntu Fedora SUSE "Arch Linux" Nix)
```

与其他一些编程语言不同，你不使用逗号作为数组元素分隔符。

那挺好的。让我们看看如何访问数组元素。

## 在 Bash 中访问数组元素

使用索引（数组中的位置）访问数组元素。要访问索引 N 处的数组元素，请使用：

```Bash
${array_name[N]}
```

> 💡 与大多数其他编程语言一样，Bash Shell 中的数组从索引 0 开始。这意味着第一个元素的索引为 0，第二个元素的索引为 1，第 n 个元素的索引为 `n-1`。

因此，如果你想打印 SUSE，你将使用：

```Bash
echo ${distros[2]}
```

![Example of accessing array elements in bash shell](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/accessing-array-elements-bash.png)

> 🚧 `${` 之后或 `}` 之前不能有任何空格。你不能像 `${ array[n] }` 那样使用它。

## 一次访问所有数组元素

假设你要打印数组的所有元素。

你可以一一使用 `echo ${array[n]}` 但这确实没有必要。有一个更好更简单的方法：

```Bash
${array[*]}
```

这将为你提供所有数组元素。

![Accessing all array elements at once in bash shell](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/accessing-all-array-elements-bash.png)

## 在 Bash 中获取数组长度

如何知道数组中有多少个元素？ 有一个专门的方法 [在 Bash 中获取数组长度](https://linuxhandbook.com:443/array-length-bash/)：

```Bash
${#array_name[@]}
```

就这么简单，对吧？

![Get array length in bash](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/get-array-length-bash.png)

## 在 Bash 中添加数组元素

如果必须向数组添加其他元素，请使用 `+=` 运算符 [将元素追加到 Bash 中的现有数组](https://linuxhandbook.com:443/bash-append-array/)：

```Bash
array_name+=("new_value")
```

这是一个例子：

![Append new element to array](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/append-element-to-array.png)

> 🚧 追加元素时使用 `()` 很重要。

你还可以使用索引将元素设置在任何位置。

```Bash
array_name[N]=new_value
```

**但请记住使用正确的索引编号。** 如果在现有索引上使用它，新值将替换该元素。

如果你使用“越界”索引，它仍会添加到最后一个元素之后。例如，如果数组长度为 6，并且你尝试在索引 9 处设置新值，则该值仍将作为最后一个元素添加到第 7 个位置（索引 6）。

## 删除数组元素

你可以使用 Shell 内置的 `unset` 通过提供索引号来删除数组元素：

```Bash
unset array_name[N]
```

这是一个示例，我删除了数组的第四个元素。

![Delete array element in bash](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/delete-array-element-bash.png)

你还可以通过 unset 来删除整个数组：

```Bash
unset array_name
```

> 💡 Bash 中没有严格的数据类型规则。你可以创建一个同时包含整数和字符串的数组。

## 🏋️ 练习时间

让我们练习一下你所学到的有关 Bash 数组的知识。

**练习 1**：创建一个 Bash 脚本，其中包含五个最佳 Linux 发行版的数组。全部打印出来。

现在，用 “Hannah Montanna Linux” 替换中间的选择。

**练习 2**：创建一个 Bash 脚本，该脚本接受用户提供的三个数字，然后以相反的顺序打印它们。

预期输出：

```Bash
Enter three numbers and press enter
12 23 44
Numbers in reverse order are: 44 23 12
```

我希望你喜欢通过本系列学习 Bash Shell 脚本。在下一章中，你将学习如何使用 `if-else`。敬请关注。


--------------------------------------------------------------------------------

>via: https://itsfoss.com/bash-arrays/
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