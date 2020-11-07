from functools import reduce

def multipybytwo(item):
    return item*2

print(list(map(multipybytwo, [1,2,3])))

my_list = [1,2,3]
your_list = [10,20,30]
print(list(zip(my_list, your_list)))

def onlyodd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(list(map(lambda item: item*2, my_list)))
#print(reduce(accumulator, my_list, 0))
print(reduce(lambda acc, item: acc+item, my_list, 10))

my_list1 = [5,4,3]

#print(list(map(lambda item: item**2, my_list1)))

a = [(0,2), (4,3), (9,9), (10, -1)]
a.sort(key=lambda x: x[1]) # x is the tuple and the key will be in the second item.
print(a)

my_list2 = [num for num in filter(lambda item: item % 2 !=0, range(0, 100))]
my_list6 = [num for num in range(0, 100) if num % 2 == 0]
print(my_list6)
my_list3 = [num for num in filter(lambda item: item not in my_list, range(0, 100))]
#print(my_list3)
my_list4 = [num*2 for num in range(0, 100)]
#print(my_list4)
#print(list(map(lambda item: sorted(item)[1], a)))

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {k:v**2 for k, v in simple_dict.items() if v%2 ==0}
print(my_dict)

my_dict1 = {num:num*2 for num in [1,2,3]}
print(my_dict1)

some_list = ['a', 'b', 'b', 'h', 'f', 'n', 'n']
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)