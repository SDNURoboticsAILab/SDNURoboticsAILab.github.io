# 基于树莓派和 OpenCV 的人脸识别门禁系统

你是否曾惊叹于电影中那些通过“刷脸”即可进入的安全门？或是对手机上秒速解锁的人脸识别功能感到好奇？这些看似尖端的“黑科技”，其实离我们并不遥远。本项目将带你亲手打造一个迷你版的人脸识别门禁系统，将人工智能的强大能力，浓缩在一块小小的卡片式电脑——树莓派（Raspberry Pi）上。

树莓派，作为一款功能强大的微型计算机，是通往物联网（IoT）和嵌入式系统世界的绝佳入口。它能运行完整的 Linux 操作系统，让我们有机会在真实的硬件上实践软件开发与系统控制。而 OpenCV，作为计算机视觉领域最经典、最强大的开源库，则将赋予我们的树莓派一双能够“看见”和“认识”世界的眼睛。

在这个项目中，你不仅会学习到：

- **Linux 操作系统**：掌握服务器和嵌入式设备上最主流的操作系统的基本使用。
- **硬件交互**：亲手连接并驱动摄像头等外部设备，体验软件与硬件结合的魅力。
- **计算机视觉（CV）**：了解人脸检测与人脸识别的核心原理，并用代码实现它。
- **项目实践能力**：从零开始，一步步搭建、调试并最终完成一个功能完整的AI应用。

让我们一起动手，将代码注入硬件，赋予这块小小的电路板智能，打造属于你自己的第一个AI硬件作品！

### 项目须知与准备工作

