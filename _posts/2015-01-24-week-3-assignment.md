---
layout: post
title: Hello World! Task
permalink: /task-for-week-3
author: A. Sean Pue
date:   2015-01-21
categories: helloworld,assignment
author: A. Sean Pue
---


---

In our second class, in addition to a lively discussion about digital humanities (notes are [here](https://etherpad.mozilla.org/al340-week2)), we also logged into our class server and created accounts. Before
the next class (1/30), you are to login to the server again and, working through the following
instructions, create a "Hello world!" webpage in your own public directory. (There are additional readings for the first part of the class on the [syllabus](/al340/syllabus).)

### Step 1. Login to the class server

The instructions for those of you using OS X and those using Windows differ slightly.

#### On OS X
For those of you using Apple's OS X, click on the magnifier button in the upper right of the screen and then find and run the
program "Terminal." Once at the terminal prompt, type:

```
ssh youridhere@al340.digitalhumanities.msu.edu
```

This runs the Secure Shell(SSH) program, a safe and secure way to connect to another server. The server name above is `al340.digitalhumanities.msu.edu`, and the user id is `youridhere`. The `@` symbol (at) works like that of your e-mail address.

For *youridhere*, enter your user id, which we have set to the same as your MSU mail id. When prompted, enter the password
you created in class or were assigned. Note that the password will not display when you are typing:

```
youridhere@al340.digitalhumanities.msu.edu's password:
```

If you make a mistake, type control+c to break out and then try again.

#### On Windows

On Windows you can download and use the program [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html). (It is also on the Windows computers on campus). For this week's task, you can just download `putty.exe` then run it.

After running Putty, enter the Host Name as `al340.digitalhumanities.msu.edu` then click open. When prompted, enter your user id for the host server, which we set to the same as your MSU id. If you make an error on the password, hit control+c. Note that the password will not display when you are typing:

    login as: youridhere
    youridhere@al340.digitalhumanities.msu.edu's password:

### Step 2. See where you are

If all goes according to plan, you should see something like the following:

    Welcome to Ubuntu 14.10 (GNU/Linux 3.16.0-29-generic x86_64)

    * Documentation:  https://help.ubuntu.com/

    System information as of Sat Jan 24 18:08:35 EST 2015

    System load:  0.72              Processes:           176
    Usage of /:   1.8% of 96.34GB   Users logged in:     1
    Memory usage: 11%               IP address for eth0: 35.8.224.150
    Swap usage:   0%

    Graph this data and manage this system at:
    https://landscape.canonical.com/

    Last login: Sat Jan 24 18:06:20 2015 from 12-333-144-786.somewhereorother.net
    youridhere@al340:~$


As you can see, our class server is running a distribution of Linux called [Ubuntu](http://www.ubuntu.com/).

You can now see where you are in the directory structure of the server by typing:

```
pwd
```

Write down what that command returns. `pwd` stands for 'print working directory.' It shows you whatever directory you are in.

The directory you are seeing is your home directory. You can create files here and in any directory below it. You cannot access many of the other parts of the system, e.g. where other programs or the main web files are found, unless you are a *superuser.*  You can, however, install programs in your directory and execute them.

### Step 3: Create a Public Directory

In the shell, the command to change what directory you are in is `cd`. What do you think that stands for?

The directory you are currently in—the one you log into when you connect to the server–also has a very short alias. Why? Because you wind up using quite a bit and programmers like to type quickly. The alias for your home directory is: `~`. That symbol is called tilde, and it's in the upper-left corner of your keyboard.

Let's now changing to your home directory using the `~` alias. Type the following:

```
cd ~
```

Type *pwd* again:

```
pwd
```

It should be the same home directory as before.

To make a directory, the command is `mkdir`. Let's now create a public directory where you can put files that can be displayed on the web!

To do so, we first create a directory called `public_html` using the `mkdir` command:

```
mkdir ~/public_html
```

That command creates a directory called `public_html` under your home directory. In your home directory, you could also type:

```
mkdir public_html
```

Now let's list the files in your home directory. The command for that is: `ls` (short for list)

To list the directories in your present working directory, type:

```
ls
```

You should see the directory `public_html` there. You can also give parameters to `ls`. To list all the files in your home directory, type the following:

```
ls ~
```

To see the files in `public_html`, type:

```
ls ~/public_html
```

You shouldn't see anything in there yet unless you have already created it.

### Step 4: Create Hello World file

Execute the following command to create a file called "helloworld.html" in your public_html directory that contains the text "Hello world!":

```
echo "Hello world!" > ~/public_html/helloworld.html
```

Here is what that command does:

* `echo "Hello world!"`: writes the text "Hello world!" (try it on the command line!)
* `> helloworld.html`: redirects the output of the previous `echo` to...
* `~/public_html/helloworld.html`: the file 'helloworld.html' in your public directory.

Now, if you list the files in your public directory, you should see that file:

```
ls ~/public_html
```

[Here's a neat trick. Since you already typed the command above just a while ago, you can get to it again by typing the up arrow on the command line.]


The default web address for your public directory is: `http://al340.msu.edu/~youridhere/`. Replacing youridhere with your user id, enter that address into your web browser.

What happens? You should get a message that the requested URL /youridhere/ was not found on the server. If you created the directory, why is nothing showing up? The reason is that you haven't yet given permission to make your file readable by users on the web.

### Step 5: Make Your Public Directory Readable by Others

By default, only you (or a superuser) can read your current files. What we are going to do in this step is to change the attributes of your `public_html` directory so that it is accessible from the web.

To do so, enter the following command:

```
chmod 755 ~/public_html
```

`chmod` stands for 'change mode.' Why 755? What that means is that the user (you) should be able to read, write, and execute the file(7--). The group that owns the file can read and execute the files(-5-), and others can also read and execute the file(--5). You can read more about that command on wikipedia [here](http://en.wikipedia.org/wiki/Chmod). The web server, in our case Apache, is also treated as a user, so it needs to be able to open the files.

Now go to your web browser and type the web address: `http://al340.digitalhumanities.msu.edu/~youridhere/helloworld.html`

You should see the following text:

```
Hello world!
```

If you do, congratulations! You are done with this assignment. Now complete the review quiz on D2L.

![Congratulations](https://media.giphy.com/media/K3raI0cXTkzNC/giphy.gif "silly")
