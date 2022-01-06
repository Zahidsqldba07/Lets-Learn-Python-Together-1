'''----------------------------------------------------------------'''
# Let's create our first 'def()' function with a 'print()'
# function inside it, then call up our first 'def()' function,
# 'my_first_function()' to display the screen output.

def my_first_function():
    print('My first function.')

# call up 'my_first_function()'

my_first_function()
'''----------------------------------------------------------------'''
# Let's create our second 'def()' function with a
# 'print()' function inside it along with the variable
# 'software', then call up our second 'def()' function,
# 'my_second_function()' to display the screen
# output.

def my_second_function(software):
    print('My second function with',software)

# call up 'my_second_function()' along with its
# argument value 'Python 3'

my_second_function('Python 3')
'''----------------------------------------------------------------'''
# Let's create our third 'def()' function with a
# 'print()' function inside it along with the variables
# 'software' and 'program', then call up our third
# 'def()' function, 'my_third_function()' to display
# the screen output.

def my_third_function(software,program):
    print('My third function with',program)

# call up 'my_third_function()' along with its two
# argument values 'Python 3' and 'python'

my_third_function('Python 3','Python')
'''----------------------------------------------------------------'''
# Let's create our fourth 'def()' function with a
# 'print()' function inside it along with the variables
# 'software', 'program' and 'programmer', then
# call up our fourth 'def()' function, 'my_fourth_function()'
# to display the screen output.

def my_fourth_function(software,program,programmer):
    print('My fourth function with',programmer)

# call up 'my_fourth_function()' along with its
# three argument values 'Python 3', 'python' and
# 'Joseph'

my_fourth_function('Python 3','Python','Joseph')
'''----------------------------------------------------------------'''
# Let's create our fifth 'def()' function witha for-
# loop and a 'print()' function inside it, then call
# up our fifth 'def()' function, 'my_fifth_function()'
# to display the screen output.

def my_fifth_function():
    for i in range(3):
        print('loop',i,'times inside my_fifth_function.')
        
# call up 'my_fifth_function()'

my_fifth_function()
'''----------------------------------------------------------------'''
# Let's create our sixth 'def()' function with a for-
# loop and a 'print()' function inside it along with
# the variable 'software', then call up our sixth
# 'def()' function, 'my_sixth_function()' to display
# the screen output.

def my_sixth_function(software):
    for i in range(3):
        print('loop',i,'times inside my_sixth_function.',software)

# call up 'my_sixth_function()' along with its
# argument value 'Python 3'

my_sixth_function('Python 3')
'''----------------------------------------------------------------'''
# Let's create our seventh 'def()' function with
# a for-loop and a 'print()' function inside it along
# with the variables 'software' and 'program',
# then call up our seventh 'def()' function,
# 'my_seventh_function()' to display the screen
# output.

def my_seventh_function(software,program):
    for i in range(3):
        print('loop',i,'times inside my_seventh_function.',program)

# call up 'my_seventh_function()' along with its
# argument values 'Python 3' and 'Python'

my_seventh_function('Python 3','Python')
'''----------------------------------------------------------------'''
# Let's create our eighth 'def()' function with a
# for-loop and a 'print()' function inside it along
# with the variables 'software', 'program' and
# 'programmer', then call up our eighth 'def()'
# function, 'my_eighth_function()' to display
# the screen output.

def my_eighth_function(software,program,programmer):
    for i in range(3):
        print('loop',i,'times inside my_eighth_function.',programmer)

# call up 'my_eighth_function()' along with its
# argument values 'Python 3', 'Python' and 'Python'

my_eighth_function('Python 3','Python','Joseph')
'''----------------------------------------------------------------'''
# Let's create our ninth 'def()' function that returns
# a value, then call up our ninth 'def()' function,
# 'my_ninth_function()' to display the screen output.

def my_ninth_function(software):
    return software

# call up 'my_ninth_function()' along with its
# argument value 'Python 3'

print(my_ninth_function('Python 3'))
'''----------------------------------------------------------------'''
# Let's create our tenth 'def()' function that returns
# one of two values, then call up our tenth 'def()'
# function, 'my_tenth_function()' to display the
# screen output.

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
# overrides all its return values, then call up our
# twelfth 'def()' function, 'my_twelfth_function()'
# to display the screen output.

