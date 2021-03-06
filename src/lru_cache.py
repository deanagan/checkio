from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._usage = deque(maxlen=capacity)
        self._cache = {}

    def get(self, key: int) -> int:
        value = self._cache.get(key, -1)

        if value != -1:
            if key in self._usage:
                self._usage.remove(key)
            self._usage.append(key)

        return value

    def put(self, key: int, value: int) -> None:

        is_update = key in self._cache
        self._cache[key] = value
        if not is_update and len(self._usage) >= self._capacity:
            least_key = self._usage.popleft()
            self._cache.pop(least_key)

        if key in self._usage:
            self._usage.remove(key)
        self._usage.append(key)
