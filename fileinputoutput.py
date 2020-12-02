
'''
my_file = open(r'test.txt')

# seek is used to return the curser to the start of the file, otherwise the next two print statements would return blank.
my_file.seek(0)  # 0 is the first curser index in the file
print(my_file.read())
my_file.seek(6)
print(my_file.read())
my_file.seek(0)


print(my_file.readline()) # returns one line
print(my_file.readlines()) # returns all lines

my_file.close() # you must close the file!
'''

# r+ means read and write, a is append, w is write. w will write over.
# write will create a new file if it does not exist.

try:
    with open('sad.txt', mode='w') as my_file:
        print('write something and press enter twice')
        text = my_file.write(input())
        print(f'{text} characters were added to {my_file}')
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO error')
    raise err

# python fileinputoutput.py