def my_twelfth_function(software,program,programmer):
    return 'Overrides all the values.'

# call up 'my_twelfth_function()' along with its
# argument values 'Python 3', 'Python' and 'Joseph'

print(my_twelfth_function('Python 3','Python','Joseph'))
'''----------------------------------------------------------------'''
# Let's create our thirteenth 'def()' function that
# overrides two of its return values, then call up
# our thirteenth 'def()' function, 'my_thirteenth_function()'
# to display the screen output.

def my_thirteenth_function(software,program,programmer):
    return 'Override this value. '+program+'Override that value.'

# call up 'my_thirteenth_function()' along with its
# argument values 'Python 3', 'Python' and 'Joseph'

print(my_thirteenth_function('Python 3 ','Python ','Joseph'))
'''----------------------------------------------------------------'''
# Let's create our fourteenth 'def()' function that
# returns three values, then call up our fourteenth
# 'def()' function, 'my_fourteenth_function()' to
# display the screen output.

def my_fourteenth_function(software,program,programmer):
    return software+program+programmer

# call up 'my_fourteenth_function()' along with
# its argument values 'Python 3', 'Python' and
# 'Joseph'

print(my_fourteenth_function('Python 3 ','Python ','Joseph'))
'''----------------------------------------------------------------'''
# Let's create our fifteenth 'def()' function that
# uses both the variable 'software' and its value
# 'Python 3', then call up our fifteenth 'def()'
# function, 'my_fifteenth_function()' to display
# the screen output.

def my_fifteenth_function(software='Python 3'):

    print('My fifteenth function with',software+'.')

# also use string concatenation in these ways:

    print('My fifteenth function with '+software+'.')

    print('My fifteenth function with {}.'.format(software)) # old format is depreciated but can still be used

    print(f'My fifteenth function with {software}.') # new 'f' string format is most popular in Python 3 and up

my_fifteenth_function()
'''----------------------------------------------------------------'''
# Let's create our sixeenth 'def()' function that
# uses all three variables and their values 'Python 3',
# 'Python', and 'Joseph', then call up our sixteenth
# 'def()' function, 'my_sixteenth_function()' to
# display the screen output.

def my_sixteenth_function(software='Python 3',program='Python',programmer='Joseph'):

    print('My sixteenth function with',software,'and computer programmer:',programmer,'teaches me',program+'.')

# also use string concatenation in these ways:

    print('My sixteenth function with '+software+' and computer programmer: '+programmer+' teaches me '+program+'.')

    print('My sixteenth function with {} and computer programmer: {} teaches me {}.'.format(software,programmer,program))

    print(f'My sixteenth function with {software} and computer programmer: {programmer} teaches me {program}.')

my_sixteenth_function()
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
# that returns two number values, then call up
# our arithmetic 'def()' function, 'arithmetic(num)'
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
# function, 'arithmetic(num)' to display the screen
# output.

def arithmetic(a=(0,1,2,3,4,5,6,7,8,9)):
    return f'The values in variable "a" add/sum up to {sum(a)}.'

print(arithmetic())
'''----------------------------------------------------------------'''
# Let's create a mathematical 'def()' function
# that returns the 'sum' of two sets of values
# from 0 to 9 and 10 to 19, then call up our arithmetic
# 'def()' function, 'arithmetic(num)' to display
# the screen output.

def arithmetic(
    a=(0,1,2,3,4,5,6,7,8,9),
    b=(10,11,12,13,14,15,16,17,18,19)):
    return f'The sum of "a"={sum(a)} and the sum of "b"={sum(b)}.'

print(arithmetic())
'''----------------------------------------------------------------'''
# Let's create a mathematical 'def()' function
# that returns the 'sum' of three sets of values
# from 0 to 9, 10 to 19 and 20 to 21, then call up
# our arithmetic 'def()' function, 'arithmetic(num)'
# to display the screen output.

def arithmetic(
    a=(0,1,2,3,4,5,6,7,8,9),
    b=(10,11,12,13,14,15,16,17,18,19),
    c=(20,21,22,23,24,25,26,27,28,29)):
    return f'The sum of "a"={sum(a)}, the sum of "b"={sum(b)} and the sume of "c"={sum(c)}.'

print(arithmetic())
'''----------------------------------------------------------------'''

