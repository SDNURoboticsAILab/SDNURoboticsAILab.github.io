---
comments: true
---
## 前情提要

在 Windows 下想要完成 Linux 虚拟机的搭建，通常有以下几种常用方法：

1. VMware Workstation 或者 VirtualBox
   - **易于使用**：都具有直观的界面和易于使用的工具，使得创建和管理虚拟机变得非常简单。
   - **广泛兼容性**：是广泛使用的虚拟化软件，支持多种操作系统，包括各种Linux发行版。
   - **性能开销**：虚拟化层会带来一定的性能开销，尤其是在CPU和内存密集型任务中。

2. Hyper-V
   - **集成度高**：Hyper-V是Windows自带的虚拟化技术，与操作系统集成度高，无需安装额外软件即可使用。
   - **性能较好**：Hyper-V的性能通常优于第三方虚拟化软件，尤其是在网络和存储方面。
   - **安全性**：Hyper-V提供了一些高级安全功能，如虚拟机隔离、安全启动等。
   - **支持嵌套虚拟化**：可以在Hyper-V虚拟机中再运行其他虚拟机，适合需要多层虚拟化的场景。
   - **兼容性问题**：某些Linux发行版在Hyper-V上可能会有兼容性问题，尤其是在显卡驱动和网络配置方面。
   - **资源占用**：Hyper-V会占用较多的系统资源，尤其是在启用多个虚拟机时。

3. WSL
   - **简单轻量**：WSL是一个轻量级的Linux子系统，可以在Windows系统上直接运行Linux命令行工具，无需额外的虚拟机。
   - **与Windows集成**：WSL与Windows更好地集成，可以直接访问Windows文件系统，无需进行繁琐的文件共享设置。
   - **性能较好**：相对于传统虚拟机，WSL在性能上可能更加高效。
   - **不支持图形界面**：WSL目前主要支持命令行工具，不适合需要图形界面的应用程序。
   - **功能有限**：相较于完整的虚拟机，WSL在功能上可能有一定的限制，特别是对于需要完整Linux环境的应用场景。

本文将逐一介绍 VMware Workstation 安装 Ubuntu 22.04、Hyper-v 安装 Debian 12、WSL 安装 Ubuntu。

## 获取系统镜像

### 开源镜像站

常用的开源镜像站有：

[清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/)

