# 贡献指南

非常感谢你对本项目的兴趣！为了更好地协作，请按照以下指南进行贡献。

## 提交贡献

对于站内任何部分的增添、修正或删减，欢迎提出 [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)。

请在拉取请求中详细描述变更内容及其原因，拉取请求的标题推荐采用类似 [Conventional Commits](https://www.conventionalcommits.org/zh-hans/v1.0.0/) 规范。

在贡献之前，你可以在 [Issues](https://github.com/SDNURoboticsAILab/SDNURoboticsAILab.github.io/issues) 中提出疑问或需要帮助的方式。

在提交拉取请求之前，请先进行以下操作以确保变更无误：

1. 启动本地服务器进行测试：

    ```bash
    mkdocs serve
    ```

2. 或者，检查生成的静态页面：

    ```bash
    mkdocs build
    ```

拉取请求提交之后会自动检查你的内容能否正常构建，若未通过检查请先自行排查问题并解决。

## 提交信息

本仓库采用 [commitlint](https://github.com/conventional-changelog/commitlint) + [husky](https://github.com/typicode/husky) 方案自动审查 `commit message`，请确保 `commit message` 符合 [Conventional Commits](https://www.conventionalcommits.org/zh-hans/v1.0.0/) 规范。

为了简化提交信息的编写，仓库已集成 [Commitizen](https://github.com/commitizen/cz-cli) 和 [cz-git](https://github.com/Zhengqbbb/cz-git)。

具体包及版本见 [package.json](../package.json)。在首次 `commit` 前，请使用以下命令安装所有依赖：

```bash
npm install
```

安装成功后，可以使用 `git cz` 替代 `git commit`。

## 页面要求

若需修改页面，请确保文档遵守 [Markdown Rules](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md) 和 [Markdown 简体中文与西文混排要点](https://github.com/selfteaching/markdown-writing-with-mixed-cn-en)。

文档的命名方式请使用 [短横线命名法](https://en.wikipedia.org/wiki/Letter_case#Kebab_case) 或 [下划线命名法](https://en.wikipedia.org/wiki/Letter_case#Snake_case)。

此外，请同步更新 [mkdocs.yml](../mkdocs.yml) 的 `nav` 部分。

本站支持中英双语，请确保每个页面至少有两个 `Markdown` 文件：`page.md` 和 `page.en.md`，并在 [mkdocs.yml](../mkdocs.yml) 的 `i18n` 插件中的 `nav_translations` 部分添加相应的翻译。

## 图片

若提交的页面中包含图片，目前请使用以下方案：

1. 使用 [此图床](https://github.com/SDNURoboticsAILab/ImageBed)。
2. 推荐使用 [PicGo](https://picgo.github.io/PicGo-Doc/zh/guide/config.html#github%E5%9B%BE%E5%BA%8A) 和 [Typora](https://support.typora.io/Upload-Image/#picgoapp-chinese-language-only) 进行图片上传。

PicGo 的设置如下图所示：

![PicGo 设置](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/image-20240723141037880.png)

自定义域名设置为 <https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master>。

`token` 请联系仓库维护者获取。
