---
comments: true
---

# Chapter 7: Copy Files and Directories in Linux

Learn how to copy files and directories in Linux using the command line in this part of the Terminal Basics series.

Copying files is one of the most basic yet crucial tasks you will be doing regularly.

Linux has a dedicated cp command for copying both files and directories (folders).

In this part of the Terminal Basics series, you'll learn to copy files and folders in the terminal.

!!! info "📋"

```- Change directories
Just to recall, here's what you have learned so far in this Terminal Basics series:
    - [Change directories](https://itsfoss.com/change-directories/)
    - [Make new directories](https://itsfoss.com/make-directories/)
    - [List directory contents](https://itsfoss.com/list-directory-content/)
    - [Create files](https://itsfoss.com/create-files/)
    - [Reading files](https://itsfoss.com/view-file-contents/)
    - [Removing files and directories](https://itsfoss.com/delete-files-folders-linux/)
```

Let's go on with the seventh chapter in the series.

## Copying files in Linux command line

Let me show you a few examples of copying files.

### Copy a file to another directory

To copy one file to another directory, all you have to do is follow the given command syntax:

```Bash
cp Source_file Destination_directory
```

For example, here, I have copied a file named `Hello.txt` to the directory named `Tux`:

[![copy file to another directory in linux command line](https://itsfoss.com/content/images/2023/02/copy-file-to-another-directory-in-linux-command-line.png)](https://itsfoss.com/content/images/2023/02/copy-file-to-another-directory-in-linux-command-line.png)

And as you can see, the file has successfully been copied to the Tux directory.

### Copy the file but rename it

You can choose to rename the file while copying it. Just give a different name to the 'target file'.

```Bash
cp Source_file Renamed_file
```

For reference, here, I have copied a file named `Hello.txt` to the same directory by renaming it to `Renamed_Hello.txt`:

[![rename a file while copying in a same directory in linux terminal](https://itsfoss.com/content/images/2023/02/rename-a-file-while-copying-in-a-same-directory-in-linux-terminal.png)](https://itsfoss.com/content/images/2023/02/rename-a-file-while-copying-in-a-same-directory-in-linux-terminal.png)

Why would you do that? Say, you have to edit a config file. A good practice is to make a backup of the config file in the same location before editing it. This way, you can revert to the old configuration if things don't go as planned.

### Copy multiple files to another location

To copy multiple files to another directory, execute the command in the following fashion:

```Bash
cp File1 File2 File3 FileN Target_directory
```

Here, I copy multiple files to a new location.

[![copy multiple files using the cp command in linux](https://itsfoss.com/content/images/2023/02/copy-multiple-files-using-the-cp-command-in-linux.png)](https://itsfoss.com/content/images/2023/02/copy-multiple-files-using-the-cp-command-in-linux.png)

!!! note "📋"

    When you are copying multiple files, renaming them would not be possible with just the cp command.

### Deal with duplicate files while copying

By default, the cp command will override the file if a file with the same name exists in the target directory.

To avoid overriding, you can use the `-n` option with the cp command, and it won't override the existing files:

```Bash
cp -n Source_File Destination_directory
```

For example, here, I have tried to copy two files that were already there in my targeted directory and used `-v` option to showcase what is being done by the command:

```Bash
cp -n -v itsFOSS.txt LHB.txt LU.txt ~/Tux
```

[![how not to override files while copying in linux using the cp command](https://itsfoss.com/content/images/2023/02/how-not-to-override-files-while-copying-in-linux-using-the-cp-command.png)](https://itsfoss.com/content/images/2023/02/how-not-to-override-files-while-copying-in-linux-using-the-cp-command.png)

### Interactively copy files

But what about when you want to override some files, whereas some should be kept intact?

Well, you can use the cp command in the interactive mode using the `-i` option, and it will ask you each time whether the file should be overridden or not:

```Bash
cp -i Source_file Destination_directory
```

[![how to use cp command in interactive mode](https://itsfoss.com/content/images/2023/02/how-to-use-cp-command-in-interactive-mode.png)](https://itsfoss.com/content/images/2023/02/how-to-use-cp-command-in-interactive-mode.png)

!!! note "🖥️"

    Practice all the above-discussed examples yourself. You already know about creating files and folders so recreate everything.

## Copy directories in Linux command line

There is mkdir command to make new directories, rmdir to remove (empty) directories. But there is no cpdir command for copying directories.

You'll have to use the same cp command but with the recursive option `-r` to copy a directory with all its content to another location:

```Bash
cp -r Source_dir Target_dir
```

For example, here, I have copied a directory named `IF` to `LHB`:

[![how to copy a directory in linux command line](https://itsfoss.com/content/images/2023/02/how-to-copy-a-directory-in-linux-command-line.png)](https://itsfoss.com/content/images/2023/02/how-to-copy-a-directory-in-linux-command-line.png)

But it copied the entire directory 🤨

So, what do you do when you only want to copy the directory's contents, not the directory itself?

Here's what you can do:

### Copy only the contents of a directory (not the directory)

To copy only the contents of the directory, not the directory itself, you append `/.` at the end of the source directory's name:

```Bash
cp -r Source_directory/. Destination_directory
```

Here, I want to copy the contents of a directory named `IF` which contains the following three files:

[![check the file contents of directory using the tree command](https://itsfoss.com/content/images/2023/02/check-the-file-contents-of-directory-using-the-tree-command.png)](https://itsfoss.com/content/images/2023/02/check-the-file-contents-of-directory-using-the-tree-command.png)

And I will execute the following command to copy the file contents of the `IF` directory to `LHB`:

```Bash
cp -r IF/. LHB
```

[![copy the file contents of directory not a directory itself in linux command line](https://itsfoss.com/content/images/2023/02/copy-the-file-contents-of-directory-not-a-directory-itself-in-linux-command-line.png)](https://itsfoss.com/content/images/2023/02/copy-the-file-contents-of-directory-not-a-directory-itself-in-linux-command-line.png)

You can also use Source_directory/* here.

### Copy multiple directories

To copy multiple directories, you will have to execute the command in the following way:

```Bash
cp -r Dir1 Dir2 Dir3 DirN Destiniation_directory
```

For example, here, I have copied two directories named `IF` and `LU` to the `LHB`:

```Bash
cp -r IF LU ~/LHB
```

[![copy multiple directories using the cp command in linux command line](https://itsfoss.com/content/images/2023/02/copy-multiple-directories-using-the-cp-command-in-linux-command-line.png)](https://itsfoss.com/content/images/2023/02/copy-multiple-directories-using-the-cp-command-in-linux-command-line.png)

You can do the same when you want to copy files from multiple directories but not the directory itself:

```Bash
cp -r Dir1/. Dir2/. Dir3/. DirN/. Destination_directory
```

[![copy files from multiple directories but not directories their self using the cp command](https://itsfoss.com/content/images/2023/02/copy-files-from-multiple-directories-but-not-directories-their-self-using-the-cp-command.png)](https://itsfoss.com/content/images/2023/02/copy-files-from-multiple-directories-but-not-directories-their-self-using-the-cp-command.png)

!!! note "🖥️"

    You can also rename the directories the same way you renamed files.

## 📝 Test your knowledge

Now, let's see how much you remember the lessons learned so far.

- Create a directory called copy_practice
- Copy the file /etc/services to this newly created folder
- Create a folder named secrets under this directory and copy files /etc/passwd and /etc/services in it
- Copy the services file in copy_practice to the secrets folder but don't overwrite it
- Copy the secrets folder to your home directory
- Delete the secrets and copy_practice directories

That would give you some practice.

It's going well so far. You have learned quite a few things. In the next chapter, you'll see about [moving files and folders with mv command](https://itsfoss.com/move-files-linux/).

>via: https://itsfoss.com/copy-files-directory-linux/
>
>Author: [Abhishek Prakash](https://itsfoss.com/author/abhishek/)
