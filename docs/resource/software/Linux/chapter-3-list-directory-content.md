---
comments: true
---

# 终端基础：列出目录内容

在本章终端基础知识系列中，你将学习如何显示目录内容、对目录内容进行排序以及检查文件统计信息。

Linux 中的 `ls` 命令用于列出目录内容。 你可以把 `ls` 想象成 `list` 的简写。

![](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter3-ls-command-sample-output.png)

除了列出目录内容外，还有更多信息。 你可以查看文件大小、创建时间、是文件还是目录以及文件权限。 你甚至可以根据这些条件对输出进行排序。

我就不多说了。 在这个阶段，你应该只知道足够多的基本知识。

## 准备测试设置

本终端基础系列教程采用动手实践的方式，通过实践来学习知识。 最好在系统上创建一个工作场景，这样你就可以尝试一些事情并看到类似的结果，如本教程所示。

打开终端并切换到主目录，在 `practice` 目录下创建一个 `ls-command` 目录，然后进入这个新建的目录。

```
cd ~
mkdir -p practice/ls-command
cd practice/ls-command
```

**It's okay if you don't recognize some commands here. Just enter them as it is shown.**

Create a couple of empty files:

```
touch empty_file_{1,2}
```

Copy a huge text file:

```
cp /etc/services .
```

Create a few directories:

```
mkdir dir_{1..3}
```

Create a hidden file:

```
echo "Now You See Me" > .john-cena
```

And let's end the setup with a soft link (like a shortcut to a file):

```
ln -s services link_services
```

Let's see how the ls-command directory looks now:

```
abhishek@itsfoss:~/practice/ls-command$ ls
dir_1  dir_2  dir_3  empty_file_1  empty_file_2  link_services  services
```

## Long list: Listing with details

While the ls command shows the content, it doesn't give any details about the contents.

This is where you can use the long listing option `-l`.

```
ls -l
```

It will show the directory's contents in individual rows with additional information in alphabetical order:

![](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter3-ls-command-long-listing.png)

!!! note "📋"

    Most Linux distros have preconfigured to show files, directories and links in different colors. The executable files are also shown in a different color.

You'll see the following information in the long listing:

- **File type**: - for file, d for directory, l for soft links.
- **Number of hard links**: Usually 1 unless there is actually a hard link (don't worry too much about it).
- **Owner name**: The user who owns the file.
- **Group name:** The group that has access to the file.
- **File size**: Size of the file in bytes. It is always 4K (or 4096) for the directories, irrespective of the directory size.
- **Date and time**: Usually, the file's last modified time and date.
- **Filename**: Name of the file, directory, or link .

![](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter3-file-permission-explanation.webp)
*File details at a glance*

It is a good idea to know about file permission and ownership. I highly recommend reading this tutorial.

[Linux File Permissions and Ownership Explained with Examples](https://linuxhandbook.com/linux-file-permissions/?ref=itsfoss.com)

## Displaying the hidden files

Remember that you created a 'hidden file' named .john-cena? But you don't see it in the output of the ls command.

In Linux, if a filename starts with a dot (.), the file or directory is hidden from the normal view.

To see these 'hidden files', you have to use the option `-a`:

```
ls -a
```

Actually, you can combine more than one option together in most Linux commands. Let's combine it with the long listing option:

```
ls -la
```

Now, it will show the hidden .john-cena file:

![](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter3-showing-hidden-files-with-ls-command.png)
*Including hidden files in the ls command output*

Did you notice the special directories `.`(current directory) and `..`(parent directory) are also displayed now?

You can make them go away and still show other hidden files using the option `-A` instead of `-a`. Go ahead and try it.

## Display file size

The long listing option `-l` shows the file size. However, it is not easy to understand. For example, in the examples above, the services file has size 12813 bytes.

As a normal computer user, it makes more sense to see the file size in KB, MB and GB.

The ls command has a human-readable option `-h`. Combine it with the long listing option and you can see the file size in recognizable formats.

![](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter3-show-file-size-with-ls.png)
*File size with ls command*

!!! question "💡"

    The ls command doesn't display the size of directories. For directory size, you have the `du` command.

## 📝 Test your knowledge

Most Linux commands have numerous options. It is impossible for anyone to know them all, even for the most frequently used commands like ls here.

For now, you have a decent idea about listing the contents of a directory and checking file stats. It's time to put your knowledge to some test.

Try the following:

- Create a new directory called ls_exercise and enter this directory
- Use the following command to copy a file: `cp /etc/passwd .`
- Check the content of a directory. What's the filename?
- What is the size of this file?
- Copy some more files using this command: `cp /etc/aliases /etc/os-release /etc/legal .`
- Sort the files in the reverse order of modified time.
- What do you observe if you run the following command: `ls -lS`?

In the next chapter of the Terminal Basics series, you'll learn about creating files in Linux command line.

Do let me know if you have questions or suggestions.

>via: https://itsfoss.com/list-directory-content/
>
>Author: [Abhishek Prakash](https://itsfoss.com/author/abhishek/)
