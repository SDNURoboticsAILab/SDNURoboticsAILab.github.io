---
comments: true
---

# 21 个专业 Linux 用户喜爱的实用终端快捷键

> 掌握这些极致实用的快捷键，让你的 Linux 终端操作效率大幅提升。

学习 Linux 命令无疑是你的首要任务，但当你能熟练 [运用命令行](https://itsfoss.com/linux-terminal-basics/) 之后，有另一样东西值得你去关注。

**那就是终端快捷键！**

如果你不知道如何利用它们提升终端会话的效率，那你就无法真正理解它们的重要性。

在本教程中，我将为你详细讲解顶级的终端快捷键，并且举例说明它们的用法。

在我逐一解释快捷键之前，先来看一下这个备忘录，它对我将在本教程中讨论的内容进行了概览：

| 快捷键                            | 功能描述                               |
| --------------------------------- | -------------------------------------- |
| `Ctrl + A`                        | 光标快速跳至行首。                     |
| `Ctrl + E`                        | 光标快速跳至行尾。                     |
| `Ctrl + U`                        | 删除光标至行首的所有内容。             |
| `Ctrl + K`                        | 删除光标至行尾的所有内容。             |
| `Ctrl + W`                        | 删除光标前的一个单词。                 |
| `Ctrl + L`                        | 清空整个终端屏幕。                     |
| `Ctrl + C`                        | 停止正在执行的进程或命令。             |
| `Ctrl + D`                        | 注销或退出终端。                       |
| `Ctrl + Z`                        | 暂停正在执行的进程（之后可恢复执行）。 |
| `Ctrl + R`                        | 在命令历史中进行逆向搜索。             |
| 上箭头 `↑`                        | 从命令历史中显示先前的命令。           |
| 下箭头 `↓`                        | 从命令历史中显示后续的命令。           |
| `!!`                              | 重复执行最近的命令。                   |
| `!n`                              | 重复执行命令历史中的第 n 条命令。      |
| `Tab`                             | 自动补全命令，文件名或目录名。         |
| 连续按 `Tab` 两次                 | 列出所有可能的补全选项。               |
| `Ctrl + Shift + C`                | 复制所选文本或命令。                   |
| `Ctrl + Shift + V`                | 粘贴已复制的文本或命令。               |
| `Ctrl + Shift + N`                | 打开新的终端窗口。                     |
| `Ctrl + Shift + T`                | 在当前终端中打开新的选项卡。           |
| `Ctrl + Tab` 或 `Ctrl + PageDown` | 在终端的选项卡之间切换。               |

> 📋 虽然我在这篇文章中用的是大写字母，但实际上我们不需要使用大写来输入它们。比如 `Ctrl+A`，意思是同时按下 `Ctrl` 键和 `A` 键，并不意味着需要同时按下 `Shift` 键和 `a` 键来输入大写的 `A`。

接下来，我们更详细地看看这些快捷键如何使用。

### 1、Ctrl + A：光标切换至行首

当你在终端中按下 `Ctrl + A` 组合键，光标就会迅速跳到命令的起始处。这个功能在你需要修改一条长命令序列起始部分的时候十分实用。

例如，在以下示例中，你可以看到无论光标处在何位置，只需按下 `Ctrl + A`，光标就会立刻跳转至行首：

![使用 Ctrl + A 快捷键在 Linux 终端内前往行首](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154055bqykmehuomonitbl.svg)

*使用 Ctrl + A 快捷键在 Linux 终端内前往行首*

### 2、Ctrl + E：光标切换至行尾

在使用终端的过程中，如果你想迅速跳到当前行的末尾，直接按下 `Ctrl + E` 组合键就可以了。

在下面的示例中，我使用了一段样本文本，并按下 `Ctrl + E` 来快速移动到行尾：

![使用 Ctrl + E 在 linux 终端内前往行尾](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154055ud6867z7uk132176.svg)

*使用 Ctrl + E 在 linux 终端内前往行尾*

### 3、Ctrl + U：删除光标位置至行首的内容

有些时候，你可能需要删除从光标位置到行首的所有内容。

此时，你只需使用左箭头键将光标移动至你想要开始删除的位置，然后按下 `Ctrl + U` ：

![使用 Ctrl+U 从光标位置删除到行首的内容](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154055ig0ojsh0mfhch60r.svg)

*使用 Ctrl+U 从光标位置删除到行首的内容*

> 💡 在输完 `sudo` 命令输入密码时，不确定是否输入正确？没必要用退格键一路删除，只需简单地使用 `Ctrl+U` 快捷键重新开始输入密码即可。

### 4、Ctrl + K：从光标删除至行尾

如你所猜想，当你按下 `Ctrl + K` ，它会移除光标至行尾的所有内容（光标位置右侧的所有）。

使用这种快捷操作时，你先要把光标放在你想从那里开始删除的位置，然后按下 `Ctrl + K`，如下图展示的那样：

![在 Linux 终端利用 Ctrl + K 删除光标至行尾的内容](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154055lv6y3zjmo6e6c7tc.svg)

*在 Linux 终端利用 Ctrl + K 删除光标至行尾的内容*

### 5、Ctrl + W：删除光标前的一个词

我日常常用该快捷键，因为我时常打错命令，需要删除命令的一部分，这个时候只需要简单地按 `Ctrl + W` 就可以了。

当你按下 `Ctrl + W` 键时，它只会删除光标前的一个词：

![在 Linux 终端通过按 Ctrl + W 删除光标前的一个词](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154055kejskkkdir5k16s7.svg)

*在 Linux 终端通过按 Ctrl + W 删除光标前的一个词*

### 6、Ctrl + L：清理终端显示（或者理解为整理显示内容）

按下 `Ctrl + L` 并不会彻底地 [清空终端显示](https://itsfoss.com/clear-terminal-ubuntu/)，但它可以整理显示内容。如果你向上滚动，你还能找到之前的命令和执行记录。

它与 `clear` 命令有所不同。`clear` 命令会消除历史记录，而且你会在命令历史中找到 `clear` 命令的执行。

但是当你按下 `Ctrl + L` 时，它只是整理当前屏幕的显示内容，并不会出现在历史记录中，因为它本身并不是一条命令。

比如在这个示例中，我执行了历史命令，随后按下 `Ctrl + L` 键进行了屏幕清理：

![利用 Ctrl+L 清理 Linux 终端屏幕显示](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154055kwf4fee4v4u4ve1d.svg)

*利用 Ctrl+L 清理 Linux 终端屏幕显示*

### 7、Ctrl + C：终止当前进程/执行

有没有想要 [停止进行中的命令](https://itsfoss.com/stop-program-linux-terminal/)，却不知所措，最后只好关闭终端呢？解决办法其实很简单，按下 `Ctrl + C` 就行了。

当你按下这一组键时，它将发送 `SIGINT` 信号以终别过程。

例如，在这里，我结束了正在执行的命令进程：

![利用 Ctrl+C 终端快捷键来中止运行中的命令](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154055y9gx3sd9sgyygv46.svg)

*利用 Ctrl+C 终端快捷键来中止运行中的命令*

最后，你会看到 `^C` 符号，表示你按下了 `Ctrl + C` 来中止当前执行。

但是，有些进程可能不会被 `Ctrl + C` 信号所中止，此时，你可以使用 Linux 中的其他 [中止信号](https://linuxhandbook.com/termination-signals/) 来终止。

> **[如何在 Linux 中使用 SIGINT 和其它中止信号](https://linuxhandbook.com/termination-signals/)**

### 8、Ctrl + D：退出登录或者退出终端

你总是可以使用 `exit` 命令来关闭 Shell 会话和终端。你也可以选择使用 `Ctrl+D` 快捷键。

当你按 `Ctrl + D` 时，如果你正在 SSH 中使用，它会结束会话，如果再次按下，它将直接关闭终端：

![利用 Ctrl+D 来关闭会话](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154055wv444bm3syjzzv1l.gif)

*利用 Ctrl+D 来关闭会话*

### 9、Ctrl + Z：暂停当前进程

总是杀掉命令并不是个好主意，因为你有可能需要重新启动过程。

这种情况下，你可以按 `Ctrl + Z` 来暂停当前的进程，然后可以从之前暂停的地方继续。

例如，在这里，我暂停了更新进程：

![利用 Ctrl+Z 挂起一个进程](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154055n1oofbgaz3wiz4gp.gif)

*利用 Ctrl+Z 挂起一个进程*

你想更多地了解 [如何暂停命令及如何恢复它们](https://linuxhandbook.com/suspend-resume-process/) 吗？这里有一篇为此准备的详细指南：

> **[如何在 Linux 中暂停并稍后恢复一个进程](https://linuxhandbook.com/content/images/size/w256h256/2021/08/Linux-Handbook-New-Logo.png)**

### 10、Ctrl + R：搜索命令历史

当你按 `Ctrl + R` 时，它会打开一个搜索模式的提示，从中你可以键入命令的任何部分，并将找到匹配你输入的字符串的命令。

一旦你找到那个命令，只需按 `Enter` 键，它就会执行那个命令。

例如，在这里，我搜索了 `update`，返回的结果是在 Ubuntu 中的仓库更新命令（`sudo apt update`）：

![利用 Ctrl + R 快捷键从历史记录中搜索命令](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154055h26r4oo525aqyjau.svg)

*利用 Ctrl + R 快捷键从历史记录中搜索命令*

> 📋 如果你对历史记录中的任何建议都不满意，可以使用 `Ctrl+C` 退出搜索模式。

### 11、上箭头：呈现命令历史中的上一条

当你按下上箭头 `↑` 键时，命令历史中之前执行过的命令将会按次序逐一显示：

![使用箭头键向下遍历历史记录](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154055rihh99oo6z2lwsok.svg)

*使用箭头键向下遍历历史记录*

### 12、下箭头：呈现命令历史中的下一条

当你按下上箭头 `↑` 键时，它会展示先前的命令，但在有些情况下，你可能无意间点击了多次，这时你希望展示之前已显示过的命令。

这个时候，你可以使用下箭头 `↓` 键。

在以下图示中，我首先多次按下了上箭头键，然后为了返回到先前显示的命令，我按下了下箭头键：

![使用箭头键向下遍历历史记录](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154055xhf7gz05f7745ce9.svg)

*使用箭头键向下遍历历史记录*

> 📋 `Page Up` 和 `Page Down` 键也可以用于同样的目的。

### 13、!!：重复最后一条命令

有时候，你可能需要重复执行一次或多次最近的命令，此时你只需要输入 `!!`（两个感叹号）即可：

```Bash
!!
```

比如，在这里，我执行了一个 `echo` 命令，随后我用了 `!!` 来重复执行相同的命令：

![!! 命令能够重复执行你最近在终端输入的命令](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154055ogdquq1o7szqduzu.png)

*!! 命令能够重复执行你最近在终端输入的命令*

但是，这个快捷键最常用且最实用的场景是，当你忘记给命令加上 `sudo`。这样你无需重新输入整个命令，只需使用 `sudo !!` 就可以了

![在 Linux 终端中使用 !! 快捷键的实践应用](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154056ebbzsbbtfapbtmtv.png)

*在 Linux 终端中使用 !! 快捷键的实践应用*

> 💡 一个类似的键盘快捷键是 `Alt+.`，这个快捷键会给你提供上一条命令的最后一个参数或部分。假设你刚使用了 `ls /etc/apt/sources.list.d`，现在你想进入这个目录。只需输入 `cd` 然后使用 `Alt+.` 就可以。这就如同你输入 `cd /etc/apt/sources.list.d` 一样。

### 14、!n：重播历史中的第 n 条命令

你可以通过执行 Bash 的 `history` 命令来查看命令历史，每个命令都会有一个相应的索引号：

```Bash
history
```

![从历史中选择命令](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154056a0kirbe560k0fi58.png)

*从历史中选择命令*

现在，假设我想要执行倒数第二个 `echo` 命令，我会这样使用：

```Bash
!1998
```

![img](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154056irs3pqmh2p3h4e6p.png)

### 15、Tab：命令自动补全

我认为这应是终端快捷键列表的首个条目。

在输入长命令时，你可以输入一部分，然后点击 `Tab` 键，它将为你进行自动补全。

例如，这里，我通过 `Tab` 键来自动完成我的脚本执行：

![点击 Tab 来查看命令，选项与参数建议](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154056lbdkbrqvcsnrcwt2.svg)

*点击 Tab 来查看命令，选项与参数建议*

### 16、Tab（连击两次）：列出所有可能的自动补全

如果按 `Tab` 键无效果，那可能是因为当前输入的命令存在多种可能。

在这种场合，你可以连击两次 `Tab` 键，以列出所有可能的补全选项：

![连击两次 Tab 键可列出所有可能的自动补全建议](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154056t8i896s24yk6i9bn.svg)

*连击两次 Tab 键可列出所有可能的自动补全建议*

> ✋ 接下来的一些快捷键取决于终端的模拟器。虽然这些快捷键应该适用于大多数的终端应用，但不能完全确定。

### 17、Ctrl + Shift + C：复制所选文本

[复制终端中的文本](https://itsfoss.com/copy-paste-linux-terminal/)，你需要先用鼠标选取文本，然后按下 `Ctrl + Shift + C` 来复制选中的内容：

![按下 Ctrl+Shift+C 进行复制](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154056dw3dn9933u9lzlu4.gif)

*按下 Ctrl+Shift+C 进行复制*

### 18、Ctrl + Shift + V：粘贴已复制的文本

当你通过选取和按下 `Ctrl + Shift + C` 复制了文本后，你可以通过按下 `Ctrl + Shift + V` 在任何地方粘贴：

![在终端按下 Ctrl+Shift+V 进行粘贴](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154056y4gidg8s2844ddga.gif)

*在终端按下 Ctrl+Shift+V 进行粘贴*

### 19、Ctrl + Shift + N：打开新的终端窗口

当你按下 `Ctrl + Shift + N` 时，会打开一个新的终端窗口，且新窗口的工作目录与之前那个窗口内的工作目录相同：

![img](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154016byv1rs9p5o9411e1.gif)

### 20、Ctrl + Shift + T：开启新的终端标签页

就像使用网络浏览器一样，终端也支持开启多个标签页来进行不同的任务。要开启一个新的标签页，只需按下 `Ctrl + Shift + T` 就可以了：

![img](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154056vc4edtrzrhtcrtdt.gif)

### 21、Ctrl + Tab 或 Ctrl + PageDown：切换标签页

如果你按照之前的方式创建了多个标签页，你或许需要在它们之间进行切换。

为此，你可以使用 `Ctrl + Tab` 或 `Ctrl + PageDown`：

![img](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/154056czxnd51m31s3snod.gif)

> 💡 这可能更多是 Ubuntu 的功能。你可以通过 [按下 Ctrl+Alt+T 键来打开新的终端窗口](https://itsfoss.com/open-terminal-ubuntu/)。

### 接下来：必知的 Linux 命令

你喜欢这个“必备”键盘快捷键列表吗？可能你会对 [最基本却必备的 Linux 命令列表](https://itsfoss.com/essential-ubuntu-commands/) 也感兴趣：

> **[31 个最基本却必备的 Ubuntu Linux 命令](https://itsfoss.com/essential-ubuntu-commands/)**

我明白起初你可能不容易记住所有这些终端快捷键。但通过不断实践，它们会逐渐深入你的肌肉记忆。

另外，你有一些没有在这里列出的钟爱的快捷键吗？欢迎在评论区分享。

------

> via: https://itsfoss.com/linux-terminal-shortcuts/
>
> 作者：[Sagar Sharma](https://itsfoss.com/author/sagar/) 
> 
> 选题：[lujun9972](https://github.com/lujun9972) 
> 
> 译者：[ChatGPT](https://linux.net.cn/lctt/ChatGPT) 
> 
> 校对：[wxy](https://github.com/wxy)
>
> 本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.net.cn/article-16228-1.html) 荣誉推出