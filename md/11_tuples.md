## Tuples
Python Tuples are __Immutable__ objects that cannot be changed once
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
You can __update__ an existing tuple by __(re)assigning__ a variable to
another tuple.

Tuples are __faster__ than lists and protect your data against
accidental changes to these data.

The rules for tuple indices are the same as for lists and they
have the __same operations__, __functions__ as well.

To write a tuple containing a __single value__, you have to include a
comma, even though there is only one value. e.g. `t = (3, )`
