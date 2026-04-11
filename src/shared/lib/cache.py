from typing import Any


class CacheService:
    def __init__(self):
        self._cache = {}

    def set(self, name: str, data: Any):
        self._cache[name] = data

    def get(self, name: str, *args, **kwargs):
        if name not in self._cache:
            raise ValueError(f"Cache {name} not found")

        return self._cache[name]
