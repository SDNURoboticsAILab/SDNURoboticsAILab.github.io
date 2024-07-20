# 山东师范大学机器人与人工智能实验室官方网站

> [English Version](README.md)

## 部署

本项目目前采用 [MkDocs](https://github.com/mkdocs/mkdocs) 及 [Material主题](https://squidfunk.github.io/mkdocs-material/) 部署在 [GitHub Pages](https://sdnuroboticsailab.github.io/) 上。

如要在本地部署，需要有 `Python3` 环境，所需要的包见 [requirements.txt](requirements.txt)。

本站已实现自动部署，无需先本地构建静态页面再 `push`。

## 贡献

对于站内任何一部分，你若有想要增添/修正/删减等的内容，欢迎提出 [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)  ，在提交之前，请先自行运行

```bash
mkdocs serve
```

进行本地服务器测试，或者使用

```bash
mkdocs build
```

检查生成的静态页面。

本仓库采用 [commitlint](https://github.com/conventional-changelog/commitlint) + [husky](https://github.com/typicode/husky) 的方案自动进行 `commit message` 的审查，请确保 `commit message` 符合 [Conventional Commits](https://www.conventionalcommits.org/zh-hans/v1.0.0/) 规范。但也不必过多担心，本仓库已集成 [Commitizen](https://github.com/commitizen/cz-cli) 协助填写 `commit message` 。具体包及版本见 [package.json](package.json) ，在首次 `commit` 前请使用

```bash
npm install
```

安装所有依赖，安装成功后可使用 `git cz` 替代 `git commit` 。

若进行修改的是页面，请尽量确保文档遵守 [Markdown Rules](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md) 与 [Markdown 简体中文与西文混排要点](https://github.com/selfteaching/markdown-writing-with-mixed-cn-en)，并且不要忘记修改 [mkdocs.yml](mkdocs.yml) 的 `nav` 部分。

本站支持中英双语，除非此功能经商讨后弃置，否则请确保每个页面至少有两个 `Markdown` 文件： `page.md` 以及 `page.en.md` ，同时注意添加 `mkdocs.yml` 的 [mkdocs.yml](mkdocs.yml) 中的 `i18n` 插件中的 `nav_translations` 部分。

若提交的页面中含有图片，请使用[此图床](https://github.com/SDNURoboticsAILab/ImageBed)，推荐使用 [PicGo](https://picgo.github.io/PicGo-Doc/zh/guide/config.html#github%E5%9B%BE%E5%BA%8A) + [Typora](https://support.typora.io/Upload-Image/#picgoapp-chinese-language-only) 的方法。

## 待办事项

- 完善各个页面
