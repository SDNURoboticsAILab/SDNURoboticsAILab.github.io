---
comments: true
---
# 第0节课

# 开启机器人实验室之旅

现在你可能是一个无知的小白，面对着浩如烟海的教学视频、深不见底的学习深度暗暗发愁，不知道该如何下手。别担心，本攻略会一步步带大家从黑吗喽变成天命人。

本期攻略不会教大家如何去敲出优美的代码，但是会涉及老玩家们(/doge)口口相传下来的一些作为软件工程师的必备通识和素养，相信无论你是否是代码上的小白，看完都会有一定的收获

## 合格玩家的必备素养

大家的学习之路可以类比成游戏的通关之路，那么一个合格的玩家需要有哪些素养呢？

1. **好奇心**：在游戏中，好奇心驱使玩家去探索每一个角落，发现隐藏的宝藏和秘密任务。你会不断试图解开谜题，寻找隐藏的通道和秘密关卡。在代码世界中也一样，好奇心促使你去了解每一行代码的意义，每一个函数的用法。你会不断追问“为什么”，不满足于现有的答案，而是主动寻求新的知识和理解。比如，为什么这个函数会报错？为什么这个算法能提高效率？这种好奇心让你不断深入，掌握更深的知识。

2. **内驱力**：在游戏中，你可能会因为后续剧情、boss设计、隐藏地图、通关的成就感等因素来自发的游玩这款游戏。在编程学习过程中，大家也要寻找到属于自己的内驱力。**在大学，没有谁会逼着你学习**，你要自己主动学习新的编程语言和技术，尝试解决更复杂的问题。内驱力让你在面对困难时不轻易放弃，而是不断寻找解决方案，提升自己的技能。比如，学习新的框架，优化代码性能，解决复杂的bug等。

3. **坚持**：**最重要的一项**✊，或许之后上课会听的迷迷糊糊的，这里为什么会报错？并发为什么每次效果不一样？会在学习的过程中遇到数不清的问题，跳进数不清的坑。但是只要坚持你回过来看发现其实都很简单，每个大佬也都是从萌新开始的嘛

	碰到问题不可怕，找到解决问题的方式是关键，于是就引入了下一小节——**如何正确查找攻略**

## 如何正确查找攻略

1. 分析自己的代码：如果自己能解决，这个成就感是无与伦比的

2. 百度/Bing/Google：只要你正确的调教好你的浏览器(下点插件屏蔽一下广告之类的)，百度真的能查到很多东西。比如当你遇到了一个报错

![01](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/Misc/lesson0-2024-tech/01.png)

  **直接复制然后百度**

 ![02](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/Misc/lesson0-2024-tech/02.png)

是不是解决方案都有啦
  **PS：所谓的百度，通常是使用搜索引擎进行检索信息的代称，推荐大家使用Bing、Google。**

3. 问ChatGPT(**详情见后文“必备工具”**)

4. 看官方文档，大家不要觉得看文档很难就不去看了，我们gopher不像学Java的，与 Java 能用到退休的教程和生态相比，Go虽然也不是很年轻了，但是肯定也是会遇到没有教程的时候。这时候，看文档甚至看源码的能力就非常重要了(**详见后文**)

5. 向学长/姐提问

