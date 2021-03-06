
# Implement Record:
 -- what needs to/can be specified (__doc__, __qualname__, __annotations__, ...)
 -- Is it possible to dynamically select module to call module? # free with metaclass?
 -- Setting up via type vs writing metaclass (vs subclass?)
 -- 
 Comparisons:
 -- size comparison
 -- creation/serialize/deserialize?


Often in python you want an object to hold data which is lighter weight than a class, but with more structure than a dictionary.

A common way to do this is via collections.namedtuple:

`Dimensions = namedtuple('Dimensions', 'length, width, depth')`

This works acceptably in most cases, but is actually significantly slower than using a class (or using a dictionary) for many use cases.  In particular, namedtuple is based on tuple, and is efficient for lookup by index.

This has actually been significantly improved for python3.  Here are some python2 timings:

```
danny@overdue:~/code/danpy_extras/record$ python2.7 timing_tests.py 
time for namedtuple case: 0.985s
time for class case: 0.358s
time for dict case: 0.278s
time for slot class case: 0.345s
```

And the python 3 equivalent (with the record added for good measure):
```
danny@overdue:~/code/danpy_extras/record$ python3.6 timing_tests.py 
time for namedtuple case: 0.461s
time for class case: 0.337s
time for dict case: 0.242s
time for slot class case: 0.288s
time for record_case case: 0.282s
```

As you can see, the performance is best using a dictionary, followed by slot classes/record, regular class, and finally the namedtuple, which takes almost 3 times longer than a slot class in python2.

Python offers another feature: The `__slots__` property, which can be used instead of an objects `__dict__` property for objects which have a fixed number of properties.

So, we could instead define our Dimensions object like:

```class Dimensions2(object):

	__slots__ = ['height', 'length', 'width']

	def __init__(self, height, length, width):
		self.height = height
		self.length = length
		self.width = width
```


This has 2 obvious drawbacks, the first is the additional boilerplate, which can be resolved:

This was unfinished:
```
def record(name, slots):
	def __init__(self, *slots):
	return type(name, object, {'__slots__':slots})
```

The other IIRC was the signature set-up, which is resolvable in python3, by using __signature__, along with using bind to get the appropriate failure.

```
class record(type):
	def __new__(cls, name, attributes):
		class_dict = {
			'__slots__': attributes,
			'__signature__': cls._make_signature(attributes)
			'__doc__': doc or self._default_doc(name)
		super(record, cls).__new__(cls, name, (object,), {__slots__:attributes}

def __init__(self, *args):
	self.__signature__.bind(*args)
	

