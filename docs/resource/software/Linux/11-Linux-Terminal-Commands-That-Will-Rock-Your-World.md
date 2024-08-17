# 11个让你吃惊的 Linux 终端命令

作者： [Gary Newell](http://linux.about.com/od/commands/tp/11-Linux-Terminal-Commands-That-Will-Rock-Your-World.htm) 译者： [LCTT](https://linux.cn/lctt/) [Martin♡Adele](https://linux.cn/lctt/martin2011qi) 

| 2015-05-13 07:28  评论: [*13*](https://linux.cn/portal.php?mod=comment&id=5438&idtype=aid) 收藏: *22*  

我已经用了十年的Linux了，通过今天这篇文章我将向大家展示一系列的命令、工具和技巧，我希望一开始就有人告诉我这些，而不是曾在我成长道路上绊住我。

![img](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/233512pz5y93dzryzy9fur.png)

### 1. 命令行日常系快捷键

如下的快捷方式非常有用，能够极大的提升你的工作效率：

- CTRL + U - 剪切光标前的内容
- CTRL + K - 剪切光标至行末的内容
- CTRL + Y - 粘贴
- CTRL + E - 移动光标到行末
- CTRL + A - 移动光标到行首
- ALT + F - 跳向下一个空格
- ALT + B - 跳回上一个空格
- ALT + Backspace - 删除前一个单词
- CTRL + W - 剪切光标前一个单词
- Shift + Insert - 向终端内粘贴文本

那么为了让上述内容更易理解来看下面的这行命令。

```Bash
sudo apt-get intall programname
```

如你所见，命令中存在拼写错误，为了正常执行需要把“intall”替换成“install”。

想象现在光标正在行末，我们有很多的方法将她退回单词install并替换它。

我可以按两次ALT+B这样光标就会在如下的位置（这里用指代光标的位置）。

```Bash
sudo apt-get^intall programname
```

现在你可以按两下方向键并将“s”插入到install中去了。

如果你想将浏览器中的文本复制到终端，可以使用快捷键"shift + insert"。

### 2. SUDO !!

如果你还不知道这个命令，我觉得你应该好好感谢我，因为如果你不知道的话，那每次你在输入长串命令后看到“permission denied”后一定会痛苦不堪。

- sudo !!

如何使用sudo !!？很简单。试想你刚输入了如下命令：

```Bash
apt-get install ranger
```

一定会出现“Permission denied”，除非你已经登录了足够高权限的账户。

sudo !! 就会用 sudo 的形式运行上一条命令。所以上一条命令就变成了这样：

```Bash
sudo apt-get install ranger
```

如果你不知道什么是sudo，[戳这里](http://linux.about.com/cs/linux101/g/sudo.htm)。

（**警告！主页君强烈反对使用这个命令，因为如果万一上个命令存在一些笔误或者你搞错了哪条是上一条命令，那么有可能带来的后果是灾难性的！所以，千万不要执行这条命令！千万不要执行这条命令！千万不要执行这条命令！重要的事情重复三遍。**）

### 3. 暂停并在后台运行命令

我曾经写过一篇[如何在终端后台运行命令的指南](http://linux.about.com/od/commands/fl/How-To-Run-Linux-Programs-From-The-Terminal-In-Background-Mode.htm)。

- CTRL + Z - 暂停应用程序
- fg - 重新将程序唤到前台

如何使用这个技巧呢?

试想你正用nano编辑一个文件：

```Bash
sudo nano abc.txt
```

文件编辑到一半你意识到你需要马上在终端输入些命令，但是nano在前台运行让你不能输入。

你可能觉得唯一的方法就是保存文件，退出 nano，运行命令以后在重新打开nano。

其实你只要按CTRL + Z，前台的命令就会暂停，画面就切回到命令行了。然后你就能运行你想要运行命令，等命令运行完后在终端窗口输入“fg”就可以回到先前暂停的任务。

有一个尝试非常有趣就是用nano打开文件，输入一些东西然后暂停会话。再用nano打开另一个文件，输入一些什么后再暂停会话。如果你输入“fg”你将回到第二个用nano打开的文件。只有退出nano再输入“fg”，你才会回到第一个用nano打开的文件。

### 4. 使用nohup在登出SSH会话后仍运行命令

如果你用ssh登录别的机器时，[nohup命令](http://linux.about.com/library/cmd/blcmdl1_nohup.htm)真的非常有用。

那么怎么使用nohup呢？

想象一下你使用ssh远程登录到另一台电脑上，你运行了一条非常耗时的命令然后退出了ssh会话，不过命令仍在执行。而nohup可以将这一场景变成现实。

举个例子，因为测试的需要，我用我的[树莓派](http://linux.about.com/od/mobiledevicesother/a/Raspberry-Pi-Computer-Running-Linux.htm)来下载发行版。我绝对不会给我的树莓派外接显示器、键盘或鼠标。

一般我总是用[SSH](http://linux.about.com/od/commands/l/blcmdl1_ssh.htm)从笔记本电脑连接到树莓派。如果我在不用nohup的情况下使用树莓派下载大型文件，那我就必须等待到下载完成后，才能登出ssh会话关掉笔记本。可如果是这样，那我为什么要使用树莓派下文件呢？

使用nohup的方法也很简单，只需如下例中在nohup后输入要执行的命令即可：

```Bash
nohup wget http://mirror.is.co.za/mirrors/linuxmint.com/iso//stable/17.1/linuxmint-17.1-cinnamon-64bit.iso &
```

### 5. ‘在（at）’特定的时间运行Linux命令

‘nohup’命令在你用SSH连接到服务器，并在上面保持执行SSH登出前任务的时候十分有用。

想一下如果你需要在特定的时间执行相同的命令，这种情况该怎么办呢？

命令‘at’就能妥善解决这一情况。以下是‘at’使用示例。

```Bash
at 10:38 PM Friat> cowsay 'hello'at> CTRL + D
```

上面的命令能在周五下午10时38分运行程序[cowsay](http://linux.about.com/cs/linux101/g/cowsay.htm)。

使用的语法就是‘at’后追加日期时间。当at>提示符出现后就可以输入你想在那个时间运行的命令了。

CTRL + D 返回终端。

还有许多日期和时间的格式，都需要你好好翻一翻‘at’的man手册来找到更多的使用方式。

### 6. Man手册

Man手册会为你列出命令和参数的使用大纲，教你如何使用她们。Man手册看起来沉闷呆板。（我思忖她们也不是被设计来娱乐我们的）。

不过这不代表你不能做些什么来使她们变得漂亮些。

```Bash
export PAGER=most
```

你需要安装 ‘most’；她会使你的你的man手册的色彩更加绚丽。

你可以用以下命令给man手册设定指定的行长：

```Bash
export MANWIDTH=80
```

最后，如果你有一个可用的浏览器，你可以使用-H在默认浏览器中打开任意的man页。

```Bash
man -H <command>
```

注意啦，以上的命令只有在你将默认的浏览器设置到环境变量$BROWSER中了之后才效果哟。

### 7. 使用htop查看和管理进程

你用哪个命令找出电脑上正在运行的进程的呢？我敢打赌是‘[ps](http://linux.about.com/od/commands/l/blcmdl1_ps.htm)’并在其后加不同的参数来得到你所想要的不同输出。

安装‘[htop](http://www.linux.com/community/blogs/133-general-linux/745323-5-commands-to-check-memory-usage-on-linux)’吧！绝对让你相见恨晚。

htop在终端中将进程以列表的方式呈现，有点类似于Windows中的任务管理器。你可以使用功能键的组合来切换排列的方式和展示出来的项。你也可以在htop中直接杀死进程。

在终端中简单的输入htop即可运行。

```Bash
htop
```

### 8. 使用ranger浏览文件系统

如果说htop是命令行进程控制的好帮手，那么[ranger](http://ranger.nongnu.org/)就是命令行浏览文件系统的好帮手。

你在用之前可能需要先安装，不过一旦安装了以后就可以在命令行输入以下命令启动她：

```Bash
ranger
```

在命令行窗口中ranger和一些别的文件管理器很像，但是相比上下结构布局，她是左右结构的，这意味着你按左方向键你将前进到上一个文件夹，而右方向键则会切换到下一个。

在使用前ranger的man手册还是值得一读的，这样你就可以用快捷键操作ranger了。

### 9. 取消关机

无论是在命令行还是图形用户界面[关机](http://linux.about.com/od/commands/l/blcmdl8_shutdow.htm)后，才发现自己不是真的想要关机。

```Bash
shutdown -c
```

需要注意的是，如果关机已经开始则有可能来不及停止关机。

以下是另一个可以尝试命令：

- [pkill](http://linux.about.com/library/cmd/blcmdl1_pkill.htm) shutdown

### 10. 杀死挂起进程的简单方法

想象一下，你正在运行的应用程序不明原因的僵死了。

你可以使用‘ps -ef’来找到该进程后杀掉或者使用‘htop’。

有一个更快、更容易的命令叫做[xkill](http://linux.about.com/od/funnymanpages/a/funman_xkill.htm)。

简单的在终端中输入以下命令并在窗口中点击你想杀死的应用程序。

```Bash
xkill
```

那如果整个系统挂掉了怎么办呢？

按住键盘上的‘alt’和‘sysrq’不放，然后慢慢输入以下键：

- [REISUB](http://blog.kember.net/articles/reisub-the-gentle-linux-restart/)

这样不按电源键你的计算机也能重启了。

### 11. 下载Youtube视频

一般来说我们大多数人都喜欢看Youtube的视频，也会通过钟爱的播放器播放Youtube的流媒体。

如果你需要离线一段时间（比如：从苏格兰南部坐飞机到英格兰南部旅游的这段时间）那么你可能希望下载一些视频到存储设备中，到闲暇时观看。

你所要做的就是从包管理器中安装youtube-dl。

你可以用以下命令使用youtube-dl：

```Bash
youtube-dl url-to-video
```

你可以在Youtubu视频页面点击分享链接得到视频的url。只要简单的复制链接在粘帖到命令行就行了（要用shift + insert快捷键哟）。

### 总结

希望你在这篇文章中得到帮助，并且在这11条中找到至少一条让你惊叹“原来可以这样”的技巧。

------

>via: http://linux.about.com/od/commands/tp/11-Linux-Terminal-Commands-That-Will-Rock-Your-World.htm
>
>作者：[Gary Newell](http://linux.about.com/bio/Gary-Newell-132058.htm) 
>
>译者：[martin2011qi](https://github.com/martin2011qi) 
>
>校对：[wxy](https://github.com/wxy)
>
>本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](https://linux.cn/article-5438-1.html) 荣誉推出