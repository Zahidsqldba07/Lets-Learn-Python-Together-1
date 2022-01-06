'''Minute Python Program Examples'''

# Let's experiment with Python programming
# and see what we can learn together. Try expanding
# on my Python programming examples and see
# what happens. Happy Accidents and Discoveries
# always happen when we least expect it. Who
# knows? One might even happen to me too, while
# we tinker and learn some Python together.
# So what are we waiting for? Let's get into it...

# Let's play with variables and modify their
# values. We will put Socks into our variable
# container and take Shoes out of it. I could only
# wish real containers could do that. Don't you?

variable_container='Socks'

print(variable_container) # Socks

replace_value=variable_container.replace('Socks','Shoes')

print(replace_value) # Shoes

# Let's add more stuff inside the variable container.

variable_container=['Socks']

variable_container.append('Shoes')

# Let's take our stuff out of the variable container.
# so we can wear them.

print(variable_container[0]) # Socks
print(variable_container[1]) # Shoes
'''----------------------------------------------------------------'''
# Let's create a shopping container variable
# list and append the values to another, empty
# container list with a for-loop.

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

empty_container=[] # empty list []

for i in shopping_container:
    empty_container.append(i) # appended list [',',',']

print(empty_container[0]) # Pants
print(empty_container[1]) # Shirt
print(empty_container[2]) # Socks
print(empty_container[3]) # Shoes
print(empty_container[4]) # Books
print(empty_container[5]) # Pens

# Let's reduce all these repetitive 'print()' statements
# down to one.

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

empty_container=[] # empty list []

for i in shopping_container:
    empty_container.append(i) # appended list [',',',']

for i in empty_container:
    print(i)

# Let's try to reduce these two for-loops down
# to one, simply by placing the 'print' statement
# as part of the entire for-loop code block.

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

empty_container=[] # empty list []

for i in shopping_container:
    empty_container.append(i) # appended list [',',',']
    print(i)
'''----------------------------------------------------------------'''
# Let's count how many letters there are in
# a simple 'print()' function, including blank
# spaces in between letters with the 'len()'
# function.

print(len("Let's count how many letters there are in this text sentence."),
      'letters, including spaces in between letters.')

# Let's count how many shopping container
# variable list value items we have with the
# 'len()' function.

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

print(len(shopping_container),'shopping list item values.')
'''----------------------------------------------------------------'''
# Let's directly sort our shopping container
# variable list values with the 'sort()' function.

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

shopping_container.sort() # 'sort()' alters the actual list

print(shopping_container) # ['Books', 'Pants', 'Pens', 'Shirt', 'Shoes', 'Socks']
'''----------------------------------------------------------------'''
# Let's sort a copy of our shopping container
# variable list values with the 'sorted()' function,
# while keeping the original list intact and unchanged.

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

list_copy=sorted(shopping_container) # 'sorted()' list copy only

print(list_copy) # ['Books', 'Pants', 'Pens', 'Shirt', 'Shoes', 'Socks']

print(shopping_container) # ['Pants', 'Shirt', 'Socks', 'Shoes', 'Books', 'Pens']
'''----------------------------------------------------------------'''
# Let's reverse our shopping container variable
# list with the 'reverse()' function.

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

shopping_container.reverse()

print(shopping_container) # ['Pens', 'Books', 'Shoes', 'Socks', 'Shirt', 'Pants']
'''----------------------------------------------------------------'''
# Let's insert a value into our shopping container
# variable list with the 'insert()' function.

# Example 1:

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

shopping_container.insert(0,'Tie') # index '[0]'

print(shopping_container) # ['Tie', 'Pants', 'Shirt', 'Socks', 'Shoes', 'Books', 'Pens']

# Example 2:

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

shopping_container.insert(1,'Tie') # index '[1]'

print(shopping_container) # ['Pants', 'Tie', 'Shirt', 'Socks', 'Shoes', 'Books', 'Pens']
'''----------------------------------------------------------------'''
# Let's remove a list value from our shopping
# container variable list with the 'remove()'
# function.

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

shopping_container.remove('Pants')

print(shopping_container) # ['Shirt', 'Socks', 'Shoes', 'Books', 'Pens']
'''----------------------------------------------------------------'''
# Let's pop a value from our shopping container
# variable list with the 'pop()' function.

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

print(shopping_container.pop(4)) # Books

# Notice how the value 'Books' is gone from our
# shopping container?

