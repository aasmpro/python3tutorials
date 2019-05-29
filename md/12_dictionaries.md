## Dictionaries
Python dictionaries are kind of __hash table__ type which consist of
__key-value__ pairs of __unordered__ elements.
- __Keys:__ must be immutable data types ,usually numbers or
strings.
- __Values:__ can be any arbitrary Python object.

Python Dictionaries are __mutable__ objects that can change their
values.

A dictionary is enclosed by __curly braces__ (`{}`), the items are
separated by __commas__, and each key is separated from its value by
a __colon__ (`:`).

Dictionary’s values can be __assigned__ and __accessed__ using __square
braces__ (`[]`) with a key to obtain its value.

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
|`dict.keys()`|Returns list of __dict's keys__|
|`dict.values()`|Returns list of __dict's values__|
|`dict.items()`|Returns a list of __dict's (key, value)__ tuple pairs|
|`dict.get(key, default=None)`|For __key__, returns __value__ or __default__ if key not in dict|
|`dict.has_key(key)`|Returns `True` if __key in dict__, `False` otherwise|
|`dict.update(dict2)`|__Adds__ dict2's key-values pairs to dict|
|`dict.clear()`|__Removes__ all elements of dict|

Common Dictionary Functions

|Function|Description|
|--------|-----------|
|`cmp(dict1, dict2)`|__Compares__ elements of both dict.|
|`len(dict)`|Gives the __total number__ of __(key, value)__ pairs in the dictionary.|