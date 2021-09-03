Python **Functions** syntax is like:
```python
def person_data(name, age, current_year=2019):
    """function doc string, this function return year of birth"""
    born_on = current_year - age
    return "{} born on {}".format(name, born_on)
```
In this function `name` and `age` are **Required-Arguments** and
`current_year` is **Optional-Argument** with **default** value.
this function can be called like:
```python
person_data("Abolfazl", 24, 2020) # name, age and current_year are given
person_data("Abolfazl", 23) # current_year keep it’s default value 2019
person_data(age=23, name="Abolfazl") # name and age are given as keywords
```
Also arguments can be sent like **tuples** or **dictionaries** too:
```python
def print_arguments(arg, *args, **kwargs):
    print("arg = ", arg)
    print("args = ", args)
    print("kwargs = ", kwargs)
print_arguments(1, 2, 3, 4, name="Abolfazl", family="Amiri")
```
The output would be:
```
arg = 1
args = (2, 3, 4)
kwargs = {'name': 'Abolfazl', 'family': 'Amiri'}
```