print(shopping_container) # ['Pants', 'Shirt', 'Socks', 'Shoes', 'Pens']

# We can use the 'pop()' function as a stack and
# pop off every value in our shopping container
# variable list. We can use a for-loop to do this
# for us.

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

for i in range(6):
    shopping_container.pop()

print(shopping_container) # empty shopping container '[]'

# or:

for i in shopping_container:
    i.pop()

print(shopping_container) # empty shopping container '[]'

# Let's show all the popped off values with the
# 'pop()' function. We will use a for-loop for this.

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

empty_container=[] # empty list []

for i in shopping_container:
    empty_container.append(i) # appended list [',',',']

# When we recall the 'empty_container' variable
# list the screen output will be in the reverse order.
# The last value taken from the stack is the first
# value that will go back to the stack at the top,
# not the bottom where we popped off from.

for i in range(6):
    print(empty_container.pop())
'''----------------------------------------------------------------'''
# Let's completely delete a variable list value
# with the 'del()' function. We will use our shopping
# container variable list as our program example.

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

del(shopping_container[2])

# The value 'Socks' is no longer in our shopping_container
# variable list.

print(shopping_container) # ['Pants', 'Shirt', 'Shoes', 'Books', 'Pens']
'''----------------------------------------------------------------'''
# Let's clear the shopping_container variable
# list with 'clear()' function.

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

shopping_container.clear()

print(shopping_container) # []
'''----------------------------------------------------------------'''
# Let's copy a list with what is called a 'shallow
# copy' with the 'copy()' function. We will use
# our shopping container variable list for this
# program example. Note: we need to import
# the 'copy()' function by invoking the 'import
# copy' function.

import copy

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

list_copy=shopping_container.copy()

print('Copied List:', list_copy)
'''----------------------------------------------------------------'''
# Let's copy a list with what is called a 'deep
# copy' with the 'deepcopy()' function. We will
# use our shopping container variable list for
# this program example. Note: we need to
# import the 'copy()' function by invoking the
# 'import copy' function.

# The 'deepcopy()' function copies the original
# list contents, which is not a shallow copy of
# its contents. With deep copying, we are actually
# moving the whole list of values into a brand
# new list.

import copy

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

new_list=copy.deepcopy(shopping_container)

print("Old list:", shopping_container)
print("New list:", new_list)

# Here are the prefixes for how to use the 'copy()'
# and 'deepcopy()' functions.

# import copy
# copy.copy(x)
# copy.deepcopy(x)
'''----------------------------------------------------------------'''
# Let's try other things with our shopping container
# variable list. Let's change one of its values
# using indexes '[ ]'.

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

shopping_container[0]='Tie'

print(shopping_container) # ['Tie', 'Shirt', 'Socks', 'Shoes', 'Books', 'Pens']
'''----------------------------------------------------------------'''
# Let's create two lists and then put them together
# as one, huge list. Let's create the variables
# 'a' and 'b' so we can use them in our program
# example. We will use the 'extend()' function.

a=['One','Two','Three','Four','Five']
b=['Orange','Apple','Banana','peach','Watermelon']

a.extend(b)

print(a) # ['One', 'Two', 'Three', 'Four', 'Five', 'Orange', 'Apple', 'Banana', 'peach', 'Watermelon']
'''----------------------------------------------------------------'''
# Let's use a 'for-in-zip() loop to combine two
# or more variable lists together. Note: if one
# variable list is shorter than the other longer
# variable list the longer variable list will be
# shortened down to the shortest of the two
# or more variable lists. In this program example,
# we are using two equal sized variable lists
# so we can combine both variable lists together,
# without the fear of some values being left
# out.

a=['One','Two','Three','Four','Five']
b=['Orange','Apples','Bananas','peaches','Watermelons']

for x,y in zip(a,b):
    print(f'{x} {y}')

'''
One Orange
Two Apples
Three Bananas
Four peaches
Five Watermelons
'''
'''----------------------------------------------------------------'''
# Let's use our shopping container variable
# list to enumerate the values in it with the
# 'for-in-enumerate() loop'.

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

for index,values in enumerate(shopping_container):
    print(index,values)

# screen output:
'''
0 Pants
1 Shirt
2 Socks
3 Shoes
4 Books
5 Pens
'''
# Let's invoke the 'start=1' option to start our
# indexing at '1', not '0'.

for index,values in enumerate(shopping_container,start=1):
    print(index,values)

