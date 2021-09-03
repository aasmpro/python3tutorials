A list in Python is an **ordered** group of items or elements, and
these list elements don't have to be of the same type. Lists are
**mutable** objects that can change their values.

List indexes like strings starting at `0` in the **beginning of
list** and working their way from `-1` at the **end**.

Similar to strings, Lists operations include slicing (`[]` and
`[:]`), concatenation (`+`), repetition (`*`), and membership (`in`).

**access**, **update** and **delete** list elements is like:
```python
>>> list1 = ['programming', 'python', 1996, 2019, 0.5]
>>> print(list1[0])
programming
>>> print(list1[1:4])
['python', 1996, 2019]
>>> list1[2] = 2000
>>> print(list1[2])
2000
>>> del(list1[4])
>>> print(list1)
['programming', 'python', 2000, 2019]
```

Lists can have sub-lists as elements and these sub-lists may
contain other sub-lists as well.
```python
>>> persons = [["Abolfazl", 1996], ["Sarah", 1997]]
>>> name = persons[0][0]
>>> birth = persons[0][1]
>>> print("{} was born on {}".format(name, birth))
Abolfazl was born on 1996
```

Common List Functions

| Function            | Description                                        |
| ------------------- | -------------------------------------------------- |
| `cmp(list1, list2)` | **Compares** elements of both lists.               |
| `len(list)`         | Gives the total **length** of the list.            |
| `max(list)`         | Returns **item** from the list with **max value**. |
| `min(list)`         | Returns **item** from the list with **min value**. |
| `list(tuple)`       | Returns **item** from the list with **min value**. |

List **Comprehensions** consists of an **expression** followed by a for
**clause**.

Common List Methods


| Method                    | Description                                            |
| ------------------------- | ------------------------------------------------------ |
| `list.append(obj)`        | **Appends** object obj to list                         |
| `list.insert(index, obj)` | **Inserts** object obj into list **at offset index**   |
| `list.count(obj)`         | Returns **count** of how many times obj occurs in list |
| `list.index(obj)`         | Returns the **lowest index** in list that obj appears  |
| `list.remove(obj)`        | **Removes** object obj from list                       |
| `list.reverse()`          | **Reverses** objects of list in place                  |
| `list.sort()`             | **Sorts** objects of list in place                     |
