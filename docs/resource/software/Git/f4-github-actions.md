---
comments: true
---

GitHub Actions 是 GitHub 在 2018 年 10 月推出的持续集成服务，它的主要作用是让软件开发工作流程实现自动化。

持续集成包含了众多操作，像抓取代码、运行测试、登录远程服务器以及发布到第三方服务等，GitHub 把这些操作都叫做 actions。很多操作在不同项目中是相似的，具有可共享性。GitHub 为此想出了一个很棒的办法，允许开发者将每个操作写成独立的脚本文件并存放到代码仓库，这样其他开发者就可以直接引用。也就是说，如果需要某个 action，无需自己编写复杂的脚本，直接引用他人写好的就行，整个持续集成过程就变成了 actions 的组合，这是 GitHub Actions 最独特的地方。

采用CI/CD可以通过自动化流程和工具自动帮你构建应用、测试应用、部署应用，将你的应用交给流程工具来管理，做到自动触发、验证、部署等功能，从而减省人工成本、提高交付速度，在敏捷开发、DevOps中扮演着重要的角色。

GitHub Action正是这样一个实现持续集成交付的自动化流程工具，是由GitHub提供的一个组件。你可以通过YAML文件的配置定义工作流程以构建执行CI/CD流水线，并可以触发不同事件时（如代码提交push、Pull Request、schedule）自动执行这些工作流程。

## 作用

- **自动化 CI/CD**

  - 代码提交后，自动运行测试、构建项目。

  - 部署应用到服务器或云服务（如 腾讯云服务器、Vercel、GitHub Pages）。

- **代码质量保证**

  - 运行代码格式检查（Lint）、单元测试、代码覆盖率统计等。

  - 触发安全扫描、依赖漏洞检查（如 Dependabot）。

- **版本发布 & 任务自动化**

  - 自动发布新版本，创建 GitHub Releases，并打 Tag。

  - 自动合并 Pull Request 或分配 Reviewers。

## 核心概念

GitHub Actions 的配置文件叫做 workflow 文件，存放在代码仓库的.github/workflows目录。

workflow 文件采用 YAML 格式，文件名可以任意取，但是后缀名统一为.yml，比如foo.yml。一个库可以有多个 workflow 文件。GitHub 只要发现.github/workflows目录里面有.yml文件，就会自动运行该文件。

workflow 文件的配置字段非常多，详见官方文档。下面是一些基本字段。

### 触发器（Triggers）

GitHub Actions 的工作流程可以通过多种触发器启动。除了常见的 on: push，还有 on: pull_request、on: schedule（定时触发）等。触发器的选择取决于你想要的 CI/CD 触发条件。

```yaml
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  schedule:
    - cron: '0 0 * * *'
```

### 环境（Environments）

GitHub Actions 允许你为特定的任务或步骤定义环境。这可以是不同的操作系统（如 Windows、Linux、macOS），也可以是自定义的虚拟环境。这对于需要在不同环境中运行的项目非常有用。

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
  deploy:
    runs-on: windows-latest
```

### 矩阵构建（Matrix Builds）

矩阵构建允许在不同参数下并行运行同一个工作流。这对于在多个版本、操作系统或配置下测试和构建应用程序非常有用，可以加速整个流程。

```yaml
strategy:
  matrix:
    node-version: [10, 12, 14]
```

### 缓存（Caching）

GitHub Actions 允许你缓存依赖项，以减少构建和测试的时间。通过缓存，你可以在不重复下载或构建相同依赖项的情况下提高工作流的效率。

```bash
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v2
    - name: Set up Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '14'
    - name: Cache dependencies
      uses: actions/cache@v2
      with:
        path: ~/.npm
        key: ${{ runner.os }}-node-${{ hashFiles('**/*.lock') }}
        restore-keys: |
          ${{ runner.os }}-node-
    - name: Install dependencies
      run: npm install
```

### 自定义操作（Custom Actions）

除了使用 GitHub Actions 提供的内置操作外，你还可以创建自己的自定义操作。这些操作可以在不同的工作流程中重复使用，使得你的配置更加模块化和可维护。

### 部署（Deployment）

GitHub Actions 可以与部署目标（如服务器、云服务、容器等）集成，实现自动化部署。使用预定义的 deploy 操作或者自定义脚本，你可以将应用程序快速部署到目标环境。

### Secrets

Secrets 允许你安全地存储和使用敏感信息，如 API 密钥、访问令牌等。这些 Secrets 可以在工作流程中被引用，但不会被显示在日志中。

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - name: Deploy to production
      uses: my-custom-deployment-action
      with:
        api-key: ${{ secrets.DEPLOY_API_KEY }}
```

## 语法

### （1）`name`

`name`字段是 workflow 的名称。如果省略该字段，默认为当前 workflow 的文件名。

```bash
name: GitHub Actions Demo
```