1. **硬件设备**：本项目所需的核心硬件（树莓派、SD卡、摄像头模块、电源线等）可前往实验室 **文淙楼211** 借用。
2. **耐心与毅力**：硬件项目与纯软件开发不同，可能会遇到驱动不兼容、线路接触不良等问题。请保持耐心，学会通过查阅资料和动手尝试来解决问题。
3. **学习资源**：善用搜索引擎（Google/Bing）、CSDN、哔哩哔哩等平台查找教程。遇到问题时，先尝试自己解决，这也是工程师必备的核心能力。
4. **前置知识**：建议具备基础的 Python 编程和 Linux 命令行操作知识。如果不熟悉，请参考下方 Level 0 的资料先行学习。
5. **及格线**：想要通过考核，你至少要完成 **Level 3**。考核说明和提交要求详见：[https://sdnuroboticsailab.github.io/others/2025-autumn-engineering-challenges/](https://sdnuroboticsailab.github.io/others/2025-autumn-engineering-challenges/)

## Level 0：了解树莓派使用

- **树莓派 (Raspberry Pi)**：它是什么？能做什么？了解其基本接口（如GPIO, USB, CSI）。
- **Linux 基础命令**：学习如何在终端（Terminal）中进行文件和目录操作（ls, cd, mkdir）、编辑文件（nano 或 vim）、安装软件（apt-get）等。
- **OpenCV**：了解它是一个用于处理图像和视频的库，我们将用它来捕获摄像头画面、检测人脸和识别人脸。

### 参考资料：

[Ubuntu及Vim编辑器的使用方法和基础指令_ubuntuvim编辑器-CSDN博客](https://blog.csdn.net/weixin_73503608/article/details/139479617?ops_request_misc=%7B%22request%5Fid%22%3A%221df436dd884e30ca6f95dd40c8dfc920%22%2C%22scm%22%3A%2220140713.130102334.pc%5Fall.%22%7D&request_id=1df436dd884e30ca6f95dd40c8dfc920&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-2-139479617-null-null.142^v102^pc_search_result_base7&utm_term=unbuntu基础指令使用教程&spm=1018.2226.3001.4187)

[树莓派人脸识别-CSDN博客](https://blog.csdn.net/weixin_65169583/article/details/138563427?ops_request_misc=&request_id=&biz_id=102&utm_term=树莓派人脸识别项目&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-3-138563427.142^v102^pc_search_result_base7&spm=1018.2226.3001.4187)

[树莓派官方烧录工具Raspberry Pi Imager-CSDN博客](https://blog.csdn.net/qq_58018816/article/details/136131968?ops_request_misc=%7B%22request%5Fid%22%3A%22fae4f3342ea9824ffc2dc928208a7d36%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=fae4f3342ea9824ffc2dc928208a7d36&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-136131968-null-null.142^v102^pc_search_result_base7&utm_term=树莓派烧录系统到sd卡&spm=1018.2226.3001.4187)

[树莓派安装opencv及其扩展包contrib（python3）_python3-opencvcontrib-CSDN博客](https://blog.csdn.net/qq_39125451/article/details/116172832)

[树莓派人脸识别基础使用 – 旧梦逆心的秘密基地](https://www.lichengkun.com/index.php/2025/09/03/树莓派人脸识别基础使用/)

## Level 1：系统烧录与远程连接

### 任务目标：

1. 为树莓派的 SD 卡烧录官方操作系统。
2. 通过命令行（SSH）和图形界面（VNC）远程控制你的树莓派。

### 评估标准：

- 使用 Raspberry Pi Imager 工具，成功将系统镜像烧录到 SD 卡中。
-  将树莓派连接到网络，并通过 SSH 或 PuTTY 成功登录到树莓派的命令行终端。
- 在树莓派上开启 VNC 服务，并使用 VNC Viewer 在你的电脑上成功显示树莓派的图形桌面。

### 参考资料：

可以参考CSDN的博客：[树莓派官方烧录工具Raspberry Pi Imager-CSDN博客](https://blog.csdn.net/qq_58018816/article/details/136131968?ops_request_misc=%7B%22request%5Fid%22%3A%22fae4f3342ea9824ffc2dc928208a7d36%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=fae4f3342ea9824ffc2dc928208a7d36&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-136131968-null-null.142^v102^pc_search_result_base7&utm_term=树莓派烧录系统到sd卡&spm=1018.2226.3001.4187)

相关软件的官网：https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.htm

[Download VNC Viewer by RealVNC®](https://www.realvnc.com/en/connect/download/viewer/?lai_vid=aqJqr8NB0iQr&lai_sr=5-9&lai_sl=l)

https://www.raspberrypi.com/software/

## Level 2：获取摄像头实时画面

让我们的系统拥有“视觉”。在这一步，我们将安装计算机视觉库 OpenCV，并编写代码来驱动摄像头，捕获实时的视频流。

### 任务目标：

1. 在树莓派上成功安装 OpenCV 库及其依赖。
2. 编写 Python 脚本，调用摄像头并实时显示画面。

### 评估标准：

- 成功在树莓派上安装 Python 版的 OpenCV 及其扩展包 (opencv-contrib-python)。

- 运行代码后，电脑屏幕上能弹出一个窗口，实时显示树莓派摄像头所拍摄到的画面。

  运行结果如下：

  ![](https://gastigado.cnies.org/d/others/1f8b1b3ec8192b96c088d396374c07ca.png?sign=YfgoYKJ16gb9K6HLtbV9-F4cvI6cWw_p3XstPYWtJSY=:0)

### 参考资料：

OpenCV 安装教程: [树莓派安装opencv及其扩展包contrib（python3）](https://blog.csdn.net/qq_39125451/article/details/116172832)

## Level 3：实现图片人脸识别功能

要让系统“认识”人，我们首先得“教”它。这一步，我们将采集人脸数据，并训练一个初步的人脸识别模型。

## 任务目标：

1. 下载用于人脸**检测**的预训练模型（Haar Cascade）。
2. 创建自己的人脸**数据集**。
3. 训练一个人脸**识别器**，并用它来识别静态图片中的人物。

## 评估标准：

- 成功下载 haarcascade_frontalface_default.xml 模型文件，并准备好用于存放人脸图片的数据库文件夹。模型可从此链接下载：[OpenCV Haar Cascades GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades)。
- 运行数据采集脚本，从数据集中读取所有人脸图片，并训练 OpenCV 识别器，最终生成一个 .yml 格式的模型训练文件。
- 运行识别脚本，程序能够准确识别出数据库图片中的人物，用方框框出人脸并在一旁标出对应的名字。

![](https://gastigado.cnies.org/d/others/8a1233cd59c67a8d11a154644d69df47.png?sign=L5ocwJV_Ln4yluGB0C8Hx2eXLp83xMVjauHSjimE90U=:0)

## Level 4：实现实时识别与语音播报

### 任务目标：

1. 实现实时录入新的人脸信息到数据库。
2. 在实时视频流中识别出已知人物或判断为陌生人。
3. 对识别结果进行语音播报。

### 评估标准：

- 程序支持现场录入新的人脸，拍摄的照片能自动保存到指定的数据集文件夹中。
- 系统运行时，能对摄像头画面中的人脸进行实时识别。如果识别出是数据库中的成员，则语音播报其名字；如果是陌生人，则播报“陌生人，禁止进入”等提示信息。

### 参考资料：

- 项目综合教程: [树莓派人脸识别基础使用](https://www.lichengkun.com/index.php/2025/09/03/%E6%A0%91%E8%8E%93%E6%B4%BE%E4%BA%BA%E8%84%B8%E8%AF%86%E5%88%AB%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8/)
- CSDN项目参考: [树莓派人脸识别](https://blog.csdn.net/weixin_65169583/article/details/138563427)