from collections import defaultdict

class ArgumentativeDict(defaultdict):
	"""
		A form of defaultdict for which the default takes the key as input.

		Use cases might include:

		* To use a default value based on the input key.
		* To limit default behaviour to specific types of keys.
		* To log/track access attempts for missing keys (with key information).
		* To implement a cached recursive function:

		def fib(x):
			def i_fib(x):
					return cache[x-1] + cache[x-2]
			cache = ArgumentativeDict(i_fib)
			cache[0] = cache[1] = 1
			return cache[x]

		or, if preferred:
		fib_dict = ArgumentativeDict(
			lambda x: 1 if x< 2 else fib_dict[x-1] + fib_dict[x-2]
		)
	"""

	def __missing__(self, key):
		if self.default_factory is None:
			raise KeyError(key)
		self[key] = value = self.default_factory(key)
		return value

	def __repr__(self):
		return "<ArgumentativeDict(%s.%s)>: %r" % (self.default_factory.__module__, self.default_factory.__name__, self.__dict__)
