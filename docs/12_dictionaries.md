Python dictionaries are kind of **hash table** type which consist of
**key-value** pairs of **unordered** elements.

- **Keys**: must be immutable data types ,usually numbers or
strings.
- **Values**: can be any arbitrary Python object.

Python Dictionaries are **mutable** objects that can change their
values.

A dictionary is enclosed by **curly braces** (`{}`), the items are
separated by **commas**, and each key is separated from its value by
a **colon** (`:`).

Dictionary’s values can be **assigned** and **accessed** using **square
braces** (`[]`) with a key to obtain its value.

Simple script to show dictionary usage:
```python
dict1 = {'Name': 'Abolfazl', 'Age':23, 'Major': 'CSE'}

# Access dictionary data
print('name: ', dict1['Name'])
print('age: ', dict1['Age'])
print(dict1.keys())
print(dict1.values())
print(dict1.items())

# Update dictionary data
dict1['Age'] = 24
dict1['University'] = 'SBUK'
print('new age: ', dict1['Age'])
print('university: ', dict1['University'])

# Delete dictionary data
del dict1['Name']
print(dict1)
dict1.clear()
print(dict1)
```

Output:
```
name: Abolfazl
age: 23
dict_keys(['Name', 'Age', 'Major'])
dict_values(['Abolfazl', 23, 'CSE'])
dict_items([('Name', 'Abolfazl'), ('Age', 23), ('Major', 'CSE')])
new age: 24
university: SBUK
{'Age': 24, 'Major': 'CSE', 'University': 'SBUK'}
{}
```
Common Dictionary Methods

|Method|Description|
|--------|-----------|
|`dict.keys()`|Returns list of **dict's keys**|
|`dict.values()`|Returns list of **dict's values**|
|`dict.items()`|Returns a list of **dict's (key, value)** tuple pairs|
|`dict.get(key, default=None)`|For **key**, returns **value** or **default** if key not in dict|
|`dict.has_key(key)`|Returns `True` if **key in dict**, `False` otherwise|
|`dict.update(dict2)`|**Adds** dict2's key-values pairs to dict|
|`dict.clear()`|**Removes** all elements of dict|

Common Dictionary Functions

|Function|Description|
|--------|-----------|
|`cmp(dict1, dict2)`|**Compares** elements of both dict.|
|`len(dict)`|Gives the **total number** of **(key, value)** pairs in the dictionary.|