---
comments: true
---

# 从零开始使用 Github Desktop 为 Github 项目贡献源代码：以开源观察 TranslateProject 为例

对于初涉编程领域的新手来说，Git 命令行可能显得有些复杂和难以掌握。幸运的是，Github 提供了一个更为直观和用户友好的工具——Github Desktop，它大大降低了使用 Git 的门槛，使得新手也能轻松地参与到开源项目的贡献中。本文将以开源观察TranslateProject 为例，详细介绍如何使用 Github Desktop 为 Github 项目贡献源代码。

## 创建 Github 账号

在开始使用 Github 和 Github Desktop 之前，你需要一个 Github 账号。访问 Github 官方网站 [https://github.com](https://github.com)，点击右上角的「Sign up」按钮。

![image-20240826164726801](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826164726801.png)

和昵称（Name）不同，这个用户名将成为你在 GitHub 上的唯一标识符（GitHub ID），它必须由阿拉伯数字、英文字母组成，且最多可包含一个连字符（-），并且必须是全网唯一的。请确保你的用户名符合这些要求，因为它将代表你在代码社区中的身份。

![image-20240826165746066](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826165746066.png)

登录邮箱查看并输入验证码

![image-20240826170433898](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826170433898.png)

如果无法输入验证码或者输入验证码后无响应，可以点击邮件中的链接或「Open GitHub」完成验证

![image-20240826170937734](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826170937734.png)



验证你的邮箱地址后，你就拥有了一个 Github 账号，可以开始你的开源之旅了。

## 下载并配置 Github Desktop

访问 Github Desktop 下载页面 [https://desktop.github.com/download]( https://desktop.github.com/download)，根据你的系统（如 Windows 64bit）下载对应的版本，并进行安装。

完成安装后会自动运行 Github Desktop，根据提示点击「Sign in to Github.com」，会在浏览器打开授权页面，根据提示继续即可。

![image-20240826164559180](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826164559180.png)

## 安装 Markdown 编辑器

开源观察项目的文章使用 Markdown 编写。Markdown 是一种轻量级标记语言，它允许人们使用易读易写的纯文本格式编写文档，Markdown文件的后缀名便是「.md」。

你需要安装 Markdown 编辑器。如果你熟练掌握 Markdown 语法，可以使用 VScode 等编写 Markdown 代码。

本文推荐使用 Typora 进行 Markdown 的编写。Typora 是一款支持 Windows 和 macOS 的 Markdown 编辑器，以其简单、高效和优美的所见即所得写作体验而闻名。

Typora 在 1.0.0 之前为免费版。你可以从互联网 [下载旧版](https://github.com/Pure-Happiness/Typora-0.11.18/releases)，*也可以通过其他渠道 [下载最新的学习版](https://ed.qcea.top/ChaIndex/Softwares/Windows/Editor/Markdown/Typora)*。**强烈推荐有经济能力的朋友 [支持正版 Typora](https://lizhi.shop/site/products/id/520)**。

## 阅读贡献指南

在为任何开源项目贡献代码之前，了解项目的贡献规则是非常重要的。通常，项目会在其 README 文件或专门的 CONTRIBUTING 文件中详细说明如何贡献代码、代码风格指南、提交规则等。务必仔细阅读项目的贡献规则，确保你的贡献符合项目的要求。

开源观察贡献指南发布在 [https://fosscope.com/wiki](https://fosscope.com/wiki/)，在开始贡献代码之前我们需要仔细阅读 [翻译文章工作流程](https://fosscope.com/wiki/fosscope-workflow/translation-workflow) 和 [Git 格式指南](https://fosscope.com/wiki/fosscope-workflow/git-format)。

对于一般贡献者（译者），翻译流程分为申请和翻译两部分，并在过程中遵守 [Git 格式指南](https://fosscope.com/wiki/fosscope-workflow/git-format) 中的分支命名规范和提交信息规范。

初次贡献代码时，首先需要 fork 目标仓库到自己的 GitHub 账户下，然后在副本上进行修改和提交，最后通过发起 Pull Request 将改动合并回原始仓库。

## <ruby>复刻<rt>fork</rt></ruby>并<ruby>克隆<rt>clone</rt></ruby>仓库

使用浏览器访问开源观察 TranslateProject 仓库链接 [https://github.com/FOSScope/TranslateProject](https://github.com/FOSScope/TranslateProject)。

点击右上角「Fork」。

![image-20240826164436429](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826164436429.png)

在「Create a new fork」页面，<ruby>所有者<rt>Owner</rt></ruby>选择自己的账号，<ruby>仓库名称<rt>Repository name</rt></ruby>可以根据自己的需求更改，然后点击「Create fork」。

![image-20240826164505989](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826164505989.png)

打开 GitHub Desktop，找到个人账号下的 TranslateProject 仓库，然后点击「Clone」。

![image-20240826171624342](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826171624342.png)

在弹窗中的「Local path」选择在本地的存储位置，然后点击「Clone」。

![image-20240826171734007](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826171734007.png)

选择「To contribute to the parent project」，然后点击「Continue」。

![image-20240826171947956](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826171947956.png)

看到这个界面，恭喜你完成了准备工作！

![image-20240826172134075](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826172134075.png)

将仓库克隆到本地后，找到 TranslateProject 的位置，点击 `sources` 文件夹就可以挑选选题啦！

在开始贡献代码前，务必首先在浏览器打开自己 fork 的仓库，点击「Sync fork」检查仓库是否与上游保持一致。如果提示「This branch is out-of-date」，点击「Update branch」进行更新。

![image-20240826205638725](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826205638725.png)

本文挑选了 `news` 分类下的 `20240805-google-chrome-will-soon-disable-extensions-like-ublock-origin-here-s-what-you-can-do`。

然后你需要根据 [翻译文章工作流程](https://fosscope.com/wiki/fosscope-workflow/translation-workflow) 和 [Git 格式指南](https://fosscope.com/wiki/fosscope-workflow/git-format)，创建一个申请翻译的分支。

## 创建分支

根据 [Git 格式指南](https://fosscope.com/wiki/fosscope-workflow/git-format)，申请翻译的分支应该命名为 `apply/news/20240805-google-chrome-will-soon-disable-extensions-like-ublock-origin-here-s-what-you-can-do`。

**请注意，分支名末尾没有 `.md` 后缀！**

在 Github Desktop 中，点击「Current branch」，在文本框输入分支名 `apply/news/20240805-google-chrome-will-soon-disable-extensions-like-ublock-origin-here-s-what-you-can-do`，然后点击「Create new branch」

![image-20240826192026483](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826192026483.png)

点击「Publish branch」将分支发布到远程仓库，此时我们对 `apply/news/20240805-google-chrome-will-soon-disable-extensions-like-ublock-origin-here-s-what-you-can-do` 分支进行操作。

![image-20240826192405321](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826192405321.png)

## 提交更改

在申请翻译阶段，你需要使用 Typora 打开想要翻译的选题，将 `author` 下的 `{{translator}}` 替换为自己的 Github ID（也就是用户名），同时将下方译者信息中的 `{{translator}}` 替换为自己的 Github ID。

![image-20240826193139803](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826193139803.png)

保存文件并关闭 Typora，使用 Github Desktop 提交你的更改。根据 [Git 格式指南](https://fosscope.com/wiki/fosscope-workflow/git-format)，在「Summary」栏中填写提交信息 `[申请][news] Google Chrome Will Soon Disable Extensions like uBlock Origin: Here's What You Can Do!`。点击「Commit to [你的分支名]」按钮，将更改提交到本地仓库。

注意，`[申请][news]` 与后面的英文标题之间要有空格。

![image-20240826193427150](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826193427150.png)

点击「Push origin」将本地仓库的更改推送到个人远程仓库。

![image-20240826193514315](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826193139803.png)

## 创建<ruby>拉取请求<rt>Pull Request</rt></ruby>

将分支推送到 Github 仓库后，你需要创建一个拉取请求（Pull Request）。「Push origin」结束后，根据提示点击「Preview Pull Request」,再点击弹窗中的「Create pull request」。

![image-20240826193709019](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826193709019.png)

![image-20240826193739986](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826193739986.png)

*对于创建单独分支的 commit，Github Desktop 会自动提示创建拉取请求；如果对主分支提交，需要自行打开个人远程仓库，在 `Pull Request` 选项下手动创建 `Pull Request`。*

跳转到浏览器后来到新建拉取请求页面，标题和 commit 信息保持一致。如果遇到下图标题过长，一部分内容自动填写到描述的情况，请手动修改，然后点击「Create pull request」即可。

![image-20240826194139047](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826194139047.png)

![image-20240826194103975](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240826194103975.png)

等待仓库管理员审核通过，将申请分支合并到主分支，就可以进行翻译环节啦。

![image-20240827145807478](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240827145807478.png)

## 翻译和要注意的 Markdown 格式规范

在个人远程仓库「Sync fork」和「Update branch」之后，在 Github Desktop 进行「Fetch origin」和「Pull origin」，确保本地主分支代码保持最新。

![image-20240827150248194](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240827150248194.png)

![image-20240827150122704](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240827150122704.png)

![image-20240827150338401](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240827150338401.png)

根据 [Git 格式指南](https://fosscope.com/wiki/fosscope-workflow/git-format)，创建一个翻译的分支 `translate/news/20240805-google-chrome-will-soon-disable-extensions-like-ublock-origin-here-s-what-you-can-do`，将想要翻译的选题从 `sources` 目录移动到 `translated` 目录**对应的分类**下。

![image-20240827151114859](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240827151114859.png)

然后就可以对文章进行翻译啦。

完成翻译后，需要检查这些细节：

- 中英文之间、中文与数字之间、数字与单位之间需要增加空格

- 正文与链接之间增加空格

- 全角标点与其他字符之间不加空格

- 专有名词使用正确的大小写

- 完整的英文整句、特殊名词，其内容中使用半角标点

- 使用直角引号 `「『』」`

- 小组件 `{% %}` 之间的注释和句子需要翻译，用于标记卡片类型或元素的 `note`、`image`、`icon` 等不翻译


此处仅仅列举了一些常见情况，详细信息请阅读 [Markdown 排版指北](https://fosscope.com/wiki/fosscope-workflow/markdown-format-guidelines)。

## 提交和创建拉取请求

完成翻译后，和申请相同，保存文件并关闭 Typora，使用 Github Desktop 提交你的更改。根据 [Git 格式指南](https://fosscope.com/wiki/fosscope-workflow/git-format)，在「Summary」栏中填写提交信息 `[翻译][news] Google Chrome Will Soon Disable Extensions like uBlock Origin: Here's What You Can Do!`。点击「Commit to [你的分支名]」按钮，将更改提交到本地仓库。注意 `[翻译][news]` 与后面的英文标题之间要有空格。

![image-20240827152909740](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240827152909740.png)

与申请翻译阶段相同，点击「Push origin」将本地仓库的更改推送到个人远程仓库。

![image-20240827183753713](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240827183753713.png)

根据提示点击「Preview Pull Request」,再点击弹窗中的「Create pull request」。

![image-20240827184353610](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240827184353610.png)

跳转到浏览器后来到新建拉取请求页面，正确填写标题后，点击「Create pull request」即可。

![image-20240827184600543](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20240827184600543.png)

等待管理员审核 Pull Request，merge后就大功告成了！

## 参考资料

[Markdown 官方教程](https://markdown.com.cn/)

[开源观察贡献指南：翻译文章工作流程 - FOSScope](https://fosscope.com/wiki/fosscope-workflow/translation-workflow)

[开源观察贡献指南：git 格式指南 - FOSScope](https://fosscope.com/wiki/fosscope-workflow/git-format#git-提交信息规范)

[开源观察贡献指南：Markdown 排版指北 - FOSScope](https://fosscope.com/wiki/fosscope-workflow/markdown-format-guidelines)

[为什么选择Typora？ | typora中文网](https://www.typora.net/516.html)

[Typora 官方中文站 (typoraio.cn)](https://typoraio.cn/)