# screen output:
'''
1 Pants
2 Shirt
3 Socks
4 Shoes
5 Books
6 Pens
'''
'''----------------------------------------------------------------'''
# Let's covert a 'tuple()' into a 'list[]' with the
# 'list()' function program example:

shopping_container=('Pants','Shirt','Socks','Shoes','Books','Pens')

convert=list(shopping_container)

print(convert) # ['Pants', 'Shirt', 'Socks', 'Shoes', 'Books', 'Pens']
'''----------------------------------------------------------------'''
# Let's covert a 'list[]' into a 'tuple()' with the
# 'tuple()' function program example:

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

convert=tuple(shopping_container)

print(convert) # ('Pants', 'Shirt', 'Socks', 'Shoes', 'Books', 'Pens')
'''----------------------------------------------------------------'''
# Let's covert a 'set{}' into a 'tuple()' with the
# 'tuple()' function program example:

shopping_container={'Pants','Shirt','Socks','Shoes','Books','Pens'}

convert=tuple(shopping_container)

print(convert) # ('Socks', 'Shoes', 'Pants', 'Books', 'Shirt', 'Pens')
'''----------------------------------------------------------------'''
# Let's covert a 'set{}' into a 'list[]' with the
# 'list[]' function program example:

shopping_container={'Pants','Shirt','Socks','Shoes','Books','Pens'}

convert=list(shopping_container)

print(convert) # ['Pens', 'Shoes', 'Socks', 'Books', 'Pants', 'Shirt']
'''----------------------------------------------------------------'''
# Let's covert a 'tuple()' into a 'set{}' with the
# 'set{}' function program example:

shopping_container=('Pants','Shirt','Socks','Shoes','Books','Pens')

convert=set(shopping_container)

print(convert) # {'Shoes', 'Pens', 'Pants', 'Socks', 'Books', 'Shirt'}
'''----------------------------------------------------------------'''
# Let's covert a 'list()' into a 'set{}' with the
# 'set{}' function program example:

shopping_container=['Pants','Shirt','Socks','Shoes','Books','Pens']

convert=set(shopping_container)

print(convert) # {'Shoes', 'Pens', 'Pants', 'Socks', 'Books', 'Shirt'}
'''----------------------------------------------------------------'''
# Let's create a dictionary using arguments
# with the 'dict()' function. Let's use our
# shopping_container variable tuple for this
# program example.

shopping_container=dict(Pants='Shirt',Socks='Shoes',Books='Pens')

print(shopping_container) # {'Pants': 'Shirt', 'Socks': 'Shoes', 'Books': 'Pens'}
'''----------------------------------------------------------------'''
# Let's convert our shopping_container variable
# multi-list pairs into a dictionary with the 'dict()'
# function. Note: you can also combine tuple
# pairs and list pairs together. For example:

# ['Pants','Shirt'],('Socks','Shoes'),['Books','Pens']

shopping_container=['Pants','Shirt'],['Socks','Shoes'],['Books','Pens'] # three pairs

convert=dict(shopping_container)

print(convert) # {'Pants': 'Shirt', 'Socks': 'Shoes', 'Books': 'Pens'}
'''----------------------------------------------------------------'''
# Check to see of a value is in our shopping
# container variable list by omitting the 'in'
# emitter. If a value is in our shopping container
# variable list, the screen output will show
# 'True'. If a value isn't found in our shopping
# container variable list the output will show
# 'False'.

shopping_container=('Pants','Shirt','Socks','Shoes','Books','Pens')

print('Pants'in shopping_container) # True

print('Shorts'in shopping_container) # False

# Let's also invoke the 'not' operator and see
# what happens to our shopping container
# variable list program example.

shopping_container=('Pants','Shirt','Socks','Shoes','Books','Pens')

print('Pants'not in shopping_container) # False

print('Shorts'not in shopping_container) # True
'''----------------------------------------------------------------'''
# Let's create our first 'def()' function with a
# 'print()' function inside it, then call up our
# first 'def()' function, 'my_first_function()'
# to display the screen output.

def my_first_function():
    print('My first function.')

# call up 'my_first_function()'

my_first_function()
'''----------------------------------------------------------------'''
# Let's create our second 'def()' function with
# a 'print()' function inside it along with the
# variable 'software', then call up our second
# 'def()' function, 'my_second_function()' to
# display the screen output.

def my_second_function(software):
    print('My second function with',software)

