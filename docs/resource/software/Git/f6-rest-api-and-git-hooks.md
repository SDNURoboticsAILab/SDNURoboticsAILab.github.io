---
comments: true
---

## REST API

**REST API** 是可以使用 GitHub 的 API 生成脚本和应用程序，这些脚本和应用程序可自动执行进程、与 GitHub 集成并扩展 GitHub。 例如，可使用 API 对问题进行会审、生成分析仪表板或者管理发布。
各个 REST API 端点单独记录，端点按其主要影响的资源分类。 

### 在命令行中使用 GitHub CLI

GitHub CLI 是从命令行使用 GitHub REST API 的最简单方式。

1.在 macOS、Windows 或 Linux 上安装 GitHub CLI。 有关安装说明的详细信息，请参阅 GitHub CLI 存储库中的[安装](https://github.com/cli/cli)。

2.若要向 GitHub 进行身份验证，请从终端运行以下命令。

```bash
gh auth login 
```

3.选择要进行身份验证的位置：

- 如果通过 GitHub.com 访问 GitHub，请选择“GitHub.com”****。

- 如果通过其他域访问 GitHub，请选择“其他”，然后输入主机名（例如 octocorp.ghe.com）****。

4.按照屏幕上的其余提示操作。

选择 HTTPS 作为 Git 操作的首选协议时，GitHub CLI 将自动存储 Git 凭据，并对询问是否要使用 GitHub 凭据向 Git 进行身份验证的提示回答“是”。 此操作非常有用，因为这允许直接使用 git push、git pull 等 Git 命令，无需设置单独的凭据管理器或使用 SSH。

5.使用 GitHub CLI 发出请求，后接路径。 使用 --method 或 -X 标志指定方法。

```bash
gh api /octocat --method GET
```

### 在 GitHub Actions 中使用 GitHub CLI

要使用 gh auth login 命令，而是将访问令牌作为名为 GH_TOKEN 的环境变量进行传递。 GitHub 建议使用内置 GITHUB_TOKEN，而不是创建令牌。 如果无法执行此操作，请将令牌存储为机密，并将以下示例中的 GITHUB_TOKEN 替换为机密的名称。
以下示例工作流使用列出仓库议题终结点，并请求octocat/Spoon-Knife 仓库中的议题列表。

```yaml
on:
  workflow_dispatch:
jobs:
  use_API:
    runs-on: ubuntu-latest
    permissions:
      issues: read
    steps:
      - env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          gh API https://API.github.com/repos/octocat/Spoon-Knife/issues
```

### 使用 GitHub App 进行身份验证

如果使用 GitHub App 进行身份验证，则可以在工作流中创建安装访问令牌：
将 GitHub App 的 ID 存储为配置变量。 在下面的示例中，将 APP_ID 替换为配置变量的名称。 可以在应用的设置页面上或通过 API 找到应用 ID。 

为应用生成私钥。 将所生成文件的内容作为机密进行存储。 （存储文件的全部内容，包括 -----BEGIN RSA PRIVATE KEY----- 和 -----END RSA PRIVATE KEY-----。）在以下示例中，将 APP_PEM 替换为机密的名称。

添加用于生成令牌的步骤，并使用该令牌而不是 GITHUB_TOKEN。 请注意，此令牌会在60分钟后过期。

```yaml
on:
  workflow_dispatch:
jobs:
  track_pr:
    runs-on: ubuntu-latest
    steps:
      - name: Generate token
        ID: generate-token
        uses: actions/create-github-app-token@v1
        with:
          app-ID: ${{ vars.APP_ID }}
          private-key: ${{ secrets.APP_PEM }}
      - name: Use API
        env:
          GH_TOKEN: ${{ steps.generate-token.outputs.token }}
        run: |
          gh API https://API.github.com/repos/octocat/Spoon-Knife/issues

```

## Git Hooks

Git Hooks是一些脚本，它们在特定的Git动作发生时被触发，比如提交（commit）、推送（push）或者合并请求（merge request）。这些hooks可以用于自动化测试、代码风格检查、文档生成等任务。

### 设置

Git Hooks位于Git仓库的.git/hooks目录下。这些hooks以.sample为后缀的文件存在，你需要复制并重命名这些文件，去掉.sample后缀，并在其中编写你的脚本。

### 常用的 Git Hooks

#### pre-commit

pre-commit hook在执行git commit命令之前触发，常用于检查代码风格、运行测试或者格式化代码。

```python
#!/bin/sh
# pre-commit hook example: run linters and tests
 
# 检查代码风格
flake8 your_project
 
# 运行测试
pytest
```

#### pre-push

pre-push hook在执行git push命令之前触发，可以用来防止将未测试或不符合代码规范的代码推送到远程仓库。

```py
#!/bin/sh
# pre-push hook example: prevent pushing broken code
 
# 运行测试
if ! pytest; then
  echo "Tests failed, aborting push."
  exit 1
fi
```

#### post-merge

post-merge hook在合并操作后触发，可以用来自动安装依赖或者更新文档。

```python
#!/bin/sh
# post-merge hook example: install dependencies
 
# 安装依赖
pip install -r requirements.txt
```

### 最佳实践

- **保持脚本简单**：Hooks脚本应该简单明了，专注于单一任务。

- **提供有用的反馈**：如果脚本失败，提供清晰的错误信息，帮助开发者快速定位问题。

- **避免长时间运行的任务**：Hooks应该快速执行，避免阻塞Git操作。

- **跨平台兼容性**：确保你的脚本在不同操作系统上都能运行。
