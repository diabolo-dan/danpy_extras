
import unittest
import argument_dict # TODO fix relative import

class TestArgumentDict(unittest.TestCase):

	def test_identity_function(self):
		identity = lambda x: x
		test_dictionary = argument_dict.ArgumentativeDict(identity)
		self.assertEqual(test_dictionary[1], 1)
		test_dictionary[2] = 4
		self.assertEqual(test_dictionary[2], 4)
		self.assertEqual(test_dictionary[3], 3)
		self.assertListEqual(sorted(test_dictionary.keys()), [1, 2, 3])

	def test_fibonacci_dict(self):
		fib_dict = argument_dict.ArgumentativeDict(
			lambda x: 1 if x < 2 else fib_dict[x-1] + fib_dict[x-2]
		)
		self.assertEqual(fib_dict[5], 8)
		self.assertEqual(fib_dict[0], 1)
		self.assertListEqual(sorted(fib_dict.keys()), range(6))
