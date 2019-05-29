## Basic Syntax
__Python__ files have `.py` extension.

__Indentation__ is used in Python to delimit blocks. The number of
spaces is variable, but all statements within __the same block__
must be __indented the same amount__.

The header line for compound statements, such as `if`, `while`,
`def`, and `class` should be terminated with a colon ( `:` ).

The __semicolon__ ( `;` ) is optional at the end of statement, but it
is __preferred to not using it__.
```python
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
  print("False") # Error! Not using same indention.
```
__Printing__ to the Screen
```python
print("Hello World!")
```
Reading Keyboard __Input__
```python
name = input("Enter your name: ")
```
__Comments__
```python
# one line comment in python!
"""
Multi line comments in in python,
Is like this!
"""
```
Python is __dynamically typed__. You do not need to declare
variables!

The __declaration happens automatically__ when you assign a value to
a variable.

__Variables can change type__, simply by assigning them a new value
of a different type.
```python
counter = 1000
miles = 1000.0
name = "Abolfazl"
x = None
x = 2
x = "string"
```
Python allows you to assign a __single value to several variables__
simultaneously, and also allows to assign __multiple values to
multiple variables__ too.
```python
a = b = c = 3
x, y, z = 1, 2, "string"
```
