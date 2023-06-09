"""
This is an example Python Linked List that demonstrates:

  - iterators
  - Abstract Base Classes with the collections.abc module
  - deep copies with the copy module
  - data classes
  - properties
  - decorators
"""

from __future__ import annotations

import copy

import collections.abc as abc
from dataclasses import dataclass
from typing import (Any)


class LinkedList(abc.Iterable):
    """
    The LinkedList (LL) is a wrapper for three items.
     - Head pointer
     - Tail pointer
     - Node counter (cardinality)

    Only the head pointer is necessary, the latter three items are
    included for convenience.
    """

    @dataclass
    class Node:
        """
        The Node class is the atom--smallest base component--of a Linked List.
        An array element can viewed as its analog.

        For simplicity in this example, the Node will store an integers as
        data. In a later example, methods for generalizing this--through use of
        templates--will be utilized.

        This version makes use of the new Python data class feature.
        """

        data: Any = 0
        next: Node = None

    class Iterator(abc.Iterator):
        """
        A special purpose Linked List Iterator
        """

        def __init__(self, node: Node):
            self.__current_node = node

        def __next__(self):
            if self.__current_node is None:
                raise StopIteration

            next_val = (self.current_node).data

            self.__current_node = (self.current_node).next

            return next_val

        @property
        def current_node(self) -> LinkedList.Node:
            """
            Retrieve the value in this node (or None if the Node is empty).
            """

            return self.__current_node

    def __init__(self):
        """
        Construct an empty Linked List
        """

        empty_node = LinkedList.Node()

        self.__head: Node = empty_node
        self.__tail: Node = empty_node
        self.__nodes: int = 0

    def append(self, to_add: Any) -> None:
        """
        Add a Node at the end of the list
        """

        # Store the "to_add" data within the node
        new_node = LinkedList.Node(data=to_add)

        (self.__tail).next = new_node
        self.__tail = new_node

        self.__nodes += 1

    def __deepcopy__(self, memo) -> LinkedList:
        clone = LinkedList()

        for datum in self:
            clone.append(copy.deepcopy(datum, memo))

        return clone

    def __len__(self) -> int:
        return self.__nodes

    def __iter__(self) -> LinkedList.Iterator:
        it = LinkedList.Iterator(self.__head)
        next(it)
        return it

    def __str__(self) -> str:
        """
        Iterate through the LinkedList and print each individual Node
        with an index.
        """

        return "\n".join((f"Node # {index:>4} - {data:>4}"
                          for index, data in enumerate(self)))
