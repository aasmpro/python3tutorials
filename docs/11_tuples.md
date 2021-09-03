Python Tuples are **Immutable** objects that cannot be changed once
they have been created.
```python
>>> t = ("tuples", "are", "immutable", 1996)
>>> t[0]
'tuples'
>>> t[0] = "New Value"
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```
You can **update** an existing tuple by **(re)assigning** a variable to
another tuple.

Tuples are **faster** than lists and protect your data against
accidental changes to these data.

The rules for tuple indices are the same as for lists and they
have the **same operations**, **functions** as well.

To write a tuple containing a **single value**, you have to include a
comma, even though there is only one value. e.g. `t = (3, )`
