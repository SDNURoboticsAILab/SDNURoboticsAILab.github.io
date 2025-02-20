---
comments: true
---

# Git多账号配置

![](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/202411251710938.webp)
<!-- more -->
---

想象一种情况，当你在为多个不同的组织贡献代码时，出于安全性和保密性的考虑，他们会要求你用专用邮箱创建一个单独的账号来提交代码，而一般的Git托管平台提供两种方式来访问仓库，HTTTP或SSH，HTTP访问需要自行输入密码，但Github在很早之前就已经禁用了密码访问，所以考虑到安全性大多数情况我们都会使用后者。拿最常见的Github平台来举例，你可以为你的账号配置多个密钥对，但是你本地却只能有一个密钥对，在这种情况下，如果涉及到多Git账号开发的话，就需要频繁的更换密钥对，非常的不方便，所以本文就讲述了一个较为方便的解决办法，下面进行演示。



## 配置

生成两个不同的密钥对，分别对应两个不同的Git账号

```bash
$ ssh-keygen -t rsa "jack"
$ ssh-keygen -t rsa "mike
```

它默认会生成在用户目录下的`.ssh`文件夹中，密钥对默认为`id_rsa`，`id_rsa.pub`，一个公钥一个私钥。Git在默认会去读取`.ssh`路径下的密钥对，由于我们是多账号，所以就需要去指定Git哪个账号该读哪一个密钥，这就需要我们在`.git`目录下创建`config`文件，文件位于`$HOME/.git/config`，内容如下

```
Host jack.github.com
HostName github.com
User jack
PreferredAuthentications publickey
IdentityFile ~/.ssh/jack/id_rsa
AddKeysToAgent yes

Host mike.github.com
HostName github.com
User mike
PreferredAuthentications publickey
IdentityFile ~/.ssh/mike/id_rsa
AddKeysToAgent yes
```

其中比较重要的字段的释义如下

- Host：HostName的别名，Git会根据该值来判断使用哪个密钥
- HostName：Git托管平台的域名
- User：对应平台上的用户名
- IdentityFile：凭证文件，指定密钥的存放路径

然后在Github上分别给两个账号配置好公钥

![](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/202411252012346.png)

然后就完成了，完事后测试下是否成功，Git自己会根据名称去找到需要的密钥，如果成功了你会看到下面的结果

```bash
$ ssh -T git@jack.github.com
Hi jack! You've successfully authenticated, but GitHub does not provide shell access.

$ ssh -T git@mike.github.com
Hi mike! You've successfully authenticated, but GitHub does not provide shell access.
```

同样的，如果你想添加其它托管平台比如gitlab，bitbucket也是一样的操作步骤。

## 使用

配置成功后，后续再使用Git时就要稍微变一下，比如原来的Git地址是

```bash
git@github.com:fatedier/frp.git
```

那么后续的话就需要加上自己的用户名，比如

```bash
git@jack.github.com:fatedier/frp.git
```

你可以通过Git命令来将本地仓库的Remote URL替换下，一个例子如下所示。

```bash
$ git remote set-url origin git@jack.github.com:fatedier/frp.git
```

> 转载自：[Git多账号配置 | 寒江蓑笠翁](https://246859.github.io/posts/code/git/5.multiple_account.html)
