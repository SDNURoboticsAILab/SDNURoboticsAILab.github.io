---
comments: true
---
# 设置 C++ 开发环境



C++ 是一种通用编程语言，现如今广泛用于竞赛编程。它具备命令式、面向对象和泛型编程的特性。C++ 可以在多个平台上运行，如 Windows、Linux、Unix、Mac 等。在开始使用 C++ 编程之前，我们需要在本地计算机上设置一个环境，以便成功编译和运行 C++ 程序。如果你不想设置本地环境，也可以使用在线 IDE 来编译程序。

## **使用在线 IDE**

IDE 代表集成开发环境。IDE 是一种软件应用程序，为计算机程序员提供开发软件的设施。有许多在线 IDE 可供使用，这些 IDE 可以帮助你轻松地编译和运行程序，而无需设置本地开发环境。

> [ide.geeksforgeeks.org](https://ide.geeksforgeeks.org/) 是由 GeeksforGeeks 提供的一个这样的 IDE。

你可以点击“Run on IDE”按钮来运行程序。

- C++

```
#include <iostream>
using namespace std;

int main() {
    cout << "Learning C++ at GeekforGeeks";
    return 0;
}

```

**Output**

```
Learning C++ at GeekforGeeks
```

时间复杂度：O(1)

辅助空间：O(1) 

## **设置本地开发环境**

要在本地计算机上设置 C++ 集成开发环境 (IDE)，需要安装两个重要的软件：

1. C++ 编译器
2. 文本编辑器

### **1. C++ 编译器**

在安装好文本编辑器并将程序保存为 `.cpp` 扩展名的文件后，您将需要一个 C++ 编译器来编译此文件。编译器是将高级语言转换为机器能理解的低级语言的计算机程序。换句话说，它将用编程语言编写的源代码转换成计算机可以理解的另一种计算机语言。为了编译 C++ 程序，我们需要一个 C++ 编译器，它将把用 C++ 编写的源代码转换为机器码。以下是不同平台上设置编译器的详细信息。

#### 在 Linux 上安装 GNU GCC

我们将在 Linux 上安装 GNU GCC 编译器。请按照以下步骤在您的 Linux 计算机上安装和使用 GCC 编译器：

**A.** 首先，在 Linux 终端中运行以下两个命令：

```
sudo apt-get update
sudo apt-get install gcc
sudo apt-get install g++
```

**B.** 这些命令将安装 GCC 编译器。您也可以运行以下命令：

```
sudo apt-get install build-essential
```

该命令将安装所有编译和运行 C++ 程序所需的库。

**C.** 完成上述步骤后，您应检查 GCC 编译器是否正确安装。为此，请在 Linux 终端中运行以下命令：

```
g++ --version
```

**D.** 如果上述两步完成且没有错误，那么您的 Linux 环境已设置好，可以用于编译 C++ 程序。接下来的步骤将介绍如何使用 GCC 编译器在 Linux 上编译和运行 C++ 程序。

**E.** 在文本文件中编写程序，并将其保存为 `.cpp` 扩展名。我们编写了一个显示“Hello World”的程序，并将其保存为桌面上的“helloworld.cpp”文件。

**F.** 现在，您需要打开 Linux 终端并切换到保存文件的目录。然后，运行以下命令编译您的文件：

```
g++ filename.cpp -o any-name
```

**G.** *filename.cpp* 是您的源代码文件名。在我们的例子中，文件名是“helloworld.cpp”，而 *any-name* 可以是您选择的任何名称。这个名称将分配给编译器在编译后创建的可执行文件。在我们的例子中，我们选择 *any-name* 为“hello”。我们将运行上述命令如下：

```
g++ helloworld.cpp -o hello
```

**H.** 执行上述命令后，您将看到在保存源文件的相同目录中自动创建了一个新文件，其名称为您选择的 *any-name*。现在，要运行您的程序，您需要运行以下命令：

```
./hello
```

**I.** 该命令将在终端窗口中运行您的程序。

### **2. 文本编辑器**

  文本编辑器是用来编辑或编写文本的程序。我们将使用文本编辑器来输入我们的 C++ 程序。普通文本文件的扩展名是 (.txt)，但包含 C++ 程序的文件应保存为 '.cpp' 或 '.c' 扩展名。以 ‘.CPP’ 和 ‘.C’ 结尾的文件称为源代码文件，它们应该包含用 C++ 编程语言编写的源代码。这些扩展名帮助编译器识别文件中包含 C++ 程序。开始 C++ 编程之前，必须安装文本编辑器以编写程序。请按照以下说明在不同操作系统（如 Windows、Mac OS 等）上安装流行的代码编辑器，如 VS Code 和 Code::Blocks。

#### 1. Code::Blocks 安装

  有许多 IDE 可用于轻松进行 C++ 编程。其中一个流行的 IDE 是 **Code::Blocks**。

  - 从此链接选择适合您操作系统的安装包下载 Code::Blocks – [Code::Blocks 安装包](http://www.codeblocks.org/downloads/26)。
  - 下载 Code::Blocks 的安装文件后，打开它并按照说明进行安装。
  - 安装成功后，打开 Code::Blocks，进入 *文件* 菜单 -> 选择 *新建* 并 *创建空文件*。
  - 在空文件中编写您的 C++ 程序，并以 '.cpp' 扩展名保存文件。
  - 保存文件后，进入 *构建* 菜单，选择 *构建并运行* 选项。

#### 2. XCode Mac OS X 安装

  如果您是 Mac 用户，可以下载 Xcode 作为代码编辑器。

  - 要下载 Xcode，请访问苹果网站或在苹果应用商店搜索。您可以通过以下链接下载 Xcode – [Xcode for MacOS](https://developer.apple.com/xcode/)，那里会提供所有必要的安装说明。
  - 成功安装 Xcode 后，打开 Xcode 应用程序。
  - 创建新项目。进入文件菜单 -> 选择 新建 -> 选择 项目。这将为您创建一个新项目。
  - 在下一个窗口中，您需要选择项目模板。选择 C++ 模板时，选择左侧边栏的 *Application* 选项。在可用选项中选择 *command-line tools* 并点击 *下一步*。
  - 在下一个窗口中，提供所有必要的详细信息，如“组织名称”、“产品名称”等。确保选择语言为 C++。填写完信息后，点击下一步以继续。
  - 选择保存项目的位置。然后，从左侧边栏的目录列表中选择 *main.cpp* 文件。
  - 打开 main.cpp 文件后，您将看到提供的预编写 C++ 程序或模板。您可以根据需要修改此程序。要运行您的 C++ 程序，请转到 *产品* 菜单并从下拉列表中选择 *运行* 选项。

  另一个非常易于使用且现在最受欢迎的 IDE 是 **VSC（Visual Studio Code）**，适用于 Windows 和 Mac OS。

#### 3. 在 Windows 上安装 VS Code

  首先安装 [Visual Studio Code](https://code.visualstudio.com/)。打开下载的文件，点击运行 -> （接受协议）下一步 -> 下一步 -> 下一步 -> （选中所有选项）-> 下一步 -> 安装 -> 完成。现在，您将能够在桌面上看到 Visual Studio Code 图标。

  - 从 [这个链接](https://sourceforge.net/projects/mingw/) 下载 MinGW。
  - 安装后，点击“继续”。检查所有软件包（右键单击 -> 标记为安装）。然后，点击安装（左上角）-> 应用更改。（这可能需要一些时间）
  - 打开此电脑 -> C 盘 -> MinGW -> Bin。（复制此路径）
  - 右键单击“此电脑” -> 属性 -> 高级系统设置 -> 环境变量 -> （选择系统变量中的 PATH） -> 编辑 -> 新建 -> 粘贴路径，然后点击确定。
- 打开 Visual Studio Code，安装一些有用的扩展（从右侧边栏，最后一个图标可能是）：
  
  - C/C++
  - Code Runner
- 现在，进入设置 -> 设置 -> 搜索 Terminal -> 滚动到页面底部 -> 勾选 [ Code-runner: Run In Terminal ]

太好了！现在你可以开始使用了。打开任何文件夹，创建新文件，并以 ".cpp" 扩展名保存它们。

#### 4. 在 Mac OS 上安装 VS Code

首先，通过[这个链接](https://code.visualstudio.com/download)安装 Visual Studio Code。接着，我们将安装编译器 MinGW。为此，我们需要先安装 Homebrew。

要安装 Homebrew，打开终端（按 cmd + 空格），输入 Terminal 并按 Enter。在终端中复制以下命令：

```
arch -x86_64 ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install)" < /dev/null 2> /dev/null
```

这将下载并安装 Homebrew，过程可能需要一些时间。

现在，我们将在 Mac OS 上安装 MinGW 编译器。在终端中粘贴以下命令并按 Enter：

```
arch -x86_64 brew install MinGW-w64
```

- 这也是一个耗时的过程，请耐心等待！
- 打开 Visual Studio Code，安装一些有用的扩展（从右侧边栏，最后一个图标可能是）：
  - C/C++
  - Code Runner
- 现在，进入设置 -> 设置 -> 搜索 Terminal -> 滚动到页面底部 -> 勾选 [ Code-runner: Run In Terminal ]