### 提问的智慧（非常重要）

  如何提问也是一门大学问，详见[这个文档](https://lug.ustc.edu.cn/wiki/doc/smart-questions/)🙏

​	你们或许在提问题的时候觉得我们很傲慢？

#### 		🐂🐎问题

- 手机拍代码
- 只说一个笼统的问题，不说细节
- 夺命连环问

![03](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/Misc/lesson0-2024-tech/03.png)

![04](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/Misc/lesson0-2024-tech/04.jpg)

#### 例子

**你以为的傲慢**：

- 学弟：学长我vscode装不上了怎么办？
- 学长：你到官网下载安装包下载完双击它，一直点下一步就安装好了
- 学弟：官网是什么
- 学长：https://code.visualstudio.com/
- 学弟：下载按钮在哪？
- 学长：（截图）
- 学弟：好了，下载到了，然后呢？
- 学长：这个都不会还是别学了
- 学弟：（感觉学长很傲慢）...

**实际上的傲慢：**

- 学弟：学长我的电脑是64位的windows 10，我在vscode官网下载 了对应版本，在我安装过程中出现了这个问题，使用百度搜索后还是没有办法解决，你能帮我看看吗？谢谢。（同时贴上安装失败的图片）

- 学长：这个都不会还是别学了


#### 我们为什么对你们提的问题感到厌烦？

- 提的问题“过于简单“
- 提问题的方式不对
- 遇到问题就提问

#### 怎么问问题？

- 精确地描述问题并言之有物

	- 仔细、清楚地描述你的问题或者Bug的症状
	- 描述问题发生的环境
	- 描述在提问前你是怎样去研究和解决这个问题的
	- 描述在提问前你为了确定问题而采取的诊断步骤
	- 尽可能地提供一个可以`重现这个问题的可控环境`的方法

- 话不在多，在于精

	你需要提供精确有内容的信息

	这并不是要求你简单的就把成堆的错误代码或者资料完全放在你的提问中，如果你的问题是一个很大的是程序挂掉的这样一个代码运行环境，尽量把它剪裁得越小越好。

	这样做的好处至少有三点：

	- 第一，表现你为简化问题付出了努力，这可以使你得到回答问题的概率增加
	- 第二，简化问题使你更有可能得到有用的答案
	- 第三，在精炼你的 bug 报告的过程中，你很可能就自己找到了解决方法或者权宜之计

- 清楚明确地表达你的需求

	漫无边际的提问是近乎无休无止的时间黑洞。

	最有可能最有能力给你有用答案的人通常也是最忙的人（他们忙是因为要亲自完成大部分工作）。所以我们对这样无休止无节制的时间黑洞是相当厌恶的。

	所以，请界定一下你的问题，使我们花在辨识你的问题和回答所需要付出的时间减到最少。

- 询问有关代码的问题时

	千万不要动辄就要求别人帮你去调试有问题的代码，而且也不提示一下应该从何入手。相当于：你玩黑猴迷路了，直接让学长上手帮你做跑图这种重复且无趣的工作

	张贴几百行的代码，然后说一声：`这段代码有问题`，我们可能完全会忽略这样的问题，而且回都不想回

	相比于这个，只贴几十行的代码，然后说一句：`在第七行代码之后，我觉得程序会输出xxx，但实际出现的xxx`更有可能让你得到回应

	最有效描述程序代码问题的方法就是提供一段最精简的 Bug 展示的测试用例。

	什么是最精简的测试用例？那是问题的缩影；就是一小个代码片段能够刚好的展示出程序的异常行为，而不包含其他令人分散注意力的代码的内容。

	怎么才能找出最精简的测试用例？如果你知道哪一行或者哪一段代码会造成异常的行为，复制下来并且加入能够重现这个状况的代码（能让这段异常的代码正常运行）。如果你无法将问题缩减到一个特定区块，就复制一份代码并移除不影响产生问题行为的部分。总之，你发出的测试用例（或代码）越少越好。

- 截图的方式

	**不要手机拍照！不要手机拍照！不要手机拍照！**

- 有礼貌地提问

	多用`请`和`谢谢你的回答`，让回答者知道你对他们能够花费掉自己宝贵地时间来对你提供帮助心存感激。

当然，对于很多问题大家都是 0 基础，问很正常，我们还是很乐意大家提问的(学长不会吃人的，大家不要怕)

## 必备工具

### 一些懂的都懂的东西

为什么我 github 只能看运气进？为什么我 git 老是推不上去？为什么我项目拉不下来？

这些问题都是懂得都懂的，除了换镜像源之外该怎么解决呢？

挂加速器可以解决一时之需，无论是游戏加速器还是「Watt Toolkit」（Steam++），都能加速 github 等一些学术网站

如果你之后有更深的需求，这里不方便说，来私聊群里的学长学姐

### 善用AI —— Large Lauguage Model(LLM)

AI从23年初开始流行，到现在已经不是一个新鲜玩意儿了，也对行业产生了天翻地覆的影响。

**不会用AI的程序员不是好程序员**

AI可以帮助程序员解决非常多的问题，尤其是针对初学者来说。

而且现在使用AI的门槛也低了很多，国内也出现了不少好用的大模型，。也可以直接去使用ChatGPT等国外的模型。

在提问时，尽可能提供你的代码、报错或者软件运行日志；如果你知道代码的运行过程，也可以告诉AI；如果有多个问题最好将问题拆解后提问：

![image-20241023164818932](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/Misc/lesson0-2024-tech/image-20241023164818932.png)

但是，**千万不能太依赖AI，千万不能太依赖AI，千万不能太依赖AI！！**

#### 一些推荐的AI大语言模型

*[ChatGPT（4.0/4o/o1/o1mini）——毫无悬念的最强](https://chatgpt.com/)*

[通义千问——国内最强](https://tongyi.aliyun.com/)

[智谱清言——国内最强](https://chatglm.cn/?lang=zh)

[Kimi——长文本、多模态、写作](https://kimi.moonshot.cn/)

*[Claude（Claude-3-Haiku/Claude-3.5-Sonnet/Claude-3-Opus）——代码强](https://claude.ai/)*

[RawChat公益站点——Claude账号共享](https://kelaode.ai/)

[DeepSeek——代码很强](https://chat.deepseek.com/sign_in)

*[‎Gemini——善于总结](https://gemini.google.com/)*

*[Gamma——生成PPT和网页](https://gamma.app/)*

[秘塔AI搜索](https://metaso.cn/?s=blpc1)

*[Perplexity——AI搜索](https://www.perplexity.ai/)*

*[Poe——大语言模型合集](https://poe.com/login)*

[HuggingChat ——大语言模型合集](https://huggingface.co/chat/)

### GitHub

#### 什么是GitHub？

GitHub 是一个基于 Git 的代码托管平台，广泛用于软件开发和版本控制。它提供了一个协作环境，使开发者能够在全球范围内共享和管理代码。以下是 GitHub 的一些关键功能和特点：

1. **版本控制**：利用 Git 的分布式版本控制系统，开发者可以跟踪代码的更改历史，轻松管理项目的不同版本。
2. **协作工具**：通过 pull requests、issues 和 project boards，团队可以高效地进行代码审查、任务分配和项目管理。
3. **代码托管**：GitHub 提供免费的公共仓库和付费的私有仓库存储，支持多种编程语言的项目。
4. **社区和开源**：GitHub 是开源项目的热门平台，开发者可以贡献代码、报告问题和参与讨论。
5. **集成和扩展**：支持与 CI/CD 工具、项目管理软件和其他开发工具的集成，增强了开发流程的自动化和效率。
6. **GitHub Actions**：允许开发者创建自定义的自动化工作流，以实现持续集成和部署。
7. **安全性**：提供代码扫描、依赖项管理和安全警报，帮助开发者识别和修复潜在的安全漏洞。

GitHub 不仅是一个代码托管平台，也是一个开发者社区，促进了全球范围内的协作和创新。

#### 如何使用GitHub

[从零开始使用Github Desktop在Github上贡献源代码](https://sdnuroboticsailab.github.io/resource/software/Git/e3-github-contribution/)

### JetBrains全家桶

> 怎么选择 IDE

JetBrains旗下的IDE都很好用，也十分全面，像 C语言可以用 Clion，Python 可以用 PyCharm，java 可以用 IntelliJ IDEA

> 可是JetBrains的IDE好像都要付费购买欸？

这个问题不用担心，这些 IDE 学生都是可以免费使用的，完成学生认证就好了，详见下面的博客👇

[JetBrains 学生认证教程（Pycharm，IDEA… 等学生认证教程）_jetbrains学生认证-CSDN博客](https://blog.csdn.net/qq_36667170/article/details/79905198)（用官方文件+学信网在线验证的方法申请）

[jetbrains学生凭证一年后怎么续？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/508020685?utm_id=0)

> 安装好麻烦啊，为啥不直接用VSCode呢？

相较于 VSCode ，JetBrains 全家桶有以下几个优点：

1. **智能代码补全**：
	- 提供更强大的代码补全功能，能够更准确地预测和建议代码片段。
2. **内置工具**：
	- 集成了许多开发所需的工具，如调试器、测试运行器和代码分析工具，开箱即用。
3. **代码重构**：
	- 提供全面的重构选项，如重命名、提取方法等，帮助开发者更轻松地重构代码。
4. **调试支持**：
	- 内置强大的调试功能，支持断点设置、变量监视和调用堆栈查看，调试体验更流畅。
5. **项目导航**：
	- 提供更高级的项目导航功能，便于快速查找和跳转到代码中的特定部分。
6. **集成测试**：
	- 更好地支持测试框架，方便运行和管理测试。
7. **插件丰富**：
	- 虽然 VSCode 插件也很丰富，但通常更专注于增强开发体验。

VSCode 作为一个通用编辑器，虽然灵活且支持多种语言，但需要通过安装和配置插件来达到类似的功能。GoLand 则专注于 Go 语言开发，提供了更统一和集成的开发体验。

### Git

> 我在Goland写好代码之后每次都要跑到GitHub上传文件吗？

当然不用！Git 是目前世界上最先进的分布式版本控制系统，用来团队协作很方便。就不用每次上传代码都靠手动 upload files 了

 如何安装看这个👇

[Git 的安装教程（详解每个步骤）_git官网安装-CSDN博客](https://blog.csdn.net/Passerby_Wang/article/details/120767020?ops_request_misc=%7B%22request%5Fid%22%3A%22169673342216800182730025%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=169673342216800182730025&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-4-120767020-null-null.142^v95^chatgptT3_1&utm_term=安装git&spm=1018.2226.3001.4187)

但是我们基本不会再git bash里敲git命令，要么是在IDE里点点点，要么是在IDE的命令行里敲

如何使用看这个👇

[Git版本控制及Goland使用Git教程_goland配置git-CSDN博客](https://blog.csdn.net/qq_42956653/article/details/121613703?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_utm_term~default-5-121613703-blog-123849753.235^v43^pc_blog_bottom_relevance_base6&spm=1001.2101.3001.4242.4&utm_relevant_index=8)

git闯关小游戏👇

[Learn Git Branching](https://learngitbranching.js.org/?demo=&locale=zh_CN)

实验室Wiki目前有比较完善的Git教程。

### Typora

#### 什么是markdown？

Markdown是一门标记语言。假如你们知道HTML的话，Markdown和HTML可以认为是同类事物。简而言之，就是用纯文本的代码描述带格式文本的一种方法。

那么有了HTML，要Markdown有何用？最简单的答案是：HTML太难写了！

这样对于关注内容的作者而言友好了很多，而且即使是Markdown代码也有相当强的可读性。

于是写好Markdown后，如何将其显示成我们想要的格式呢？通常的做法是将Markdown编译为HTML。其实一些网站已经自带了这样的编译器，输入Markdown代码后直接将其转化为HTML，就可以交给浏览器渲染了。GitHub上的README以及各种.md格式文件的预览功能就是最典型的例子。

Markdown 编写的文档后缀为 `.md`, `.markdown`

#### 什么地方会用到markdown？

Markdown可以广泛用于文档、博客、论坛等带格式文本内容的创作，习惯后使用起来会比所见即所得的HTML编辑器更加方便快捷，较Word等格式又有纯文本这一优势。

#### typora又是啥

而 typora 就是一款非常方便的支持 md 格式的笔记软件，有很多功能：实时预览、数学公式、代码高亮、表格、支持HTML、流程图等等

这份文档就是在 typora 里敲出来的，个人认为比 word 好用多了

官网下载就完事了https://typora.io/    （看到购买通知可以无视，一直试用就好了

学习版：
[Windows（不要更新）](https://ed.qcea.top/ChaIndex/Softwares/Windows/Editor/Markdown/Typora/typora_64bit_v1.8.10_setup.zip)
[Win/Mac/Linux](https://blog.tcea.top/posts/20231001-typora-crack/)

其他一些比较不错的Markdown编辑器

[obsidian新手不完全指南 - 经验分享 - Obsidian 中文论坛](https://forum-zh.obsidian.md/t/topic/1628)

[想要玩转 Notion？你需要这份快速上手指南 - 少数派 (sspai.com)](https://sspai.com/post/57464)

## 如何高效学习

> 我除了跟着师哥师姐学习之外还能在哪里自学呢？

有这种自学的意识是非常好的，到了大学之后自驱力是成为强者的必要特质

接下来我会介绍一些学习心得

### 学习编程的一些资源

[OI Wiki](https://oi-wiki.org/)

[学堂在线](https://www.xuetangx.com/)

[Hello 算法](https://www.hello-algo.com/)

[C Primer Plus](https://ed.qcea.top/ChaIndex/Resources/Ebook/computer/c/C Primer Plus（第6版）中文版.pdf)

[C++ Primer Plus](https://ed.qcea.top/ChaIndex/Resources/Ebook/computer/c++/C++ Primer Plus（第5版）.pdf)

[算法竞赛入门经典（第2版） (刘汝佳) ](https://ed.qcea.top/ChaIndex/Resources/Ebook/computer/algorithms/算法竞赛入门经典（第2版） (刘汝佳) (Z-Library).epub)

[Linux就该这样学](https://ed.qcea.top/ChaIndex/Resources/Ebook/computer/linux/LinuxProbe.pdf)

[Python编程：从入门到实践](https://ed.qcea.top/ChaIndex/Resources/Ebook/computer/Python/Python编程：从入门到实践（第2版） ([美]埃里克·马瑟斯（Eric Matthes）) (Z-Library).pdf)

[数学建模相关](https://ed.qcea.top/ChaIndex/Resources/Ebook/MCM)

[机器人实验室Wiki教学资源模块](https://sdnuroboticsailab.github.io/)

[Linux 中国](https://linux.net.cn/)

[It's FOSS ](https://itsfoss.com/)

[开源观察](https://fosscope.com/)

[洛谷](https://www.luogu.com.cn/)

[力扣 (LeetCode)](https://leetcode.cn/problemset/)

[Codeforces](https://codeforces.com/)

[牛客网](https://www.nowcoder.com/)

[实验室OJ](http://120.26.104.144/)

### 官方文档/Wiki>网络教程>AI>师哥师姐

#### 网站资源

这个是覆盖面积最广的，也是质量最参差不齐的

首先是 [**CSDN**](https://www.csdn.net/)，这个东西很抽象，应该是国内最老牌的技术交流网站，但是正因如此质量参差不齐，有很多灌水，缝合，抄袭的文章。所以说在上面找资源等于史里掏金，当然对于初学者而言还是很有帮助的（~~Gitcode~~）

然后是字节搞的[稀土掘金](https://juejin.cn/)，观感比CSDN好多了，但是也有缺陷就是有时候想搜的内容在上面搜不到

比较推荐的是 [stackoverflow](https://stackoverflow.com/)，全世界知名的技术交流论坛，但是对英语能力有一定要求

然后可能有同学想看视频资源，b站也是个不错的选择，但是质量更是参差不齐，我觉得大部分看文档就能理解没必要去浪费时间看视频，除非视频资源真的讲的很好。

很多优质的个人博客也可以研究学习

其他诸如极客时间等等就不一一介绍了

#### 学会看官方文档

官方文档其实可以说是了解一个组件最高效的方式，在有一定编程基础后看官方文档入门是不二之选

以下图为例，这是 Halo 的官方文档，介绍了包含的所有官方库以及其他功能

![09](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/Misc/lesson0-2024-tech/09.png)

很多组件是国外开发的，因此也是英文的，看懂其实并不难，只是一开始会有畏难情绪，能过四级就没多大阅读障碍了

如果实在看起觉得恼火可以找找有没有中文镜像站或者直接整页翻译

#### 学会看源码

这个估计已经是很高级的能力了，与 Java 能用到退休的教程和生态相比，Go虽然也不是很年轻了，但是肯定也是会遇到没有教程的时候。

这时候咋办？看源码！

而且看源码还能提高你的 Coding 能力，在找工作面试的时候面试官也很有可能问到 go 的一些常见底层实现。例如看到某个库的教程觉得讲的太烂了，这个时候就可以去看看相应的源码

除此之外学习也是从“抄袭”开始的，抄的是代码逻辑，排版风格...然后把这些东西融会贯通贯通成为自己的，GitHub上就有很多开源项目供大家学习

### 时间管理能力

> 觉得上了大学之后没有想象中那么轻松？觉得一周里课太多？觉得事情很多忙不过来？

这也是很多同学大一时会犯的通病

首先我们需要明确一个前提：**靠学校教的东西以后出去吃不了饭**

> 如果你的目标是本科毕业直接就业，那么你绝对需要自己好好规划时间

首先说本科毕业就业，那么你对绩点就不需要那么看重了，每科能过就行

就大一上而言，需要重视的就是高数和线代。难道C语言就不重要了吗？当然很重要，重要的是它是很多人接触的第一门编程语言，能培养编程思维。说C语言不需要重视是因为学校里教的很水，拿我自己举例子，我暑假学了一点C，上课一节课没听最后期末总成绩都能上90。也就是说有这时间听老师上课讲不如自己自学。高数和线代要好好学，要不然期末突击也不太好过。

因此可以得出除了高数和线代都是水课，一周加起来也才五节课，这么来看是不是就轻松很多了呢。其他时间可以狠狠地拿来学编程了，老师管的严的把电脑搬到最后一排坐着；管的不严的emm。。你懂的

> 那我想保研或者考研咋办呢

考研的话其实和上面差别不大，只是不能抱着只是为了通过考试的心态了，要正儿八经好好学**想考专业的专业课**。

但是保研的话就不一样了，我反正觉得挺坐牢的😭，每门课你都得认真对待，平时分考试分都不能落下。上课该回答问题就回答问题🙋

### 考研篇



### 保研篇



### 就业篇



## 后记

**选择大于努力**

That's all
