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

	def __init__(self, func):
		self.func = func
		super(ArgumentativeDict, self).__init__(func)
	def __getitem__(self, key):
		if key not in self:
			self[key] = self.func(key)
		return super(ArgumentativeDict, self).__getitem__(key)
