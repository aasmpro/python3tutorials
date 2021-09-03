# these are all strings
str1 = 'str1'
str2 = '''str2'''
str3 = "str3"
str4 = """str4"""
print(type(str1), type(str2), type(str3), type(str4))

# strings formatting
num = 6
string = "I have {} books!".format(6)
print(string)

# strings are immutable
str1 = "strings are immutable!"
str1[0] = "S"
