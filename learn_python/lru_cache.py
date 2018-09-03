class Node:


class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = dict()
        self.