## Lists
A list in Python is an __ordered__ group of items or elements, and
these list elements don't have to be of the same type. Lists are
__mutable__ objects that can change their values.

List indexes like strings starting at `0` in the __beginning of
list__ and working their way from `-1` at the __end__.

Similar to strings, Lists operations include slicing (`[]` and
`[:]`), concatenation (`+`), repetition (`*`), and membership (`in`).

__access__, __update__ and __delete__ list elements is like:
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

|Function|Description|
|--------|-----------|
|`cmp(list1, list2)`|__Compares__ elements of both lists.|
|`len(list)`|Gives the total __length__ of the list.|
|`max(list)`|Returns __item__ from the list with __max value__.|
|`min(list)`|Returns __item__ from the list with __min value__.|
|`list(tuple)`|Returns __item__ from the list with __min value__.|

List __Comprehensions__ consists of an __expression__ followed by a for
__clause__.

Common List Methods


|Method|Description|
|--------|-----------|
|`list.append(obj)`|__Appends__ object obj to list|
|`list.insert(index, obj)`|__Inserts__ object obj into list __at offset index__|
|`list.count(obj)`|Returns __count__ of how many times obj occurs in list|
|`list.index(obj)`|Returns the __lowest index__ in list that obj appears|
|`list.remove(obj)`|__Removes__ object obj from list|
|`list.reverse()`|__Reverses__ objects of list in place|
|`list.sort()`|__Sorts__ objects of list in place|
