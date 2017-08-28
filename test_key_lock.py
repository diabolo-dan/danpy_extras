import unittest
import key_lock # TODO fix relative import
import threading
import time

NUM_RESOURCES = 100

class TestKeyLock(unittest.TestCase):
	def setUp(self):
		self.lock = key_lock.KeyLock()

	def test_lock_acquisition(self):
		with self.lock(1):
			pass
		with self.lock(2):
			with self.lock(3):
				pass
		self.assertEqual({}, self.lock._lock_for_key)

	def test_non_deterministic_success(self):
		"""
		Poor way to test the behaviour works correctly,
		but better than any alternatives I can think of right now. :/
		"""
		resources = [False] * NUM_RESOURCES

		def run_thread():
			for j in range(NUM_RESOURCES):
				with self.lock(j):
					self.assertEqual(resources[j], False)
					resources[j] = True
					time.sleep(0.0001)
					self.assertEqual(resources[j], True)
					resources[j] = False

		threads =[threading.Thread(target=run_thread) for _ in range(500)]
		for thread in threads:
			thread.start()
		for thread in threads:
			thread.join()
		self.assertEqual({}, self.lock._lock_for_key)
