from typing import Any


class Cache:
    def __init__(self):
        self._cache = {}

    def has(self, key: str):
        return key in self._cache

    def add(self, key: str, value: Any):
        self._cache[key] = value

    def get(self, key: str):
        return self._cache.get(key, None)
