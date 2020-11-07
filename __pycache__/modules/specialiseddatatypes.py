from array import array
import datetime
from collections import Counter, defaultdict, OrderedDict

#li = [num for num in range(1, 8)]
li = [1, 2, 3, 4, 5, 6, 7, 7]
sentence = 'blah blah blah thinking about python'
print(Counter(li))  # Retruns a dict where value is the count of list contents.
print(Counter(sentence))

# if int was used it would return 0, as int alone = 0
dict = defaultdict(lambda: 'key does not exist', {'a': 1, 'b': 2})
print(dict['c'])  # Returns 'key does not exist' instead of key error.


d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 2
d2['b'] = 1

# Returns False, but normal dictionaries would be True in Python older than 3.6!
print(d2 == d)
print(d2 is d)  # Returns False of course.


print(datetime.time(5, 45, 2))
print(datetime.date.today())


arr = array('i', [1, 2, 3])
print(arr[0])  # This uses much less memory!
