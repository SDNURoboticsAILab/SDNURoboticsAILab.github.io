---
comments: true
---

# 第 6 章：在 Linux 中删除文件和文件夹

You have learned to create files and directories. Now it is time to learn about deleting files and folders in the command line.

In the earlier chapters of the Terminal Basics series, you learned to [create new files](https://itsfoss.com/create-files/) and directories (folders).

Let's now see how you can delete files and folders in the Linux terminal.

## Deleting files

To remove files, you can use the rm command in the following fashion:

```
rm filename_or_path
```

You won't see any output if the file is successfully deleted.

Here's an example where I removed one of the files named `new_file`. When I list the directory contents, you can see that `new_file` no longer exists.

[![Removing files in Linux terminal](https://itsfoss.com/content/images/2023/03/delete-files-linux-terminal.png)](https://itsfoss.com/content/images/2023/03/delete-files-linux-terminal.png)*Removing a single file*

You can also remove multiple files in the same command:

```
rm file1 file2 file3
```

Let me show an example of deleting two files in a single command.

[![Deleting multiple files in single rm command](https://itsfoss.com/content/images/2023/03/remove-multiple-files-linux-terminal.png)](https://itsfoss.com/content/images/2023/03/remove-multiple-files-linux-terminal.png)*Removing multiple files*

### 🏋️ Exercise file deletion

Let's practice what you just learned. Create a directory named practice_delete and switch to it:

```
mkdir practice_delete && cd practice_delete
```

Now create a few empty files:

```
touch file1 file2 file3
```

Delete the file3:

```
rm file3
```

Now, let's do something extra. Run this command and change the permission on file2:

```
chmod u-w file1 file2
```

Try deleting file2 now:

```
rm file2
```

Do you see a message '**remove write protected file**'? That's because you removed the write permission (for modification) from this file.

You can **press Y or enter key to confirm the deletion or N to deny the removal.**

If you don't want to see this message and still delete it, you can use the force delete option `-f`. Try it by deleting `file1`:

```
rm -f file1
```

Here's a replay of all the above examples to help you:

[![Deleting files in Linux terminal](https://itsfoss.com/content/images/2023/03/file-delete-example.svg)](https://itsfoss.com/content/images/2023/03/file-delete-example.svg)

!!! warning "🚧"

    There is no trash bin in the Linux command line. Once the file is deleted, you cannot undo the action to bring it back from the trash bin as you do in the graphical file manager. For this reason, be extra careful while deleting the files.

### Remove but with caution

The lack of trash bin makes the deletion a permanent jobs of sort. This is why you should be careful about what files are you deleting.

There is an interactive mode with option `-i`. With this, you'll be asked to confirm the deletion.

```
rm -i filename
```

This is helpful when you are deleting several files based on a certain pattern.

Here's an example where I am interactively deleting all the files that match file_ pattern in their name. I delete some and keep some in the interactive mode.

[![Deleting files in interactive mode](https://itsfoss.com/content/images/2023/03/interactive-delete-example.svg)](https://itsfoss.com/content/images/2023/03/interactive-delete-example.svg)

!!! question "💡"

    I advise switching to the directory where the files are located and then removing them. This helps in reducing any potential caused by a typo in file path.

## Deleting directories

There is a dedicated rmdir command to remove directories in Linux.

```
rmdir dir_name
```

However, it can only delete empty directories. If the directory has any files or subdirectories in it, the rmdir command will throw error.

```
abhishek@itsfoss:~/practice_delete$ rmdir dir2
rmdir: failed to remove 'dir2': Directory not empty
```

And that makes it less useful in most cases.

So, how do you delete a non-empty folder then? Well, you use the same rm command that you used earlier for removing files.

Yes, the same rm command but with the recursive option `-r`:

```
rm -r dir_name
```

### 🏋️ Exercise folder deletion

Let's practice what you learned.

Switch to practice_delete folder if you are not already there. Now, create two directories dir1 and dir2.

```
mkdir dir1 dir2
```

Create a file in dir2:

```
touch dir2/file
```

Now try deleting the directories using the rmdir command:

```
rmdir dir1
rmdir dir2
```

Since the dir2 is not empty, rmdir command will fail. Instead, use the rm command with recursive option:

```
rm -r dir2
```

Here's a replay of all the above command examples to help you out:

[
  ](https://itsfoss.com/content/images/2023/03/folder-delete-example.svg)

!!! question "💡"

    The interactive deletion mode is even more helpful while deleting a directory with the recursive option of the rm command: `rm-ri dir_name`

## 📝 Test your knowledge

Prepare a directory tree that looks like this:

```
.
├── dir1
│   ├── file1
│   ├── file2
│   └── file3
├── dir2
├── dir3
└── file
```

Basically, you create a file named file and three directories dir1, dir2 and dir3 in the current directory (practice_delete). And then you create files file1, file2 and file3 in dir1.

Now do the following:

- Delete `file2`.
- Switch to the `dir3` and force delete the file named `file` in the upper directory.
- Delete all the contents of dir1 but not the directory itself.
- List the contents of the `dir`.

I encourage you to discuss the practice questions in the [It's FOSS community forum](https://itsfoss.community/?ref=itsfoss.com).

This is going good. You have learned several basic things like switching directories, checking the contents of a directory, and creating and deleting files and directories.

In the next chapter, you'll learn about copying files and folders in the terminal. Stay tuned!

*via: https://itsfoss.com/delete-files-folders-linux/*
