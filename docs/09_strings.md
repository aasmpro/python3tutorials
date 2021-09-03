Python Strings are **Immutable** objects that cannot change their
values.

```python
>>> str1 = "strings are immutable!"
>>> str1[0] = "S"
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

You can update an existing string by **(re)assigning a variable** to
another string.

**Python does not support a character type**; these are treated as
strings of length one.

Python accepts single (`'`), double (`"`) and triple (`'''` or `"""`)
quotes to denote string literals.

```python
str1 = 'str1' 
str2 = '''str2''' 
str3 = "str3"
str4 = """str4""" 
```

String indexes starting at `0` in the **beginning of the string** and
working their way from `-1` at the **end of string**.

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

| Operator | Description                                                                            | Example                             |
| -------- | -------------------------------------------------------------------------------------- | ----------------------------------- |
| `+`      | **Concatenation** - Adds values on either side of the operator                         | `a+b >>> HelloPython`               |
| `*`      | **Repetition** - Creates new strings, concatenating multiple copies of the same string | `a*2 >>> HelloHello`                |
| `[]`     | **Slice** - Gives the character from the given index                                   | ```a[1] >>> e``` ``` a[-1] >>> o``` |
| `[:]`    | **Range Slice** - Gives the characters from the given range                            | `a[1:4] >>> ell`                    |
| `in`     | **Membership** - Returns true if a character exists in the given string                | `'H' in a >>> True`                 |

Common String Methods

| Method                                | Description                                                                                                                      |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `str.count(sub, beg=0, end=len(str))` | **Counts** how many times sub occurs in string or in a substring of string if starting index beg and ending index end are given. |
| `str.isalpha()`                       | Returns `True` if string has at least 1 character and all characters are alphanumeric and `False` otherwise.                     |
| `str.isdigit()`                       | Returns `True` if string contains only digits and `False` otherwise.                                                             |
| `str.lower()`                         | Converts letters in string to **lowercase**.                                                                                     |
| `str.upper()`                         | Converts letters in string to **uppercase**.                                                                                     |
| `str.replace(old, new)`               | **Replaces** all occurrences of **old** in string with **new**.                                                                  |
| `str.split(str=' ')`                  | **Splits** string according to delimiter `str` (space if not provided) and returns **list of substrings**.                       |
| `str.strip()`                         | **Removes** all leading and trailing **white spaces** of string.                                                                 |
| `str.title()`                         | Returns **"titlecased"** version of string.                                                                                      |

Common String Functions

| Function | Description                              |
| -------- | ---------------------------------------- |
| `str(x)` | To convert `x` to an **String**          |
| `len(x)` | Gives the total **length** of the string |
