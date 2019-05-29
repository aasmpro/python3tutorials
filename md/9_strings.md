## Strings
Python Strings are __Immutable__ objects that cannot change their
values.

```python
>>> str1 = "strings are immutable!"
>>> str1[0] = "S"
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

You can update an existing string by __(re)assigning a variable__ to
another string.

__Python does not support a character type__; these are treated as
strings of length one.

Python accepts single (`'`), double (`"`) and triple (`'''` or `"""`)
quotes to denote string literals.

```python
str1 = 'str1' 
str2 = '''str2''' 
str3 = "str3"
str4 = """str4""" 
```

String indexes starting at `0` in the __beginning of the string__ and
working their way from `-1` at the __end of string__.

```
positive indexes    >>      | 0 | 1 | 2 | 3 | 4 |
string is 'HELLO'   >>      | H | E | L | L | O |
negative indexes    >>      |-5 |-4 |-3 |-2 |-1 |
```

String formatting

```python
>>> num = 6
>>> string = "I have {} books!".format(num)
>>> print(string)
I have 6 books!
```

Common String Operators, Assume: `a='Hello'` and `b='Python'`

|Operator|Description|Example|
|--------|-----------|-------|
|`+`     |__Concatenation__ - Adds values on either side of the operator|`a+b >>> HelloPython`|
|`*`     |__Repetition__ - Creates new strings, concatenating multiple copies of the same string|`a*2 >>> HelloHello`|
|`[]`    |__Slice__ - Gives the character from the given index|```a[1] >>> e``` ``` a[-1] >>> o```|
|`[:]`   |__Range Slice__ - Gives the characters from the given range|`a[1:4] >>> ell`|
|`in`    |__Membership__ - Returns true if a character exists in the given string|`'H' in a >>> True`|

Common String Methods

|Method|Description|
|--------|-----------|
|`str.count(sub, beg=0, end=len(str))`|__Counts__ how many times sub occurs in string or in a substring of string if starting index beg and ending index end are given.|
|`str.isalpha()`|Returns `True` if string has at least 1 character and all characters are alphanumeric and `False` otherwise.|
|`str.isdigit()`|Returns `True` if string contains only digits and `False` otherwise.|
|`str.lower()`|Converts letters in string to __lowercase__.|
|`str.upper()`|Converts letters in string to __uppercase__.|
|`str.replace(old, new)`|__Replaces__ all occurrences of __old__ in string with __new__.|
|`str.split(str=' ')`|__Splits__ string according to delimiter `str` (space if not provided) and returns __list of substrings__.|
|`str.strip()`|__Removes__ all leading and trailing __white spaces__ of string.|
|`str.title()`|Returns __"titlecased"__ version of string.|

Common String Functions

|Function|Description|
|--------|-----------|
|`str(x)`|To convert `x` to an __String__|
|`len(x)`|Gives the total __length__ of the string|
