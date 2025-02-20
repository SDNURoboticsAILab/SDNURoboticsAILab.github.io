---
comments: true
---

GitHub Pages 是 GitHub 提供的一个免费的静态网站托管服务，它允许 GitHub 用户创建和托管自己的静态网站，这些网站可以通过特定的 GitHub 仓库进行管理和托管。

![image-20250220202029952](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20250220202029952.png)

- 免费托管： GitHub Pages 提供免费的静态网站托管服务，允许用户将自己的网站内容托管在 GitHub 上，用户不需要支付额外的托管费用；
- 使用简单： 创建和管理 GitHub Pages 静态网站相对简单，特别是对于熟悉 GitHub 的用户来说，用户只需在自己的 GitHub 帐户中创建一个特定名称的仓库，将网站文件上传到该仓库即可；
- 自定义域名： 用户可以选择使用自定义域名来访问他们的 GitHub Pages 网站，这使得它们更适合个人网站、博客和项目页面；
- 支持多种静态网站生成工具： GitHub Pages 支持多种静态网站生成工具，如 Jekyll、Hugo、Gatsby 等，以及纯HTML、CSS 和 JavaScript 等前端技术，这使得用户能够根据自己的需求选择适合他们的工具；
- 自动构建： GitHub Pages 可以自动构建用户上传的网站内容，无需用户手动生成或编译网页，这使得发布网站变得更加简单。

对于开发人员和技术爱好者来说，GitHub Pages 是一个很好的选择，用于托管个人网站、博客、文档、项目页面等静态内容，它提供了一个方便的方式来分享和展示自己的作品。

## 快速搭建第一个Github Pages网站

Github Pages的站点类型有几种：

- 个人或组织站点（User or Organization sites）：对于个人或组织站点，每个GitHub用户或组织只能有一个站点，它通常使用username.github.io或organizationname.github.io的格式，这是GitHub Pages的默认站点，通常用于个人网站、博客等。

- 项目站点（Project sites）：对于项目站点，每个GitHub仓库可以有一个关联的GitHub Pages站点，这意味着对于每个项目，您可以创建一个独立的GitHub Pages站点，无需限制。

### 个人（组织）类型的网站

Step1： 新建一个项目

登录Github：https://github.com/，在顶部菜单栏点击“+”，然后“New repository”新建仓库，输入项目的相关信息，然后“Create repository”创建仓库：

![image-20250220202153633](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20250220202153633.png)

Step2： 创建一个界面文件

首先创建一个index.html，输入文件内容，点击提交：

![image-20250220202210030](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20250220202210030.png)

Step3： 访问

大概等待几十秒，访问：https://用户名.github.io/，即可部署第一个属于自己的静态网站了，可以看到部署成功了：

![image-20250220202230855](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20250220202230855.png)

### 项目类型的网站

Step1： 新建一个项目

登录Github：https://github.com/，在顶部菜单栏点击“+”，然后“New repository”新建仓库，输入项目的相关信息，然后“Create repository”创建仓库：

![image-20250220202302165](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20250220202302165.png)

Step2： 创建一个界面文件

同样是创建一个index.html文件，写入内容并提交：

![image-20250220202316239](C:\Users\excnies\AppData\Roaming\Typora\typora-user-images\image-20250220202316239.png)

Step3： 设置Github Pages

点击Settings -> Pages -> 选择部署的代码分支（如main）-> 点击 Save

![image-20250220202326693](C:\Users\excnies\AppData\Roaming\Typora\typora-user-images\image-20250220202326693.png)

Step4： 保存并访问

点击上图的保存，然后不断刷新保存之后的页面，直至出现Gtihub Pages的地址：

![image-20250220202338115](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/image-20250220202338115.png)

点击跳转之后，可以看到已经为该项目创建了静态网站了。

## 用 GitHub 的 gh-pages 分支展示自己的项目

Github创建项目仓库后随即只产生一个master分支，只需要再添加gh-pages分支就可以创建静态页面了。这利用了项目站点（即Project Pages）的方式。

如图所示，通过git-add -A、git -commit -m “...” 命令把完成的项目上传到github上以后，默认的是处于master分支。接着我们要做的是展现dist目录下的静态文件，只需要使用下面语句：

git subtree push --prefix=dist origin gh-pages

 意思就是把指定的dist文件提交到gh-pages分支上。那这时候，我们看到已经多出了一个gh-pages分支。

![image-20250220202415645](C:\Users\excnies\AppData\Roaming\Typora\typora-user-images\image-20250220202415645.png)

我们先去仓库的 Settings 页面，点击左侧的 Pages 菜单，将 Branch 的分支选择刚刚创建的 gh-pages 分支。创建完成后访问 Github用户名.github.io/创建的仓库名 即可。

