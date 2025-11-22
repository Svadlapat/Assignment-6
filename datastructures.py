# datastructures.py
# Array, Stack, Queue, Singly Linked List, TreeNode

from typing import Any, Optional, Iterable, Iterator


# ------------------------------------------------------------
# Array Wrapper
# ------------------------------------------------------------
class Array:
    def __init__(self, initial: Optional[Iterable[Any]] = None):
        self._data = list(initial) if initial else []

    def insert(self, idx, value):
        if idx < 0 or idx > len(self._data):
            raise IndexError("Index out of bounds")
        self._data[idx:idx] = [value]

    def delete(self, idx):
        if idx < 0 or idx >= len(self._data):
            raise IndexError("Index out of bounds")
        return self._data.pop(idx)

    def access(self, idx):
        return self._data[idx]

    def append(self, value):
        self._data.append(value)

    def __iter__(self) -> Iterator[Any]:
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"Array({self._data})"


# ------------------------------------------------------------
# Stack
# ------------------------------------------------------------
class Stack:
    def __init__(self):
        self._data = []

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def top(self):
        if not self._data:
            raise IndexError("top from empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


# ------------------------------------------------------------
# Queue
# ------------------------------------------------------------
class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, val):
        self._data.append(val)

    def dequeue(self):
        if not self._data:
            raise IndexError("dequeue from empty queue")
        return self._data.pop(0)

    def front(self):
        if not self._data:
            raise IndexError("front from empty queue")
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0


# ------------------------------------------------------------
# Singly Linked List
# ------------------------------------------------------------
class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def insert_front(self, val):
        self.head = Node(val, self.head)
        self._size += 1

    def insert_back(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(val)
        self._size += 1

    def delete_front(self):
        if not self.head:
            raise IndexError("delete from empty list")
        val = self.head.value
        self.head = self.head.next
        self._size -= 1
        return val

    def traverse(self):
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def __len__(self):
        return self._size

    def __repr__(self):
        return "SinglyLinkedList([" + ", ".join(str(x) for x in self.traverse()) + "])"


# ------------------------------------------------------------
# Tree Node (Optional)
# ------------------------------------------------------------
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __repr__(self):
        return f"TreeNode({self.value})"
