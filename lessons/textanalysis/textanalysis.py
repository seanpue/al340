# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # Textual Analysis in Python (for DHers, etc).
# # Part One: Basic Python
# 
# Author: A. Sean Pue
# 
# A lesson for AL340 Digital Humanities Seminar (Spring 2015)
# 
# Michigan State University

# <markdowncell>

# ## Welcome!
# This is an IPython Notebook. It contains numerous cells that can be of different types (Markdown, Code, Headings).
# 
# #### Your turn
# 
# Select the cell above this one by clicking it with your mouse. That is select the header **Textual Analysis**.
# 
# You can see that it contains text in a format called Markdown. To execute the cell,
# press `shift+enter.` To complete this tutorial (which is meant for a classroom), execute the cells and follow the instructions.

# <markdowncell>

# #### Your turn
# The cell below this one is producing an error. To fix it, change the cell type to Markdown (from Code) and then execute it by pressing `shift+enter`.

# <codecell>

I am really *Markdown* but I am set as Code. Fix me!

# <markdowncell>

# Python in Fifteen Minutes
# -------------------------

# <markdowncell>

# ### Why?
# 
# * Python is easy to learn
# * Python is easy to read
# * Python has lots of great tools to do things quickly

# <markdowncell>

# ### How?

# <markdowncell>

# This will be a very quick introduction to Python. 
# 
# We will focus on:
# * Setting variables
# * Writing comments
# * Python and spaces
# * Outputing
# * Functions and Types
# * Basic math
# * Basic text manipulation
# * Some Data Structures (Lists, Sets, and Dictionaries)
# * Getting help
# * Writing Functions
# * Testing and Checking

# <markdowncell>

# ### Setting Variables
# 
# A **variable** is basically a labeled box that you put things in. To set a variable in Python, you use the equal sign. Let's try.

# <codecell>

X = 1
Y=2

# <markdowncell>

# ### Writing Comments
# 
# You can make notes to yourself and others in Python by starting or ending a line with `#`.
# 

# <codecell>

# Here is an example
X = 1
X=1  # This line is considered less readable than the above.

# <markdowncell>

# ## Python and Spaces

# <markdowncell>

# One of the features of Python that makes it so readable is that it 
# cares very deeply about the space at the beginning of lines (indentation), so
# make sure you don't have a space at the beginning of the line.
# Otherwise, you will get an error.

# <markdowncell>

# #### Your Turn
# An IndentationError occurs below due to an extra space at the beginning. 
# Fix it.

# <codecell>

X = 1 #This is okay
# An IndentationError here due to the space
 X = 2

# <markdowncell>

# ### Outputing
# 
# There are different ways to output your variables and so forth.
# The IPython Notebook will output a variable or answer to an equation
# if it is the last command that is executing in the particular cell.

# <codecell>

# Here, nothing is displayed because there is just a variable set.
X=1

# <codecell>

# Here X is the last declaration in the cell, so X is displayed.
X=1
X

# <codecell>

# Here we have a declaration without a variable.
1

# <markdowncell>

# You can also use the command `print` followed by a variable or declaration.

# <codecell>

X=1
print 1
print X

# <markdowncell>

# You can `print` multiple variables or declarations together by using a comma.

# <codecell>

print 1,1,X,X

# <markdowncell>

# There are also ways to output to files and so forth. You can also produce HTML within the notebook.

# <markdowncell>

# #### Your Turn
# 
# Fill in the following 3 cells with the code you need to do the commands listed in the comments.

# <codecell>

# 1. In this cell, write the code to output the number 3. Do not use print

#YOURCODEHERE

# <codecell>

# 2. In this cell, do the same using print.

#YOURCODEHERE

# <codecell>

# 3. Do the following

# print the number 4 on its own line.

#YOURCODEHERE

# next, set X to 5

#YOURCODEHERE

# print X followed by 3

# <markdowncell>

# ## Basic Math
# 
# It's easy to do math in Python. The basic operators are +,-,/, and * for addition, subtraction, division, and multiplication.

# <codecell>

1+1

# <codecell>

4/2

# <codecell>

5*2

# <markdowncell>

# You can also use parentheses, e.g. `( )`, to specify the order of operations.

# <codecell>

(4-1)*3

# <markdowncell>

# You can use `+=` to add on to a number, too.

# <codecell>

X=1
X+=1
X

# <markdowncell>

# #### Your turn
# 
# Write code to answer the following: $777777 \times 666666 - 2$ 

# <codecell>

# The answer you should get is 518517481480
  
#YOURCODEHERE

# <markdowncell>

