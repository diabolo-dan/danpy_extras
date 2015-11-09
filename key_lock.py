from threading import Lock
from contextlib import contextmanager
from collections import defaultdict

class KeyLock(object):
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
