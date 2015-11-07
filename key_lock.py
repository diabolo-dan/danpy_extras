from threading import Lock
from contextlib import contextmanager
from collections import defaultdict

class KeyLock(object):
	def __init__(self):
		self.glock = Lock()
		self.lock_for_key = defaultdict(Lock)
		self.waiters_for_key = defaultdict(int)

	@contextmanager
	def safe_lock(self, key):
		with self.glock:
			key_lock = self.lock_for_key[key]
			self.waiters_for_key[key] += 1
		with key_lock:
			yield
		with self.glock:
			self.waiters_for_key[key] -= 1
			if not self.waiters_for_key[key]:
				del self.waiters_for_key[key]
				del self.lock_for_key[key]

	def __call__(self, key):
		return self.safe_lock(key)
