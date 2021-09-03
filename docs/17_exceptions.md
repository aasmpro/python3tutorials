In Python all **exceptions** are sub-classes of `Exception` class.

Trying to open a file that does not exist:
```python
try:
    file = open('example2.txt', 'r')
    print('file content >>', file.read())
    file.close()
except NameError:
    print('NameError raised!')
except Exception as e:
    print(e)
finally:
    print('this will be printed anyway!')
```
Output:
```
[Errno 2] No such file or directory: 'example2.txt'
this will be printed anyway!
```
