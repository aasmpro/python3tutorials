Python files have `.py` extension.

**Indentation** is used in Python to delimit blocks. The number of
spaces is variable, but all statements within **the same block**
must be **indented the same amount**.

The header line for compound statements, such as `if`, `while`,
`def`, and `class` should be terminated with a colon ( `:` ).

The **semicolon** ( `;` ) is optional at the end of statement, but it
is **preferred to not using it**.
```python
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
  print("False") # Error! Not using same indention.
```
**Printing** to the Screen
```python
print("Hello World!")
```
Reading Keyboard **Input**
```python
name = input("Enter your name: ")
```
**Comments**
```python
# one line comment in python!
"""
Multi line comments in in python,
Is like this!
"""
```
Python is **dynamically typed**. You do not need to declare
variables!

The **declaration happens automatically** when you assign a value to
a variable.

**Variables can change type**, simply by assigning them a new value
of a different type.
```python
counter = 1000
miles = 1000.0
name = "Abolfazl"
x = None
x = 2
x = "string"
```
Python allows you to assign a **single value to several variables**
simultaneously, and also allows to assign **multiple values to
multiple variables** too.
```python
a = b = c = 3
x, y, z = 1, 2, "string"
```
