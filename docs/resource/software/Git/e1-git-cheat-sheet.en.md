# Git Quick Reference Guide

## Create Directory (Local System)

| **Purpose**                                                  | **Command**                              |
| ------------------------------------------------------------ | ---------------------------------------- |
| Create a New Directory inside Home Directory                 | `cd -/directory name`                    |
| Create a New Git  Repository     Add a single file  or add all files in a Directory | `git init`                               |
| git add <file_name> or git add --all                         | `git add <file_name>` or `git add --all` |
| Clone into  a remote repository                              | `git clone <link>`                       |

## Commands to Check Status

| **Purpose**                      | **Command** |
| -------------------------------- | ----------- |
| To show files that have changed  | `git status` |
| Show difference in changed files | `git diff` |
|Show the log files|`git log`|

## Commands Dealing With Branches

| **Purpose**                             | **Command**                   |
| --------------------------------------- | ----------------------------- |
| Show the current branch that you are in | `git branch <branch name>`    |
| Create a new branch and switch to that  | `git checkout b <branchname>` |
| Switch to an existing branch            | `git checkout <branchname>`   |
| Delete and existing branch              | `git checkout d <branchname>` |

## Commands To Revert Changes

| **Purpose**                           | **Command**              |
| ------------------------------------- | ------------------------ |
| Revert a particular commit  by its ID | `git revert <commit id>` |
| Revert all commits                    | `git revert hard`        |
| Revert the last change                | `git revert ^HEAD`       |
| Fix the last commit                   | `git commit amend`       |

## Commands To Publish Your Changes

| **Purpose**                                         | **Command**                             |
| --------------------------------------------------- | --------------------------------------- |
| Commit your  local changes                          | `git commit -m "Update"`                |
| Commit your  local changes (Edit  Separate Message) | `git commit -a`                         |
| Push changes to your repo                           | `git push u origin  master/branch name` |
| For other developers                                | `git format patch origin`               |
| For any help                                        | `git --help`                            |

[Read More](https://itsfoss.com/basic-git-commands-cheat-sheet/)
