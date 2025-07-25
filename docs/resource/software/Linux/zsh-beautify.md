---
comments: true
---

# 配置一个简洁高效的 Zsh

Shell 是类 Unix 系统中超级好用的工具，而 Zsh 是 shell 中的佼佼者，但是现在网上一搜索 Zsh 的配置方案，遍地都是的互相复制粘贴的 oh-my-zsh 配置方案。**事实上 oh-my-zsh 并不好用**，严重拖慢了 Zsh 的速度，反而让你的工作并不高效。现在将我自己的使用方案分享给大家，教大家配置一个高效好用的 Zsh。

### 安装 Zsh

我笔记本电脑使用的是 ArchLinux，服务器使用的是 Ubuntu。主要介绍这两个发行版的配置方法，红帽系的发行版请自行尝试。

![img](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/223906vnc5jh7aacdnaihh.png)

我个人喜欢尽量从发行版的源里安装。从源安装具有方便，稳定，容易维护等优点。

#### 在 ArchLinux 安装 Zsh

终端里面输入：

```Bash
sudo pacman -Sy zsh
```

#### 在 Ubuntu 安装 Zsh

终端里面输入：

```Bash
sudo apt-get updatesudo apt-get install zsh
```

### 安装插件

我只需要两个插件：

- `zsh-autosuggestions`：这个是自动建议插件，能够自动提示你需要的命令。
- `zsh-syntax-highlighting`：这个是代码高亮插件，能够使你的命令行各个命令清晰明了。

还有一个主题：

- `zsh-theme-powerlevel10k` 这个主题提供漂亮的提示符，可以显示当前路径、时间、命令执行成功与否，还能够支持 git 分支显示等等。

同样是尽可能从源里面安装。

> Ubuntu 20.10 的源里面是 `powerlevel9k`，配置好后实际使用体验和 `powerlevel10k` 差别不大。

#### 在 ArchLinux 安装插件和主题

终端里面输入命令：

```Bash
sudo pacman -S zsh-autosuggestions zsh-syntax-highlighting zsh-theme-powerlevel10k zsh-completions
```

#### 在 Ubuntu 安装插件和主题

终端里面输入命令：

```Bash
sudo apt-get install zsh-autosuggestions zsh-syntax-highlighting zsh-theme-powerlevel9k
```

这样插件和主题就安装好了。

### 更改默认 shell，并配置插件和主题

安装好了之后就是启用 Zsh，并且配置插件和主题了。

#### 更改默认 shell

终端输入命令：

```Bash
chsh -s /usr/bin/zsh
```

ArchLinux 和 Ubuntu 都是同样的操作，然后注销并重新登录，就启用了 Zsh。第一次进入 Zsh 会自动出现一个配置界面，这个界面可以根据需要自定义 Zsh。

![img](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/223907orolqh0e4td0i040.png)

在这里输入 `1` 就可以进入配置界面了。

![img](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/223908l84l8f9rddlbqh9h.png)

配置界面中各个菜单代表的意思分别是：

- `1`：设置命令历史记录相关的选项
- `2`：设置命令补全系统
- `3`：设置热建
- `4`：选择各种常见的选项，只需要选择“On”或者“Off”
- `0`：退出，并使用空白（默认）配置
- `a`：终止设置并退出
- `q`：退出

这里根据提示，然后按照你自己的喜好配置就可以了。配置好后，会在你的用户目录下生成 `.zshrc` 文件。然后我们要去这个文件中启用插件和主题。

#### 配置插件和主题

Zsh 的配置文件是 `~/.zshrc` 文件，这个文件在你的用户目录下 `~/`。删掉了这个文件，再次进入 Zsh，又会触发 Zsh 的配置界面。

##### 在 ArchLinux 启用插件和主题

打开 `~/.zshrc` 文件，将以下行代码添加到其中：

```Bash
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zshsource /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zshsource /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme
```

##### 在 Ubuntu 启用插件和主题

打开 `~/.zshrc` 文件，将以下行代码添加到其中：

```Bash
source /usr/share/powerlevel9k/powerlevel9k.zsh-themesource /usr/share/zsh-autosuggestions/zsh-autosuggestions.zshsource /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
```

这样就成功的启用了插件和主题，插件不需要额外的配置就很好用，有额外配置需求的可以自行研究。

而 `powerlevel10k` 主题在首次进入时，会触发一个配置界面。

![img](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/223909zwayxxx5z7a6wpwv.png)

然后根据提示和你的喜好一步步完成配置即可。

![img](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/223910juq6p3noc63d3nlr.png)

这里可以选择你喜欢的提示符。

**配置完成后就可以愉快的使用啦！**

![img](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/223913ouug962ttgghzg98.png)

---

作者： [Chao-zhi](https://www.insidentally.com/2020/10/config-zsh/) 

原文：[https://linux.net.cn/article-13030-1.html](https://linux.net.cn/article-13030-1.html)