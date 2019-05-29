## Modules
A __module__ is a __file__ consisting of Python code that can define
__functions__, __classes__ and __variables__.

You can use __any Python source file as a module__ by executing an
import statement.
```python
import datetime
```
Python's `from` statement lets you import __specific attributes__ from
a module into the current __namespace__.
```python
from datetime import datetime, timezone
from json.encoder import JSONEncoder
```
`import *` statement can be used to import __all names__ from a module
into the current __namespace__.
```
from datetime import *
```
