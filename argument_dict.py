from collections import defaultdict

class ArgumentativeDict(defaultdict):
	"""
		A form of defaultdict for which the default takes the key as input.

		Use Cases Are:

		To implement a cached recursive function:

		fib_dict = ArgumentativeDict(
			lambda x: 1 if x< 2 else fib_dict[x-1] + fib_dict[x-2]
		)
		or locally cached:
		def fib(x):
			def i_fib(x):
					return cache[x-1] + cache[x-2]
			cache = ArgumentativeDict(i_fib)
			cache[0] = cache[1] = 1
			return cache[x]
	"""

	def __missing__(self, key):
		if self.default_factory is None:
			raise KeyError(key)
		self[key] = value = self.default_factory(key)
		return value

	def __repr__(self):
		return "<ArgumentativeDict(%s.%s)>: %r" % (self.default_factory.__module__, self.default_factory.__name__, self.__dict__)
