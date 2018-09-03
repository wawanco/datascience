from abc import ABC, abstractmethod
from collections.abc import MutableMapping
from random import randrange


class MapBase(MutableMapping, ABC):
    class Item:
        """Lightweight composite to store key-value pairs as map items."""

        def __init__(self, k, v):
            self.key = k
            self.value = v

        def __eq__(self, other):
            return self.key == other.key

        def __ne__(self, other): return not (self == other)

        def __lt__(self, other): return self.key < other.key


class UnsortedTableMap(MapBase):
    def __init__(self):
        self._table = []

    def __getitem__(self, k):
        for item in self._table:
            if k == item.key:
                return item.value
        raise KeyError("Key Error: " + repr(k))

    def __setitem__(self, k, v):
        for item in self._table:
            if k == item.key:
                item.value = v
                return
        self._table.append(self.Item(k, v))

    def __delitem__(self, k):
        for j in range(len(self._table)):
            if k == self._table[j].key:
                self._table.pop(j)
                return
        raise KeyError("Key Error: " + repr(k))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item


class HashMapBase(MapBase):
    def __init__(self, cap=11, p=109345121):
        self._table = [None] * cap
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p - 1)
        self._shift = randrange(p)

    @abstractmethod
    def _bucket_getitem(self, j, k):
        pass

    @abstractmethod
    def _bucket_setitem(self, j, k, v):
        pass

    @abstractmethod
    def _bucket_delitem(self, j, k):
        pass

    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for k, v in old:
            self[k] = v

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def __str__(self):
        s = '{\n\t'
        s += '\n\t'.join(['{} -> {}'.format(item.key, item.value) for item in self])
        return s + '\n}'


class ChainHashMap(HashMapBase):

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error ' + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error ' + repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for item in bucket:
                    yield item


if __name__ == "__main__":
    m = ChainHashMap()
    m['spanish'] = 'hola'
    m['american'] = 'hello'
    m['english'] = 'hello'
    m['french'] = 'salut'
    print(m)
    del m['american']
    print(m)
