import inspect

class _Record(object):
	__slots__ = ()
	def __init__(self, *args):
		bound_args = self.__signature__.bind(*args).arguments
		for attribute in self.__slots__:
			setattr(self, attribute, bound_args[attribute])

	def __repr__(self):
		slot_values = ['{}={}'.format(attribute, getattr(self, attribute)) for attribute in self.__slots__]
		return '{}({})'.format(self.__name__, ', '.join(slot_values))


class record(type):
	def __new__(cls, name, slots):
		signature = inspect.Signature(
			inspect.Parameter(attribute, inspect.Parameter.POSITIONAL_OR_KEYWORD) for attribute in slots
		)
		class_dict = {
			'__slots__': slots,
			'__signature__': signature,
			'__name__': name,
			'__doc__': '{}({})'.format(name, ', '.join(slots))
		}
		return super(record, cls).__new__(cls, name, (_Record,), class_dict)

	def __init__(self, name, slots):
		pass
