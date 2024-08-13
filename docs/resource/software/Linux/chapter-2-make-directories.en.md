---
comments: true
---

# Chapter 2: Making Directories in Linux Terminal

Learn to make new folders in the Linux command line in this part of the Terminal Basics tutorial series.

In the previous chapter of the Terminal Basics series, you learned about [changing folders in the Linux command line](https://itsfoss.com/change-directories/).

I gave an exercise at the end that briefly mentioned making directories.

In this part of the series, I'll discuss how to create new folders on the Linux command line using the mkdir command.

```Bash
mkdir dir_name
```

mkdir is short of make directories. Let's see about using this command.

!!! note "📋"

    In case you didn't know, folders are called directories in Linux.

## Making a new directory in Linux

You should be familiar with the [concept of absolute and relative paths in Linux](https://linuxhandbook.com/absolute-vs-relative-path/?ref=itsfoss.com) by now. If not, please refer to this tutorial.

[Absolute vs Relative Path in Linux: What’s the Difference?](https://linuxhandbook.com/absolute-vs-relative-path/?ref=itsfoss.com)

Open the terminal on your system if it is not already opened. Normally, you start with your home directory (/home/username). But for the sake of this tutorial and to recall a couple of things, I presume you are not in your home directory.

So, change to your home directory first.

```Bash
cd
```

Yes. If you simply enter cd without any options and arguments, it takes you to your home directory. You could also use `cd ~` among other methods.

Here, make a new directory called practice.

```Bash
mkdir practice
```

Can you switch to this newly created practice directory?

```Bash
cd practice
```

Great! Now you have a dedicated folder where you'll practice the Linux command line tutorials in this series.

![](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter2-make-directory-example.svg)](https://itsfoss.com/content/images/2023/02/make-directory-example.svg)*Watch a replay of the above-discussed example*

## Creating multiple new directories

You just created a new directory. What if you have to create more than one? Let's say three of them.

You may use the mkdir command three times in a row for each of them. It will work. However, it is not really needed. You can save time and effort by creating multiple directories at the same time like this:

```Bash
mkdir dir1 dir2 dir3
```

Go on and do that please. You can list the contents of the `practice` directory to see all the newly created directories. More on the ls command later.

![](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter2-create-multiple-directories-linux.png)

!!! question "💡"

    You cannot have two folders or files of the same name in the same location.

## Making multiple nested subdirectories

So, you now know about creating multiple directories at once.

But what if you have to create a nested directory structure? Let's say that you have to create a directory subdir2 inside subdir1 inside dir1.

```Bash
dir1/subdir1/subdir2
```

The problem here is that subdir1 does not exist. So if you try `mkdir dir1/subdir1/subdir32, you'll get an error:

```Bash
abhishek@itsfoss:~/practice$ mkdir dir1/subdir1/subdir2
mkdir: cannot create directory ‘dir1/subdir1/subdir2’: No such file or directory
```

If you didn't know better, you would go for `mkdir dir1/subdir1` and then run `mkdir dir1/subdir2`. That will work. However, there is a much better way.

You use the `-p` option, which makes parent directories if needed. If you run the command below:

```Bash
mkdir -p dir1/subdir1/subdir2
```

It will create subdir1 and then subdir2 inside subdir1.

!!! question "💡"

    There is no naming convention, but it is better to avoid spaces in file and directory names. Use underscore or dash instead because handling spaces in file/directory names requires special effort.

## 📝 Test your knowledge

This is rather a short tutorial because the mkdir command has only a few options.

Now, let me give you some practice exercises to utilize the `practice` directory you had created earlier.

- Without entering the `dir2` directory, create two new subdirectories in it.
- Without entering the `dir3` directory, create two-level nested subdirectories (subdir1/subdir2)
- Change to the dir2 directory. From here, create a directory named temp_stuff in your home directory. Don't worry; we will delete it later in this tutorial series.
- Go back to the parent `practice` directory and try to create a directory named `dir3`. You see an error. Can you make it go away with the `-p` option?

In the next chapter of the Terminal Basics series, you'll learn about [listing the contents of a directory](https://itsfoss.com/list-directory-content/) with the ls command.

Do let me know if you have questions or suggestions.

>via: https://itsfoss.com/make-directories/
>
>Author: [Abhishek Prakash](https://itsfoss.com/author/abhishek/)