![image-20250220202427975](C:\Users\excnies\AppData\Roaming\Typora\typora-user-images\image-20250220202427975.png)

## 静态网站生成工具

我们需要的页面肯定不是只有一行文本的，希望其更加的丰富，其实GitHub Pages支持多种静态网站生成工具。

以下是一些GitHub Pages支持的主要静态网站生成工具：

- Jekyll（[https://jekyllrb.com](https://jekyllrb.com/)）： Jekyll是GitHub Pages的默认静态网站生成工具，它使用Markdown文件和Liquid模板引擎来创建静态网站，Jekyll对于博客和文档站点非常流行。

- Hugo（https://gohugo.io/）： Hugo是另一个受欢迎的静态网站生成工具，它非常快速且易于使用，它使用Go语言编写，支持多种主题和内容组织方式。

- Gatsby（https://www.gatsbyjs.com/）： Gatsby是基于React的静态网站生成工具，它可以构建高性能、现代化的网站，Gatsby适用于博客、电子商务、应用程序文档等。

- VuePress（https://vuepress.vuejs.org/）： VuePress是Vue.js驱动的静态网站生成工具，专注于文档站点，它支持Markdown文件和Vue组件。
- Hexo（https://hexo.io/）： Hexo是一个快速、简单的博客框架，使用Markdown文件来生成静态博客，它是Node.js应用程序。
- Pelican（https://blog.getpelican.com/）： Pelican是使用Python编写的静态网站生成器，适用于博客和文档。
- Middleman（https://middlemanapp.com/）： Middleman是Ruby编写的静态网站生成工具，支持多种模板和数据源，适用于各种项目。
- Sphinx（https://www.sphinx-doc.org/）： Sphinx是一个Python文档生成工具，通常用于技术文档和文档站点。
- MkDocs（https://www.mkdocs.org）： MkDocs是Python编写的文档生成工具，使用Markdown文件创建文档站点。

## 实战：GitHub Pages托管Vue3+Vite项目

> 前面都没有问题的，可以直接跳到第七步

### 一、创建一个Vue3+Vite项目并运行

#### 1. 创建

```sh
npm create vue@latest
```

可以根据自己的需求进行选择

![image-20240607081809068](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/2919536-20240607103603654-92364947.png)

#### 2. 安装依赖

```sh
npm i
```

#### 3. 运行

```sh
npm run dev
```

![image-20240607082206152](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/2919536-20240607103813705-1964780820.png)

### 二、修改 `vite.config.js` 文件

在此文件中，`defineConfig` 中加入 `base` 参数，具体如下：

```js
export default defineConfig({
  base: '/vue3-vite',
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
```

此时你会发现，本地运行的项目路径变成了 `http://localhost:5173/vue3-vite/`

### 三、初始化git仓库并提交

可以使用命令

```sh
git init
```

也可以使用`vscode`的可视化操作来初始化git仓库

> 说明：使用此方式，创建的默认的分支是**main**，如果想要使用**master**作为默认分支需要修改vscode配置【设置 → 用户 → 扩展 → Git → 一直滚，直到找到如下 → 将**输入框中的main改为master**即可】
>
> ![image-20240607093113839](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/2919536-20240607104000821-2031818571.png)

![image-20240607082954956](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/2919536-20240607104047731-1271663136.png)

输入提交信息( 我这边使用的是 `git-commit-plugin` )

> 具体使用可以参考这篇文章 [结合企业实践来规范你的Git commit（含插件使用指南）-阿里云开发者社区 (aliyun.com)](https://developer.aliyun.com/article/1492295)

```none
🎉 init: 完成创建
```

然后点击 `√ 提交`，在弹出的警示框中，点击 `是`即可完成提交

### 四、创建仓库

进入 Github 主页，点击右上角的 `+`按钮

> 有人会问，你这边怎么是中文的？那自然是安装了浏览器插件GithubCN了，可以在插件市场[GithubCN - Microsoft Edge Addons](https://microsoftedge.microsoft.com/addons/detail/githubcn/onlodfoebaobhmlhgcbddjngjbkdbfaj?hl=zh-CN)自己下载

![image-20240607083934180](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/2919536-20240607104238285-231070414.png)

输入仓库名称(一般跟上面的base保存一致)和描述信息(随意)，然后点击 **创建仓库** 按钮即可

![image-20240607084634584](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/2919536-20240607104421575-181826881.png)

### 五、绑定远程仓库

> 说明一下，我这边推送上去的是master分支，你们可能是main分支，这是由于我做过默认分支修改的
>
> 如果想要把默认分支更改成master分支可以参考这篇文章的第二点 [github将默认main分支改成master - 简书 (jianshu.com)](https://www.jianshu.com/p/e8342a72c101)

可以使用他所提供的命令

```sh
git remote add origin https://github.com/qmcx-ming/vue3-vite.git
git branch -M master
git push -u origin master
```

#### 1. 复制仓库地址

![image-20240607085704928](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/2919536-20240607104505587-705878983.png)

#### 2. 添加远程存储库

这边我使用的是可视化的形式，操作如下：

![image-20240607102306534](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/2919536-20240607104625009-656523132.png)

#### 3. 粘贴地址

![image-20240607085849147](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/2919536-20240607104657274-81611939.png)

当然，你也可以 `从 GitHub 添加远程存储库`

#### 4. 输入远程存储库的名称

> 此处我命名为GitHub，是为了后续添加其他远程存储库便于区分，如：Gitee...

![image-20240607093430176](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/2919536-20240607104720893-1349249820.png)

回车即可

如果出现了什么报错，不要慌，查看一下远程仓库有没有绑定上就好了

```sh
git remote
```

出现以下，一般是ok的了

```none
GitHub
```

### 六、推送

点击 **发布 Branch** 按钮即可完成推送

![image-20240607093753016](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/2919536-20240607104758974-1857207707.png)

刷新一下GitHub页面，就OK了

### 七、GitHub Pages

#### 1. 切换构建和部署源为 GitHub Actions

![image-20240607094855112](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/2919536-20240607104845042-1127074974.png)

![image-20240607094927464](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/2919536-20240607104905435-1599729838.png)

#### 2. 输入文件的名称

![image-20240607095010723](https://img2024.cnblogs.com/blog/2919536/202406/2919536-20240607104944076-1127672415.png)

![image-20240607095126877](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/2919536-20240607105000996-906323267.png)

#### 3. 粘贴配置

> [部署静态站点 | Vite 官方中文文档 (vitejs.dev)](https://cn.vitejs.dev/guide/static-deploy.html#github-pages)
>
> ```yaml
> # 将静态内容部署到 GitHub Pages 的简易工作流程
> name: Deploy static content to Pages
> 
> on:
>   # 仅在推送到默认分支时运行。
>   push:
>     branches: ['main']
> 
>   # 这个选项可以使你手动在 Action tab 页面触发工作流
>   workflow_dispatch:
> 
> # 设置 GITHUB_TOKEN 的权限，以允许部署到 GitHub Pages。
> permissions:
>   contents: read
>   pages: write
>   id-token: write
> 
> # 允许一个并发的部署
> concurrency:
>   group: 'pages'
>   cancel-in-progress: true
> 
> jobs:
>   # 单次部署的工作描述
>   deploy:
>     environment:
>       name: github-pages
>       url: ${{ steps.deployment.outputs.page_url }}
>     runs-on: ubuntu-latest
>     steps:
>       - name: Checkout
>         uses: actions/checkout@v4
>       - name: Set up Node
>         uses: actions/setup-node@v4
>         with:
>           node-version: 20
>           cache: 'npm'
>       - name: Install dependencies
>         run: npm ci
>       - name: Build
>         run: npm run build
>       - name: Setup Pages
>         uses: actions/configure-pages@v4
>       - name: Upload artifact
>         uses: actions/upload-pages-artifact@v3
>         with:
>           # Upload dist folder
>           path: './dist'
>       - name: Deploy to GitHub Pages
>         id: deployment
>         uses: actions/deploy-pages@v4
> ```

将在线编辑器中的内容清理掉，粘贴官方文档的配置

#### 4. 提交

点击右上角的 **提交更改(Commit changes)**

在弹出的对话框中，输入**提交信息(Commit message)**

```none
✨ feat: 增加GitHub Pages配置
```

点击 **提交更改(Commit changes)**

创建需要一些时间，一般等圈圈转完了就好了，或者也可以点进入看看

![image-20240607100104338](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/2919536-20240607105113925-1288222374.png)

#### 6. 创建完成

![image-20240607100305960](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/2919536-20240607105158672-1493201757.png)

然后回到Pages

![image-20240607100536412](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/git/2919536-20240607105224242-312304395.png)

点击链接即可访问😆

不要忘了，远程仓库加了配置文件后，本地也需要做一次拉取的，同步一下

> https://www.cnblogs.com/qmcx/p/18236736
>
> https://docs.github.com/zh/pages/getting-started-with-github-pages
>
> https://www.github-zh.com/getting-started/github-pages
>
> https://www.cnblogs.com/MuYunyun/p/6082359.html
>
> https://blog.csdn.net/WHYbeHERE/article/details/140378572
>
> https://blog.csdn.net/qq_20042935/article/details/133920722