# Now, subtract 666666 from 777777 and multiply by the result by two.

# <codecell>

# The answer you should get is 222222.
# HINT: To do this on one line, you will need to use parentheses.

#YOURCODEHERE

# <markdowncell>

# ## Functions
# 
# A **function** is code that when called with a particular
# input gives a particular output. In math, this takes the form:
#     
#     f(X) = 2 + X
#     f(2) = 4
#     
# Python uses a similar format.
# 
# Here let's use the [built-in function](https://docs.python.org/2/library/functions.html#min)  `abs()` which gives the absolute value of a number (e.g. |-1|=1)

# <codecell>

abs(-1)

# <codecell>

abs(2-1) 

# <markdowncell>

# You can specify multiple inputs. Let's try another built-in function called `min`, which gives the minimum value of the numbers based to it.

# <codecell>

min(4,2,1)

# <codecell>

X=0
min(4,3,2,X)

# <markdowncell>

# Note that you can also add to an existing number (or texts, as we will see) by using `+=`.

# <codecell>

X = 1
X += 1
X

# <markdowncell>

# ## Number Types

# <markdowncell>

# You can find out the `type` of a variable or declaration using the function `type`. Let's try it.
# 

# <codecell>

type(1)

# <markdowncell>

# There are a number of basic numeric types, including `int` and `float.`
# 
# `int` is a whole number, positive or negative. To set it, you can do the following: `x=1` or `int(1)`.
# 
# `float` (for floating-point number) is a more precise number and includes a decimal. To set one, you can include a decimal point in your number, e.g. `x=1.0`, or use the function `float(1)`.

# <codecell>

type(1)

# <codecell>

type(1.0)

# <codecell>

type(2*3)

# <codecell>

type(2.0*3)

# <markdowncell>

# The distinction between `int` and `float` can be a bit of gotcha, as Python will provide an `int` answer if one of the variables is not set as a `float` (by adding a `decimal` to the declaration).

# <markdowncell>

# ### Your turn
# 
# Adjust the following code to return .5:

# <codecell>

# Fix below to return .5 (not 0). 
X = 1/2
print X

# <markdowncell>

# ## Testing for Equivalence
# 
# Python has two special words, `True` and `False`, to tell the
# veracity of something, and a special type `bool` to hold that value.

# <codecell>

x = True
type(x)

# <markdowncell>

# You can test whether or not something equals something else using the
# operator `==`, and to see if they are not equal using `!=`. 

# <codecell>

x = 1
x == 1

# <codecell>

x = 2
x != 1

# <codecell>

type(True)

# <markdowncell>

# ## Testing as You Go

# <markdowncell>

# You can check to make sure your expectations are correct using the command
# assert, which will through an error if your assertion is not correct.

# <codecell>

x = 1
assert x == 1 # no problem here
assert x == 1.0 # no problem here, either
assert type(x)==float # it's an int not a float!

# <markdowncell>

# ## Strings
# 
# Python is great at manipulation strings of text, and there is a special `str` type. To designate a string,
# type text in single or double quotation marks.

# <codecell>

s = 'Hello'
t = "there"
type(s)

# <markdowncell>

# Strings can be combined using `+`:

# <codecell>

s + ' ' + t+ ' what\'s your name?' # you can use \' to put a ' inside ''s

# <markdowncell>

# To get the length of a string, use the function `len`.

# <codecell>

len('Hello')

# <markdowncell>

# Strings also have numerous functions available to them. To use them,
# type a string variable followed by a period and then
# the function.

# <codecell>

s = 'Hello'
print s.capitalize() # capitalizes the first letter
print s.upper()      # capitalizes all letters
print s.lower()     # lowercases all letters


# <codecell>

a = 'X'.lower() # makes the string 'X' lowercase
b = 'x'.upper() # makes the strin g'x' uppercase
print (a + b).upper() # joins a and b and turns them uppercase
print (a + b).lower().upper() # does the above but then turns it uppercase 

# <markdowncell>

# You can turn a number into a string, and a string into a number 
# as follows.

# <codecell>

s='1'
i=int(s)
f=float(s)
print s,i,f

# <markdowncell>

# ## Other Data Structures: Lists, Sets, and Dictionaries

# <markdowncell>

# Python has a number of other data structures besides the ones we have learned (`int`,`float`,`str`,`bool`)

# <markdowncell>

# Python is not "strongly typed" which means the `type` of your variable
# can changes, as in the following:

# <codecell>

x = 1
print x,type(x)
x = 1.0
print x,type(x)
x = '1'
print x,type(x)
x = False
print x,type(x)

# <markdowncell>

