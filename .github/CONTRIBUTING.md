# Contribution Guide

Thank you very much for your interest in this project! To collaborate better, please follow the guidelines below.

## Submitting Contributions

For any additions, corrections, or deletions within the site, feel free to submit a [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).

Please describe the changes and their reasons in detail in the pull request. It is recommended that the title of the pull request follows the [Conventional Commits](https://www.conventionalcommits.org/zh-hans/v1.0.0/) specification.

Before contributing, you can raise questions or seek help in the [Issues](https://github.com/SDNURoboticsAILab/SDNURoboticsAILab.github.io/issues) section.

Before submitting a pull request, please do the following to ensure the changes are correct:

1. Start the local server for testing:

    ```bash
    mkdocs serve
    ```

2. Or, check the generated static pages:

    ```bash
    mkdocs build
    ```

After submitting the pull request, it will automatically check if your content can be built normally. If the check fails, please troubleshoot and resolve the issue yourself.

## Commit Messages

This repository uses the [commitlint](https://github.com/conventional-changelog/commitlint) + [husky](https://github.com/typicode/husky) scheme to automatically review `commit messages`. Please ensure that `commit messages` comply with the [Conventional Commits](https://www.conventionalcommits.org/zh-hans/v1.0.0/) specification.

To simplify the writing of commit messages, the repository has integrated [Commitizen](https://github.com/commitizen/cz-cli) and [cz-git](https://github.com/Zhengqbbb/cz-git).

For specific packages and versions, see [package.json](../package.json). Before the first `commit`, please install all dependencies using the following command:

```bash
npm install
```

After successful installation, you can use `git cz` instead of `git commit`.

## Page Requirements

If you need to modify the page, please ensure that the document complies with [Markdown Rules](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md) and [Markdown Writing with Mixed Chinese and Western Text](https://github.com/selfteaching/markdown-writing-with-mixed-cn-en).

In addition, please update the `nav` section of [mkdocs.yml](../mkdocs.yml) accordingly.

This site supports both Chinese and English. Please ensure that each page has at least two `Markdown` files: `page.md` and `page.en.md`, and add the corresponding translation in the `nav_translations` section of the `i18n` plugin in [mkdocs.yml](../mkdocs.yml).

## Images

If the submitted page contains images, please use the following solutions:

1. Use [this image bed](https://github.com/SDNURoboticsAILab/ImageBed).
2. It is recommended to use [PicGo](https://picgo.github.io/PicGo-Doc/zh/guide/config.html#github%E5%9B%BE%E5%BA%8A) and [Typora](https://support.typora.io/Upload-Image/#picgoapp-chinese-language-only) for image uploads.

The PicGo settings are shown in the image below:

![PicGo Settings](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/image-20240723141037880.png)

Set the custom domain to <https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master>.
