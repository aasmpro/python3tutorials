# access, update and delete list elements
list1 = ['programming', 'python', 1996, 2019, 0.5]
print(list1[0])
print(list1[1:4])
list1[2] = 2000
print(list1[2])
del (list1[4])
print(list1)

# lists with sub-lists
print()
persons = [["Abolfazl", 1996], ["Sarah", 1997]]
name = persons[0][0]
birth = persons[0][1]
print("{} was born on {}".format(name, birth))

# list comprehensions
print()
a = [1, 2, 3]
print([x ** 2 for x in a])
print([x + 1 for x in [x ** 2 for x in a]])
