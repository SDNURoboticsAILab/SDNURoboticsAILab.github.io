# Shell、Bash、CMD、PowerShell 的区别与联系

## 预备知识

**[『DOS』](https://zh.wikipedia.org/wiki/DOS)**：是**磁盘操作系统**（英文：Disk Operating System）的缩写，是个人计算机上的一类操作系统。DOS 家族包括 MS-DOS、PC-DOS、DR-DOS、FreeDOS、PTS-DOS、ROM-DOS、JM-OS等，其中以 [MS-DOS](https://zh.wikipedia.org/wiki/MS-DOS) 最为著名。虽然这些系统常被简称为”DOS”，但没有任何一个系统单纯以”DOS”命名。

Bash 是 Linux 系统的命令解释器，并作为可通过 Bash 脚本用于自动化和重复性任务的工具而闻名。 [PowerShell](https://cn.a-d.site/?cat=powershell) 具有相同的用途，但适用于 Windows 系统。

## Shell 介绍

**『Shell』 =『图形用户界面（GUI）shell』 + 『命令行界面（CLI）的 shell』** ，捋一下 Mac / Linux / Windows 下常见的 `shell`。讲解 `shell`、`bash`、`cmd`、`zsh`、`PowerShell` 等的区别。

**『Shell / 壳层』**：命令行界面的解释器，用户和系统内核的沟通桥梁。分为：①命令行界面（CLI） ；② 图形用户界面（GUI）。[注释](https://zh.wikipedia.org/wiki/殼層)

![img](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/%E6%AE%BC%E5%B1%A4shell.png)

## 图形用户界面（GUI）shell

### MacOS 的 shell

**『Finder / 访达』**: 在 MacOS 中，能让用户管理文件、文件、磁盘、网络，以及启动其他的应用程序的引用程序。[注释](https://zh.wikipedia.org/wiki/Finder)

### Linux 的 shell

**『X窗口管理器』**: 独立的 `X窗口管理器`，例如 [Blackbox](https://zh.wikipedia.org/wiki/Blackbox) 与 [Fluxbox](https://zh.wikipedia.org/wiki/Fluxbox) 。[注释](https://en.wikipedia.org/wiki/X_window_manager)

**『Desktop Environment / 桌面环境』**: 桌面环境是依靠于窗口管理器的的扩展实现。如 [KDE](https://zh.wikipedia.org/wiki/KDE)、[GNOME](https://zh.wikipedia.org/wiki/GNOME)、[Xfce](https://zh.wikipedia.org/wiki/Xfce)、[DDE](https://en.wikipedia.org/wiki/Deepin) 。[注释](https://en.wikipedia.org/wiki/Desktop_environment)

### Windows 的 shell

**『Explorer / 文件资源管理器』**: 此操作系统中浏览电脑中文件与文件夹结构的基本工具，`win + E` 快捷键呼出。[注释](https://zh.wikipedia.org/wiki/檔案總管)

**『开始菜单』**: 屏幕的左下角菜单， `win` 键呼出。[注释](https://zh.wikipedia.org/wiki/開始功能表)

**『DOS Shell』**: 1998 年发布于 MS-DOS 的文件管理器，是终端里面生成的可视化界面。[注释](https://en.wikipedia.org/wiki/DOS_Shell)

## 命令行界面（CLI）的 shell

### MacOS / Linux 的 shell

**『sh / Bourne shell』**: 1977 在 Version 7 Unix 上的默认 shell。[注释](https://zh.wikipedia.org/wiki/Bourne_shell)

**『Bash』**: 名称由来 Bourne-Again SHell，在 GNU 计划中，于 1989 发布于第一个版本，是 sh 的兼容的开源的续作。亦是 Linux 和 MacOS （含10.14之前）的默认 shell。[注释](https://zh.wikipedia.org/wiki/Bash)

**『Z shell / Zsh』**: 是 sh + bash + 扩展功能。自2019 年起，MacOS 的默认 Shell 已从 『Bash 』改为『Zsh』。[注释](https://zh.wikipedia.org/wiki/Z_shell)

### Windows 的 shell

**『命令提示符 / cmd.exe』**：是 Win32 应用程序，取代『COMMAND.COM』。**Windows命令提示符（cmd.exe）** 是 Windows NT 下的一个用于运行 Windows 控制台程序或某些 DOS 程序的壳层程序；[注释](https://zh.wikipedia.org/wiki/命令提示字元)

**『PowerShell』** : 包括 ①`Windows PowerShel` + ②`PowerShell Core` ，基于 .NET 框架开发，自 2016 年后开源且跨平台。① 为前四年的版本，仅支持 Win 平台；② 则是其演进，支持跨平台 Linux 和 Mac。[注释](https://zh.wikipedia.org/wiki/PowerShell)

**『COMMAND.COM』**: 是一个16位的 DOS 应用程序。已经被 `命令提示符(cmd.exe)` 取代在 MS-DOS、Windows 95、Windows 98、Windows 98SE 和 Windows Me 上的默认命令行界面。[注释](https://en.wikipedia.org/wiki/COMMAND.COM)

## Bash 脚本与 PowerShell

我们将在下面的几个关键领域比较 Bash 脚本和 [PowerShell](https://cn.a-d.site/?cat=powershell) 脚本。

### 主要区别

类别 | Bash | PowerShell
---|---|---
系统 | 在Linux上原生运行。可在Windows、MacOS、Unix、BSD上使用。 | 在Windows上原生运行。可在Linux、MacOS上使用。
用途 | 用户Shell和命令行解释器 | Windows的任务自动化和配置管理
输入/输出 | 将所有内容视为纯文本 | 将所有内容视为对象
最适合 | Linux环境和服务器 | Microsoft环境和程序——如Active Directory、SQL等
语法 | 使用GNU程序和内置的Linux命令 | 使用cmdlets和内置的Windows命令
可用性 | Linux默认安装，无需下载 | Windows默认安装，可通过第三方cmdlets和API扩展

上表突出显示了主要差异。如果您想更深入地了解 Bash 脚本和 [PowerShell](https://cn.a-d.site/?cat=powershell) 脚本之间的主要区别，可以继续阅读。

### 系统兼容性

让我们从一个显而易见但非常重要的开始。

大多数人认为 Bash 脚本适用于 Linux。这是真的。但 Bash 也可以在 Unix、BSD 和 MacOS 上使用。甚至 Microsoft 也通过安装适用于 Linux 的 Windows 子系统，在 Windows 上轻松使用 Bash。因此，您当然可以在各种不同的操作系统上运行 Bash 脚本。

然而，它在 Linux 上仍然是最常见和最实用的。 BSD、MacOS 和 Windows 默认情况下不使用 Bash。可以肯定地说，如果您正在学习 Bash 脚本，您将在 Linux 上使用它。

PowerShell 类似，只不过它是 Windows 系统原生的。它仍然受到 Linux 发行版和 MacOS 的官方支持。 至少可以说，将 Windows [PowerShell](https://cn.a-d.site/?cat=powershell) 脚本移植到 Linux 系统上运行可能会很尴尬。将 Bash 脚本移植到 Windows 也是如此。当然，您可以通过这种方式完成一些任务，但使用每个操作系统各自的工具会更好。

Bash 可以直接与 Linux 系统上运行的进程交互。拥有适当的权限，您可以启动或停止任何服务并完全控制所有系统功能。在 Windows 上，Bash 的功能非常有限，不能直接影响应用程序的运行。

使用 PowerShell，您可以创建用于部署 Windows、管理 [Active Directory](https://cn.a-d.site/?cat=activedirectory) 等的脚本。但在 Linux 上，PowerShell 仅限于简单的脚本语言和沙箱，就像 Windows 上的 Bash 一样。

### 核心功能

Bash 和 [PowerShell](https://cn.a-d.site/?cat=powershell) 都是命令行解释器和用户 shell。您可以整天使用它们中的任何一个，而无需实际创建 Bash 或 [PowerShell](https://cn.a-d.site/?cat=powershell) 脚本。然而，它们处理命令输出的方式存在很大差异。

Bash 将所有内容视为纯文本，这使得它易于使用，但其范围有所限制。通常，如果您计划在 Linux 上制作需要面向对象编程或多行代码的脚本，则需要升级到更深入的编程语言，例如 Python。

PowerShell 将输出视为对象。这意味着它能够从一个 cmdlet 获取输出并将其传递到另一个 cmdlet。 [PowerShell](https://cn.a-d.site/?cat=powershell) 可以通过这种方式处理复杂的数据。 Bash 因其简单性而著称，如果您要在 Linux 上自动执行任务，Bash 脚本非常适合这项工作。 [PowerShell](https://cn.a-d.site/?cat=powershell) 可以应对一些更大的挑战，但在 Windows 上最有用，尤其是在管理任务中，因为大多数其他事情都可以在 GUI 中轻松处理。

## 命令提示符与 PowerShell

Windows为什么有两个命令行工具，一个叫 CMD 命令提示符，另外一个叫 PowerShell，它们两个究竟有什么区别，我们先来看 Windows 官网怎么说：

>Windows 的两个命令行工具，它们都可以用来进行人机交互，并且提供一个用于自动化 IT 操作的环境。
>
>CMD Shell是最早内置于 Windows 的 Shell, 用于执行 Windows 命令, 执行批处理文件。
>
>PowerShell 的设计目的是扩展 CMD Shell 的功能, 可以运行称为 cmdlet 的 PowerShell 命令, cmdlet 类似于 Windows 命令, 但是提供了更多可扩展的脚本语言功能。

你可以在 PowerShell 中运行 Windows 命令, 和 POWERShell 专属的 cmdlet 命令。但是 CMD Shell 只允许运行 Windows 命令, 不能运行 cmdlet 命令, 事实上, CMD 是老旧的 DOS 操作系统继承下来的产物, 所以它的功能十分有限, 你输入命令, Windows 执行命令仅此而已。

然而 PowerShell 不仅是更蓝了, 也更强了, 除了能执行普通的 Windows 命令以外, 它还是一个完整的脚本语言运行环境。

我们来对比一下它们的不同。首先我在命令提示符里输入 1+1 回车, 由于这不是一个 Windows 命令, CMD 完全不懂要干什么, 所以直接报错。

```cmd
Microsoft Windows[版本10.0.22631.38801]
(c)MicrosoftCorporation。保留所有权利。

C:\Users\excnies>1+1
'1+1’不是内部或外部命令，也不是可运行的程序或批处理文件。
```

然而在PowerShell中, 他明白 1+1 需要进行数字运算, 所以输出了 2。

```powershell
Windows PowerShell
版权所有 （C）	Microsoft Corporation。保留所有权利。

安装最新的 PowerShell，了解新功能和改进！https://aka.ms/PSWindows

PS C:\Users\excnies> 1+1
2
```

在 PowerShell 中也可以定义变量, 比如我先定义一个 `var1` 等于 1, 然后我们再定义一个 `var2` 等于 2, 我们可以对变量进行运算。

```powershell
Windows PowerShell
版权所有 （C）	Microsoft Corporation。保留所有权利。

安装最新的 PowerShell，了解新功能和改进！https://aka.ms/PSWindows

PS C:\Users\excnies> $var1 =1
PS C:\Users\excnies> $var2=2
PS C:\Users\excnies> varl + $var2
3
```

这其实很像一些高级编程语言的命令行交互环境了, 比如说 Python。

其实 PowerShell 完全可以作为 CMD 命令提示行的上位, 替代cmdlet这个单词是 command let 的缩写, 是一种专门在 Windows PowerShell 中使用的命令,  cmdlet 是由 .net 库编写的。

cmdlet 的命名规范遵循动词横杠名词的格式, 例如 `Get-Process`, 顾名思义就是获取当前进程。`Set-Location` 意思是切换目录。这时候你也许会好奇, Windows 已经有了 `cd` 命令, 为什么又要发明一种又臭又长的 `Set-Location` 命令呢。

事实上, PowerShell 的 `Set-Location` 不仅仅能用于更改文件的目录, 还可以用于更改其他的东西, 比如注册表目录, 证书存储目录等等, 这使得PowerShell的 `Set-Location`, 比传统的 CMD 中的 `cd` 更强大, 传统的 Windows 命令通常返回**纯文本**的输出, 这使得对输出进行解析和处理变得困难, 而 PowerShell 中的 cmdlet 返回的是 **.net 对象**, 允许更复杂和精确的数据操作, 这种对象模型使得数据在管道中传递时, 能够保留其结构。

###  别名机制

为了让 PowerShell 能完全兼容旧版的CMD命令, 微软使用了一种叫 `alias`, 也就是别名的机制。我们可以使用 `Get-Alias` 命令, 来查看所有的别名关系。

````powershell
PS C:\Users\excnies> Get-Alias

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Alias           % -> ForEach-Object
Alias           ? -> Where-Object
Alias           ac -> Add-Content
Alias           asnp -> Add-PSSnapin
Alias           cat -> Get-Content
Alias           cd -> Set-Location
Alias           CFS -> ConvertFrom-String                          3.1.0.0    Microsoft.PowerShell.Utility
Alias           chdir -> Set-Location
Alias           clc -> Clear-Content
Alias           clear -> Clear-Host
Alias           clhy -> Clear-History
Alias           cli -> Clear-Item
Alias           clp -> Clear-ItemProperty
Alias           cls -> Clear-Host
Alias           clv -> Clear-Variable
Alias           cnsn -> Connect-PSSession
Alias           compare -> Compare-Object
Alias           conda -> Invoke-Conda                              0.0        Conda
Alias           copy -> Copy-Item
Alias           cp -> Copy-Item
Alias           cpi -> Copy-Item
Alias           cpp -> Copy-ItemProperty
Alias           curl -> Invoke-WebRequest
Alias           cvpa -> Convert-Path
Alias           dbp -> Disable-PSBreakpoint
Alias           del -> Remove-Item
Alias           diff -> Compare-Object
Alias           dir -> Get-ChildItem
Alias           dnsn -> Disconnect-PSSession
Alias           ebp -> Enable-PSBreakpoint
Alias           echo -> Write-Output
Alias           epal -> Export-Alias
Alias           epcsv -> Export-Csv
Alias           epsn -> Export-PSSession
Alias           erase -> Remove-Item
Alias           etenv -> Enter-CondaEnvironment                    0.0        Conda
Alias           etsn -> Enter-PSSession
Alias           exenv -> Exit-CondaEnvironment                     0.0        Conda
Alias           exsn -> Exit-PSSession
Alias           fc -> Format-Custom
Alias           fhx -> Format-Hex                                  3.1.0.0    Microsoft.PowerShell.Utility
Alias           fl -> Format-List
Alias           foreach -> ForEach-Object
Alias           ft -> Format-Table
Alias           fw -> Format-Wide
Alias           gal -> Get-Alias
Alias           gbp -> Get-PSBreakpoint
Alias           gc -> Get-Content
Alias           gcb -> Get-Clipboard                               3.1.0.0    Microsoft.PowerShell.Management
Alias           gci -> Get-ChildItem
Alias           gcm -> Get-Command
Alias           gcs -> Get-PSCallStack
Alias           gdr -> Get-PSDrive
Alias           genv -> Get-CondaEnvironment                       0.0        Conda
Alias           ghy -> Get-History
Alias           gi -> Get-Item
Alias           gin -> Get-ComputerInfo                            3.1.0.0    Microsoft.PowerShell.Management
Alias           gjb -> Get-Job
Alias           gl -> Get-Location
Alias           gm -> Get-Member
Alias           gmo -> Get-Module
Alias           gp -> Get-ItemProperty
Alias           gps -> Get-Process
Alias           gpv -> Get-ItemPropertyValue
Alias           group -> Group-Object
Alias           gsn -> Get-PSSession
Alias           gsnp -> Get-PSSnapin
Alias           gsv -> Get-Service
Alias           gtz -> Get-TimeZone                                3.1.0.0    Microsoft.PowerShell.Management
Alias           gu -> Get-Unique
Alias           gv -> Get-Variable
Alias           gwmi -> Get-WmiObject
Alias           h -> Get-History
Alias           history -> Get-History
Alias           icm -> Invoke-Command
Alias           iex -> Invoke-Expression
Alias           ihy -> Invoke-History
Alias           ii -> Invoke-Item
Alias           ipal -> Import-Alias
Alias           ipcsv -> Import-Csv
Alias           ipmo -> Import-Module
Alias           ipsn -> Import-PSSession
Alias           irm -> Invoke-RestMethod
Alias           ise -> powerShell_ise.exe
Alias           iwmi -> Invoke-WmiMethod
Alias           iwr -> Invoke-WebRequest
Alias           kill -> Stop-Process
Alias           lp -> Out-Printer
Alias           ls -> Get-ChildItem
Alias           man -> help
Alias           md -> mkdir
Alias           measure -> Measure-Object
Alias           mi -> Move-Item
Alias           mount -> New-PSDrive
Alias           move -> Move-Item
Alias           mp -> Move-ItemProperty
Alias           mv -> Move-Item
Alias           nal -> New-Alias
Alias           ndr -> New-PSDrive
Alias           ni -> New-Item
Alias           nmo -> New-Module
Alias           npssc -> New-PSSessionConfigurationFile
Alias           nsn -> New-PSSession
Alias           nv -> New-Variable
Alias           ogv -> Out-GridView
Alias           oh -> Out-Host
Alias           popd -> Pop-Location
Alias           ps -> Get-Process
Alias           pushd -> Push-Location
Alias           pwd -> Get-Location
Alias           r -> Invoke-History
Alias           rbp -> Remove-PSBreakpoint
Alias           rcjb -> Receive-Job
Alias           rcsn -> Receive-PSSession
Alias           rd -> Remove-Item
Alias           rdr -> Remove-PSDrive
Alias           ren -> Rename-Item
Alias           ri -> Remove-Item
Alias           rjb -> Remove-Job
Alias           rm -> Remove-Item
Alias           rmdir -> Remove-Item
Alias           rmo -> Remove-Module
Alias           rni -> Rename-Item
Alias           rnp -> Rename-ItemProperty
Alias           rp -> Remove-ItemProperty
Alias           rsn -> Remove-PSSession
Alias           rsnp -> Remove-PSSnapin
Alias           rujb -> Resume-Job
Alias           rv -> Remove-Variable
Alias           rvpa -> Resolve-Path
Alias           rwmi -> Remove-WmiObject
Alias           sajb -> Start-Job
Alias           sal -> Set-Alias
Alias           saps -> Start-Process
Alias           sasv -> Start-Service
Alias           sbp -> Set-PSBreakpoint
Alias           sc -> Set-Content
Alias           scb -> Set-Clipboard                               3.1.0.0    Microsoft.PowerShell.Management
Alias           select -> Select-Object
Alias           set -> Set-Variable
Alias           shcm -> Show-Command
Alias           si -> Set-Item
Alias           sl -> Set-Location
Alias           sleep -> Start-Sleep
Alias           sls -> Select-String
Alias           sort -> Sort-Object
Alias           sp -> Set-ItemProperty
Alias           spjb -> Stop-Job
Alias           spps -> Stop-Process
Alias           spsv -> Stop-Service
Alias           start -> Start-Process
Alias           stz -> Set-TimeZone                                3.1.0.0    Microsoft.PowerShell.Management
Alias           sujb -> Suspend-Job
Alias           sv -> Set-Variable
Alias           swmi -> Set-WmiInstance
Alias           tee -> Tee-Object
Alias           trcm -> Trace-Command
Alias           type -> Get-Content
Alias           wget -> Invoke-WebRequest
Alias           where -> Where-Object
Alias           wjb -> Wait-Job
Alias           write -> Write-Output
````

这个 `Get-Alias` 表格也不全是旧的 CMD 命令, 其中还吸纳了一些 Linux 命令, 比如 `ls` 就是一个 Linux 命令, 我们在 CMD 中输入 `ls` 直接报错, 因为 `ls` 不是Windows命令, 但是在PowerShell中输入 `ls`, 它就会显示当前目录的文件结构, 因为 `ls` 与 `Get-ChildrenItem` 是别名关系, 如果你熟悉 Linux 命令, 可能会感到狂喜, 因为好多命令都是通用的, 又减少了一部分学习成本, 我们可以使用 `Get-Command` 命令来查看别名, 可以看出, `ls` 就是 `Get-ChildrenItem` 的别名。

```powershell
PS C:\Users\excnies> Get-Alias

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Alias           ls -> Get-ChildItem
```

旧版的 CMD 命令, 在 PowerShell 中都通过别名链接到一个 cmdlet 命令, 比如在 PowerShell 中, cd 就是 `Set-Location` 的别名, 他们两个在 PowerShell 中是完全等价的, 这里要注意一点, CMD 中的 `cd` 与 PowerShell 中的 `cd` 虽然长得一样, 功能也类似, 但是底层的实现本质已经有了区别, 前者是一个简单的 Windows 命令, 后者则是一个用 .net 库编写的 cmdlet。

PowerShell 是支持命令补全的。 比如当前目录下有一个 runme.exe 文件，你只需要输入 runme.exe 再按下回车就能自动给你补全为 ./runme.exe。 你甚至可以直接输个 ru 就按 tab 也能补全（只要 runme 是唯一一个 ru 开头的文件名）。 另外补全甚至支持通配符，即 r*u 再 tab 表示尝试用目录中 r 开头 u 结尾（不包含文件名）的程序名补全。 不仅是文件名，包括 cmdlet 的命令名和参数名都能补全。

综上所述, CMD 用户可以无缝过渡到 PowerShell, 不用支付任何学习成本,  Linux 用户也可以丝滑的学习使用 PowerShell, 因为好多命令都是共通的, 因此 PowerShell 完全可以作为 CMD 的上位替代, 用惯了 CMD 的各位用户, 不妨来尝试使用一下 PowerShell。

### 管道符

这个竖线 `|` 就是管道符, 意思是把上个命令的输出结果, 作为下个命令的输入, 可以像拼接管道一样把命令拼接起来, 形成一条流水线, 由于 cmdlet 返回的是一个 .net 对象, 可以很方便的使用管道符进行命令的拼接。

![屏幕截图_20240817_165518](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE_20240817_165518.png)

我举几个例子带大家感受一下, 第一个命令获取前五个 CPU 占用率最高的进程, 这里 `Get-Process` 命令用来获取进程, 然后使用管道符传递给下一个命令进行排序, 这里的排序依据是根据 CPU 的占用时间, 然后通过管道符再传递到下一个命令进行筛选, 这里筛选前五个我们执行一下，就显示出 CPU 占用率最高的前五个进程：

```powershell
PS C:\Users\excnies> Get-Process | Sort-Object CPU -Descending | Select-Object -First 5

Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
   2216      85    49104     173492       2.53   5060   1 explorer
    521      26    34816      57940       2.22   6000   1 RuntimeBroker
   1021      66    71868     140104       1.75   5816   1 SearchApp
    641      32    62164      74640       0.94   7072   1 powerShell
    468      28    14552      27720       0.50   4220   1 vmtoolsd
```

命令计算 Windows 目录下面所有 EXE 可执行文件的大小。 `Get-ChildrenItem` 用来列出目录下面所有的文件, `$env:windir` 指的就是 C 盘的 Windows 目录, 通过管道符传递给下一个命令, `Measure-Object -Sum Length` 命令用来求和的, 我们看到总大小是 7183 KB。

```powershell
PS C:\Users\excnies> Get-ChildItem $env:windir -Filter *.exe | Measure-Object -Sum Length


Count    : 9
Average  :
Sum      : 7183512
Maximum  :
Minimum  :
Property : Length
```

 假设有一个 data.csv 文件里面存储了用户信息, 我们使用 `Import-Csv` 读取这个文件, 然后传递给下一个命令, 下一个命令用来筛选, 筛选出年龄大于 30 岁的用户, 传递给下一个命令转换成 HTML 格式的, 然后再传递给下一个命令, 输出成 output.html

```powershell
PS C:\Users\excnies> Import-Csv data.csv | Where-Object {$_.Age -gt 30} | ConvertTo-Html | Out-File output.csv
```

### 脚本编程

CMD 与 PowerShell 都可以编写脚本语言的批处理程序, CMD 的脚本语言扩展名是 .bat 文件, 而 PowerShell 的扩展名是 .ps1 文件。它们的区别是 .bat 文件非常的难用, 比 .ps1 文件, 它多了很多的局限性, 然后语法也非常的老旧。比如 .bat 文件中甚至不允许 `if` 嵌套, 两个条件只能使用 `goto` 语句来连接, 整个代码支离破碎, 完全不符合人类阅读习惯, 不管是编码还是调试都带来非常大的痛苦, 

```bat
@echo off
setlocal

set var1=1
set var2=2

if %var1%==1 goto FirstLevelMet
goto End

:FirstLevelMet
echo First level condition met
if %var2%==2 goto secondLevelMet
gotoEnd

:SecondLevelMet
echo Second level condition met

:End
pause
```

我们再来看 PowerShell, PowerShell更像一个现代版的编程语言, 可以使用括号与嵌套, if 表示代码层级, 可以看到代码行数直接砍半了, 所以编写复杂的Windows 批处理程序, 我建议直接还是使用 PowerShell, 因为它更符合人类的阅读习惯, 更像一个现代版的编程语言：

```powershell
$var1 = 1
$var2 = 2

if ($var1 -eg 1) {
	Write-Output "First level condition met"
	if($var2 -eg 2) {
		Write-0utput "Second level condition met"
		}
	}
pause
```

## 总结

**『Shell』 =『图形用户界面（GUI）shell』 + 『命令行界面（CLI）的 shell』**

![img](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/bash/Shell_GUI_CLI.svg)

------

## 『PowerShell』和其它命令解释器比较

重点关心一下 **『PowerShell』** 的一些命令，看一下 **PowerShell命令行与其他命令行解释器的内部和外部命令的比较。[注释](https://zh.wikipedia.org/wiki/PowerShell) **

| PowerShell（命令行） | PowerShell（别名）                         | [命令提示符](https://zh.wikipedia.org/wiki/命令提示符)       | [Unix shell](https://zh.wikipedia.org/wiki/Unix_shell)       | 描述                                                         |
| -------------------- | ------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Get-ChildItem        | gci, dir, ls                               | [dir](https://zh.wikipedia.org/wiki/Dir_(命令))              | [ls](https://zh.wikipedia.org/wiki/Ls)                       | 列出目前或指定文件夹中的所有文件和文件夹                     |
| Test-Connection      | [ping](https://zh.wikipedia.org/wiki/Ping) | [ping](https://zh.wikipedia.org/wiki/Ping)                   | [ping](https://zh.wikipedia.org/wiki/Ping)                   | 从目前电脑向指定电脑发送[Ping](https://zh.wikipedia.org/wiki/Ping)，或指示另一台电脑这样做 |
| Get-Content          | gc, type, cat                              | [type](https://zh.wikipedia.org/w/index.php?title=TYPE_(DOS_command)&action=edit&redlink=1) | [cat](https://zh.wikipedia.org/wiki/Cat_(Unix))              | 获取文件内容                                                 |
| Get-Command          | gcm                                        | [help](https://zh.wikipedia.org/w/index.php?title=Help_(command)&action=edit&redlink=1) | [type](https://zh.wikipedia.org/w/index.php?title=Type_(Unix)&action=edit&redlink=1), [which](https://zh.wikipedia.org/w/index.php?title=Which_(command)&action=edit&redlink=1), [compgen](https://zh.wikipedia.org/w/index.php?title=Compgen_(Unix)&action=edit&redlink=1) | 列出可用的命令                                               |
| Get-Help             | help, man                                  | [help](https://zh.wikipedia.org/w/index.php?title=Help_(command)&action=edit&redlink=1) | [apropos](https://zh.wikipedia.org/w/index.php?title=Apropos_(Unix)&action=edit&redlink=1), [man](https://zh.wikipedia.org/wiki/手册页) | 在控制台上打印命令的文档                                     |
| Clear-Host           | cls, clear                                 | [cls](https://zh.wikipedia.org/w/index.php?title=Cls_(computing)&action=edit&redlink=1) | [clear](https://zh.wikipedia.org/wiki/Clear_(Unix))          | 清除屏幕                                                     |
| Copy-Item            | cpi, copy, cp                              | [copy](https://zh.wikipedia.org/wiki/Copy_(命令)), [xcopy](https://zh.wikipedia.org/w/index.php?title=Xcopy&action=edit&redlink=1), [robocopy](https://zh.wikipedia.org/w/index.php?title=Robocopy&action=edit&redlink=1) | [cp](https://zh.wikipedia.org/wiki/Cp_(Unix))                | 将文件和文件夹复制到另一个位置                               |
| Move-Item            | mi, move, mv                               | [move](https://zh.wikipedia.org/w/index.php?title=Move_(command)&action=edit&redlink=1) | [mv](https://zh.wikipedia.org/wiki/Mv_(Unix))                | 将文件和文件夹移动到新位置                                   |
| Remove-Item          | ri, del, erase, rmdir, rd, rm              | [del](https://zh.wikipedia.org/w/index.php?title=Del_(command)&action=edit&redlink=1), [erase](https://zh.wikipedia.org/w/index.php?title=Del_(command)&action=edit&redlink=1), [rmdir](https://zh.wikipedia.org/wiki/Rmdir), [rd](https://zh.wikipedia.org/wiki/Rmdir) | [rm](https://zh.wikipedia.org/wiki/Rm_(Unix)), rmdir         | 删除文件或文件夹                                             |
| Rename-Item          | rni, ren, mv                               | [ren](https://zh.wikipedia.org/w/index.php?title=Ren_(command)&action=edit&redlink=1), rename | [mv](https://zh.wikipedia.org/wiki/Mv_(Unix))                | 重命名单个文件、文件夹、硬链接或符号链接                     |
| Get-Location         | gl, cd, pwd                                | [cd](https://zh.wikipedia.org/wiki/Cd_(命令))                | [pwd](https://zh.wikipedia.org/wiki/Pwd)                     | 显示工作路径（目前文件夹）                                   |
| Pop-Location         | popd                                       | [popd](https://zh.wikipedia.org/w/index.php?title=Pushd_and_popd&action=edit&redlink=1) | popd                                                         | 将工作路径更改为最近推送到堆栈上的位置                       |
| Push-Location        | pushd                                      | [pushd](https://zh.wikipedia.org/w/index.php?title=Pushd_and_popd&action=edit&redlink=1) | pushd                                                        | 将工作路径存储到堆栈中                                       |
| Set-Location         | sl, cd, chdir                              | [cd](https://zh.wikipedia.org/wiki/Cd_(命令)), [chdir](https://zh.wikipedia.org/wiki/Cd_(命令)) | cd                                                           | 改变工作路径                                                 |
| Tee-Object           | tee                                        | 不适用                                                       | [tee](https://zh.wikipedia.org/wiki/Tee)                     | 将输入管道传输到文件或变量，并沿管道传递输入                 |
| Write-Output         | echo, write                                | [echo](https://zh.wikipedia.org/wiki/Echo_(命令))            | echo                                                         | 将字符串或其他对像打印到[标准流](https://zh.wikipedia.org/wiki/標準串流) |
| Get-Process          | gps, ps                                    | tlist,[tasklist](https://zh.wikipedia.org/w/index.php?title=Tasklist&action=edit&redlink=1) | [ps](https://zh.wikipedia.org/wiki/Ps_(Unix))                | 列出所有正在执行的进程                                       |
| Stop-Process         | spps, kill                                 | [kill](https://zh.wikipedia.org/w/index.php?title=Kill_(command)&action=edit&redlink=1),[taskkill](https://zh.wikipedia.org/wiki/Kill_(命令)) | kill[[e\]](https://zh.wikipedia.org/wiki/PowerShell#cite_note-UNIX_kill_misnomer-12) | 停止正在执行的进程                                           |
| Select-String        | sls                                        | [findstr](https://zh.wikipedia.org/wiki/Findstr)             | [find](https://zh.wikipedia.org/wiki/Find), [grep](https://zh.wikipedia.org/wiki/Grep) | 打印与模式匹配的行                                           |
| Set-Variable         | sv, set                                    | [set](https://zh.wikipedia.org/w/index.php?title=Environment_variable&action=edit&redlink=1) | env, export, set, setenv                                     | 创建或更改[环境变量](https://zh.wikipedia.org/wiki/环境变量)的内容 |
| Invoke-WebRequest    | iwr, curl, wget                            | [curl](https://zh.wikipedia.org/wiki/CURL)                   | [wget](https://zh.wikipedia.org/wiki/Wget), curl             | 获取互联网上的网页内容                                       |

---

## 参考资料

- 偕臧, Shell、Bash、CMD、PowerShell 的区别, https://ifmet.cn/posts/d0c4daee/
- Linux-Console, Bash 脚本与 PowerShell：有什么区别？ , https://cn.linux-console.net/?p=10215
- 技术爬爬虾, windows为什么有两个命令行工具？命令提示符与PowerShell有什么区别？, https://www.bilibili.com/video/BV1Nx4y147n3/
