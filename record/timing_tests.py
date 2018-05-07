from __future__ import print_function

import timeit
import collections

CaseSetup = collections.namedtuple('CaseSetup', 'name call setup')

namedtuple_case = CaseSetup(
	name='namedtuple',
	call='nt_case.a',
	setup="""
import collections
NTCase = collections.namedtuple('NTCase', 'a,b,c')
nt_case = NTCase(1,2,3)
	"""
)

class_case = CaseSetup(
	name='class',
	call='class_case.a',
	setup="""
class ClassCase(object):
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
class_case = ClassCase(1,2,3)
	"""
)

dict_case = CaseSetup(
	name='dict',
	call='dict_case["a"]',
	setup="""
dict_case = {"a":1, "b":2, "c":3}
	"""
)



slot_class = CaseSetup(
	name='slot class',
	call='slot_class.a',
	setup="""
class SlotCase(object):
	__slots__ = 'a', 'b', 'c'
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
slot_class = SlotCase(1,2,3)
	"""
)

record_case = CaseSetup(
	name='record_case',
	call='record_case.a',
	setup="""
import record
record_case = record.record('record_case', ['a', 'b', 'c'])
	"""
)

for case in (namedtuple_case, class_case, dict_case, slot_class, record_case):
	time = timeit.timeit(case.call, setup=case.setup, number=10**7)
	print("time for {name} case: {time:.3f}s".format(name=case.name, time=time))