### （2）`on`

`on`字段指定触发 workflow 的条件，通常是某些事件。

```bash
on: push
```

上面代码指定，`push`事件触发 workflow。

`on`字段也可以是事件的数组。

```bash
on: [push, pull_request]
```

上面代码指定，`push`事件或`pull_request`事件都可以触发 workflow。

完整的事件列表，请查看[官方文档](https://help.github.com/en/articles/events-that-trigger-workflows)。除了代码库事件，GitHub Actions 也支持外部事件触发，或者定时运行。

### （3）`on.<push|pull_request>.<tags|branches>`

指定触发事件时，可以限定分支或标签。

```bash
on:
  push:
    branches:    
      - master
```

上面代码指定，只有`master`分支发生`push`事件时，才会触发 workflow。

### （4）`jobs.<job_id>.name`

workflow 文件的主体是`jobs`字段，表示要执行的一项或多项任务。

`jobs`字段里面，需要写出每一项任务的`job_id`，具体名称自定义。`job_id`里面的`name`字段是任务的说明。

```javascript
jobs:
  my_first_job:
    name: My first job
  my_second_job:
    name: My second job
```

上面代码的`jobs`字段包含两项任务，`job_id`分别是`my_first_job`和`my_second_job`。

### （5）`jobs.<job_id>.needs`

`needs`字段指定当前任务的依赖关系，即运行顺序。

```javascript
jobs:
  job1:
  job2:
    needs: job1
  job3:
    needs: [job1, job2]
```

上面代码中，`job1`必须先于`job2`完成，而`job3`等待`job1`和`job2`的完成才能运行。因此，这个 workflow 的运行顺序依次为：`job1`、`job2`、`job3`。

### （6）`jobs.<job_id>.runs-on`

`runs-on`字段指定运行所需要的虚拟机环境。它是必填字段。目前可用的虚拟机如下。

- `ubuntu-latest`，`ubuntu-18.04`或`ubuntu-16.04`
- `windows-latest`，`windows-2019`或`windows-2016`
- `macOS-latest`或`macOS-10.14`

下面代码指定虚拟机环境为`ubuntu-18.04`。

```javascript
runs-on: ubuntu-18.04
```

### （7）`jobs.<job_id>.steps`

`steps`字段指定每个 Job 的运行步骤，可以包含一个或多个步骤。每个步骤都可以指定以下三个字段。

- `jobs.<job_id>.steps.name`：步骤名称。
- `jobs.<job_id>.steps.run`：该步骤运行的命令或者 action。
- `jobs.<job_id>.steps.env`：该步骤所需的环境变量。

下面是一个完整的 workflow 文件的范例。

```javascript
name: Greeting from Mona
on: push

jobs:
  my-job:
    name: My Job
    runs-on: ubuntu-latest
    steps:
    - name: Print a greeting
      env:
        MY_VAR: Hi there! My name is
        FIRST_NAME: Mona
        MIDDLE_NAME: The
        LAST_NAME: Octocat
      run: |
        echo $MY_VAR $FIRST_NAME $MIDDLE_NAME $LAST_NAME.
```

上面代码中，`steps`字段只包括一个步骤。该步骤先注入四个环境变量，然后执行一条 Bash 命令。

## 实战

### Python 代码设计的自动格式检查

1.**触发时机**：当代码推送到 main 分支或向 main 分支发起 PR 时触发

2.**工具选择**：

- 使用 black 进行代码格式化

- 使用 isort 规范导入语句排序

- 均采用非交互模式 (--quiet) 运行

3.**验证逻辑**：

- 自动应用格式化修改

- 通过 git diff 检查是否有代码变动

- 如果发现未提交的格式修改，终止流程并给出修复提示

4.**版本控制建议**：

- 推荐在 pip install 时锁定格式化工具版本

- 可通过项目根目录添加 pyproject.toml 文件自定义格式化规则

```yaml
name: Check Python Code Format

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  check-format:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'  # 可指定具体版本如 '3.10'

      - name: Install formatters
        run: |
          python -m pip install black isort
          # 若要锁定版本，可使用：
          # python -m pip install black==23.3.0 isort==5.12.0

      - name: Run format check
        run: |
          # 尝试自动格式化代码
          black . --quiet
          isort . --quiet
        
          # 检查是否有未提交的格式修改
          git diff --exit-code
          if [ $? -ne 0 ]; then
              echo "::error::Code formatting issues found. Please run:"
              echo "black . && isort ."
              echo "Then commit the changes."
              exit 1
          fi

```

> https://cloud.tencent.com/developer/article/2493914
>
> https://blog.csdn.net/daddykei/article/details/135456076
>
> https://www.ruanyifeng.com/blog/2019/09/getting-started-with-github-actions.html
>
> https://www.cnblogs.com/qmcx/p/18236736