# call up 'my_second_function()' along with its
# argument value 'Python 3'

my_second_function('Python 3')
'''----------------------------------------------------------------'''
# Let's create our third 'def()' function with a
# 'print()' function inside it along with the variables
# 'software' and 'program', then call up our
# third 'def()' function, 'my_third_function()'
# to display the screen output.

def my_third_function(software,program):
    print('My third function with',program)

# call up 'my_third_function()' along with its
# two argument values 'Python 3' and 'python'

my_third_function('Python 3','Python')
'''----------------------------------------------------------------'''
# Let's create our fourth 'def()' function with
# a 'print()' function inside it along with the
# variables 'software', 'program' and 'programmer',
# then call up our fourth 'def()' function,
# 'my_fourth_function()' to display the screen
# output.

def my_fourth_function(software,program,programmer):
    print('My fourth function with',programmer)

# call up 'my_fourth_function()' along with its
# three argument values 'Python 3', 'python'
# and 'Joseph'

my_fourth_function('Python 3','Python','Joseph')
'''----------------------------------------------------------------'''
# Let's create our fifth 'def()' function with a
# for-loop and a 'print()' function inside it, then
# call up our fifth 'def()' function, 'my_fifth_function()'
# to display the screen output.

def my_fifth_function():
    for i in range(3):
        print('loop',i,'times inside my_fifth_function.')

# call up 'my_fifth_function()'

my_fifth_function()
'''----------------------------------------------------------------'''
# Let's create our sixth 'def()' function with a
# for-loop and a 'print()' function inside it along
# with the variable 'software', then call up our
# sixth 'def()' function, 'my_sixth_function()'
# to display the screen output.

def my_sixth_function(software):
    for i in range(3):
        print('loop',i,'times inside my_sixth_function.',software)

# call up 'my_sixth_function()' along with its
# argument value 'Python 3'

my_sixth_function('Python 3')
'''----------------------------------------------------------------'''
# Let's create our seventh 'def()' function with
# a for-loop and a 'print()' function inside it
# along with the variables 'software' and
# 'program', then call up our seventh 'def()'
# function, 'my_seventh_function()' to display
# the screen output.

def my_seventh_function(software,program):
    for i in range(3):
        print('loop',i,'times inside my_seventh_function.',program)

# call up 'my_seventh_function()' along with
# its argument values 'Python 3' and 'Python'

my_seventh_function('Python 3','Python')
'''----------------------------------------------------------------'''
# Let's create our eighth 'def()' function with
# a for-loop and a 'print()' function inside it
# along with the variables 'software', 'program'
# and 'programmer', then call up our eighth
# 'def()' function, 'my_eighth_function()' to
# display the screen output.

def my_eighth_function(software,program,programmer):
    for i in range(3):
        print('loop',i,'times inside my_eighth_function.',programmer)

# call up 'my_eighth_function()' along with its
# argument values 'Python 3', 'Python' and 'Python'

my_eighth_function('Python 3','Python','Joseph')
'''----------------------------------------------------------------'''
# Let's create our ninth 'def()' function that
# returns a value, then call up our ninth 'def()'
# function, 'my_ninth_function()' to display
# the screen output.

def my_ninth_function(software):
    return software

# call up 'my_ninth_function()' along with its
# argument value 'Python 3'

print(my_ninth_function('Python 3'))
'''----------------------------------------------------------------'''
# Let's create our tenth 'def()' function that
# returns one of two values, then call up our
# tenth 'def()' function, 'my_tenth_function()'
# to display the screen output.

def my_tenth_function(software,program):
    return program

# call up 'my_tenth_function()' along with its
# argument values 'Python 3' and 'Python'

print(my_tenth_function('Python 3','Python'))
'''----------------------------------------------------------------'''
# Let's create our eleventh 'def()' function that
# returns one of three values, then call up our
# eleventh 'def()' function, 'my_eleventh_function()'
# to display the screen output.

def my_eleventh_function(software,program,programmer):
    return programmer

# call up 'my_eleventh_function()' along with its
# argument values 'Python 3', 'Python' and 'Joseph'

print(my_eleventh_function('Python 3','Python','Joseph'))
'''----------------------------------------------------------------'''
# Let's create our twelfth 'def()' function that
# overrides all its return values, then call up
# our twelfth 'def()' function, 'my_twelfth_function()'
# to display the screen output.

