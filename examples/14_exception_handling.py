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
