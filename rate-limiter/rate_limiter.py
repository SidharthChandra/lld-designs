import threading
import time
from buckets import TokenBucket, LeakyBucket

class RateLimiter:
    """
    Manages buckets for different users.
    Follows OCP/DIP by using a factory for bucket creation.
    """
    def __init__(self, bucket_factory):
        """
        :param bucket_factory: A callable that returns a new bucket instance.
        """
        self.bucket_factory = bucket_factory
        self.buckets = {}
        self.lock = threading.Lock()

    def allow_request(self, user_id, tokens=1):
        bucket = self._get_bucket(user_id)
        return bucket.allow_request(tokens)

    def _get_bucket(self, user_id):
        with self.lock:
            if user_id not in self.buckets:
                # SRP: Creation logic is delegated to the factory
                self.buckets[user_id] = self.bucket_factory()
            return self.buckets[user_id]


class RequestHandler:
    """
    Client class that uses the rate limiter.
    Follows DIP by accepting any limiter implementation.
    """
    def __init__(self, rate_limiter):
        self.rate_limiter = rate_limiter

    def handle_request(self, user_id, tokens=1):
        if self.rate_limiter.allow_request(user_id, tokens):
            print(f"[ALLOWED] User: {user_id}")
            return True
        print(f"[DENIED]  User: {user_id}")
        return False


if __name__ == "__main__":
    # --- Switching to Token Bucket ---
    print("--- Using Token Bucket Strategy ---")
    token_factory = lambda: TokenBucket(capacity=5, refill_rate=2)
    limiter = RateLimiter(bucket_factory=token_factory)
    handler = RequestHandler(rate_limiter=limiter)
    
    uid = "user_token"
    for _ in range(3): handler.handle_request(uid)

    # --- Switching to Leaky Bucket ---
    print("\n--- Using Leaky Bucket Strategy ---")
    leaky_factory = lambda: LeakyBucket(capacity=5, leak_rate=2)
    limiter = RateLimiter(bucket_factory=leaky_factory)
    handler = RequestHandler(rate_limiter=limiter)
    
    uid = "user_leaky"
    for _ in range(3): handler.handle_request(uid)
