
Often in python you want an object to hold data which is lighter weight than a class, but with more structure than a dictionary.

A common way to do this is via collections.namedtuple:

`Dimensions = namedtuple('Dimensions', 'length, width, depth')`

This works acceptably in most cases, but is actually significantly slower than using a class (or using a dictionary) for many use cases.  In particular, namedtuple is based on tuple, and is efficient for lookup by index.

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

```
def record(name, slots):
	def __init__(self, 
	return type(name, object, {'__slots__':slots})
```
