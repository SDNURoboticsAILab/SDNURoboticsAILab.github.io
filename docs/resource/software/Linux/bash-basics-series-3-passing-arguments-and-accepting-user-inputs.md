---
comments: true
---

# Bash 基础知识系列 #3：传递参数和接受用户输入

> 在 Bash 基础系列的这一章中，学习如何向 Bash 脚本传递参数并使它们具有交互性。

来让 Bash 脚本有参数吧 😉

你可以通过向 Bash 脚本传递变量来使其更加有用和更具交互性。

让我通过示例详细向你展示这一点。

## 将参数传递给 Shell 脚本

当你运行 Shell 脚本时，你可以按以下方式向其中添加其他变量：

```Bash
./my_script.sh var1 var2
```

在脚本内部，你可以使用 `$1` 作为第一个参数，`$2` 作为第二个参数，依此类推。

> 💡 `$0` 是一个特殊变量，保存正在执行的脚本的名称。

让我们通过一个实际的例子来看看。切换到保存练习 Bash 脚本的目录。

```Bash
mkdir -p bash_scripts && cd bash_scripts
```

现在，创建一个名为 `arguments.sh` （我想不出更好的名称）的新 Shell 脚本，并向其中添加以下行：

```Bash
#!/bin/bash

echo "Script name is: $0"
echo "First argument is: $1"
echo "Second argument is: $2"
```

保存文件并使其可执行。现在像往常一样运行脚本，但这次向其中添加任意两个字符串。你将看到屏幕上打印的详细信息。

> 🚧 参数由空格（空格、制表符）分隔。如果参数中有空格，请使用（英文）双引号将其引起来，否则它将被视为单独的参数。

![Pass arguments to the bash scripting](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/run-bash-script-with-arguments.png)

> 💡 Bash 脚本最多支持 255 个参数。但对于参数 10 及以上，你必须使用花括号 `${10}`、`${11}`...`${n}`。

正如你所看到的，`$0` 代表脚本名称，而其余参数存储在编号变量中。你还可以在脚本中使用一些其他特殊变量。

| 特殊变量 | 变量描述 |
| :- | :- |
| `$0` | 脚本名称 |
| `$1`、`$2`、……`$9` | 脚本参数 |
| `${n}` | 脚本参数从 10 到 255 |
| `$#` | 参数数量 |
| `$@` | 所有参数 |
| `$$` | 当前 Shell 的进程 ID |
| `$!` | 最后执行的命令的进程 ID |
| `$?` | 最后执行命令的退出状态 |

> 🏋️‍♀️ 修改上面的脚本以显示参数数量。

### 如果参数数量不匹配怎么办？

在上面的示例中，你为 Bash 脚本提供了两个参数并在脚本中使用了它们。

但是，如果你只提供一个参数或三个参数怎么办？

让我们实际做一下吧。

![Passing fewer or more arguments to bash script](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/passing-non-matching-arguments-bash-shell.png)

正如你在上面所看到的，当你提供的参数超出预期时，结果仍然是一样的。不使用其他参数，因此不会产生问题。

但是，当你提供的参数少于预期时，脚本将显示空白。如果脚本的一部分依赖于缺少的参数，这可能会出现问题。

## 接受用户输入并制作交互式 Bash 脚本

你还可以创建提示用户通过键盘提供输入的 Bash 脚本。这使你的脚本具有交互性。

`read` 命令提供了此功能。你可以这样使用它：

```Bash
echo "Enter something"
read var
```

上面的 `echo` 命令不是必需的，但最终用户不会知道他们必须提供输入。然后用户在按回车键之前输入的所有内容都存储在 `var` 变量中。

你还可以显示提示消息并在单行中获取值，如下所示：

```Bash
read -p "Enter something? " var
```

让我们看看它的实际效果。创建一个新的 `interactive.sh` Shell 脚本，内容如下：

```Bash
#!/bin/bash

echo "What is your name, stranger?"
read name
read -p "What's your full name, $name? " full_name
echo "Welcome, $full_name"
```

在上面的示例中，我使用 `name` 变量来获取名称。然后我在提示中使用 `name` 变量，并在 `full_name` 变量中获取用户输入。我使用了两种使用 `read` 命令的方法。

现在，如果你授予执行权限，然后运行此脚本，你会注意到该脚本显示 `What is your name, stranger?`，然后等待你从键盘输入内容。你提供输入，然后它会显示 `What's your full name` 消息，并再次等待输入。

以下是供你参考的示例输出：

![Interactive bash shell script](https://itsfoss.com/content/images/2023/06/interactive-bash-shell-script.png)

## 🏋️ 练习时间

是时候练习你所学到的东西了。尝试为以下场景编写简单的 Bash 脚本。

**练习 1**：编写一个带有三个参数的脚本。你必须使脚本以相反的顺序显示参数。

预期输出：

```Bash
abhishek@itsfoss:~/bash_scripts$ ./reverse.sh ubuntu fedora arch
Arguments in reverse order:
arch fedora ubuntu
```

**练习 2**：编写一个脚本，显示传递给它的参数数量。

提示：使用特殊变量 `$#`。

预期输出：

```Bash
abhishek@itsfoss:~/bash_scripts$ ./arguments.sh one and two and three
Total number of arguments: 5
```

**练习 3**：编写一个脚本，将文件名作为参数并显示其行号。

提示：使用 `wc` 命令来计算行号。

你可以在社区中讨论你的解决方案。

很好！ 现在你可以（传递）参数了 :) 在下一章中，你将学习在 Bash 中执行基本数学运算。


--------------------------------------------------------------------------------

>via: https://itsfoss.com/bash-pass-arguments/
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