# ### Lists
# 
# A list is a collection of different variables. The format is: 
#     `[item1,item2,item3]`
# The items can be of different types. The first element of a list is at [0]. As with `str` (strings) you can get a length using `len`.

# <codecell>

my_list = ['A',1,2,3,'B'] 
print my_list
print 'the first item is',my_list[0]
print 'length of my_list is',len(my_list)

# <markdowncell>

# You can also select from the end of a list using a negative number, e.g. `l[-1]`, and you can select a range of items using a colon, e.g. l[0:2]

# <codecell>

l = ['0',1,2,3,'5']
print 'the first two items are',l[0:2] # l[start_at,end_before]
print 'The last item is',l[-1] # use negative numbers to read from end
print 'The first to next-to-last items are',l[0:-1]

# <markdowncell>

# #### Your turn
# 
# Using the following list, select ['B','C','D']

# <codecell>

l = ['A','B','C','D','E','F']

# YOURCODEHERE

# <markdowncell>

# To append to a list use the `.append` command or `+=`

# <codecell>

l=['A','B','C','D','E','F']
l+='G'
print l
l.append('H')
print l

# <markdowncell>

# ### Sets
# 
# A `set` is like a `list` but it does not have any duplicates.
# To define one, use the command `set`.

# <codecell>

l = ['A','A','A','B']
print l,type(l)
s = set(l)
print s,set(s)

# <markdowncell>

# ### Dictionary
# 
# A dictionary (`dict`)is a structure that allows you to use a key. To define one, you can use curly brackets, e.g. {'hi':'hindi','en':'urdu'}, and then access or set individual items using square brackets

# <codecell>

langs = {}
print langs, type(langs)
langs['hi'] = 'Hindi'
print langs, len(langs)  # you can get the length, too

# Here is a way to set it all at once

langs = {'hi': 'Hindi', 'en': 'English', 'myfavnumber': 7}
print len(langs),langs['myfavnumber']

# <markdowncell>

# To get the keys of a dictionary, use the funciton `.keys`, e.g. langs.keys()

# <codecell>


print langs.keys()

# <markdowncell>

# ### Iterating (through lists, etc.)
# 
# Iterating moves going one-my-one through something. 
# 
# To go through every element in a list, use the `for` command as below.

# <codecell>

colors = ['red','white','blue','green']
for x in colors:
    print x

# <markdowncell>

# #### Your Turn
# 
# Write code below to add 'purple' to the list of colors and then print out 'I like <color here>', e.g. 'I like blue'.

# <codecell>

colors = ['red','white','blue','green']

# YOURCODEHERE

# <markdowncell>

# ## Writing Functions
# 
# Whenever you have a task that you need to repeat, it is usually worthwhile
# to make a function. As mentioned above, a function is code that takes an input and returns an output.
# 
# In Python, you define a Python using the following pattern:
# 
# ```
# def my_function(): # put your input inside the ()s
#     # your code here
#     return # your output here output
# ```
# Here is an example:
# ```
# def add_one(x)
#     x = x + 1
#     return x
# ```
# You can have multiple inputs, and the output can be whatever form you want, too. Spacing is important, as you need a standard indentation (usually 4 or 2 spaces) after the definition. That makes it easier to read.  
# 
# Below is an example.

# <codecell>

def add_two(x):
    return x+2

def add_three(x):
    o = x+2
    return o

def add_five(x):
    assert x
    return add_two(add_three(x))

y = 0
y = add_two(y)
print y
y = add_three(y)
print y
y = add_five(y)
print y

# <markdowncell>

# ### Your turn
# 
# Write a function named `quote_me` to add an exclamation mark to a string.

# <codecell>

# So quote_me('Hello') should output: Hello!
def quote_me(s):
    # YOURCODEHERE
    return #YOURCODEHERETOO

# <markdowncell>

# ### Importing Libraries
# 
# To get extended features from Python, you need to import modules. You may need to install those modules, too. You can use the command `import`. Below we will import the module `sys`, which provides information about your system.

# <codecell>

import sys
print sys.version # this shows your version of Python, etc.

# <markdowncell>

# Above, you see you can access a variable or a function by prefacing it my the name of the module. If you want to import the variable or version into the 'name space' your code so that you can access it directly, use the command `from`...`import`...

# <codecell>

from sys import version
print version # we no longer need the sys

# <markdowncell>

# You can also import a module and give its own name using the command `import`...`as`...

# <codecell>

import sys as my_own_system
print my_own_system.version

# <markdowncell>

# ### Nice work!
# We're now ready in the next lesson to jump into textual analysis with Python!

# <codecell>


