import inspect

class Dimensions2(object):

	__slots__ = ['height', 'length', 'width']

	def __init__(self, height, length, width):
		self.height = height
		self.length = length
		self.width = width

class _Record(object):
	__slots__ = ()
	def __init__(self, *args):
		bound_args = self.__signature__.bind(*args).arguments
		for attribute in self.__slots__:
			setattr(self, attribute, bound_args[attribute])


class record(type):
	def __new__(cls, name, slots):
		print('__new__')
		for i in inspect.stack(3):
			print(inspect.getmodule(i).__name__)
		signature = inspect.Signature(
			inspect.Parameter(attribute, inspect.Parameter.POSITIONAL_OR_KEYWORD) for attribute in slots
		)
		class_dict = {
			'__slots__': slots,
			'__signature__': signature,
		}
		return super(record, cls).__new__(cls, name, (_Record,), class_dict)

	def __init__(self, name, slots):
		print('__init__')
		pass

print('Dim3')
Dimensions3 = record('Dimensions3', ['height', 'length', 'width'])

d2 = Dimensions2(1,2,3)
d3 = Dimensions3(1,2,3)

for attr in dir(d2):
	a2 = getattr(d2, attr)
	a3 = getattr(d3, attr)
	#print(attr, a2==a3, a2, a3)