def my_twelfth_function(software,program,programmer):
    return 'Overrides all the values.'

# call up 'my_twelfth_function()' along with its
# argument values 'Python 3', 'Python' and 'Joseph'

print(my_twelfth_function('Python 3','Python','Joseph'))
'''----------------------------------------------------------------'''
# Let's create our thirteenth 'def()' function
# that overrides two of its return values, then
# call up our thirteenth 'def()' function,
# 'my_thirteenth_function()' to display the
# screen output.

def my_thirteenth_function(software,program,programmer):
    return 'Override this value. '+program+'Override that value.'

# call up 'my_thirteenth_function()' along with its
# argument values 'Python 3', 'Python' and 'Joseph'

print(my_thirteenth_function('Python 3 ','Python ','Joseph'))
'''----------------------------------------------------------------'''
# Let's create our fourteenth 'def()' function
# that returns three values, then call up our
# fourteenth 'def()' function, 'my_fourteenth_function()'
# to display the screen output.

def my_fourteenth_function(software,program,programmer):
    return software+program+programmer

# call up 'my_fourteenth_function()' along with
# its argument values 'Python 3', 'Python' and
# 'Joseph'

print(my_fourteenth_function('Python 3 ','Python ','Joseph'))
'''----------------------------------------------------------------'''
# Let's create a mathematical 'def()' function
# that returns a number value, then call up our
# arithmetic 'def()' function, 'arithmetic(num)'
# to display the screen output.

def arithmetic(num):
    return num+num

print(arithmetic(2)) # 4

print(int(arithmetic(2))) # 4

print(float(arithmetic(2))) # 4.0
'''----------------------------------------------------------------'''
# Let's create a mathematical 'def()' function
# that returns two number values, then call
# up our arithmetic 'def()' function, 'arithmetic(num)'
# to display the screen output.

def arithmetic(num1,num2):
    return num1+num2

print(arithmetic(1,2)) # 3

print(int(arithmetic(1,2))) # 3

print(float(arithmetic(1,2))) # 3.0
'''----------------------------------------------------------------'''
# Let's create a mathematical 'def()' function
# that returns three number values, then call
# up our arithmetic 'def()' function, 'arithmetic(num)'
# to display the screen output.

def arithmetic(num1,num2,num3):
    return num1+num2*num3

print(arithmetic(1,2,3)) # 7

print(int(arithmetic(1,2,3))) # 7

print(float(arithmetic(1,2,3))) # 7.0
'''----------------------------------------------------------------'''
# Let's create a mathematical 'def()' function
# that returns three number values, then call
# up our arithmetic 'def()' function, 'arithmetic(num)'
# to display the screen output.

def arithmetic(num1,num2,num3):
    return num1+num2*num3/num2-num1

print(arithmetic(1,2,3)) # 3

print(int(arithmetic(1,2,3))) # 3

print(float(arithmetic(1,2,3))) # 3.0
'''----------------------------------------------------------------'''
# Let's create a mathematical 'def()' function
# that returns the 'sum' of all ten number values
# from 0 to 9, then call up our arithmetic 'def()'
# function, 'arithmetic(num)' to display the
# screen output.

def arithmetic(a=(0,1,2,3,4,5,6,7,8,9)):
    return f'The values in variable "a" add/sum up to {sum(a)}.'

print(arithmetic())
'''----------------------------------------------------------------'''
# Let's create a mathematical 'def()' function
# that returns the 'sum' of two sets of values
# from 0 to 9 and 10 to 19, then call up our
# arithmetic 'def()' function, 'arithmetic(num)'
# to display the screen output.

def arithmetic(
    a=(0,1,2,3,4,5,6,7,8,9),
    b=(10,11,12,13,14,15,16,17,18,19)):
    return f'The sum of "a"={sum(a)} and the sum of "b"={sum(b)}.'

print(arithmetic())
'''----------------------------------------------------------------'''
# Let's create a mathematical 'def()' function
# that returns the 'sum' of three sets of values
# from 0 to 9, 10 to 19 and 20 to 21, then call
# up our arithmetic 'def()' function, 'arithmetic(num)'
# to display the screen output.

def arithmetic(
    a=(0,1,2,3,4,5,6,7,8,9),
    b=(10,11,12,13,14,15,16,17,18,19),
    c=(20,21,22,23,24,25,26,27,28,29)):
    return f'The sum of "a"={sum(a)}, the sum of "b"={sum(b)} and the sume of "c"={sum(c)}.'

