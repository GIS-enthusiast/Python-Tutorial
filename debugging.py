

# linting, pylint etc, highlighting on text to show mistakes.
# use IDEs like pycharm
# learn to read errors
# pdb, the python debugger


import pdb


def add(num1, num2):
    pdb.set_trace()
    t = 4*5
    return num1 + num2


add(4, 'SDfasg')
