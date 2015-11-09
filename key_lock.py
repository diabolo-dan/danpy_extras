from threading import Lock
from contextlib import contextmanager
from collections import defaultdict

class KeyLock(object):
	"""
	A collection of Key-seperated Locks in the form of context_managers.

	For use with dynamically created resources that are used for an extended period.

	Use as:
		keyed_lock = KeyLock()
		...
		with keyed_lock(my_key):
			long_running_resource_use(my_key)

	Be aware that this has extra overhead compared to just using a single Lock, so will be slower for many use-cases.

	A good use case would be taking a Lock on a resource while waiting for a response to an external request.
	"""

	def __init__(self):
		self._glock = Lock()
		self._lock_for_key = defaultdict(Lock)
		self._waiters_for_key = defaultdict(int)

	@contextmanager
	def safe_lock(self, key):
		with self.glock:
			key_lock = self._lock_for_key[key]
			self._waiters_for_key[key] += 1
		with key_lock:
			yield
		with self._glock:
			self._waiters_for_key[key] -= 1
			if not self._waiters_for_key[key]:
				del self._waiters_for_key[key]
				del self._lock_for_key[key]

	def __call__(self, key):
		return self._safe_lock(key)
