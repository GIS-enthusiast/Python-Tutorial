
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper


def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

#my_list = make_list(100)
# print(my_list)


@performance
def generator_function(num):
    for i in range(num):
        yield i * 2

#g = generator_function(100)
# print(next(g)) # If you exceed the next yield you recieve a stop iteration error.


@performance
def long_time():
    print('1')
    for i in range(1000000):
        i*5


@performance
def long_time2():
    print('2')
    for i in list(range(1000000)):
        i*5

# long_time()
# long_time2()

# The below is essentially under the hood in a for loop.


def special_forloop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator)*2)
        except StopIteration:
            break

# special_forloop([1,2,3])

# The class MyGen mimics what range does under the hood.


class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):  # __iter__ built into python
        return self

    def __next__(self):  # __next__ built into python
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 100)
# for i in gen:
#    print(i)


@performance
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = b + temp


@performance
def fib2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = b + temp
    return result


for x in fib(1000):
    print(x)

print(fib2(1000))
