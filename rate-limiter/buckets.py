import threading
import time
from abc import ABC, abstractmethod

class RateLimitBucket(ABC):
    """Abstract base class for rate limiting algorithms."""
    @abstractmethod
    def allow_request(self, tokens=1):
        """Return True if request is allowed, False otherwise."""
        pass

class TokenBucket(RateLimitBucket):
    """Concrete implementation of a bucket algorithm."""
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_refill = time.time()
        self.lock = threading.Lock()

    def allow_request(self, tokens=1):
        with self.lock:
            self._refill()
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False

    def _refill(self):
        now = time.time()
        time_passed = now - self.last_refill
        self.tokens = min(self.capacity, self.tokens + time_passed * self.refill_rate)
        self.last_refill = now


class LeakyBucket(RateLimitBucket):
    """Concrete implementation of a leaky bucket algorithm (metering)."""
    def __init__(self, capacity, leak_rate):
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.current_level = 0
        self.last_leak_time = time.time()
        self.lock = threading.Lock()

    def allow_request(self, tokens=1):
        with self.lock:
            self._leak()
            if self.current_level + tokens <= self.capacity:
                self.current_level += tokens
                return True
            return False

    def _leak(self):
        now = time.time()
        time_passed = now - self.last_leak_time
        leaked_amount = time_passed * self.leak_rate
        self.current_level = max(0, self.current_level - leaked_amount)
        self.last_leak_time = now
