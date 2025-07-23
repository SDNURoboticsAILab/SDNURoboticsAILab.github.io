---
comments: true
---

# Bash 基础知识系列 #4：算术运算

> 在本系列的第四章，学习在 Bash 中使用基本数学运算。

你可以使用 Bash 脚本做很多事情。对变量执行简单的算术运算就是其中之一。

Bash shell 中算术运算的语法如下：

```Bash
$((arithmetic_operation))
```

假设你必须计算两个变量的总和。你这样做：

```Bash
sum=$(($num1 + $num2))
```

`(())` 内空格的使用没有限制。你可以使用 `$(( $num1+ $num2))`、`$(( $num1+ $num2 ))` 或者 `$(( $num1+ $num2 ))`。它们都一样。

在通过示例详细讨论之前，我先分享一下它支持的算术运算符。

## Bash 中的基本算术运算符

以下是 Bash shell 中算术运算符的列表。

| 运算符 | 描述 |
| :- | :- |
| `+` | 加法 |
| `-` | 减法|
| `*` | 乘法|
| `/` | 整数除法（不带小数） |
| `%` | 模除法（仅余数）|
| `**` | 求幂（a 的 b 次方）|

> 🚧 Bash 不支持浮点数（小数）。你必须使用其他命令（例如 `bc`）来处理它们。

## Bash 中的加法和减法

让我们通过编写一个脚本来看看它，该脚本从用户那里获取两个数字，然后打印它们的总和和减法。

```Bash
#!/bin/bash

read -p "Enter first number: " num1
read -p "Enter second number: " num2

sum=$(($num1+$num2))
sub=$(($num1-$num2))
echo "The summation of $num1 and $num2 is $sum"
echo "The substraction of $num2 from $num1 is $sub"
```

我相信你熟悉上一章中使用 `read` 命令来 [在 Bash 中接受用户输入](https://itsfoss.com/bash-pass-arguments/)。

你应该关注这两行：

```Bash
sum=$(($num1+$num2))
sub=$(($num1-$num2))
```

将此脚本保存为 `sum.sh` 并运行它。给它一些输入并检查结果。

![Example of addition and subtraction in Bash shell script](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/addition-substraction-bash-script.png)

## Bash 中的乘法

现在让我们转向乘法。

这是一个将公里转换为米的示例脚本（这给美国读者带来了麻烦 :D）。作为参考，1 公里等于 1000 米。

```Bash
#!/bin/bash

read -p "Enter distance in kilometers: " km
meters=$(($km*1000))

echo "$km KM equals to $meters meters"
```

将脚本保存为 `multi.sh`，赋予其执行权限并运行它。这是一个示例输出：

![Multiplication in bash script](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/multiplication-bash-script.png)

看起来不错，不是吗？ 让我们继续进行除法。

## Bash 脚本中的除法

让我们用一个非常简单的脚本来看看除法：

```Bash
#!/bin/bash

num1=50
num2=5

result=$(($num1/$num2))

echo "The result is $result"
```

你很容易猜到结果：

```Bash
The result is 10
```

没关系。但是让我们更改数字并尝试将 50 除以 6。结果如下：

```Bash
The result is 8
```

**但这不正确。** 正确答案应该是 8.33333。

这是因为 Bash 默认情况下只处理整数。你需要额外的命令行工具来处理浮点（小数）。

最流行的工具是 [bc](https://www.gnu.org/software/bc/manual/html_mono/bc.html)，它是一种处理数学运算的非常强大的计算器语言。不过，你现在不需要关注细节。

你必须通过管道将算术运算“回显”给 `bc`：

```Bash
echo "$num1/$num2" | bc -l
```

于是，将之前的脚本修改为：

```Bash
#!/bin/bash

num1=50
num2=6

result=$(echo "$num1/$num2" | bc -l)

echo "The result is $result"
```

现在你得到结果：

```Bash
The result is 8.33333333333333333333
```

请注意 `result=$(echo "$num1/$num2" | bc -l)`，它现在使用你在 [本系列第 2 章](https://itsfoss.com/bash-use-variables/) 中看到的命令替换。

`-l` 选项加载标准数学库。默认情况下，`bc` 最多保留 20 位小数。你可以通过以下方式将比例更改为较小的位数：

```Bash
result=$(echo "scale=3; $num1/$num2" | bc -l)
```

让我们看看 Bash 中浮点的更多示例。

## 在 Bash 脚本中处理浮点

让我们修改 `sum.sh` 脚本来处理浮点。

```Bash
#!/bin/bash

read -p "Enter first number: " num1
read -p "Enter second number: " num2

sum=$( echo "$num1+$num2" | bc -l)
sub=$( echo "scale=2; $num1-$num2" | bc -l)
echo "The summation of $num1 and $num2 is $sum"
echo "The substraction of $num2 from $num1 is $sub"
```

现在尝试运行它，看看是否可以正确处理浮点：

![Floating points in bash script](https://itsfoss.com/content/images/2023/07/floating-point-bash.png)

## 🏋️🤸 练习时间

是时候一起做一些数学和 Bash 练习了。

**练习 1**：创建一个脚本，接受以 GB 为单位的输入并以 MB 和 KB 为单位输出其等效值。

**练习 2**：编写一个带有两个参数并以指数格式输出结果的脚本。因此，如果输入 2 和 3，输出将为 8，即 2 的 3 次方。

**提示**：使用幂运算符 `**`。

**练习 3**：编写一个将摄氏度转换为华氏度的脚本。

**提示**：使用公式 F = C x (9/5) + 32。你必须在此处使用 `bc` 命令。

你可以在社区中讨论练习及其方案。

在下一章中，你将 [了解 Bash 中的数组](https://itsfoss.com/bash-arrays/)。敬请关注。


--------------------------------------------------------------------------------

>via: https://itsfoss.com/bash-arithmetic-operation/
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