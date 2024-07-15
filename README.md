# Official website of Robotics and AI Lab, SDNU

> [Simplified Chinese Version](README-zh.md)

## Deployment

This project is currently deployed on [GitHub Pages](https://sdnuroboticsailab.github.io/) using [MkDocs](https://github.com/mkdocs/mkdocs) and the [Material Theme](https://squidfunk.github.io/mkdocs-material/).

To deploy locally, you need a `Python3` environment, and the required packages can be found in `requirements.txt`.

The site has automatic deployment in place, so there is no need to build static pages locally before pushing.

## Contribution

If you have any content you want to add, correct, or delete on this site, you are welcome to submit a [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).

If you are modifying a page, please ensure that the document complies with [Markdown Rules](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md) and [Markdown Writing with Mixed Chinese and English](https://github.com/selfteaching/markdown-writing-with-mixed-cn-en). Also, don't forget to update the `nav` section of `mkdocs.yml`.

This site supports both Chinese and English. Unless this feature is abandoned after discussion, please ensure that each page has at least two `Markdown` files: `page.md` and `page.en.md`, and remember to add them to the `nav_translations` section of the `i18n` plugin in `mkdocs.yml`.

If the pages you submit contain images, please use [this image bed](https://github.com/SDNURoboticsAILab/ImageBed). It is recommended to use the [PicGo](https://picgo.github.io/PicGo-Doc/zh/guide/config.html#github%E5%9B%BE%E5%BA%8A) + [Typora](https://support.typora.io/Upload-Image/#picgoapp-chinese-language-only) method.

## To-Do List

- Improve each page
- Add `logo` and `favicon`
