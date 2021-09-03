# conditionals
x = int(input("Please enter positive integer: "))
if x < 0:
    x = 0
    print("negative integer changed to zero")
elif x == 0:
    print("zero")
elif x == 1:
    print("single")
else:
    print("multiple")

# and inline conditionals
a = input("a: ")
b = input("b: ")
x = "Smaller" if a < b else "Bigger"
print("a is {} than b!".format(x))
