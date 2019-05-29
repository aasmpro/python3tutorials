## Conditionals
In Python, `True` and `False` are Boolean objects of class `'bool'` and
they are __immutable__.

Python assumes any __non-zero__ and __non-null__ values as `True`,
otherwise it is `False` value.

Python does not provide __switch/case__ statements as in other
languages.

Example of Python `if` statement:
```python
x = int(input("Please enter positive integer: "))
if x < 0:
    x = 0
    print("negative integer changed to zero")
elif x == 0:
    print("zero")
elif x == 1:
    print("single")
else:
    print("multiple")
```

Inline conditional expression:
```python
a, b = 10, 12
x = "Smaller" if a < b else "Bigger"
```
