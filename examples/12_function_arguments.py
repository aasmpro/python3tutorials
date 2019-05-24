def print_arguments(arg, *args, **kwargs):
    print("arg = ", arg)
    print("args = ", args)
    print("kwargs = ", kwargs)


print_arguments(1, 2, 3, 4, name="Abolfazl", family="Amiri")