print(arithmetic())
'''----------------------------------------------------------------'''
# Let's play with easy to understand, very small
# classes, so we have a much better understanding
# of them. Let's create a object variable called
# 'software' and make its value output 'Python'.

class My_first_beginner_class:
    software='Python'

print(My_first_beginner_class.software) # Python
'''----------------------------------------------------------------'''
# Let's add one more object variable to our
# class to see how objects work inside classes.

class My_second_beginner_class:
    software='Python 3'
    program='Python'

print(My_second_beginner_class.software) # output screen: 'Python'
print(My_second_beginner_class.program) # output screen: 'Python 3'
'''----------------------------------------------------------------'''
# Let's add just one more object variable to
# our class to see how objects work inside
# classes.

class My_third_beginner_class:
    software='Python 3'
    program='Python'
    programmer='Joseph'

print(My_third_beginner_class.software) # output screen: 'Python'
print(My_third_beginner_class.program) # output screen: 'Python 3'
print(My_third_beginner_class.programmer) # output screen: 'Joseph'
'''----------------------------------------------------------------'''
# Let's create a class using the initialise '__init__'
# method to retrieve values.

class My_fourth_beginner_class:
    def __init__(self,software):
        self.software=software

print(My_fourth_beginner_class('Python 3').software) # output screen: 'Python 3'
'''----------------------------------------------------------------'''
# Let's add one more object variable to our
# class to see how the '__init__' method works.

class My_fifth_beginner_class:
    def __init__(self,software,program):
        self.software=software
        self.program=program

print(My_fifth_beginner_class('Python 3','Python').software) # output screen: 'Python 3'
print(My_fifth_beginner_class('Python 3','Python').program) # output screen: 'Python'
'''----------------------------------------------------------------'''
# Let's add just one more object variable to
# our class to see how the '__init__' method
# works.

class My_sixth_beginner_class:
    def __init__(self,software,program,programmer):
        self.software=software
        self.program=program
        self.programmer=programmer

print(My_sixth_beginner_class('Python 3','Python','Joseph').software) # output screen: 'Python 3'
print(My_sixth_beginner_class('Python 3','Python','Joseph').program) # output screen: 'Python'
print(My_sixth_beginner_class('Python 3','Python','Joseph').programmer) # output screen: 'Joseph'

# Let's get rid of some long strings in our three
# 'print()' functions by using a variable 'a' instead.

a=My_sixth_beginner_class('Python 3','Python','Joseph')

print(a.software) # output screen: 'Python 3'
print(a.program) # output screen: 'Python'
print(a.programmer) # output screen: 'Joseph'

# or:

a=My_sixth_beginner_class('Python 3','Python','Joseph').software
b=My_sixth_beginner_class('Python 3','Python','Joseph').program
c=My_sixth_beginner_class('Python 3','Python','Joseph').programmer

print(a) # output screen: 'Python 3'
print(b) # output screen: 'Python'
print(c) # output screen: 'Joseph'
'''----------------------------------------------------------------'''
# Let's create a class that will return a value
# along with another example of the '__init__'
# method.

class My_seventh_beginner_class:
    def __init__(self,software):
        self.software=software
    def computer():
            return software

a=My_seventh_beginner_class('Python 3')

print(a.software) # output screen: Python 3
'''----------------------------------------------------------------'''
# Let's add one more return value to our class
# to see how the '__init__' method works.

class My_eighth_beginner_class:
    def __init__(self,software,program):
        self.software=software
        self.program=program
    def computer():
            return software,program

a=My_eighth_beginner_class('Python 3','Python')

print(a.software) # output screen: Python 3
print(a.program) # output screen: Python
'''----------------------------------------------------------------'''
# Let's add just one more return value to our
# class to see how the '__init__' method works.

class My_ninth_beginner_class:
    def __init__(self,software,program,programmer):
        self.software=software
        self.program=program
        self.programmer=programmer
    def computer():
            return software,program,programmer

a=My_ninth_beginner_class('Python 3','Python','Joseph')

print(a.software) # output screen: Python 3
print(a.program) # output screen: Python
print(a.programmer) # output screen: Joseph
'''----------------------------------------------------------------'''
# Let's override some of these values and see
# what happens to our screen output values.

class My_tenth_beginner_class:
    def __init__(self,software,program,programmer):
        self.software='Monty'
        self.program=program
        self.programmer='Flying Circus'
    def computer():
            return software,program,programmer

