for letter in 'Python':
    print(letter, end='-')
print()  # end of 1st example
list_data = ['P', 'y', 't', 'h', 'o', 'n']
for d in list_data:
    print(d, end='*')
print()  # end of 2nd example
for index in range(len(list_data)):
    print(list_data[index], end='_')
print()  # end of 3rd example
count, string = 0, 'Python'
while count <= 5:
    print(string[count], end=' ')
    count += 1
print()  # end of 4th example
dict_data = {0: 'P', 1: 'y', 2: 't', 3: 'h', 4: 'o', 5: 'n'}
for key, value in dict_data.items():
    print(key, value, end=' | ')
