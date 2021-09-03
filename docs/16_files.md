Opening a file, writing some data and then printing it’s content:
```python
# use 'w' for write mode, and 'a' for append mode.
# these modes will create file if not exist
file_object = open(file='example.txt', mode='a')
file_object = open(file='example.txt', mode='w')

# writing to file
file_object.write('write this lines!\nto the file.\n')
file_object.writelines(['line 3\n', 'line 4\n', 'line 6'])

# files most be closed to save changes
file_object.close()

# use 'r' for read mode.
# this mode will raise FileNotFoundError Exception if file not exist
file_object = open(file='example.txt', mode='r')

# reading file content
print("readline  output >>", file_object.readline(), end='')
print("readlines output >>", file_object.readlines())
print("read      output >>", file_object.read(), end='')
file_object.close()
```
Output:
```
readline    output >> write this lines!
readlines   output >> ['to the file.\n', 'line 3\n', 'line 4\n', 'line 6'] 
read        output >>
```
