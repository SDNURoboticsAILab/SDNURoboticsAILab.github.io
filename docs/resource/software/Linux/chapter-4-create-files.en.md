---
comments: true
---

# Chapter 4: Creating Files in Linux

In this chapter of Linux Terminal Basics series for beginners, learn about creating new files using Linux commands.

So far, in this Terminal Basics series, you have learned to:

- [Change directories](https://itsfoss.com/change-directories/)
- [Make new directories](https://itsfoss.com/make-directories/)
- [List directory contents](https://itsfoss.com/list-directory-content/)

Let's now learn about creating files in the Linux command line. I'll briefly discuss adding content to the file. However, details on editing text files will be covered later.

## Create a new empty file with touch command

Using the touch command is pretty straightforward.

```
touch filename
```

Switch to your home directory and create a new directory called `practice_files` and switch to this directory:

```
mkdir practice_files && cd practice_files
```

!!! question "💡"

    The && is a way to combine two commands. The second command only runs when the first command is executed successfully.

Now, create a new file named new_file:

```
touch new_file
```

That's it. You have just created a new empty file.

List the directory content and check the properties of the file with ls -l command.

![](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter4-touch-example.svg)
*Using touch command to create new file*

!!! question "💡"

    The touch command's original purpose is to 'touch' a file and change its timestamp. If the provided file does not exist, it creates a new file with the name.

## Create a new file using the echo command

I should have introduced you to the echo command long back. Better late than never. The echo command displays whatever you provide to it. Hence the name echo.

```
echo Hello World
```

You can use redirection and route the output to a file. And hence creating a new file in the process:

```
echo "Hello World" >> other_new_file
```

This way, you create a new file named `other_new_file` with the text `Hello World` in it.

![](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter4-echo-example.svg)
*Using echo command to create new file*

Remember, if the provided file already exists, with >> redirection, you add a new line to the file. You can also use > redirection but then it will replace the existing content of the file.

More on redirection can be found in the below tutorial.

[Input Output & Error Redirection in Linux [Beginner’s Guide]](https://linuxhandbook.com/redirection-linux/?ref=itsfoss.com)

## Create new files using the cat command

The original purpose of the cat command was to concatenate files. However, it is primarily used for displaying the contents of a file.

It can also be used to create a new file with the option to add content. For that, you can use the same > and >> redirections.

```
cat >> another_file
```

But this one will create a new file and allow you to add some text to it. Adding text is optional. **You can exit the cat entering mode by using Ctrl+d or Ctrl+c keys.**

![](https://cdn.jsdelivr.net/gh/SDNURoboticsAILab/ImageBed@master/img/resources/linux/chapter4-cat-example.svg)
*Using cat command to create new file*

Again, the append mode >> adds new text at the end of file content while the clobber mode > replaces the existing content with new.

!!! question "🏋️"

    Use the long listing display with ls -l and notice the timestamps. Now touch the file `touch other_new_file`. Do you see the difference in the timestamps?

## 📝 Test your knowledge

You have learned about creating new files. Here are a few simple exercises to practice what you just learned. It includes a little bit of the previous chapters as well.

- Use the touch command to create three new files named file1, file2 and file3. Hint: You don't need to run touch three times.
- Create a directory called files and create a file named my_file in it.
- Use the cat command to create a file called `your_file` and add the following text in it "This is your file".
- Use the echo command to add a new line "This is our file" to your_file.
- Display all the files in reverse chronological order (refer to chapter 3). Now use the touch command to modify the timestamp of file2 and file3. Now display the content in reverse chronological order again.

That's pretty fun. You are making good progress. You have learned to create new files in this chapter. Next, you'll learn about viewing the contents of a file.

*via: https://itsfoss.com/create-files/*
