---
comments: true
---

Bash 基础知识系列 #7：If Else 语句
======

> 如果这样，那就那样，否则就……。还不明白吗？了解了 Bash Shell 脚本中的 if-else 语句后就明白了。

Bash 支持 if-else 语句，以便你可以在 shell 脚本中使用逻辑推理。

通用的 if-else 语法如下：

```Bash
if [ expression ]; then

  # 如果条件为真则执行此块，否则转到下一个

elif [ expression ]; then

  # 如果条件为真则执行此块，否则转到下一个

else 

  # 如果以上条件都不成立，则执行此块

fi
```

正如你所注意到的：

- `elif` 用于 “否则如果” 类型的条件。
- if-else 条件始终以 `fi` 结尾。
- 使用分号 `;` 和 `then` 关键字

在展示 if 和 else-if 的示例之前，我先分享一下常见的比较表达式（也称为测试条件）。

## 测试条件

以下是可用于数字比较的测试条件运算符：

| 条件 | 当满足以下条件时为真 | 
| :- | :- |
| `$a -lt $b` | `$a < $b`（`$a` **小于** `$b`）|
| `$a -gt $b` | `$a > $b`（`$a` **大于** `$b`）|
| `$a -le $b` | `$a <= $b`（`$a` **小于等于** `$b` ）|
| `$a -ge $b` | `$a >= $b` （`$a` **大于等于** `$b`）
| `$a -eq $b` | `$a == $b` |
| `$a -ne $b` | `$a != $b` |

如果你要比较字符串，可以使用以下测试条件：

| 条件 | 当满足以下条件时为真 |
| :- | :- |
| `"$a" = "$b"` | `$a` 与 `$b`  相同 | 
| `"$a" == "$b"` | `$a` 与 `$b` 相同 | 
| `"$a" != "$b"` | `$a` 与 `$b` 不同 | 
| `-z "$a"` | `$a` 为空字符串 |

文件类型检查也有条件：

| 条件 | 当满足以下条件时为真 |
| :- | :- |
| `-f $a` | `$a` 是一个文件 |
| `-d $a` | `$a` 是一个目录 |
| `-L $a` | `$a` 是一个链接 |

现在你已经了解了各种比较表达式，让我们在各种示例中看看它们的实际应用。

## 在 Bash 中使用 if 语句

让我们创建一个脚本来告诉你给定的数字是否为偶数。

这是我的脚本，名为 `even.sh`：

```Bash
#!/bin/bash

read -p "Enter the number: " num

mod=$(($num%2))

if [ $mod -eq 0 ]; then
	echo "Number $num is even"
fi
```

当模数运算（`%`）整除给定数字（本例中为 2）时，它返回零。

> 🚧 特别注意空格。左括号和右括号与条件之间必须有空格。同样，条件运算符（-le、== 等）前后必须有空格。

这是我运行脚本时显示的内容：

![Running a script with if statement example in bash](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/bash-if-example.png)

你是否注意到，当数字为偶数时，脚本会告诉你，但当数字为奇数时，脚本不会显示任何内容？ 让我们使用 else 来改进这个脚本。

## 使用 if else 语句

现在我在前面的脚本中添加了一条 `else` 语句。这样，当你得到一个非零模数（因为奇数不能除以 2）时，它将进入 `else` 块。

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

让我们用相同的数字再次运行它：

![Running a bash script that checks odd even number](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/bash-if-else-example.png)

正如你所看到的，该脚本更好，因为它还告诉你该数字是否为奇数。

## 使用 elif（否则如果）语句

这是一个检查给定数字是正数还是负数的脚本。在数学中，0 既不是正数也不是负数。该脚本也检查了这一事实。

```Bash
#!/bin/bash

read -p "Enter the number: " num

if [ $num -lt 0 ]; then
	echo "Number $num is negative"
elif [ $num -gt 0 ]; then
	echo "Number $num is positive"
else
	echo "Number $num is zero"
fi
```

让我运行它来涵盖这里的所有三种情况：

![Running a script with bash elif statement](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/bash-elif.png)

## 用逻辑运算符组合多个条件

到目前为止，一切都很好。但是你是否知道通过使用与（&&）、或（||）等逻辑运算符可以在一个条件中包含多个条件？ 它使你能够编写复杂的条件。

让我们编写一个脚本来告诉你给定的年份是否是闰年。

你还记得闰年的条件吗？ 它应该被 4 整除，但如果它能被 100 整除，那么它就不是闰年。但是，如果能被 400 整除，则为闰年。

这是我的脚本。

```Bash
#!/bin/bash

read -p "Enter the year: " year

if [[ ($(($year%4)) -eq 0 && $(($year%100)) != 0) || ($(($year%400)) -eq 0) ]]; then
	echo "Year $year is leap year"
else
	echo "Year $year is normal year"
fi
```

> 💡 注意上面双括号 `[[ ]]` 的使用。如果你使用逻辑运算符，则这是强制性的。

通过使用不同的数据运行脚本来验证脚本：

![Example of running  bash script with logical operators in if statement](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/bash-logical-operators-in-if-else.png)

## 🏋️ 练习时间

让我们做一些练习吧 :)

**练习 1**：编写一个 Bash Shell 脚本，检查作为参数提供给它的字符串的长度。如果未提供参数，它将打印 “empty string”。

**练习 2**：编写一个 Shell 脚本来检查给定文件是否存在。你可以提供完整的文件路径作为参数或直接在脚本中使用它。

**提示**：文件使用 -f 选项

**练习 3**：通过检查给定文件是否是常规文件、目录或链接或者是否不存在来增强之前的脚本。

**提示**：使用 -f、-d 和 -L

**练习 3**：编写一个接受两个字符串参数的脚本。脚本应检查第一个字符串是否包含第二个参数的子串。

**提示**：请参阅上一章 [Bash 字符串](https://itsfoss.com/bash-strings/)

我希望你喜欢 Bash 基础知识系列。在下一章中，你将了解如何在 Bash 中使用循环。继续编写 Bash！


--------------------------------------------------------------------------------

>via: https://itsfoss.com/bash-if-else/
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