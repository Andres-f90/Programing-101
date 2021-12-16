# Programming 101 with Python

- [Programming 101 with Python](#programming-101-with-python)
  - [Installing Python](#installing-python)
    - [Environments](#environments)
    - [Creating environments with Anaconda](#creating-environments-with-anaconda)
    - [Installing Packages](#installing-packages)
  - [Running a Python Script](#running-a-python-script)
    - [IDLE](#idle)
    - [Visual Studio Code (VSCode)](#visual-studio-code-vscode)
    - [Jupyter Notebooks](#jupyter-notebooks)
  - [First Steps](#first-steps)
    - [Print Statement](#print-statement)
    - [Type Function](#type-function)
    - [User Inputs](#user-inputs)
  - [Variables](#variables)
    - [Variables vs. Values](#variables-vs-values)
    - [Integers](#integers)
    - [Strings](#strings)
      - [F-Strings](#f-strings)
      - [Change](#change)
    - [Boolean](#boolean)
    - [Float](#float)
  - [Complex Types of Variables](#complex-types-of-variables)
    - [Arrays](#arrays)
    - [String](#string)
    - [Tuples](#tuples)
    - [Dictionaries (Or sometimes Hash Tables)](#dictionaries-or-sometimes-hash-tables)
  - [Functions](#functions)
  - [Expressions](#expressions)
    - [Arguments](#arguments)
  - [Conditionals](#conditionals)
    - [`if` statement](#if-statement)
  - [Loops](#loops)
    - [`for` loops](#for-loops)
    - [`while` loops](#while-loops)
  - [Documentation](#documentation)
  - [Additional questions](#additional-questions)

## Installing Python

Go to [this LINK](https://www.python.org/) and in the 'Downloads' section you'll find the download button. Follow the installer instructions.

### Environments

When are environments used: Different projects, each with it's own dependencies.

What do they do: They have the packages needed for each project and you can jump between them with ease. Each environment can have a different python version.

> **Anaconda:** Is a distribution for Python and R programming languages that helps (among other things) to manage environments. Using the Anaconda Navigator, you can create and delete environments with just clicks, choosing the python version you desire. You can also edit it's packages, installing, updating and deleting them.

### Creating environments with Anaconda

There are two ways to manage environments with Anaconda:

1. Using Anaconda Navigator: You can follow the instructions in the [Official Anaconda Documentation](https://docs.anaconda.org/anaconda/navigator/tutorials/manage-environments/).
2. Using CMD (Command Prompt): To manage environments with terminal (or CMD), read the [Conda Documentation](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?highlight=environments).

### Installing Packages

Now that you created an environment, it's time to prepare for the coding session. The next thing you wanna do is install the packages you need. For that, you can also use:

1. Anaconda Navigator: This is the [Official Conda Guide](https://docs.anaconda.org/anaconda/navigator/tutorials/manage-packages/) to manage packages.
2. CMD: This is the [Official Conda Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html) to manage packages with `conda`.

## Running a Python Script

### IDLE

djkldjd

### Visual Studio Code (VSCode)

hjdkd

### Jupyter Notebooks

[getting started with anaconda](https://anaconda.cloud/tutorials/getting-started-with-anaconda-individual-edition%3Fsource%3Dosx_installer)

## First Steps

### Print Statement

The `print()` function shows any object (even a function as we will see in the next section) inside the parenthesis in terminal when the file is executed. You can put variables inside the parenthesis, as well as values directly. For example:

>  Python code:
>
> ```python
> print('Hello World!')
> my_variable = 55
> print(my_variable)
> ```
>
> Terminal Response:
>
> ```
> Hello World!
> 55
> ```

### Type Function

The `type()` function is used to display the data type of a value or a variable. You put the desired object inside the parenthesis and it will show the type in the terminal.

>  Python code:
>
>  ```python
>  print(type('Hello World!'))
>  my_variable = 55
>  print(type(my_variable))
>  ```
>
>  Terminal Response:
>
>  ```
>  <class 'str'>
>  <class 'int'>
>  ```

### User Inputs

​		Get data of the users
​    input(). It allows us to ask for the user to give us a data
​    <var> = input(<message: >)
​    input always returns/give us strings
​    int 'hugging' with parenthesis will change it for int

example: int (input()):

## Variables

### Variables vs. Values

> - "Value" is the actual data or instructions stored in computer. Think of it in terms of math: A value is just a thing that never changes, like the number 42, the letter 'H', or the sequence of letters that constitutes "Hello World!".
>
> - "Variable" is a way for locating the data, a value-replacing reference, but not itself the set of data or instruction stored in the computer. Is just a name that stands for a value in a certain scope of the program. Every time a variable is evaluated, its value needs to be looked up in an *environment*.
>
> – As found in [Stackoverflow](https://stackoverflow.com/questions/25494791/checking-understanding-of-variable-v-s-value-and-function-vs-abstracti)

### Integers

**Definition:** A kind of variable containing a number not decimal

first we name the varible, then we assign the number we want

### Strings
**Definition:** Is a sequence of characters that are in quotes, the different quotes can't be merged
 examples: "hello" - 'hello'
    

first  we need to name the variable, with quotation marks always,  next we write what we want

#### F-Strings
An F-String is defined with the letter `f` and single quotation marks. If we want to input some code inside the String, we can use `{}`. This kind of strings is specially useful to get variables inside the String with ease.

*Example:* `f'This is a String. 5+5={5+5}` is gonna represent `This is a String. 5+5=10`.

> Strings are gonna be seen again later, because they are a complex kind of variable.

####  Change
to change s

### Boolean
**Definition:** the variable Boolean just have two options to assign (false, true)

>  Booleans are gonna be later used in conditionals and loops.

### Float

**Definition:** This is for having a decimal number "the number with a Dot it's called float beacuse it have a comma floating in the number

*Example:*  4.4

## Complex Types of Variables

### Arrays

**Definition:** This variable is used to have inside more variales even it self

*Example:*  v_list = [4.4, 16, v_list2=['hello'], false]

Lists start indexing from number 0.

Indexation

can access to this index with
    <str>[<index>]
 slicing (for strings)
    <string>[index for start slicing , index for finish slicing]
    python[1:4] we  stop in the next index we want to stop
    <python>[start : end : jump]
   **example:** <python>[1:6:2]

- `len(list)`: Returns the length of the list.

    It's a data structure that storage many values on sequence
    (used for lists)
    index begins from zero, can have any type of data
    mutable = can be modified
    Access an element of the list
        <list>[index]
    Add an element
        ~<list>.append(<elem>)
        ~<list>.insert(<index>,<elem>)
    Remover un elemento
        <list>.remove(<elem>)
    Find an element in the list
        <elem> in <list>
    .index(<elem>)para el indice
        <list>.index(<elem>)
    Change an  element
        <list>[<índex>] = <new_value>
    Methodology of the list
        mutual operations of the lists
        <list>.<method>(<parameters>)
        .count(<elem>)
    
    ​    .extend(<list>)
    
    ​    .pop()
    
    ​    .reverse()
    
    ​    .sort()

### String

Strings are basically lists, and as so, they have all the previously seen properties (indexation and slicing).

In addition to those, `Strings` have special methods than can be used following the next example: <cadena>.<method>(<values>)

 Some of the special String methods are:

- `my_string.capitalize()`: The method capitalize djsh
- `my_string.find(to_find)`: This method finds if the value of `to_find` is inside `my_string`
- .isdigit
- .index
- .islower
- isalnum
- .isupper
- .isalpha
- .lower
- .isdecimal
- .upper

> If it begins with "is" probably would be True/False

### Tuples

data structure no mutable  with ordered sequence of elements

b = (1,2,3,4)

counted elements with index

find an element:

    <elem> in <tuple>
    <tuple>.index(<elem>)
    <tuple>.count(<elem>)

### Dictionaries (Or sometimes Hash Tables)

Collection of pair key-value

{'A':45 , 'B':30}

A (key)  45 (value)

with the comma we separate the key-value

the key must be unique

~Access a value:

```python
 <diccionary>[<key>]
 <diccionary>.get(<key>)
```

~Add and modify :

   <diccionary>[<key>] = <new_value>
    (will create a new pair if exists a new key, but if already exists will update the key) 

~Remove

​    del <dicc>[<key>]

~Check if exist

    <elem(key)> in <dicc>

## Functions

Function: name assigned to a process o sequence of specified instructions

variables rules
    only can begging with an letter  like a or A
    only alphanumerical and _

## Expressions

​    merge of values, variables, operators,  resulting in a value

1. Logical operators:

   uses Booleans  

   'and' evaluate from left to right  if are True both operators have to be True

   'or' only if both operators are False will be False

   'not' will change True to False - False for True

   their priority is : not, and, or

2. Relational operators:

   they compare values and return Booleans

   < 	>=

   <	<=

   ==  (equal to)	!= (not equal to)

   can be used with strings

3. Assign operators:

   assign values to variables

   =	+= (add and update value)

   -= (minus and update value)	*=

   /=	**=

   //=	%=

4. Arithmetic operators:

   +,-,*,/,// _floor dision, ** _exponent,% module

   PEMDAS

   -parenthesis

   -exponent

   -multiplication

   -division

   -add

   -minus

### Arguments

## Conditionals

are conditional sentences 
    instruction or group de instructions that the execute is up to a Boolean

### `if` statement

## Loops

### `for` loops

Design to loop through a collection or an iterable object.

it let execute one  or more code lines several times

control structure

for-cycle used for the times we know how many times will  execute repeating the instruction

iteration = reapeat cycle

for <var> in range(<start>,<end>):
    #code

~control variable

descriptive names

updated automatically

    range(start, stop][, step])
    range(start, stop)
    range(stop)
    .
    for <var> in <iterable>:
        #codigo
    for <var> in [<list>]:
        #code
    for <key> in <diccionary>
    for <key> in <diccionary>.values()
    for <keys>,<value> in <diccionary>.items()

### `while` loops



## Documentation

Documentation to find important things for Python such as built-in functions
    -python.org
    -documentation
    -python docs
    -menu para español y su versión
    funciones built-in

##  Additional questions

what happens if we put the variable down?
how to put ' not puting a letter??

