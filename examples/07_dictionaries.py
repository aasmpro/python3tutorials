dict1 = {'Name': 'Abolfazl', 'Age': 23, 'Major': 'CSE'}

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