a=My_tenth_beginner_class('Python 3','Python','Joseph')

print(a.software) # output screen: Monty
print(a.program) # output screen: Python
print(a.programmer) # output screen: Flying Circus
'''----------------------------------------------------------------'''
# Let's learn how to properly do string concatenation
# with strings and string values alike. For example:

variable='string concatenation'

print('I love',variable,'so much!')

print('I love '+variable+' so much!')

print('I love '+variable,'so much!')

print('I love',variable+' so much!')

print('I love {} so much!'.format(variable)) # old format is depreciated but can still be used

print(f'I love {variable} so much!')  # new 'f' string format is most popular in Python 3 and up
'''----------------------------------------------------------------'''
# The string concatenation examples above
# work fine. However, there will be times when
# you will have to invoke the 'str()' function
# or the 'int()' function, or both. For example:

a=1+2

print('1+2 =',a,'is correct!') # default string concatenation

print('1+2 ='+str(a)+' is correct!') # the 'str()' function converts an integer value to a string

print('1+2 =',str(a)+' is correct!') # the 'str()' function converts an integer value to a string

print('1+2 = '+str(a),' is correct!') # the 'str()' function converts an integer value to a string

print(f'1+2 = {a} is correct!')  # new 'f' string format is most popular in Python 3 and up
'''----------------------------------------------------------------'''
# Here are some ideas for 'casting' variables.

text_string=int('3') # converts a text string value to an integer value

integer_number=str(3) # converts an integer value to a text string value

print(text_string+2) # this is an integer value, not a text value

print(integer_number+'3') # this is a text string value only, not an integer value
'''----------------------------------------------------------------'''
# Let's create a 'def()' function that uses four
# types of string concatenation, then call up
# our string_concatenation 'def()' function,
# 'string_concatenation(num)' to display the
# screen output.

def string_concatenation(software='Python 3'):

    print('My fifteenth function with',software+'.')

# also use string concatenation in these ways:

    print('My string concatenation function with '+software+'.')

    print('My string concatenation function with {}.'.format(software)) # old format is depreciated but can still be used

    print(f'My string concatenation function with {software}.') # new 'f' string format is most popular in Python 3 and up

string_concatenation()
'''----------------------------------------------------------------'''
# Let's create a 'def()' function that uses five
# types of string concatenation, then call up
# our string concatenation 'def()' function,
# 'string_concatenation()' to display the
# screen output.

def string_concatenation(software='Python 3',program='Python',programmer='Joseph'):

    print('My string concatenation function with',software,'and computer programmer:',programmer,'teaches me',program+'.')

# also use string concatenation in these ways:

    print('My string concatenation function with '+software+' and computer programmer: '+programmer+' teaches me '+program+'.')

    print('My string concatenation function with',software+' and computer programmer: '+programmer,'teaches me',program+'.')

    print('My string concatenation function with {} and computer programmer: {} teaches me {}.'.format(software,programmer,program))

    print(f'My string concatenation function with {software} and computer programmer: {programmer} teaches me {program}.')

string_concatenation()
'''----------------------------------------------------------------'''
# Let's have a bit of fun in our last Python
# programming lesson with the 'f' string format
# to make string concatenating much easier
# for beginners to understand. The 'f' string
# format eliminates commas ',' and plus '+'
# signs altogether, leaving out the worry of
# potential errors on the beginner's part.
# However, as you get more advanced with
# programming in general, you might find it
# more convenient to do old school string
# concatenation instead. Also note: that the
# old string format is depreciated in Python 3
# and up, which simply means it still works,
# but it's not necessary to use anymore
# hence the 'f' string format.

submarine='Subroutine'
subroutine='Submarine'
programmer='Joesph'

print(f'I am not a {submarine}. I travel underwater like a fish.')

print(f'I am not a {subroutine}. I get sent to call parts of program code.')

print(f'We All Live In A Yellow {subroutine}, not A Yellow {submarine}. A Yellow {submarine}.')

print(f'But the {submarine} and the {subroutine} both love "Poutine" and so does {programmer}.')
'''----------------------------------------------------------------'''
# The new 'f' format makes it much easier to
# concatenate strings together, without the
# worry of invoking commas ',' and '+' signs
# to concatenate strings; meaning mixed
# strings, text values and integer values
# together.

# Well, that's it! That's all for today...
