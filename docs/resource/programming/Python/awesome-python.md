---
comments: true
---
# Awesome Python [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> 来源: https://github.com/vinta/awesome-python

一份精选的 Python 框架、库、软件和资源列表。

灵感来源于 [awesome-php](https://github.com/ziadoz/awesome-php)。

- [Awesome Python](#awesome-python)
    - [管理面板 (Admin Panels)](#admin-panels)
    - [算法与设计模式 (Algorithms and Design Patterns)](#algorithms-and-design-patterns)
    - [ASGI 服务器 (ASGI Servers)](#asgi-servers)
    - [异步编程 (Asynchronous Programming)](#asynchronous-programming)
    - [音频 (Audio)](#audio)
    - [认证 (Authentication)](#authentication)
    - [构建工具 (Build Tools)](#build-tools)
    - [内置类增强 (Built-in Classes Enhancement)](#built-in-classes-enhancement)
    - [缓存 (Caching)](#caching)
    - [ChatOps 工具 (ChatOps Tools)](#chatops-tools)
    - [内容管理系统 (CMS)](#cms)
    - [代码分析 (Code Analysis)](#code-analysis)
    - [命令行界面开发 (Command-line Interface Development)](#command-line-interface-development)
    - [命令行工具 (Command-line Tools)](#command-line-tools)
    - [计算机视觉 (Computer Vision)](#computer-vision)
    - [配置文件 (Configuration Files)](#configuration-files)
    - [密码学 (Cryptography)](#cryptography)
    - [数据分析 (Data Analysis)](#data-analysis)
    - [数据验证 (Data Validation)](#data-validation)
    - [数据可视化 (Data Visualization)](#data-visualization)
    - [数据库驱动 (Database Drivers)](#database-drivers)
    - [数据库 (Database)](#database)
    - [日期和时间 (Date and Time)](#date-and-time)
    - [调试工具 (Debugging Tools)](#debugging-tools)
    - [深度学习 (Deep Learning)](#deep-learning)
    - [DevOps 工具 (DevOps Tools)](#devops-tools)
    - [分布式计算 (Distributed Computing)](#distributed-computing)
    - [分发 (Distribution)](#distribution)
    - [文档 (Documentation)](#documentation)
    - [下载器 (Downloader)](#downloader)
    - [编辑器插件和 IDE (Editor Plugins and IDEs)](#editor-plugins-and-ides)
    - [电子邮件 (Email)](#email)
    - [环境管理 (Environment Management)](#environment-management)
    - [文件处理 (File Manipulation)](#file-manipulation)
    - [函数式编程 (Functional Programming)](#functional-programming)
    - [游戏开发 (Game Development)](#game-development)
    - [地理定位 (Geolocation)](#geolocation)
    - [GUI 开发 (GUI Development)](#gui-development)
    - [硬件 (Hardware)](#hardware)
    - [HTML 处理 (HTML Manipulation)](#html-manipulation)
    - [HTTP 客户端 (HTTP Clients)](#http-clients)
    - [图像处理 (Image Processing)](#image-processing)
    - [Python 实现 (Implementations)](#implementations)
    - [交互式解释器 (Interactive Interpreter)](#interactive-interpreter)
    - [国际化 (Internationalization)](#internationalization)
    - [任务调度 (Job Scheduler)](#job-scheduler)
    - [日志 (Logging)](#logging)
    - [机器学习 (Machine Learning)](#machine-learning)
    - [杂项 (Miscellaneous)](#miscellaneous)
    - [自然语言处理 (Natural Language Processing)](#natural-language-processing)
    - [网络虚拟化 (Network Virtualization)](#network-virtualization)
    - [新闻订阅 (News Feed)](#news-feed)
    - [ORM](#orm)
    - [包管理 (Package Management)](#package-management)
    - [包仓库 (Package Repositories)](#package-repositories)
    - [渗透测试 (Penetration testing)](#penetration-testing)
    - [权限 (Permissions)](#permissions)
    - [进程 (Processes)](#processes)
    - [推荐系统 (Recommender Systems)](#recommender-systems)
    - [代码重构 (Refactoring)](#refactoring)
    - [RESTful API](#restful-api)
    - [机器人 (Robotics)](#robotics)
    - [RPC 服务器 (RPC Servers)](#rpc-servers)
    - [科学计算 (Science)](#science)
    - [搜索 (Search)](#search)
    - [序列化 (Serialization)](#serialization)
    - [无服务器框架 (Serverless Frameworks)](#serverless-frameworks)
    - [Shell](#shell)
    - [特定格式处理 (Specific Formats Processing)](#specific-formats-processing)
    - [静态网站生成器 (Static Site Generator)](#static-site-generator)
    - [标签 (Tagging)](#tagging)
    - [任务队列 (Task Queues)](#task-queues)
    - [模板引擎 (Template Engine)](#template-engine)
    - [测试 (Testing)](#testing)
    - [文本处理 (Text Processing)](#text-processing)
    - [第三方 API (Third-party APIs)](#third-party-apis)
    - [URL 处理 (URL Manipulation)](#url-manipulation)
    - [视频 (Video)](#video)
    - [Web 资源管理 (Web Asset Management)](#web-asset-management)
    - [Web 内容提取 (Web Content Extracting)](#web-content-extracting)
    - [Web 爬虫 (Web Crawling)](#web-crawling)
    - [Web 框架 (Web Frameworks)](#web-frameworks)
    - [WebSocket](#websocket)
    - [WSGI 服务器 (WSGI Servers)](#wsgi-servers)
- [资源 (Resources)](#resources)
    - [新闻资讯 (Newsletters)](#newsletters)
    - [播客 (Podcasts)](#podcasts)
- [贡献 (Contributing)](#contributing)

---

## 管理面板 (Admin Panels)

*用于管理界面的库。*

* [ajenti](https://github.com/ajenti/ajenti) - 你的服务器值得拥有的管理面板。
* [django-grappelli](https://github.com/sehmaschine/django-grappelli) - Django Admin-Interface 的一个炫酷皮肤。
* [flask-admin](https://github.com/flask-admin/flask-admin) - 用于 Flask 的简单且可扩展的管理界面框架。
* [flower](https://github.com/mher/flower) - Celery 的实时监控和 Web 管理界面。
* [jet-bridge](https://github.com/jet-admin/jet-bridge) - 适用于任何具有漂亮 UI 的应用程序的管理面板框架 (例如 Jet Django)。
* [wooey](https://github.com/wooey/wooey) - 一个能为 Python 脚本自动创建 Web UI 的 Django 应用。
* [streamlit](https://github.com/streamlit/streamlit) - 一个能让你在几分钟内构建仪表盘、生成报告或创建聊天应用的框架。

## 算法与设计模式 (Algorithms and Design Patterns)

*数据结构、算法和设计模式的 Python 实现。另请参阅 [awesome-algorithms](https://github.com/tayllan/awesome-algorithms)。*

* 算法
    * [algorithms](https://github.com/keon/algorithms) - 数据结构和算法的极简示例。
    * [python-ds](https://github.com/prabhupant/python-ds) - 用于编程面试的数据结构和算法集合。
    * [sortedcontainers](https://github.com/grantjenks/python-sortedcontainers) - 快速且纯 Python 实现的有序集合。
    * [thealgorithms](https://github.com/TheAlgorithms/Python) - 所有用 Python 实现的算法。
* 设计模式
    * [pypattyrn](https://github.com/tylerlaberge/PyPattyrn) - 一个简单而有效的库，用于实现常见的设计模式。
    * [python-patterns](https://github.com/faif/python-patterns) - Python 中的设计模式集合。
    * [transitions](https://github.com/pytransitions/transitions) - 一个轻量级、面向对象的有限状态机实现。

## ASGI 服务器 (ASGI Servers)

*[ASGI](https://asgi.readthedocs.io/en/latest/) 兼容的 Web 服务器。*

* [daphne](https://github.com/django/daphne) - 一个用于 ASGI 和 ASGI-HTTP 的 HTTP、HTTP2 和 WebSocket 协议服务器。
* [uvicorn](https://github.com/encode/uvicorn) - 一个基于 uvloop 和 httptools 实现的闪电般快速的 ASGI 服务器。
* [hypercorn](https://github.com/pgjones/hypercorn) - 一个基于 Hyper 库并受 Gunicorn 启发的 ASGI 和 WSGI 服务器。

## 异步编程 (Asynchronous Programming)

*用于异步、并发和并行执行的库。另请参阅 [awesome-asyncio](https://github.com/timofurrer/awesome-asyncio)。*

* [asyncio](https://docs.python.org/3/library/asyncio.html) - (Python 标准库) 异步 I/O、事件循环、协程和任务。
    - [awesome-asyncio](https://github.com/timofurrer/awesome-asyncio)
* [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) - (Python 标准库) 一个用于异步执行可调用对象的高级接口。
* [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) - (Python 标准库) 基于进程的并行。
* [trio](https://github.com/python-trio/trio) - 一个友好的异步并发和 I/O 库。
* [twisted](https://github.com/twisted/twisted) - 一个事件驱动的网络引擎。
* [uvloop](https://github.com/MagicStack/uvloop) - 超快速的 asyncio 事件循环。
* [eventlet](https://github.com/eventlet/eventlet) - 支持 WSGI 的异步框架。
* [gevent](https://github.com/gevent/gevent) - 一个基于协程的 Python 网络库，使用 [greenlet](https://github.com/python-greenlet/greenlet)。

## 音频 (Audio)

*用于处理音频及其元数据的库。*

* 音频
    * [audioread](https://github.com/beetbox/audioread) - 跨库 (GStreamer + Core Audio + MAD + FFmpeg) 音频解码。
    * [audioFlux](https://github.com/libAudioFlux/audioFlux) - 一个用于音频和音乐分析、特征提取的库。
    * [dejavu](https://github.com/worldveil/dejavu) - 音频指纹识别。
    * [kapre](https://github.com/keunwoochoi/kapre) - Keras 音频预处理器。
    * [librosa](https://github.com/librosa/librosa) - 用于音频和音乐分析的 Python 库。
    * [matchering](https://github.com/sergree/matchering) - 一个用于自动化参考音频母带处理的库。
    * [mingus](http://bspaans.github.io/python-mingus/) - 一个带有 MIDI 文件和播放支持的高级音乐理论和记谱包。
    * [pyaudioanalysis](https://github.com/tyiannak/pyAudioAnalysis) - 音频特征提取、分类、分割和应用。
    * [pydub](https://github.com/jiaaro/pydub) - 通过简单易用的高级接口处理音频。
    * [timeside](https://github.com/Parisson/TimeSide) - 开放的 Web 音频处理框架。
* 元数据
    * [beets](https://github.com/beetbox/beets) - 音乐库管理器和 [MusicBrainz](https://musicbrainz.org/) 标签器。
    * [eyed3](https://github.com/nicfit/eyeD3) - 一个处理音频文件（特别是包含 ID3 元数据的 MP3 文件）的工具。
    * [mutagen](https://github.com/quodlibet/mutagen) - 一个处理音频元数据的 Python 模块。
    * [tinytag](https://github.com/devsnd/tinytag) - 一个用于读取 MP3、OGG、FLAC 和 Wave 文件音乐元数据的库。

## 认证 (Authentication)

*用于实现认证方案的库。*

* OAuth
    * [authlib](https://github.com/lepture/authlib) - JavaScript 对象签名和加密草案的实现。
    * [django-allauth](https://github.com/pennersr/django-allauth) - “开箱即用” 的 Django 认证应用。
    * [django-oauth-toolkit](https://github.com/jazzband/django-oauth-toolkit) - 用于 Django 的 OAuth 2 工具。
    * [oauthlib](https://github.com/oauthlib/oauthlib) - 一个通用且完整的 OAuth 请求签名逻辑实现。
* JWT
    * [pyjwt](https://github.com/jpadilla/pyjwt) - Python 中的 JSON Web Token 实现。
    * [python-jose](https://github.com/mpdavis/python-jose/) - Python 中的 JOSE 实现。

## 构建工具 (Build Tools)

*从源代码编译软件。*

* [bitbake](https://github.com/openembedded/bitbake) - 一个类似 make 的嵌入式 Linux 构建工具。
* [buildout](https://github.com/buildout/buildout) - 用于从多个部分创建、组装和部署应用程序的构建系统。
* [platformio](https://github.com/platformio/platformio-core) - 一个用于通过不同开发平台构建代码的控制台工具。
* [pybuilder](https://github.com/pybuilder/pybuilder) - 一个用纯 Python 编写的持续构建工具。
* [scons](https://github.com/SCons/scons) - 一款软件构建工具。

## 内置类增强 (Built-in Classes Enhancement)

*用于增强 Python 内置类的库。*

* [attrs](https://github.com/python-attrs/attrs) - 替代类定义中 `__init__`、`__eq__`、`__repr__` 等的样板代码。
* [bidict](https://github.com/jab/bidict) - 高效、Pythonic 的双向映射数据结构和相关功能。
* [box](https://github.com/cdgriffith/Box) - 支持高级点符号访问的 Python 字典。
* [dataclasses](https://docs.python.org/3/library/dataclasses.html) - (Python 标准库) 数据类。
* [dotteddict](https://github.com/carlosescri/DottedDict) - 一个提供通过点路径表示法访问列表和字典的库。

## 内容管理系统 (CMS)

*内容管理系统。*

* [feincms](https://github.com/feincms/feincms) - 基于 Django 构建的最先进的内容管理系统之一。
* [indico](https://github.com/indico/indico) - 一个功能丰富的事件管理系统，由 [CERN](https://en.wikipedia.org/wiki/CERN) 制作。
* [wagtail](https://github.com/wagtail/wagtail) - 一个 Django 内容管理系统。

## 缓存 (Caching)

*用于缓存数据的库。*

* [beaker](https://github.com/bbangert/beaker) - 一个用于会话和缓存的 WSGI 中间件。
* [django-cache-machine](https://github.com/django-cache-machine/django-cache-machine) - Django 模型的自动缓存和失效。
* [django-cacheops](https://github.com/Suor/django-cacheops) - 一个支持自动粒度事件驱动失效的智能 ORM 缓存。
* [dogpile.cache](https://github.com/sqlalchemy/dogpile.cache) - dogpile.cache 是由 Beaker 的原作者们制作的下一代替代品。
* [hermescache](https://pypi.org/project/HermesCache/) - 具有基于标签的失效和雪崩效应预防功能的 Python 缓存库。
* [pylibmc](https://github.com/lericson/pylibmc) - [libmemcached](https://libmemcached.org/libMemcached.html) 接口的 Python 封装。
* [python-diskcache](https://github.com/grantjenks/python-diskcache) - 基于 SQLite 和文件的缓存后端，查找速度比 memcached 和 redis 更快。

## ChatOps 工具 (ChatOps Tools)

*用于聊天机器人开发的库。*

* [errbot](https://github.com/errbotio/errbot/) - 最简单且最流行的聊天机器人，用于实现 ChatOps。

## 代码分析 (Code Analysis)

*静态分析、linter 和代码质量检查工具。另请参阅 [awesome-static-analysis](https://github.com/mre/awesome-static-analysis)。*

* 代码分析
    * [code2flow](https://github.com/scottrogowski/code2flow) - 将你的 Python 和 JavaScript 代码转换为 DOT 流程图。
    * [prospector](https://github.com/PyCQA/prospector) - 一个分析 Python 代码的工具。
    * [vulture](https://github.com/jendrikseipp/vulture) - 一个用于查找和分析无用 Python 代码的工具。
* 代码 Linter
    * [flake8](https://github.com/PyCQA/flake8) - 对 `pycodestyle`、`pyflakes` 和 McCabe 的封装。
        * [awesome-flake8-extensions](https://github.com/DmytroLitvinov/awesome-flake8-extensions)
    * [pylint](https://github.com/pylint-dev/pylint) - 一个完全可定制的源代码分析器。
    * [ruff](https://github.com/astral-sh/ruff) - 一个极速的 Python linter 和代码格式化工具。
* 代码格式化
    * [black](https://github.com/psf/black) - 不妥协的 Python 代码格式化工具。
    * [isort](https://github.com/timothycrosley/isort) - 一个用于排序导入的 Python 工具/库。
    * [yapf](https://github.com/google/yapf) - 来自 Google 的又一个 Python 代码格式化工具。
* 静态类型检查，另请参阅 [awesome-python-typing](https://github.com/typeddjango/awesome-python-typing)
    * [mypy](https://github.com/python/mypy) - 在编译时检查变量类型。
    * [pyre-check](https://github.com/facebook/pyre-check) - 高性能的类型检查。
    * [typeshed](https://github.com/python/typeshed) - 带有静态类型的 Python 库 stub 集合。
* 静态类型注解生成器
    * [monkeytype](https://github.com/Instagram/MonkeyType) - 一个通过收集运行时类型来为 Python 生成静态类型注解的系统。
    * [pytype](https://github.com/google/pytype) - Pytype 可以在不需要类型注解的情况下，为 Python 代码检查并推断类型。

## 命令行界面开发 (Command-line Interface Development)

*用于构建命令行应用的库。*

* 命令行应用开发
    * [cement](https://github.com/datafolklabs/cement) - Python 的 CLI 应用框架。
    * [click](https://github.com/pallets/click/) - 一个以可组合方式创建优美命令行界面的包。
    * [cliff](https://github.com/openstack/cliff) - 一个用于创建多级命令的命令行程序的框架。
    * [python-fire](https://github.com/google/python-fire) - 一个可以从任何 Python 对象创建命令行界面的库。
    * [python-prompt-toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit) - 一个用于构建强大交互式命令行的库。
* 终端渲染
    * [alive-progress](https://github.com/rsalmei/alive-progress) - 一种新型的进度条，具有实时吞吐量、预计完成时间和非常酷的动画。
    * [asciimatics](https://github.com/peterbrittain/asciimatics) - 一个创建全屏文本 UI 的包（从交互式表单到 ASCII 动画）。
    * [bashplotlib](https://github.com/glamp/bashplotlib) - 在终端中制作基本绘图。
    * [colorama](https://github.com/tartley/colorama) - 跨平台的彩色终端文本。
    * [rich](https://github.com/Textualize/rich) - 用于在终端中显示富文本和优美格式的 Python 库。还提供了一个出色的 `RichHandler` 日志处理器。
    * [tqdm](https://github.com/tqdm/tqdm) - 用于循环和 CLI 的快速、可扩展的进度条。

## 命令行工具 (Command-line Tools)

*用于提高生产力的有用 CLI 工具。*

* 生产力工具
    * [copier](https://github.com/copier-org/copier) - 一个用于渲染项目模板的库和命令行工具。
    * [cookiecutter](https://github.com/cookiecutter/cookiecutter) - 一个从 cookiecutters (项目模板) 创建项目的命令行工具。
    * [doitlive](https://github.com/sloria/doitlive) - 一个用于在终端中进行现场演示的工具。
    * [howdoi](https://github.com/gleitz/howdoi) - 通过命令行即时获得编码答案。
    * [invoke](https://github.com/pyinvoke/invoke) - 一个用于管理面向 shell 的子进程并将可执行 Python 代码组织成 CLI 可调用任务的工具。
    * [pathpicker](https://github.com/facebook/PathPicker) - 从 bash 输出中选择文件。
    * [thefuck](https://github.com/nvbn/thefuck) - 修正你上一条控制台命令。
    * [tmuxp](https://github.com/tmux-python/tmuxp) - 一个 [tmux](https://github.com/tmux/tmux) 会话管理器。
    * [try](https://github.com/timofurrer/try) - 一个极其简单的 CLI，用于尝试 Python 包——从未如此简单。
* CLI 增强
    * [httpie](https://github.com/httpie/cli) - 一个命令行 HTTP 客户端，是 cURL 的用户友好型替代品。
    * [iredis](https://github.com/laixintao/iredis) - 具有自动补全和语法高亮的 Redis CLI。
    * [litecli](https://github.com/dbcli/litecli) - 具有自动补全和语法高亮的 SQLite CLI。
    * [mycli](https://github.com/dbcli/mycli) - 具有自动补全和语法高亮的 MySQL CLI。
    * [pgcli](https://github.com/dbcli/pgcli) - 具有自动补全和语法高亮的 PostgreSQL CLI。

## 计算机视觉 (Computer Vision)

*用于计算机视觉的库。*

* [easyocr](https://github.com/JaidedAI/EasyOCR) - 开箱即用的 OCR，支持 40 多种语言。
* [kornia](https://github.com/kornia/kornia/) - 用于 PyTorch 的开源可微分计算机视觉库。
* [opencv](https://opencv.org/) - 开源计算机视觉库。
* [pytesseract](https://github.com/madmaze/pytesseract) - [Google Tesseract OCR](https://github.com/tesseract-ocr) 的一个封装。
* [tesserocr](https://github.com/sirfz/tesserocr) - 另一个简单、对 Pillow 友好的 `tesseract-ocr` API 封装，用于 OCR。

## 配置文件 (Configuration Files)

*用于存储和解析配置选项的库。*

* [configparser](https://docs.python.org/3/library/configparser.html) - (Python 标准库) INI 文件解析器。
* [configobj](https://github.com/DiffSK/configobj) - 带验证的 INI 文件解析器。
* [hydra](https://github.com/facebookresearch/hydra) - Hydra 是一个用于优雅配置复杂应用程序的框架。
* [python-decouple](https://github.com/HBNetwork/python-decouple) - 将设置与代码严格分离。

## 密码学 (Cryptography)

* [cryptography](https://github.com/pyca/cryptography) - 一个旨在向 Python 开发者公开加密原语和配方的包。
* [paramiko](https://github.com/paramiko/paramiko) - 领先的原生 Python SSHv2 协议库。
* [pynacl](https://github.com/pyca/pynacl) - 网络和密码学 (NaCl) 库的 Python 绑定。

## 数据分析 (Data Analysis)

*用于数据分析的库。*

* [pandas](http://pandas.pydata.org/) - 提供高性能、易于使用的数据结构和数据分析工具的库。
* [aws-sdk-pandas](https://github.com/aws/aws-sdk-pandas) - AWS 上的 Pandas。
* [datasette](https://github.com/simonw/datasette) - 一个用于探索和发布数据的开源多功能工具。
* [optimus](https://github.com/hi-primus/optimus) - 使用 PySpark 轻松实现敏捷数据科学工作流。

## 数据验证 (Data Validation)

*用于验证数据的库。在许多情况下用于表单验证。*

* [cerberus](https://github.com/pyeve/cerberus) - 一个轻量级且可扩展的数据验证库。
* [colander](https://github.com/Pylons/colander) - 验证和反序列化通过 XML、JSON、HTML 表单 post 获得的数据。
* [jsonschema](https://github.com/python-jsonschema/jsonschema) - [JSON Schema](http://json-schema.org/) 的 Python 实现。
* [schema](https://github.com/keleshev/schema) - 一个用于验证 Python 数据结构的库。
* [schematics](https://github.com/schematics/schematics) - 数据结构验证。
* [voluptuous](https://github.com/alecthomas/voluptuous) - 一个 Python 数据验证库。
* [pydantic](https://github.com/pydantic/pydantic) - 使用 Python 类型提示进行数据验证。

## 数据可视化 (Data Visualization)

*用于数据可视化的库。另请参阅 [awesome-javascript](https://github.com/sorrycc/awesome-javascript#data-visualization)。*

* [altair](https://github.com/altair-viz/altair) - 用于 Python 的声明式统计可视化库。
* [bokeh](https://github.com/bokeh/bokeh) - 用于 Python 的交互式 Web 绘图。
* [bqplot](https://github.com/bloomberg/bqplot) - Jupyter Notebook 的交互式绘图库。
* [cartopy](https://github.com/SciTools/cartopy) - 一个支持 matplotlib 的地图绘制 Python 库。
* [diagrams](https://github.com/mingrammer/diagrams) - 代码即图表。
* [matplotlib](https://github.com/matplotlib/matplotlib) - 一个 Python 2D 绘图库。
* [plotnine](https://github.com/has2k1/plotnine) - 一个基于 ggplot2 的 Python 图形语法。
* [pygal](https://github.com/Kozea/pygal) - 一个 Python SVG 图表创建器。
* [pygraphviz](https://github.com/pygraphviz/pygraphviz/) - [Graphviz](http://www.graphviz.org/) 的 Python 接口。
* [pyqtgraph](https://github.com/pyqtgraph/pyqtgraph) - 交互式实时 2D/3D/图像绘图和科学/工程小部件。
* [seaborn](https://github.com/mwaskom/seaborn) - 使用 Matplotlib 进行统计数据可视化。
* [vispy](https://github.com/vispy/vispy) - 基于 OpenGL 的高性能科学可视化。

## 数据库 (Database)

*用 Python 实现的数据库。*

* [pickleDB](https://github.com/patx/pickledb) - 一个简单轻量级的 Python 键值存储。
* [tinydb](https://github.com/msiemens/tinydb) - 一个微型的、面向文档的数据库。
* [zodb](https://github.com/zopefoundation/ZODB) - Python 的原生对象数据库。一个键值和对象图数据库。

## 数据库驱动 (Database Drivers)

*用于连接和操作数据库的库。*

* MySQL - [awesome-mysql](http://shlomi-noach.github.io/awesome-mysql/)
    * [mysqlclient](https://github.com/PyMySQL/mysqlclient) - 支持 Python 3 的 MySQL 连接器 ([mysql-python](https://sourceforge.net/projects/mysql-python/) 的 fork)。
    * [pymysql](https://github.com/PyMySQL/PyMySQL) - 一个与 mysql-python 兼容的纯 Python MySQL 驱动。
* PostgreSQL - [awesome-postgres](https://github.com/dhamaniasad/awesome-postgres)
    * [psycopg](https://github.com/psycopg/psycopg) - 最流行的 Python PostgreSQL 适配器。
* SQLite - [awesome-sqlite](https://github.com/planetopendata/awesome-sqlite)
    * [sqlite3](https://docs.python.org/3/library/sqlite3.html) - (Python 标准库) 兼容 DB-API 2.0 的 SQLite 接口。
    * [sqlite-utils](https://github.com/simonw/sqlite-utils) - 用于操作 SQLite 数据库的 Python CLI 工具和库。
* 其他关系型数据库
    * [pymssql](https://github.com/pymssql/pymssql) - 一个简单的 Microsoft SQL Server 数据库接口。
    * [clickhouse-driver](https://github.com/mymarilyn/clickhouse-driver) - 带有原生接口的 ClickHouse Python 驱动。
* NoSQL 数据库
    * [cassandra-driver](https://github.com/datastax/python-driver) - Apache Cassandra 的 Python 驱动。
    * [happybase](https://github.com/python-happybase/happybase) - 一个对开发者友好的 Apache HBase 库。
    * [kafka-python](https://github.com/dpkp/kafka-python) - Apache Kafka 的 Python 客户端。
    * [pymongo](https://github.com/mongodb/mongo-python-driver) - MongoDB 的官方 Python 客户端。
    * [motor](https://github.com/mongodb/motor) - MongoDB 的异步 Python 驱动。
    * [redis-py](https://github.com/redis/redis-py) - Redis 的 Python 客户端。

## 日期和时间 (Date and Time)

*用于处理日期和时间的库。*

* [arrow](https://github.com/arrow-py/arrow) - 一个 Python 库，提供了一种明智且人性化的方法来创建、操作、格式化和转换日期、时间和时间戳。
* [dateutil](https://github.com/dateutil/dateutil) - 标准 Python [datetime](https://docs.python.org/3/library/datetime.html) 模块的扩展。
* [pendulum](https://github.com/sdispater/pendulum) - 让 Python 的 datetimes 变得简单。
* [pytz](https://pypi.org/project/pytz/) - 世界时区定义，现代和历史的。将 [tz database](https://en.wikipedia.org/wiki/Tz_database) 引入 Python。

## 调试工具 (Debugging Tools)

*用于调试代码的库。*

* pdb-like 调试器
    * [ipdb](https://github.com/gotcha/ipdb) - 支持 IPython 的 [pdb](https://docs.python.org/3/library/pdb.html)。
    * [pudb](https://github.com/inducer/pudb) - 一个全屏、基于控制台的 Python 调试器。
* Tracing (追踪)
    * [manhole](https://github.com/ionelmc/python-manhole) - 调试 UNIX 套接字连接，并为所有线程呈现堆栈跟踪和一个交互式提示符。
    * [python-hunter](https://github.com/ionelmc/python-hunter) - 一个灵活的代码追踪工具包。
* Profiler (性能分析器)
    * [py-spy](https://github.com/benfred/py-spy) - Python 程序的采样性能分析器。用 Rust 编写。
    * [vprof](https://github.com/nvdv/vprof) - 可视化 Python 性能分析器。
* 其他
    * [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) - 为 Django 显示各种调试信息。
    * [flask-debugtoolbar](https://github.com/pallets-eco/flask-debugtoolbar) - django-debug-toolbar 的 flask 移植版。
    * [icecream](https://github.com/gruns/icecream) - 通过一个简单的函数调用来检查变量、表达式和程序执行。
    * [pyelftools](https://github.com/eliben/pyelftools) - 解析和分析 ELF 文件和 DWARF 调试信息。

## 深度学习 (Deep Learning)

*用于神经网络和深度学习的框架。另请参阅 [awesome-deep-learning](https://github.com/ChristosChristofidis/awesome-deep-learning)。*

* [keras](https://github.com/keras-team/keras) - 一个高级神经网络库，能够运行在 TensorFlow 或 Theano 之上。
* [pytorch](https://github.com/pytorch/pytorch) - Python 中的张量和动态神经网络，具有强大的 GPU 加速功能。
* [pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) - 深度学习框架，用于快速训练、部署和交付 AI 产品。
* [stable-baselines3](https://github.com/DLR-RM/stable-baselines3) - Stable Baselines (深度) 强化学习算法的 PyTorch 实现。
* [tensorflow](https://github.com/tensorflow/tensorflow) - 由 Google 创建的最受欢迎的深度学习框架。
* [theano](https://github.com/Theano/Theano) - 一个用于快速数值计算的库。

## DevOps 工具 (DevOps Tools)

*用于 DevOps 的软件和库。*

* 配置管理
    * [ansible](https://github.com/ansible/ansible) - 一个极其简单的 IT 自动化平台。
    * [cloudinit](https://github.com/canonical/cloud-init) - 一个处理云实例早期初始化的多发行版包。
    * [openstack](https://www.openstack.org/) - 用于构建私有云和公有云的开源软件。
    * [pyinfra](https://github.com/pyinfra-dev/pyinfra) - 一个多功能的 CLI 工具和 Python 库，用于自动化基础设施。
    * [saltstack](https://github.com/saltstack/salt) - 基础设施自动化和管理系统。
* SSH-style 部署
    * [cuisine](https://github.com/sebastien/cuisine) - Fabric 的类 Chef 功能。
    * [fabric](https://github.com/fabric/fabric) - 一个简单、Pythonic 的远程执行和部署工具。
* 进程管理
    * [supervisor](https://github.com/Supervisor/supervisor) - 用于 UNIX 的 Supervisor 进程控制系统。
* 监控
    * [psutil](https://github.com/giampaolo/psutil) - 一个跨平台的进程和系统实用程序模块。
* 备份
    * [borg](https://github.com/borgbackup/borg) - 一个带压缩和加密的去重归档器。

## 分布式计算 (Distributed Computing)

*用于分布式计算的框架和库。*

* 批处理
    * [dask](https://github.com/dask/dask) - 一个用于分析计算的灵活并行计算库。
    * [luigi](https://github.com/spotify/luigi) - 一个帮助你构建复杂批处理作业管道的模块。
    * [PySpark](https://github.com/apache/spark) - [Apache Spark](https://spark.apache.org/) Python API。
    * [Ray](https://github.com/ray-project/ray/) - 一个用于并行和分布式 Python 的系统，统一了机器学习的生态系统。
* 流处理
    * [faust](https://github.com/robinhood/faust) - 一个流处理库，将 [Kafka Streams](https://kafka.apache.org/documentation/streams/) 的思想移植到 Python。
    * [streamparse](https://github.com/Parsely/streamparse) - 通过 [Apache Storm](http://storm.apache.org/) 对实时数据流运行 Python 代码。

## 分发 (Distribution)

*创建用于发布分发的打包可执行文件的库。*

* [py2app](https://github.com/ronaldoussoren/py2app) - 冻结 Python 脚本 (Mac OS X)。
* [py2exe](https://github.com/py2exe/py2exe) - 冻结 Python 脚本 (Windows)。
* [pyarmor](https://github.com/dashingsoft/pyarmor) - 一个用于混淆 python 脚本、将混淆后的脚本绑定到固定机器或使混淆后的脚本过期的工具。
* [pyinstaller](https://github.com/pyinstaller/pyinstaller) - 将 Python 程序转换为独立的可执行文件 (跨平台)。
* [shiv](https://github.com/linkedin/shiv) - 一个命令行工具，用于构建完全自包含的 zipapps (PEP 441)，但包含其所有依赖项。

## 文档 (Documentation)

*用于生成项目文档的库。*

* [sphinx](https://github.com/sphinx-doc/sphinx/) - Python 文档生成器。
    * [awesome-sphinxdoc](https://github.com/yoloseem/awesome-sphinxdoc)
* [pdoc](https://github.com/mitmproxy/pdoc) - Epydoc 的替代品，用于为 Python 库自动生成 API 文档。

## 下载器 (Downloader)

*用于下载的库。*

* [akshare](https://github.com/jindaxiang/akshare) - 一个为人类构建的金融数据接口库！
* [s3cmd](https://github.com/s3tools/s3cmd) - 一个用于管理 Amazon S3 和 CloudFront 的命令行工具。
* [youtube-dl](https://github.com/ytdl-org/youtube-dl/) - 一个用于从 YouTube 和其他视频网站下载视频的命令行程序。

## 编辑器插件和 IDE (Editor Plugins and IDEs)

* Emacs
    * [elpy](https://github.com/jorgenschaefer/elpy) - Emacs Python 开发环境。
* Vim
    * [jedi-vim](https://github.com/davidhalter/jedi-vim) - Jedi 自动补全库的 Vim 绑定。
    * [python-mode](https://github.com/python-mode/python-mode) - 一个将 Vim 变成 Python IDE 的全能插件。
    * [YouCompleteMe](https://github.com/Valloric/YouCompleteMe) - 包含基于 [Jedi](https://github.com/davidhalter/jedi) 的 Python 补全引擎。
* Visual Studio
    * [PTVS](https://github.com/Microsoft/PTVS) - Visual Studio 的 Python 工具。
* Visual Studio Code
    * [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - 官方 VSCode 扩展，对 Python 提供丰富的支持。
* IDE
    * [PyCharm](https://www.jetbrains.com/pycharm/) - JetBrains 出品的商业 Python IDE。有免费社区版。
    * [spyder](https://github.com/spyder-ide/spyder) - 开源 Python IDE。

## 电子邮件 (Email)

*用于发送和解析电子邮件的库。*

* 邮件服务器
    * [modoboa](https://github.com/modoboa/modoboa) - 一个邮件托管和管理平台，包括一个现代化的 Web UI。
    * [salmon](https://github.com/moggers87/salmon) - 一个 Python 邮件服务器。
* 客户端
    * [imbox](https://github.com/martinrusev/imbox) - 为人类设计的 Python IMAP。
    * [yagmail](https://github.com/kootenpv/yagmail) - 又一个 Gmail/SMTP 客户端。
* 其他
    * [flanker](https://github.com/mailgun/flanker) - 一个电子邮件地址和 Mime 解析库。
    * [mailer](https://github.com/marrow/mailer) - 高性能可扩展的邮件投递框架。

## 环境管理 (Environment Management)

*用于 Python 版本和虚拟环境管理的库。*

* [pyenv](https://github.com/pyenv/pyenv) - 简单的 Python 版本管理。
* [virtualenv](https://github.com/pypa/virtualenv) - 一个创建隔离 Python 环境的工具。

## 文件处理 (File Manipulation)

*用于文件处理的库。*

* [mimetypes](https://docs.python.org/3/library/mimetypes.html) - (Python 标准库) 将文件名映射到 MIME 类型。
* [pathlib](https://docs.python.org/3/library/pathlib.html) - (Python 标准库) 一个跨平台、面向对象的路径库。
* [path.py](https://github.com/jaraco/path.py) - [os.path](https://docs.python.org/3/library/os.path.html) 的模块封装。
* [python-magic](https://github.com/ahupp/python-magic) - libmagic 文件类型识别库的 Python 接口。
* [watchdog](https://github.com/gorakhargosh/watchdog) - 用于监控文件系统事件的 API 和 shell 工具。

## 函数式编程 (Functional Programming)

*用 Python 进行函数式编程。*

* [coconut](https://github.com/evhub/coconut) - 为简单、优雅、Pythonic 的函数式编程而构建的 Python 变体。
* [funcy](https://github.com/Suor/funcy) - 一个酷炫实用的函数式工具。
* [more-itertools](https://github.com/erikrose/more-itertools) - `itertools` 之外更多用于操作可迭代对象的例程。
* [returns](https://github.com/dry-python/returns) - 一组类型安全的 monad、transformer 和组合工具。
* [cytoolz](https://github.com/pytoolz/cytoolz/) - `Toolz` 的 Cython 实现：高性能的函数式工具。
* [toolz](https://github.com/pytoolz/toolz) - 用于迭代器、函数和字典的函数式工具集合。

## GUI 开发 (GUI Development)

*用于图形用户界面应用的库。*

* [curses](https://docs.python.org/3/library/curses.html) - 内置的 [ncurses](http://www.gnu.org/software/ncurses/) 封装，用于创建终端 GUI 应用。
* [Eel](https://github.com/ChrisKnott/Eel) - 用于制作类似 Electron 的简单离线 HTML/JS GUI 应用的库。
* [enaml](https://github.com/nucleic/enaml) - 用类似 QML 的声明式语法创建漂亮的用户界面。
* [Flexx](https://github.com/zoofIO/flexx) - Flexx 是一个纯 Python 工具包，用于创建 GUI，使用 Web 技术进行渲染。
* [Gooey](https://github.com/chriskiehl/Gooey) - 一行代码将命令行程序变成完整的 GUI 应用。
* [kivy](https://kivy.org/) - 一个用于创建 NUI 应用的库，可在 Windows、Linux、Mac OS X、Android 和 iOS 上运行。
* [pyglet](https://github.com/pyglet/pyglet) - 一个跨平台的 Python 窗口和多媒体库。
* [PyGObject](https://pygobject.readthedocs.io/) - GLib/GObject/GIO/GTK+ (GTK+3) 的 Python 绑定。
* [PyQt](https://doc.qt.io/qtforpython/) - [Qt](https://www.qt.io/) 跨平台应用和 UI 框架的 Python 绑定。
* [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI) - tkinter、Qt、WxPython 和 Remi 的封装。
* [pywebview](https://github.com/r0x0r/pywebview/) - 一个围绕 webview 组件的轻量级跨平台原生封装。
* [Tkinter](https://wiki.python.org/moin/TkInter) - Tkinter 是 Python 事实上的标准 GUI 包。
* [Toga](https://github.com/pybee/toga) - 一个 Python 原生、操作系统原生的 GUI 工具包。
* [urwid](http://urwid.org/) - 一个用于创建终端 GUI 应用的库，对小部件、事件、丰富色彩等有强大支持。
* [wxPython](https://wxpython.org/) - wxWidgets C++ 类库与 Python 的融合。
* [DearPyGui](https://github.com/RaylockLLC/DearPyGui/) - 一个简单的 GPU 加速 Python GUI 框架。

## GraphQL

*用于处理 GraphQL 的库。*

* [graphene](https://github.com/graphql-python/graphene/) - Python 的 GraphQL 框架。

## 游戏开发 (Game Development)

*优秀的游戏开发库。*

* [Arcade](https://api.arcade.academy/en/latest/) - Arcade 是一个现代 Python 框架，用于制作具有引人入胜的图形和声音的游戏。
* [Cocos2d](https://www.cocos.com/en/cocos2d-x) - cocos2d 是一个用于构建 2D 游戏、演示和其他图形/交互式应用的框架。
* [Harfang3D](http://www.harfang3d.com) - 用于 3D、VR 和游戏开发的 Python 框架。
* [Panda3D](https://www.panda3d.org/) - 由迪士尼开发的 3D 游戏引擎。
* [Pygame](http://www.pygame.org/news.html) - Pygame 是一组专为编写游戏而设计的 Python 模块。
* [PyOgre](http://www.ogre3d.org/tikiwiki/PyOgre) - Ogre 3D 渲染引擎的 Python 绑定，可用于游戏、模拟等任何 3D 应用。
* [PyOpenGL](http://pyopengl.sourceforge.net/) - OpenGL 及其相关 API 的 Python ctypes 绑定。
* [PySDL2](https://pysdl2.readthedocs.io) - 基于 ctypes 的 SDL2 库封装。
* [RenPy](https://www.renpy.org/) - 一个视觉小说引擎。

## 地理定位 (Geolocation)

*用于地理编码地址和处理经纬度的库。*

* [django-countries](https://github.com/SmileyChris/django-countries) - 一个为模型和表单提供国家字段的 Django 应用。
* [geodjango](https://docs.djangoproject.com/en/dev/ref/contrib/gis/) - 一个世界级的地理 Web 框架。
* [geojson](https://github.com/jazzband/geojson) - 用于 GeoJSON 的 Python 绑定和工具。
* [geopy](https://github.com/geopy/geopy) - Python 地理编码工具箱。

## HTML 处理 (HTML Manipulation)

*用于处理 HTML 和 XML 的库。*

* [beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - 为迭代、搜索和修改 HTML 或 XML 提供 Pythonic 的习惯用法。
* [bleach](https://github.com/mozilla/bleach) - 一个基于白名单的 HTML 清理和文本链接化库。
* [cssutils](https://pypi.org/project/cssutils/) - 一个用于 Python 的 CSS 库。
* [html5lib](https://github.com/html5lib/html5lib-python) - 一个符合标准的库，用于解析和序列化 HTML 文档和片段。
* [lxml](http://lxml.de/) - 一个非常快速、易于使用且功能多样的处理 HTML 和 XML 的库。
* [markupsafe](https://github.com/pallets/markupsafe) - 为 Python 实现了一个 XML/HTML/XHTML 标记安全字符串。
* [pyquery](https://github.com/gawel/pyquery) - 一个类似 jQuery 的 HTML 解析库。
* [untangle](https://github.com/stchris/untangle) - 将 XML 文档转换为 Python 对象以便于访问。
* [WeasyPrint](http://weasyprint.org) - 一个可以导出为 PDF 的 HTML 和 CSS 可视化渲染引擎。
* [xmldataset](https://xmldataset.readthedocs.io/en/latest/) - 简单的 XML 解析。
* [xmltodict](https://github.com/martinblech/xmltodict) - 使用 XML 就像使用 JSON 一样。

## HTTP 客户端 (HTTP Clients)

*用于处理 HTTP 的库。*

* [httpx](https://github.com/encode/httpx) - 下一代 Python HTTP 客户端。
* [requests](https://github.com/psf/requests) - 为人类设计的 HTTP 请求库。
* [treq](https://github.com/twisted/treq) - 基于 Twisted 的 HTTP 客户端构建的类似 requests 的 API。
* [urllib3](https://github.com/urllib3/urllib3) - 一个具有线程安全连接池、文件 post 支持、易于使用的 HTTP 库。

## 硬件 (Hardware)

*用于硬件编程的库。*

* [keyboard](https://github.com/boppreh/keyboard) - 在 Windows 和 Linux 上挂钩和模拟全局键盘事件。
* [mouse](https://github.com/boppreh/mouse) - 在 Windows 和 Linux 上挂钩和模拟全局鼠标事件。
* [pynput](https://github.com/moses-palmer/pynput) - 一个控制和监控输入设备的库。
* [scapy](https://github.com/secdev/scapy) - 一个出色的数据包处理库。

## 图像处理 (Image Processing)

*用于处理图像的库。*

* [pillow](https://github.com/python-pillow/Pillow) - Pillow 是友好的 [PIL](http://www.pythonware.com/products/pil/) fork。
* [python-barcode](https://github.com/WhyNotHugo/python-barcode) - 在 Python 中创建条形码，无需额外依赖。
* [pymatting](http://github.com/pymatting/pymatting) - 一个用于 alpha matting (抠图) 的库。
* [python-qrcode](https://github.com/lincolnloop/python-qrcode) - 一个纯 Python QR 码生成器。
* [pywal](https://github.com/dylanaraps/pywal) - 一个从图像生成配色方案的工具。
* [pyvips](https://github.com/libvips/pyvips) - 一个内存需求低、速度快的图像处理库。
* [quads](https://github.com/fogleman/Quads) - 基于四叉树的计算机艺术。
* [scikit-image](http://scikit-image.org/) - 一个用于 (科学) 图像处理的 Python 库。
* [thumbor](https://github.com/thumbor/thumbor) - 一个智能图像服务。它能按需裁剪、调整大小和翻转图像。
* [wand](https://github.com/emcconville/wand) - [MagickWand](http://www.imagemagick.org/script/magick-wand.php) (ImageMagick 的 C API) 的 Python 绑定。

## Python 实现 (Implementations)

*Python 的各种实现。*

* [cpython](https://github.com/python/cpython) - **默认、使用最广泛的用 C 语言编写的 Python 编程语言实现。**
* [cython](https://github.com/cython/cython) - Python 的优化静态编译器。
* [clpython](https://github.com/metawilm/cl-python) - 用 Common Lisp 编写的 Python 编程语言实现。
* [ironpython](https://github.com/IronLanguages/ironpython3) - 用 C# 编写的 Python 编程语言实现。
* [micropython](https://github.com/micropython/micropython) - 一个精简高效的 Python 编程语言实现。
* [numba](https://github.com/numba/numba) - 面向科学 Python 的 LLVM JIT 编译器。
* [peachpy](https://github.com/Maratyszcza/PeachPy) - 嵌入在 Python 中的 x86-64 汇编器。
* [pypy](https://foss.heptapod.net/pypy/pypy) - 一个非常快速且兼容的 Python 语言实现。
* [pyston](https://github.com/pyston/pyston/) - 一个使用 JIT 技术的 Python 实现。

## 交互式解释器 (Interactive Interpreter)

*交互式 Python 解释器 (REPL)。*

* [bpython](https://github.com/bpython/bpython) - 一个精美的 Python 解释器界面。
* [Jupyter Notebook (IPython)](https://jupyter.org) - 一个丰富的工具包，帮助你最大限度地利用交互式 Python。
    * [awesome-jupyter](https://github.com/markusschanta/awesome-jupyter)
* [ptpython](https://github.com/jonathanslenders/ptpython) - 基于 [python-prompt-toolkit](https://github.com/jonathanslenders/python-prompt-toolkit) 构建的高级 Python REPL。

## 国际化 (Internationalization)

*用于处理 i18n 的库。*

* [Babel](http://babel.pocoo.org/en/latest/) - Python 的国际化库。
* [PyICU](https://github.com/ovalhub/pyicu) - International Components for Unicode C++ 库 ([ICU](http://site.icu-project.org/)) 的一个封装。

## 任务调度 (Job Scheduler)

*用于调度任务的库。*

* [Airflow](https://airflow.apache.org/) - Airflow 是一个以编程方式编写、调度和监控工作流的平台。
* [APScheduler](http://apscheduler.readthedocs.io/en/latest/) - 一个轻量但强大的进程内任务调度器，可以让你调度函数。
* [django-schedule](https://github.com/thauber/django-schedule) - 一个用于 Django 的日历应用。
* [doit](http://pydoit.org/) - 一个任务运行器和构建工具。
* [gunnery](https://github.com/gunnery/gunnery) - 用于分布式系统的多功能任务执行工具，带有基于 Web 的界面。
* [Joblib](https://joblib.readthedocs.io/) - 一套在 Python 中提供轻量级流水线作业的工具。
* [Plan](https://github.com/fengsp/plan) - 像写代码一样轻松编写 crontab 文件。
* [Prefect](https://github.com/PrefectHQ/prefect) - 一个现代化的工作流编排框架，可以轻松构建、调度和监控稳健的数据管道。
* [schedule](https://github.com/dbader/schedule) - 为人类设计的 Python 任务调度库。
* [Spiff](https://github.com/knipknap/SpiffWorkflow) - 一个用纯 Python 实现的强大的工作流引擎。
* [TaskFlow](https://docs.openstack.org/developer/taskflow/) - 一个帮助任务执行变得简单、一致和可靠的 Python 库。

## 日志 (Logging)

*用于生成和处理日志的库。*

* [logbook](http://logbook.readthedocs.io/en/stable/) - Python 日志的替代品。
* [logging](https://docs.python.org/3/library/logging.html) - (Python 标准库) Python 的日志工具。
* [loguru](https://github.com/Delgan/loguru) - 旨在为 Python 带来愉快日志体验的库。
* [sentry-python](https://github.com/getsentry/sentry-python) - 用于 Python 的 Sentry SDK。
* [structlog](https://www.structlog.org/en/stable/) - 结构化日志，变得简单。

## 机器学习 (Machine Learning)

*用于机器学习的库。另请参阅 [awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning#python)。*

* [gym](https://github.com/openai/gym) - 一个用于开发和比较强化学习算法的工具包。
* [H2O](https://github.com/h2oai/h2o-3) - 开源、快速、可扩展的机器学习平台。
* [Metrics](https://github.com/benhamner/Metrics) - 机器学习评估指标。
* [NuPIC](https://github.com/numenta/nupic) - Numenta 智能计算平台。
* [scikit-learn](http://scikit-learn.org/) - 最流行的 Python 机器学习库。
* [Spark ML](http://spark.apache.org/docs/latest/ml-guide.html) - [Apache Spark](http://spark.apache.org/) 的可扩展机器学习库。
* [vowpal_porpoise](https://github.com/josephreisinger/vowpal_porpoise) - [Vowpal Wabbit](https://github.com/JohnLangford/vowpal_wabbit/) 的轻量级 Python 封装。
* [xgboost](https://github.com/dmlc/xgboost) - 一个可扩展、便携且分布式的梯度提升库。
* [MindsDB](https://github.com/mindsdb/mindsdb) - MindsDB 是现有数据库的开源 AI 层，允许你使用标准查询轻松开发、训练和部署最先进的机器学习模型。

## Microsoft Windows

*在 Microsoft Windows 上进行 Python 编程。*

* [Python(x,y)](http://python-xy.github.io/) - 基于 Qt 和 Spyder 的面向科学应用的 Python 发行版。
* [pythonlibs](http://www.lfd.uci.edu/~gohlke/pythonlibs/) - Python 扩展包的非官方 Windows 二进制文件。
* [PythonNet](https://github.com/pythonnet/pythonnet) - Python 与 .NET 公共语言运行时 (CLR) 的集成。
* [PyWin32](https://github.com/mhammond/pywin32) - 用于 Windows 的 Python 扩展。
* [WinPython](https://winpython.github.io/) - 用于 Windows 7/8 的便携式开发环境。

## 杂项 (Miscellaneous)

*不适合上述类别的有用库或工具。*

* [blinker](https://github.com/jek/blinker) - 一个快速的 Python 进程内信号/事件分发系统。
* [boltons](https://github.com/mahmoud/boltons) - 一组纯 Python 工具。
* [itsdangerous](https://github.com/pallets/itsdangerous) - 将受信任数据传递到不受信任环境的各种辅助工具。
* [magenta](https://github.com/magenta/magenta) - 一个利用人工智能生成音乐和艺术的工具。
* [pluginbase](https://github.com/mitsuhiko/pluginbase) - 一个简单但灵活的 Python 插件系统。
* [tryton](http://www.tryton.org/) - 一个通用的商业框架。

## 自然语言处理 (Natural Language Processing)

*用于处理人类语言的库。*

- 通用
    * [gensim](https://github.com/RaRe-Technologies/gensim) - 为人类设计的主题建模。
    * [langid.py](https://github.com/saffsd/langid.py) - 独立的语言识别系统。
    * [nltk](http://www.nltk.org/) - 一个领先的平台，用于构建处理人类语言数据的 Python 程序。
    * [pattern](https://github.com/clips/pattern) - 一个网络挖掘模块。
    * [polyglot](https://github.com/aboSamoor/polyglot) - 支持数百种语言的自然语言处理管道。
    * [pytext](https://github.com/facebookresearch/pytext) - 一个基于 PyTorch 的自然语言建模框架。
    * [PyTorch-NLP](https://github.com/PetrochukM/PyTorch-NLP) - 一个支持快速进行深度学习 NLP 研究原型设计的工具包。
    * [spacy](https://spacy.io/) - 一个用于 Python 和 Cython 的工业级自然语言处理库。
    * [Stanza](https://github.com/stanfordnlp/stanza) - 斯坦福 NLP 小组的官方 Python 库，支持 60 多种语言。
- 中文
    * [funNLP](https://github.com/fighting41love/funNLP) - 一个中文 NLP 工具和数据集的集合。
    * [jieba](https://github.com/fxsjy/jieba) - 最流行的中文文本分割库。
    * [pkuseg-python](https://github.com/lancopku/pkuseg-python) - 一个用于各种领域中文分词的工具包。
    * [snownlp](https://github.com/isnowfy/snownlp) - 一个处理中文文本的库。

## 网络虚拟化 (Network Virtualization)

*用于虚拟网络和 SDN (软件定义网络) 的工具和库。*

* [mininet](https://github.com/mininet/mininet) - 一个用 Python 编写的流行网络模拟器和 API。
* [napalm](https://github.com/napalm-automation/napalm) - 用于操作网络设备的跨厂商 API。
* [pox](https://github.com/noxrepo/pox) - 一个基于 Python 的 SDN 控制应用，如 OpenFlow SDN 控制器。

## 新闻订阅 (News Feed)

*用于构建用户动态的库。*

* [django-activity-stream](https://github.com/justquick/django-activity-stream) - 从你网站上的行为生成通用活动流。
* [Stream Framework](https://github.com/tschellenbach/Stream-Framework) - 使用 Cassandra 和 Redis 构建新闻订阅和通知系统。

## ORM

*实现对象关系映射或数据映射技术的库。*

* 关系型数据库
    * [Django Models](https://docs.djangoproject.com/en/dev/topics/db/models/) - Django ORM。
    * [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL 工具包和对象关系映射器。
        * [awesome-sqlalchemy](https://github.com/dahlia/awesome-sqlalchemy)
    * [dataset](https://github.com/pudo/dataset) - 将 Python 字典存储在数据库中——适用于 SQLite、MySQL 和 PostgreSQL。
    * [orator](https://github.com/sdispater/orator) - Orator ORM 提供了一个简单而优美的 ActiveRecord 实现。
    * [orm](https://github.com/encode/orm) - 一个异步 ORM。
    * [peewee](https://github.com/coleifer/peewee) - 一个小巧、富有表现力的 ORM。
    * [pony](https://github.com/ponyorm/pony/) - 提供面向生成器的 SQL 接口的 ORM。
    * [pydal](https://github.com/web2py/pydal/) - 一个纯 Python 数据库抽象层。
* NoSQL 数据库
    * [hot-redis](https://github.com/stephenmcd/hot-redis) - Redis 的富 Python 数据类型。
    * [mongoengine](https://github.com/MongoEngine/mongoengine) - 一个用于处理 MongoDB 的 Python 对象-文档映射器。
    * [PynamoDB](https://github.com/pynamodb/PynamoDB) - [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 的 Pythonic 接口。
    * [redisco](https://github.com/kiddouk/redisco) - 一个用于在 Redis 中持久化简单模型和容器的 Python 库。

## 包管理 (Package Management)

*用于包和依赖管理的库。*

* [pip](https://pip.pypa.io/en/stable/) - Python 的包安装器。
    * [pip-tools](https://github.com/jazzband/pip-tools) - 一套用于保持你固定的 Python 依赖更新的工具。
    * [PyPI](https://pypi.org/)
* [conda](https://github.com/conda/conda/) - 跨平台、与 Python 无关的二进制包管理器。
* [poetry](https://github.com/sdispater/poetry) - Python 依赖管理和打包变得简单。

## 包仓库 (Package Repositories)

*本地 PyPI 仓库服务器和代理。*

* [bandersnatch](https://github.com/pypa/bandersnatch/) - Python 打包管理局 (PyPA) 提供的 PyPI 镜像工具。
* [devpi](https://github.com/devpi/devpi) - PyPI 服务器和打包/测试/发布工具。
* [localshop](https://github.com/jazzband/localshop) - 本地 PyPI 服务器 (自定义包和 pypi 自动镜像)。
* [warehouse](https://github.com/pypa/warehouse) - 下一代 Python 包仓库 (PyPI)。

## 渗透测试 (Penetration Testing)

*用于渗透测试的框架和工具。*

* [fsociety](https://github.com/Manisso/fsociety) - 一个渗透测试框架。
* [setoolkit](https://github.com/trustedsec/social-engineer-toolkit) - 一个社会工程学工具包。
* [sqlmap](https://github.com/sqlmapproject/sqlmap) - 自动 SQL 注入和数据库接管工具。

## 权限 (Permissions)

*允许或拒绝用户访问数据或功能的库。*

* [django-guardian](https://github.com/django-guardian/django-guardian) - 为 Django 1.2+ 实现的对象级权限。
* [django-rules](https://github.com/dfunckt/django-rules) - 一个小巧但强大的应用，为 Django 提供对象级权限，无需数据库。

## 进程 (Processes)

*用于启动和与操作系统进程通信的库。*

* [delegator.py](https://github.com/amitt001/delegator.py) - 为人类设计的 [Subprocesses](https://docs.python.org/3/library/subprocess.html) 2.0。
* [sarge](https://sarge.readthedocs.io/en/latest/) - subprocess 的又一个封装。
* [sh](https://github.com/amoffat/sh) - 一个功能齐全的 Python subprocess 替代品。

## 推荐系统 (Recommender Systems)

*用于构建推荐系统的库。*

* [annoy](https://github.com/spotify/annoy) - C++/Python 的近似最近邻，为内存使用优化。
* [fastFM](https://github.com/ibayer/fastFM) - 一个用于因子分解机的库。
* [implicit](https://github.com/benfred/implicit) - 针对隐式数据集的协同过滤的快速 Python 实现。
* [libffm](https://github.com/guestwalk/libffm) - 一个用于场感知因子分解机 (FFM) 的库。
* [lightfm](https://github.com/lyst/lightfm) - 多种流行推荐算法的 Python 实现。
* [spotlight](https://github.com/maciejkula/spotlight) - 使用 PyTorch 的深度推荐模型。
* [Surprise](https://github.com/NicolasHug/Surprise) - 一个用于构建和分析推荐系统的 scikit。
* [tensorrec](https://github.com/jfkirk/tensorrec) - TensorFlow 中的一个推荐引擎框架。

## 代码重构 (Refactoring)

*Python 的代码重构工具和库*

 * [Bicycle Repair Man](http://bicyclerepair.sourceforge.net/) - Bicycle Repair Man，一个 Python 的重构工具。
 * [Bowler](https://pybowler.io/) - 现代 Python 的安全代码重构。
 * [Rope](https://github.com/python-rope/rope) - Rope 是一个 python 重构库。

## RESTful API

*用于构建 RESTful API 的库。*

* Django
    * [django-rest-framework](https://github.com/encode/django-rest-framework) - 一个强大而灵活的构建 Web API 的工具包。
    * [django-tastypie](https://github.com/django-tastypie/django-tastypie) - 为 Django 应用创建美味的 API。
* Flask
    * [eve](https://github.com/pyeve/eve) - 由 Flask、MongoDB 和良好意图驱动的 REST API 框架。
    * [flask-api](https://github.com/flask-api/flask-api) - 用于 Flask 的可浏览 Web API。
    * [flask-restful](https://github.com/flask-restful/flask-restful) - 快速为 Flask 构建 REST API。
* Pyramid
    * [cornice](https://github.com/Cornices/cornice) - Pyramid 的 RESTful 框架。
* 框架无关
    * [falcon](https://github.com/falconry/falcon) - 一个用于构建云 API 和 Web 应用后端的高性能框架。
    * [fastapi](https://github.com/tiangolo/fastapi) - 一个现代、快速的 Web 框架，用于基于标准 Python 3.6+ 类型提示构建 API。
    * [hug](https://github.com/hugapi/hug) - 一个用于清晰地暴露 API 的 Python 3 框架。
    * [sandman2](https://github.com/jeffknupp/sandman2) - 为现有数据库驱动系统自动生成 REST API。
    * [sanic](https://github.com/sanic-org/sanic) - 一个为速度而生的 Python 3.6+ Web 服务器和 Web 框架。

## 机器人 (Robotics)

*用于机器人学的库。*

* [PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics) - 这是各种机器人算法及其可视化的汇编。
* [rospy](http://wiki.ros.org/rospy) - 这是 ROS (机器人操作系统) 的一个库。

## RPC 服务器 (RPC Servers)

*兼容 RPC 的服务器。*

* [RPyC](https://github.com/tomerfiliba/rpyc) (Remote Python Call) - 一个透明且对称的 Python RPC 库。
* [zeroRPC](https://github.com/0rpc/zerorpc-python) - zerorpc 是一个基于 [ZeroMQ](http://zeromq.org/) 和 [MessagePack](http://msgpack.org/) 的灵活 RPC 实现。

## 科学计算 (Science)

*用于科学计算的库。另请参阅 [Python-for-Scientists](https://github.com/TomNicholas/Python-for-Scientists)。*

* [astropy](http://www.astropy.org/) - 一个天文学领域的社区 Python 库。
* [bcbio-nextgen](https://github.com/chapmanb/bcbio-nextgen) - 为全自动高通量测序分析提供最佳实践流程。
* [bccb](https://github.com/chapmanb/bcbb) - 与生物分析相关的有用代码集合。
* [Biopython](http://biopython.org/wiki/Main_Page) - Biopython 是一套免费的生物计算工具。
* [cclib](http://cclib.github.io/) - 一个用于解析和解释计算化学软件包结果的库。
* [Colour](http://colour-science.org/) - 实现了大量的色彩理论转换和算法。
* [Karate Club](https://github.com/benedekrozemberczki/karateclub) - 用于图结构数据的无监督机器学习工具箱。
* [NetworkX](https://networkx.github.io/) - 一个用于复杂网络的高效软件。
* [NIPY](http://nipy.org) - 一系列神经影像工具包。
* [NumPy](http://www.numpy.org/) - Python 科学计算的基础包。
* [ObsPy](https://github.com/obspy/obspy/wiki/) - 一个用于地震学的 Python 工具箱。
* [Open Babel](https://open-babel.readthedocs.io/) - 一个旨在“说”多种化学数据语言的化学工具箱。
* [PyDy](http://www.pydy.org/) - Python Dynamics 的缩写，用于辅助动态运动建模的工作流程。
* [PyMC](https://github.com/pymc-devs/pymc3) - 马尔可夫链蒙特卡洛采样工具包。
* [QuTiP](http://qutip.org/) - Python 中的量子工具箱。
* [RDKit](http://www.rdkit.org/) - 化学信息学和机器学习软件。
* [SciPy](https://www.scipy.org/) - 一个基于 Python 的开源软件生态系统，用于数学、科学和工程。
* [SimPy](https://gitlab.com/team-simpy/simpy) - 一个基于进程的离散事件仿真框架。
* [statsmodels](https://github.com/statsmodels/statsmodels) - Python 中的统计建模和计量经济学。
* [SymPy](https://github.com/sympy/sympy) - 一个用于符号数学的 Python 库。
* [Zipline](https://github.com/quantopian/zipline) - 一个 Pythonic 的算法交易库。

## 搜索 (Search)

*用于索引数据和执行搜索查询的库和软件。*

* [django-haystack](https://github.com/django-haystack/django-haystack) - Django 的模块化搜索。
* [elasticsearch-dsl-py](https://github.com/elastic/elasticsearch-dsl-py) - Elasticsearch 的官方高级 Python 客户端。
* [elasticsearch-py](https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/index.html) - [Elasticsearch](https://www.elastic.co/products/elasticsearch) 的官方低级 Python 客户端。
* [pysolr](https://github.com/django-haystack/pysolr) - [Apache Solr](https://lucene.apache.org/solr/) 的一个轻量级 Python 封装。
* [whoosh](http://whoosh.readthedocs.io/en/latest/) - 一个快速、纯 Python 的搜索引擎库。

## 序列化 (Serialization)

*用于序列化复杂数据类型的库*

* [marshmallow](https://github.com/marshmallow-code/marshmallow) - 一个轻量级库，用于将复杂对象与简单 Python 数据类型之间进行转换。
* [pysimdjson](https://github.com/TkTech/pysimdjson) - [simdjson](https://github.com/lemire/simdjson) 的 Python 绑定。
* [python-rapidjson](https://github.com/python-rapidjson/python-rapidjson) - [RapidJSON](https://github.com/Tencent/rapidjson) 的一个 Python 封装。
* [ultrajson](https://github.com/esnme/ultrajson) - 一个用 C 编写并带有 Python 绑定的快速 JSON 解码器和编码器。

## 无服务器框架 (Serverless Frameworks)

*用于开发无服务器 Python 代码的框架。*

* [python-lambda](https://github.com/nficano/python-lambda) - 一个用于在 AWS Lambda 中开发和部署 Python 代码的工具包。
* [Zappa](https://github.com/zappa/Zappa) - 一个用于在 AWS Lambda 和 API Gateway 上部署 WSGI 应用的工具。

## Shell

*基于 Python 的 Shell。*

* [xonsh](https://github.com/xonsh/xonsh/) - 一个由 Python 驱动、跨平台、面向 Unix 的 shell 语言和命令提示符。

## 特定格式处理 (Specific Formats Processing)

*用于解析和处理特定文本格式的库。*

* 通用
    * [tablib](https://github.com/jazzband/tablib) - 一个用于 XLS、CSV、JSON、YAML 格式的表格数据集的模块。
* Office
    * [docxtpl](https://github.com/elapouya/python-docx-template) - 通过 jinja2 模板编辑 docx 文档。
    * [openpyxl](https://openpyxl.readthedocs.io/en/stable/) - 一个用于读写 Excel 2010 xlsx/xlsm/xltx/xltm 文件的库。
    * [pyexcel](https://github.com/pyexcel/pyexcel) - 提供一个 API 用于读取、操作和写入 csv、ods、xls、xlsx 和 xlsm 文件。
    * [python-docx](https://github.com/python-openxml/python-docx) - 读取、查询和修改 Microsoft Word 2007/2008 docx 文件。
    * [python-pptx](https://github.com/scanny/python-pptx) - 用于创建和更新 PowerPoint (.pptx) 文件的 Python 库。
    * [unoconv](https://github.com/unoconv/unoconv) - 在 LibreOffice/OpenOffice 支持的任何文档格式之间进行转换。
    * [XlsxWriter](https://github.com/jmcnamara/XlsxWriter) - 一个用于创建 Excel .xlsx 文件的 Python 模块。
    * [xlwings](https://github.com/ZoomerAnalytics/xlwings) - 一个 BSD 许可的库，可以轻松地从 Excel 调用 Python，反之亦然。
    * [xlwt](https://github.com/python-excel/xlwt) / [xlrd](https://github.com/python-excel/xlrd) - 从 Excel 文件中写入和读取数据及格式信息。
* PDF
    * [pdfminer.six](https://github.com/pdfminer/pdfminer.six) - Pdfminer.six 是原始 PDFMiner 的社区维护分支。
    * [PyPDF2](https://github.com/mstamy2/PyPDF2) - 一个能够分割、合并和转换 PDF 页面的库。
    * [ReportLab](https://www.reportlab.com/opensource/) - 允许快速创建丰富的 PDF 文档。
* Markdown
    * [Mistune](https://github.com/lepture/mistune) - 最快且功能齐全的纯 Python Markdown 解析器。
    * [Python-Markdown](https://github.com/waylan/Python-Markdown) - John Gruber's Markdown 的 Python 实现。
* YAML
    * [PyYAML](http://pyyaml.org/) - Python 的 YAML 实现。
* CSV
    * [csvkit](https://github.com/wireservice/csvkit) - 用于转换和处理 CSV 的工具。
* 归档
    * [unp](https://github.com/mitsuhiko/unp) - 一个可以轻松解压归档文件的命令行工具。

## 静态网站生成器 (Static Site Generator)

*静态网站生成器是一种将一些文本+模板作为输入并产生 HTML 文件作为输出的软件。*

* [lektor](https://github.com/lektor/lektor) - 一个易于使用的静态 CMS 和博客引擎。
* [mkdocs](https://github.com/mkdocs/mkdocs/) - 对 Markdown 友好的文档生成器。
* [makesite](https://github.com/sunainapai/makesite) - 简单、轻量且无魔法的静态网站/博客生成器 (< 130 行)。
* [nikola](https://github.com/getnikola/nikola) - 一个静态网站和博客生成器。
* [pelican](https://github.com/getpelican/pelican) - 支持 Markdown 和 reST 语法的静态网站生成器。

## 标签 (Tagging)

*用于为项目添加标签的库。*

* [django-taggit](https://github.com/jazzband/django-taggit) - Django 的简单标签功能。

## 任务队列 (Task Queues)

*用于处理任务队列的库。*

* [celery](https://docs.celeryproject.org/en/stable/) - 一个基于分布式消息传递的异步任务队列/作业队列。
* [dramatiq](https://github.com/Bogdanp/dramatiq) - 一个用于 Python 3 的快速可靠的后台任务处理库。
* [huey](https://github.com/coleifer/huey) - 小型的多线程任务队列。
* [mrq](https://github.com/pricingassistant/mrq) - 一个使用 Redis 和 gevent 的 Python 分布式工作任务队列。
* [rq](https://github.com/rq/rq) - Python 的简单作业队列。

## 模板引擎 (Template Engine)

*用于模板和词法分析的库和工具。*

* [Genshi](https://genshi.edgewall.org/) - 用于生成 Web 感知输出的 Python 模板工具包。
* [Jinja2](https://github.com/pallets/jinja) - 一个现代且对设计师友好的模板语言。
* [Mako](http://www.makotemplates.org/) - 用于 Python 平台的超快速和轻量级模板。

## 测试 (Testing)

*用于测试代码库和生成测试数据的库。*

* 测试框架
    * [hypothesis](https://github.com/HypothesisWorks/hypothesis) - Hypothesis 是一个先进的 Quickcheck 风格的基于属性的测试库。
    * [nose2](https://github.com/nose-devs/nose2) - `nose` 的继任者，基于 `unittest2`。
    * [pytest](https://docs.pytest.org/en/latest/) - 一个成熟且功能齐全的 Python 测试工具。
    * [Robot Framework](https://github.com/robotframework/robotframework) - 一个通用的测试自动化框架。
    * [unittest](https://docs.python.org/3/library/unittest.html) - (Python 标准库) 单元测试框架。
* 测试运行器
    * [green](https://github.com/CleanCut/green) - 一个简洁、多彩的测试运行器。
    * [mamba](http://nestorsalceda.github.io/mamba/) - Python 的终极测试工具。诞生于 BDD 的旗帜下。
    * [tox](https://tox.readthedocs.io/en/latest/) - 在多个 Python 版本中自动构建和测试分发包。
* GUI / Web 测试
    * [locust](https://github.com/locustio/locust) - 用 Python 编写的可扩展用户负载测试工具。
    * [PyAutoGUI](https://github.com/asweigart/pyautogui) - PyAutoGUI 是一个为人类设计的跨平台 GUI 自动化 Python 模块。
    * [Schemathesis](https://github.com/kiwicom/schemathesis) - 一个用于对使用 Open API / Swagger 规范构建的 Web 应用进行自动基于属性测试的工具。
    * [Selenium](https://pypi.org/project/selenium/) - [Selenium](http://www.seleniumhq.org/) WebDriver 的 Python 绑定。
    * [sixpack](https://github.com/seatgeek/sixpack) - 一个与语言无关的 A/B 测试框架。
    * [splinter](https://github.com/cobrateam/splinter) - 用于测试 Web 应用的开源工具。
* Mock
    * [doublex](https://pypi.org/project/doublex/) - 强大的 Python 测试替身框架。
    * [freezegun](https://github.com/spulec/freezegun) - 通过 mock datetime 模块来穿越时空。
    * [httmock](https://github.com/patrys/httmock) - 用于 Python 2.6+ 和 3.2+ 的 requests mock 库。
    * [httpretty](https://github.com/gabrielfalcao/HTTPretty) - Python 的 HTTP 请求 mock 工具。
    * [mock](https://docs.python.org/3/library/unittest.mock.html) - (Python 标准库) 一个 mock 和 patching 库。
    * [mocket](https://github.com/mindflayer/python-mocket) - 一个支持 gevent/asyncio/SSL 的 socket mock 框架。
    * [responses](https://github.com/getsentry/responses) - 一个用于 mock `requests` Python 库的工具库。
    * [VCR.py](https://github.com/kevin1024/vcrpy) - 在你的测试中记录和回放 HTTP 交互。
* 对象工厂
    * [factory_boy](https://github.com/FactoryBoy/factory_boy) - Python 的测试数据生成器替代品。
    * [mixer](https://github.com/klen/mixer) - 另一个测试数据生成器替代品。支持 Django、Flask、SQLAlchemy、Peewee 等。
    * [model_mommy](https://github.com/vandersonmota/model_mommy) - 在 Django 中创建用于测试的随机数据。
* 代码覆盖率
    * [coverage](https://pypi.org/project/coverage/) - 代码覆盖率测量。
* 伪造数据
    * [fake2db](https://github.com/emirozer/fake2db) - 伪造数据库生成器。
    * [faker](https://github.com/joke2k/faker) - 一个生成伪造数据的 Python 包。
    * [mimesis](https://github.com/lk-geimfari/mimesis) - 一个帮助你生成伪造数据的 Python 库。
    * [radar](https://pypi.org/project/radar/) - 生成随机的日期/时间。

## 文本处理 (Text Processing)

*用于解析和处理纯文本的库。*

* 通用
    * [chardet](https://github.com/chardet/chardet) - 兼容 Python 2/3 的字符编码检测器。
    * [difflib](https://docs.python.org/3/library/difflib.html) - (Python 标准库) 用于计算差异的辅助工具。
    * [ftfy](https://github.com/LuminosoInsight/python-ftfy) - 自动修复损坏的 Unicode 文本，使其更一致。
    * [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy) - 模糊字符串匹配。
    * [Levenshtein](https://github.com/ztane/python-Levenshtein/) - 快速计算 Levenshtein 距离和字符串相似度。
    * [pangu.py](https://github.com/vinta/pangu.py) - 偏执的文本间距。
    * [pyfiglet](https://github.com/pwaller/pyfiglet) - 用 Python 编写的 figlet 实现。
    * [pypinyin](https://github.com/mozillazg/python-pinyin) - 将汉字转换为拼音。
    * [textdistance](https://github.com/orsinium/textdistance) - 使用 30 多种算法计算序列之间的距离。
    * [unidecode](https://pypi.org/project/Unidecode/) - Unicode 文本的 ASCII 音译。
* Slugify
    * [awesome-slugify](https://github.com/dimka665/awesome-slugify) - 一个可以保留 unicode 的 Python slugify 库。
    * [python-slugify](https://github.com/un33k/python-slugify) - 一个将 unicode 转换为 ASCII 的 Python slugify 库。
    * [unicode-slugify](https://github.com/mozilla/unicode-slugify) - 一个以 Django 为依赖项、生成 unicode slug 的 slugifier。
* 唯一标识符
    * [hashids](https://github.com/davidaurelio/hashids-python) - [hashids](http://hashids.org) 的 Python 实现。
    * [shortuuid](https://github.com/skorokithakis/shortuuid) - 一个用于生成简洁、明确且 URL 安全的 UUID 的库。
* 解析器
    * [ply](https://github.com/dabeaz/ply) - lex 和 yacc 解析工具的 Python 实现。
    * [pygments](http://pygments.org/) - 一个通用的语法高亮器。
    * [pyparsing](https://github.com/pyparsing/pyparsing) - 一个用于生成解析器的通用框架。
    * [python-nameparser](https://github.com/derek73/python-nameparser) - 将人名解析为其各个组成部分。
    * [python-phonenumbers](https://github.com/daviddrysdale/python-phonenumbers) - 解析、格式化、存储和验证国际电话号码。
    * [python-user-agents](https://github.com/selwin/python-user-agents) - 浏览器用户代理字符串解析器。
    * [sqlparse](https://github.com/andialbrecht/sqlparse) - 一个非验证的 SQL 解析器。

## 第三方 API (Third-party APIs)

*用于访问第三方服务 API 的库。另请参阅 [List of Python API Wrappers and Libraries](https://github.com/realpython/list-of-python-api-wrappers)。*

* [apache-libcloud](https://libcloud.apache.org/) - 一个 Python 库通吃所有云。
* [boto3](https://github.com/boto/boto3) - 亚马逊网络服务 (AWS) 的 Python 接口。
* [django-wordpress](https://github.com/istrategylabs/django-wordpress) - 用于 Django 的 WordPress 模型和视图。
* [facebook-sdk](https://github.com/mobolic/facebook-sdk) - Facebook Platform Python SDK。
* [google-api-python-client](https://github.com/google/google-api-python-client) - Google APIs 的 Python 客户端库。
* [gspread](https://github.com/burnash/gspread) - Google Spreadsheets Python API。
* [twython](https://github.com/ryanmcgrath/twython) - Twitter API 的一个 Python 封装。

## URL 处理 (URL Manipulation)

*用于解析 URL 的库。*

* [furl](https://github.com/gruns/furl) - 一个使解析和操作 URL 变得简单的小型 Python 库。
* [purl](https://github.com/codeinthehole/purl) - 一个简单的、不可变的 URL 类，具有用于查询和操作的清晰 API。
* [pyshorteners](https://github.com/ellisonleao/pyshorteners) - 一个纯 Python URL 缩短库。
* [webargs](https://github.com/marshmallow-code/webargs) - 一个友好的库，用于解析 HTTP 请求参数，内置对流行 Web 框架的支持。

## 视频 (Video)

*用于处理视频和 GIF 的库。*

* [moviepy](https://zulko.github.io/moviepy/) - 一个用于基于脚本进行电影编辑的模块，支持多种格式，包括动画 GIF。
* [scikit-video](https://github.com/aizvorski/scikit-video) - 用于 SciPy 的视频处理例程。
* [vidgear](https://github.com/abhiTronix/vidgear) - 最强大的多线程视频处理框架。

## Web 资源管理 (Web Asset Management)

*用于管理、压缩和最小化网站资源的工具。*

* [django-compressor](https://github.com/django-compressor/django-compressor) - 将链接和内联的 JavaScript 或 CSS 压缩成单个缓存文件。
* [django-pipeline](https://github.com/jazzband/django-pipeline) - Django 的资源打包库。
* [django-storages](https://github.com/jschneier/django-storages) - Django 的自定义存储后端集合。
* [fanstatic](http://www.fanstatic.org/en/latest/) - 将静态文件依赖打包、优化并作为 Python 包提供。
* [fileconveyor](http://wimleers.com/fileconveyor) - 一个检测文件并将其同步到 CDN、S3 和 FTP 的守护进程。
* [flask-assets](https://github.com/miracle2k/flask-assets) - 帮助你将 webassets 集成到 Flask 应用中。
* [webassets](https://github.com/miracle2k/webassets) - 为静态资源打包、优化并管理唯一的缓存清除 URL。

## Web 内容提取 (Web Content Extracting)

*用于提取 Web 内容的库。*

* [html2text](https://github.com/Alir3z4/html2text) - 将 HTML 转换为 Markdown 格式的文本。
* [lassie](https://github.com/michaelhelmick/lassie) - 为人类设计的 Web 内容检索。
* [micawber](https://github.com/coleifer/micawber) - 一个用于从 URL 提取富内容的小型库。
* [newspaper](https://github.com/codelucas/newspaper) - Python 中的新闻提取、文章提取和内容策展。
* [python-readability](https://github.com/buriy/python-readability) - arc90's readability 工具的快速 Python 移植。
* [requests-html](https://github.com/psf/requests-html) - 为人类设计的 Pythonic HTML 解析。
* [sumy](https://github.com/miso-belica/sumy) - 一个用于自动摘要文本文档和 HTML 页面的模块。
* [textract](https://github.com/deanmalmgren/textract) - 从任何文档（Word、PowerPoint、PDF 等）中提取文本。
* [toapi](https://github.com/gaojiuli/toapi) - 每个网站都提供 API。

## Web 爬虫 (Web Crawling)

*用于自动化网页抓取的库。*

* [feedparser](https://github.com/kurtmckee/feedparser) - 通用 feed 解析器。
* [grab](https://github.com/lorien/grab) - 网站抓取框架。
* [mechanicalsoup](https://github.com/MechanicalSoup/MechanicalSoup) - 一个用于自动化与网站交互的 Python 库。
* [scrapy](https://github.com/scrapy/scrapy) - 一个快速的高级屏幕抓取和 Web 爬虫框架。

## Web 框架 (Web Frameworks)

*传统的全栈 Web 框架。另请参阅 [RESTful API](https://github.com/vinta/awesome-python#restful-api)。*

* 同步
    * [django](https://github.com/django/django) - Python 中最流行的 Web 框架。
        * [awesome-django](https://github.com/shahraizali/awesome-django)
        * [awesome-django](https://github.com/wsvincent/awesome-django)
    * [flask](https://github.com/pallets/flask) - Python 的微框架。
        * [awesome-flask](https://github.com/humiaozuzu/awesome-flask)
    * [pyramid](https://pylonsproject.org/) - 一个小巧、快速、务实、开源的 Python Web 框架。
        * [awesome-pyramid](https://github.com/uralbash/awesome-pyramid)
    * [masonite](https://github.com/MasoniteFramework/masonite) - 现代且以开发者为中心的 Python Web 框架。
* 异步
    * [tornado](https://github.com/tornadoweb/tornado) - 一个 Web 框架和异步网络库。

## WebSocket

*用于处理 WebSocket 的库。*

* [autobahn-python](https://github.com/crossbario/autobahn-python) - 用于 Twisted 和 [asyncio](https://docs.python.org/3/library/asyncio.html) 的 Python WebSocket 和 WAMP。
* [channels](https://github.com/django/channels) - 为 Django 提供对开发者友好的异步功能。
* [websockets](https://github.com/aaugustin/websockets) - 一个用于构建 WebSocket 服务器和客户端的库，注重正确性和简单性。

## WSGI 服务器 (WSGI Servers)

*兼容 WSGI 的 Web 服务器。*

* [gunicorn](https://github.com/benoitc/gunicorn) - 预分叉 (Pre-forked)，从 Ruby 的 Unicorn 项目移植而来。
* [uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/) - 一个旨在开发用于构建托管服务的完整技术栈的项目，用 C 编写。
* [waitress](https://github.com/Pylons/waitress) - 多线程，为 Pyramid 提供支持。
* [werkzeug](https://github.com/pallets/werkzeug) - 一个 Python 的 WSGI 工具库，为 Flask 提供支持，并可以轻松嵌入到你自己的项目中。

# 资源 (Resources)

在哪里发现学习资源或新的 Python 库。

## 新闻资讯 (Newsletters)

* [Awesome Python Newsletter](http://python.libhunt.com/newsletter)
* [Pycoder's Weekly](https://pycoders.com/)
* [Python Tricks](https://realpython.com/python-tricks/)
* [Python Weekly](https://www.pythonweekly.com/)

## 播客 (Podcasts)

* [Django Chat](https://djangochat.com/)
* [Python Bytes](https://pythonbytes.fm)
* [Talk Python To Me](https://talkpython.fm/)
* [Python Test](https://podcast.pythontest.com/)
* [The Real Python Podcast](https://realpython.com/podcasts/rpp/)

# 贡献 (Contributing)

我们随时欢迎你的贡献！请先查看 [贡献指南](https://github.com/vinta/awesome-python/blob/master/CONTRIBUTING.md)。

- - -

如果你对这个精选列表有任何疑问，请随时在 Twitter 上联系我 [@VintaChen](https://twitter.com/VintaChen) 或在 GitHub 上提交 issue。