[USTC Open Source Software Mirror](https://mirrors.ustc.edu.cn/)

[阿里巴巴开源镜像站](https://developer.aliyun.com/mirror/)

[华为开源镜像站](https://mirrors.huaweicloud.com/home)

以[清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/)为例，进入网站，选择右侧“获取下载链接”

![image-20241024201915228](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024201915228.png)

![image-20241024202007670](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024202007670.png)

在弹出的窗口中，左侧列表（CentOS，Debian，Fedora，Ubuntu）为不同的 Linux 发行版本，右侧为每个发行版下载镜像的链接。

以 Debian 为例简单解释一下关键字

- 12.7.0：这是指 Debian 操作系统的版本号，表示该版本是 Debian 12 的第七个小版本更新
- 小括号的第一个参数表示镜像适用的操作系统架构，包括 amd64，arm64，arm64，armhf，
  i386 等，一般选择 amd64
- Cinnamon，GNOME，KDE，LXDE，LXQt，MATE，Xfce 等：表示镜像包含的桌面环境
- DVD, Part 1：包含大量软件包，相对应的镜像体积也很大，适合在没有网络连接的情况下安装。通
  常会分为多部分（如Part 1、Part 2等），但 Part 1通常是最重要的。
- netinst：网络安装镜像，较小的ISO文件，安装时需要通过网络下载软件包。
- live：带有特定桌面环境的实时系统，可以不安装直接运行，用于体验和测试系统。安装后也是相
  应的桌面环境。
- BD, Part 1：适用于蓝光光盘（Blu-ray Disc）的镜像，包含更多软件包。
- mac：为苹果电脑的硬件做了特别优化的版本，通常适用于旧款Mac设备。
- edu： Debian 的教育版本，预装了一些适合教育环境的软件和工具
- Ubuntu这边，大体与Debian类似，但是需要注意：
- desktop：桌面版，带有图形用户界面（如GNOME、KDE等），适合个人用户或办公环境使用，预
  装了图形化工具和应用程序。
- server：服务器版，通常不包含图形界面，适用于服务器环境，强调性能和安全性。常用于搭建网
  络服务、数据库、文件服务器等。

而对于Ubuntu，大体与Debian类似：

- desktop：桌面版，带有图形用户界面（默认为 GNOME），适合个人用户或办公环境使用，预
  装了图形化工具和应用程序。
- server：服务器版，通常不包含图形界面，适用于服务器环境，强调性能和安全性。常用于搭建网
  络服务、数据库、文件服务器等。

鼓励大家多多尝试不同的发行版本和不同的桌面环境。

### 猹盘系统镜像频道

https://ed.qcea.top/ChaIndex/Systems

点击“Linux”；收录了常用和很多经典的 Linux 发行版镜像，可能没有收录较新的 Linux 发行版。

### 一些常用的发行版直链

[ubuntu-22.04.4-desktop-amd64.iso](https://mirrors.tuna.tsinghua.edu.cn/ubuntu-releases/jammy/ubuntu-22.04.4-desktop-amd64.iso)

[debian-live-12.7.0-amd64-kde.iso](https://mirrors.tuna.tsinghua.edu.cn/debian-cd/current-live/amd64/iso-hybrid/debian-live-12.7.0-amd64-kde.iso)

[kali-linux-2024.3-installer-amd64.iso](https://mirrors.tuna.tsinghua.edu.cn/kali-images/current/kali-linux-2024.3-installer-amd64.iso)

## 使用 VMware Workstation 安装 Ubuntu 22.04

### 安装 VMware Workstation

[按住Ctrl点击这里（彩色字体是超链接，这是标准打开方法）下载Vmware Workstation](https://ed.qcea.top/ChaIndex/Softwares/Windows/System/VirtualMachine/Vmware/VMware-workstation-full-17.6.1-24319023.exe)或者打开群文件发的安装包

一直点下一步就可以

![image-20241024202133350](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024202133350.png)

默认安装在 C 即可，VMware Workstation 本身不会占用很多内存。想要更改安装目录的话记得装在一个自己知道的位置，注意路径不要**放在 D 盘根目录**（请参考下图设置）

![image-20241024202330130](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024202330130.png)

“用户体验设置”推荐全部取消勾选

![image-20241024202425744](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024202425744.png)

最后点击“完成”

![image-20241024202554327](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024202554327.png)

第一次打开 VMware Workstation 会提示输入许可证密钥，我们选择“将VMware Workstation 17 用于“个人用途”，然后点击“继续”

![image-20241024203105397](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024203105397.png)

### 创建新的虚拟机

选择“创建新的虚拟机”

![image-20241024203156849](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024203156849.png)

选择“自定义” → “下一步”

![image-20241024203210089](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024203210089.png)

选择“稍后安装操作系统”，点击“下一步”

![image-20241024203231361](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024203231361.png)

客户机操作系统选择“Linux”，版本选择“Ubuntu 64 位”（取决于想要安装的系统镜像和版本），点击“下一步”

![image-20241024203251328](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024203251328.png)

虚拟机名称随意，位置根据实际情况选择。虚拟机**占用存储空间较大**且由**很多文件**组成，建议选择一个自己**记得住且空间足够**的位置，**为每个虚拟机单独建立一个文件夹安装**。

![image-20241024203630894](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024203630894.png)

处理器数量设置为 1，内核数量建议根据自己需求和电脑配置（**不要超过电脑本身的内核数**）设置。

![image-20241023100430358](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241023100430358.png)

如果不知道自己电脑 CPU 的内核数，可以右键任务栏空白处 → “任务管理器” → 侧边栏点击“性能” → “CPU” → 在红色框区域内右键 → “将图形更改为” → “逻辑处理器”，数红色框区域有几个小框框，就是 CPU 有几个内核。

![image-20241024204409656](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024204409656.png)

虚拟机内存大小可以根据需求设置，推荐 4-8 G，点击“4 G”即可快速设置。

![image-20241024204851085](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024204851085.png)

虚拟磁盘大小根据需求设置，建议不低于 20 G。

注意，**不要勾选**“立即分配所有磁盘空间”，这样虚拟机实际使用多少空间，就会占用电脑多少空间，而不是一次性占用设置的磁盘大小。

![image-20241024205134850](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024205134850.png)

完成虚拟机创建后，选择下载好的系统镜像，点击“确定”

![image-20241024205758818](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024205758818.png)

点击“▶️开启此虚拟机”进行开机。

如果提示“您在运行该虚拟机时启用了侧通道缓解。侧通道缓解可增强安全性，但也会降低性能。”，关闭虚拟机，点击“虚拟机” → “设置” → “选项” → “高级” → 勾选“为启用了Hyper-V白的主机禁用侧通道缓解”，确定即可。

![image-20241024211226258](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024211226258.png)

如果提示与 Hyper-V 不兼容，请移除 Hyper-V 后再进行操作。

### 安装 Ubuntu 22.04

进入 Ubuntu 22.04，选择 “Try or Install Ubuntu” 。

![20](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/20.png)

进入安装界面，左侧可以切换中文，但是**推荐先使用英文进行安装**。然后点击 “Install Ubuntu”。

![21](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/21.png)

键盘布局，无特殊需求使用默认设置即可。

![22](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/22.png)

使用默认设置即可，如有需求可以勾选“为图形或无线硬件，以及其它媒体格式安装第三方软件”（可能导致安装时间较长）

![23](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/23.png)

可以直接选择“Erase disk and install ubuntu”，然后“Install Now”。

![image-20241024213038389](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024213038389.png)

如果希望自定义分区，点击“Something else” → “Continue”；先点击“New Partition Table”，然后选中“free space”新建分区即可。下面是一个自定义分区是示例，仅供参考；完成分区后点击“Install Now”。

![image-20241024213453223](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024213453223.png)

地区默认上海即可

![image-20241024213733969](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024213733969.png)

设置用户名、计算机名称和密码。用户名推荐使用英文 + 数字，计算机名称推荐电脑型号/用途 + 系统版本，密码推荐以字母开头。建议勾选“Login automatically”；“Use Active Directory”可以不勾选，完成后点击“Continue”。

![image-20241024213925879](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024213925879.png)

耐心等待安装。安装完成后，点击“Restart Now”

![28](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/28.png)

出现这个界面，点击“可移动设备” → “CD/DVD” → “断开连接”后，点击虚拟机界面，按下回车即可。

![image-20241024215838446](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024215838446.png)

稍等片刻，看到以下界面就代表你的第一台虚拟机就完成安装了，恭喜你打开了Linux世界的大门~

![image-20241024220136060](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241024220136060.png)

## 使用 Hyper-V 安装 Debian 12

### 开启 Hyper-V

Hyper-V 是微软专有的虚拟化平台，你可以使用该平台在 Windows 操作系统上运行其他操作系统。在 Windows 11 中，默认情况下禁用此功能，因为不是每个人都需要它。但是，您可以在需要时启用它。

Hyper-V 预安装在 Windows 11 专业版、企业版和教育版中，只需启用即可。但是，在其他版本（如 Windows 11 家庭版）中，缺少启用 Hyper-V 的选项。

#### 检查硬件虚拟化兼容性

按 Win + X，选择“终端”或者“Windows Powershell”，输入下面指令：

```powershell
systeminfo
```

这将生成一个列表，您将在列表末尾找到“Hyper-V 要求”部分，其中包含 4 个要求的详细信息。

如果满足这些要求，结果将显示为“是”。但是，如果发现“在固件中启用虚拟化”状态为“否”，请自行搜索如何在BIOS中开启虚拟化（如，惠普星 BookPro 13 如何开启硬件虚拟机）。

按 Win + Pause，在 Windows 规格下，可以查看你的 Windows 版本（家庭版、专业版、企业版、教育版）：

![image-20241026113133365](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241026113133365.png)

#### 对于专业版、企业版、教育版

按 Win + S 输入“启用或关闭 Windows 功能”，在弹出的窗口勾选“Hyper-V”、“虚拟机平台”，然后单击“确定”。

![image-20241026113503898](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241026113503898.png)

现在将看到一个应用更改的窗口。完成后单击关闭，重启生效。

也可以按 Win + X，选择“终端”或者“Windows Powershell”，输入下面指令：

```powershell
DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V
```

当系统询问时，输入 Y 以重新启动计算机。计算机现在将重新启动，当它重新启动时，Hyper-V 应成功启用。

#### 对于家庭版

对于大陆用户，绝大多数零售笔记本都搭载家庭中文版。由于 Windows 家庭版没有 Hyper-V，在启用虚拟化后，新建空白文本，复制粘贴以下批处理代码后保存，保存更改文本 .txt 后缀为 .bat 格式，这样就能变为批处理脚本。右键以管理员身份运行即可。

```cmd
pushd "%~dp0"
dir /b %SystemRoot%\servicing\Packages\*Hyper-V*.mum >hyper-v.txt
for /f %%i in ('findstr /i . hyper-v.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\%%i"
del hyper-v.txt
Dism /online /enable-feature /featurename:Microsoft-Hyper-V -All /LimitAccess /ALL
pause
```

重新启动后，Hyper-V 将在 Windows 上安装并自动启用。

### 新建虚拟机

按 Win + S 搜索 Hyper-V，打开 Hyper-V 管理器

可以“点击固定到"开始"屏幕”方便开启

![image-20241025111121674](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025111121674.png)

点击左侧栏的主机名，然后在右侧栏点击“新建” → “虚拟机”

![image-20241025111655921](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025111655921.png)

名称任取；虚拟机默认存储在 C 盘，建议修改到其他位置

![image-20241025112620324](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025112620324.png)

建议选择“第二代”

![image-20241025112637851](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025112637851.png)

内存使用默认配置即可

![image-20241025112703165](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025112703165.png)

连接选择“Default Switch”

![image-20241025123049651](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025123049651.png)

硬盘使用默认设置即可，虚拟硬盘默认在虚拟机目录下

![image-20241025112746553](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025112746553.png)

选择下载好的 Debian 12 系统镜像

![image-20241025113019363](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025113019363.png)

创建完成，在启动前，点击左侧的“设置”；

禁用安全启动

![image-20241025113337232](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025113337232.png)

禁用检查点

![image-20241025113414866](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025113414866.png)

开启“来宾服务”

![image-20241025113512554](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025113512554.png)

完成后点击“确定”即可。

### 安装 Debian 12

点击“连接” → “启动”启动虚拟机

![image-20241025115115291](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025115115291.png)

选择“Start Installer”，按回车

![image-20241025115337519](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025115337519.png)

选择简体中文，下一步

![image-20241025115838973](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025115838973.png)

位置和键盘使用默认配置即可

如果提示网络自动配置失败，选择“继续” → “暂时不配置网络”即可

![42aa227ea7d37c88875ba4dc4fe95862](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/42aa227ea7d37c88875ba4dc4fe95862.png)

主机名任取，然后点击“继续”

![image-20241025120754143](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025120754143.png)

域名可以不用填写，“继续”

![image-20241025120850621](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025120850621.png)

设置 root 用户密码（请一定要记住），“继续”

![image-20241025120924731](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025120924731.png)

设置普通用户的用户名，继续

![image-20241025121053970](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025121053970.png)

设置普通用户的密码，可以与 root 密码相同，“继续”

![image-20241025121138327](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025121138327.png)

选择“向导 - 使用整个磁盘” → “继续”

![image-20241025121918151](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025121918151.png)

继续

![image-20241025121934781](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025121934781.png)

选择“将所有文件放在同一个分区中（推荐新手使用）” → “继续”

![image-20241025121945870](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025121945870.png)

“完成分区操作并将修改写入磁盘” → “继续”

![image-20241025122018242](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025122018242.png)

选择“是” → “继续”

![image-20241025122059255](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025122059255.png)

如果有这个界面，选择“否”，“继续”

![image-20241025122446241](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025122446241.png)

选择“是” → “继续”

![image-20241025122539669](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025122539669.png)

选择“中国” → “继续”

![image-20241025122607591](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025122607591.png)

选择任意以 mirrors 开头的镜像站，“继续”

![image-20241025122636713](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025122636713.png)

可以不用填写，“继续”

![image-20241025122725149](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025122725149.png)

选择 `debian-live-12.7.0-amd64-kde.iso` 这个镜像的话，这里会从镜像站下载文件，需要等待一会，具体时间视网络情况而定（哪个倒霉蛋等了一个小时啊）

![image-20241025124130497](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025124130497.png)

可能会有一个是否参加软件包流行度的调查，根据个人喜好选择，然后“继续”

![image-20241025183211732](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025183211732.png)

这里选择是否安装桌面环境，以及安装哪种桌面环境，自行决定；建议勾选上SSH Server

![image-20241025183258684](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025183258684.png)

选择“是”，“继续”

![image-20241025183409090](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025183409090.png)

选择“/dev/sda”，“继续”

![image-20241025183430484](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025183430484.png)

选择“继续”，虚拟机会自行重启

![image-20241025183516407](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025183516407.png)

稍等片刻，看到以下界面（不同桌面环境会有所不同）就代表你的第一台虚拟机就完成安装了，赶快输入你的密码，打开Linux的大门吧~

![image-20241025183622000](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025183622000.png)

![image-20241025183824931](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241025183824931.png)

## 使用 WSL 安装 Ubuntu

时间来到 2017 年，事情正在起变化🤣。微软正式发布了「适用于 Linux 的 Windows 子系统」，即人们熟知的 Windows Subsystem for Linux，简称 WSL。

在 2019 年，微软又基于 Hyper-V 架构的部分功能，推出了全新的 WSL 2。它能够在一个高度优化的虚拟化中运行完整的 Linux 内核。

WSL 2 只需要较少的系统资源，就能实现 Windows 和 Linux 之间的无缝集成。虽然 WSL 2 也使用了虚拟化技术，但它会自动在后台运行和管理，无需用户手动配置或维护（要维护也可以）。

WSL 2 主要面向将 Windows 作为生产力工具，但又希望在 Linux 环境中完成工作的用户和开发人员。你可以运行`grep`、`awk` 和`sed`等命令行工具，以及依赖这些工具的 Bash 脚本。不仅如此，你还可以从 WSL 命令行启动 Windows 应用，甚至在 Windows 上运行 Linux 图形应用。

WSL 2 使用了 Hyper-V 架构的一部分功能，但对 Windows 11 的版本并没有限制。家庭版、教育版、专业版和企业版都可以安装。

除了`x86_64`架构外，WSL 2 也支持`ARM`处理器。但要在基于 ARM 的设备上运行，所使用的 Linux 系统也必须是 ARM 版本。

如果你使用的虚拟机软件支持[嵌套虚拟化](https://www.sysgeek.cn/hyper-v-nested-virtualization/)，WSL 2 也可以在虚拟机中的 Windows 上运行。

### 启用 WSL 和虚拟化平台

按 Win + S 输入“启用或关闭 Windows 功能”，在弹出的窗口勾选“适用于于Linux的Windows子系统”、“虚拟机平台”，然后单击“确定”。

![image-20241026133025469](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241026133025469.png)

重启后，按 Win + X，选择“终端”或者“Windows Powershell”，输入下面指令：

```powershell
wsl --install #安装WSL
```

以上命令会启用 WSL 2 所需的所有功能，并默认下载 Ubuntu 发行版。安装需要几分钟，完成后会提示你重启 Windows。

![image-20241026132004532](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/1st-vms/image-20241026132004532.png)

重新登录 Windows 11 后，系统会自动弹出一个命令行窗口，以继续安装并启用 Ubuntu。按命令提示设置好你的 Linux 用户账户和密码后，即可开始使用。