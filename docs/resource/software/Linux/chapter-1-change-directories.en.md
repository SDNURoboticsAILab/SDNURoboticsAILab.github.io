---
comments: true
---

# Chapter 1: Changing Directories in Linux Terminal

Learn how to change directories in the Linux command line using absolute and relative paths in this part of the Terminal Basics series.

The [cd command in Linux](https://itsfoss.com/cd-command/) allows you to change directories (folders). You just have to give the path to the directory.

```Bash
cd path_to_directory
```

And here comes the first challenge if you are new to Linux. You are probably not sure about the path.

Let's tackle that first.

## Understanding paths in Linux

The path traces the location in the Linux directory structure. Everything starts at the root and then goes from there.

You can check your current location with the following:

```Bash
pwd
```

It should show an output like /home/username. Of course, it will be your username.

As you can see, paths are composed of / and directory names. Path `/home/abhishek/scripts` means the folder scripts is inside the folder `abhishek`, which is inside the folder `home`. The first `/` is for root (from where the filesystem starts), the trailing / are separators for the directories.

![Path in Linux](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter1path-linux.webp )

!!! note "🖥️"

    Type `ls /` in the terminal and press enter. It will show you the content of the root directory. Try it.

Now, there are two ways to specify a path: absolute and relative.

**Absolute path**: It starts with the root and then traces the location from there. If a path starts with /, it is an absolute path.

**Relative path**: This path originates from your current location in the filesystem. If I am in the location `/home/abhishek` and I have to go to `/home/abhishek/Documents`, I can simply go to `Documents` instead of specifying the absolute path `/home/abhishek/Documents`.

Before I show you the difference between the two, you should get familiar with two special directory notations:

- . (single dot) denotes the current directory.
- .. (two dots) denote the parent directory taking you one directory above the current one.

Here's a pictorial representation.

![Absolute path vs relative path](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter1relative-path-cd.png )

Want more on paths in Linux? This article will help you.

[Absolute vs Relative Path in Linux: What’s the Difference?](https://linuxhandbook.com/absolute-vs-relative-path/?)

## Changing directory with cd command

Now that you are familiar with the concept of path, let's see how you can change the directory.

!!! note "🖥️"

    If you just type cd and press enter, it will take you to your home directory from any location. Go on, try it.

Enter the following command to see the directories inside your home directories:

```Bash
ls
```

This is what it shows to me:

```Bash
abhishek@ituxedo:~$ ls
Desktop    Downloads  Pictures  Templates  VirtualBoxVMs
Documents  Music      Public    Videos
```

Yours may be similar but not exactly the same.

Let's say you want to go to the Documents directory. Since it is available under the current directory, it will be easier to use the relative path here:

```Bash
cd Documents
```

!!! question "💡"

    The default terminal emulators of most Linux distributions show you the current location in the prompt itself. You don't have to use pwd all the time just to know where you are.

![Most Linux terminal prompts show the current location](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter1linux-terminal-prompt.png )

*Most Linux terminal prompts show the current location*

Now, let's say you want to switch to the Templates directory that was located in your home directory.

You can use the relative path `../Templates` (.. takes you to the one directory above Documents to /home/username and from there you go to Templates).

But let's go for the absolute path instead. Please change 'abhishek' with your username.

```Bash
cd /home/abhishek/Templates
```

Now you are in the Templates directory. How about going to the Downloads directory? Use the relative path this time:

```Bash
cd ../Downloads
```

Here's a replay of all the above directory change examples you just read.

![cd command example](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter1cd-command-example.svg )

*Watch a replay of the above cd command examples*

!!! question "💡"

    Utilize the tab completion in the terminal. Start typing a few letters of the command and directory and hit the tab key. It will try to autocomplete or show you the possible options. 

## Troubleshooting

You may encounter a few common errors while changing the directories in Linux terminal.

### No such file or directory

If you see an error like this while changing the directories:

> bash: cd: directory_name: No such file or directory

Then you made mistake with the path or name of the directories. Here are a few things to note.

- Make sure there is no typo in the directory name.
- Linux is case sensitive. Downloads and downloads are not the same.
- You are not specifying the correct path. Perhaps you are in some other location? Or did you miss the first / in the absolute path?

![Common examples of "no such file or directory" error](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter1common-errors-with-cd.png )

*Common examples of "no such file or directory" error*

### Not a directory

If you see an error like this:

> bash: cd: filename: Not a directory

It means that you are trying to use the cd command with a file, not a directory (folder). Clearly, you cannot enter a file the same way you enter a folder and hence this error.

![Not a directory error with the cd command](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter1not-a-directory-error-linux.png )

*Not a directory error with the cd command*

### Too many arguments

Another common rookie Linux mistake:

> bash: cd: too many arguments

The cd commands take only one argument. That means that you can only specify one directory to the command.

If you specify more than one or mistyped a path by adding a space to the path, you'll see this error.

![Too many arguments error in Linux terminal](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter1too-many-arguments.png )

*cd commands accepts only one argument*

!!! question "🏋🏻"

    If you press cd -, it will take you to your previous directory. It's quite handy when you are switching between two distant locations. You don't have to type the long paths again.

## Special directory notations

Before ending this tutorial, let me quickly tell you about the special notation `~`. In Linux, ~ is a shortcut for the user's home directory.

If user `abhi` is running it, ~ would mean `/home/abhi` and if user `prakash` was running it, it would mean `/home/prakash`.

To summarize all the special directory notations you learned in this chapter of the terminal basics series:

| **Notation** | **Description**    |
| ------------ | ------------------ |
| .            | Current directory  |
| ..           | Parent directory   |
| ~            | Home directory     |
| \-           | Previous directory |

## 📝 Test your knowledge

Here are a few simple exercises to test your newly learned knowledge of the path and the cd command.

Move to your home directory and create a nested directory structure with this command:

```Bash
mkdir -p sample/dir1/dir2/dir3
```

Now, try this one by one:

- Go to the dir3 using either absolute or relative path
- Move to dir1 using relative path
- Now go to dir2 using the shortest path you can imagine
- Change to the sample directory using absolute path
- Go back to your home directory

Now that you know how to change directories, how about you [learn about creating directories](https://itsfoss.com/make-directories/) as well? The next chapter of this series discusses that.

And, of course, your feedback on this new series is welcome. What can I do to improve it?

---

>via: [https://itsfoss.com/change-directories/](https://itsfoss.com/change-directories/)
>
>Author: [Abhishek Prakash](https://itsfoss.com/author/abhishek/)
