#!/usr/bin/python3
"""define classes"""

class Node:
    """Class Node of singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a new Node

        Args:
            data (int): data of the new Node
            next_node (Node): next node of the new node
        """
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """Get/set the data of the Node"""
            return (self__data)

        @data.setter
        def data(self, value):
            if not isinstance(value, int):
                raise TypeError("data must be an integer")
            self.__data = value

        @property
        def next_node(self):
            """Get/set next_node"""
            return (self.__next_node)

        @next_node.setter
        def next_node(self, value):
            if not isinstance(value, Node) and value is not None:
                raise TypeError("next_node must be a Node object")
            self.__next_node = value

class SinglyLinkedList:
    """Represent a singly linked list"""

    def __int__(self):
        """Initilize a new singlylinkedlist"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert new node in the list

        Args:
             value (Node): new node to insert
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Print representation of the linked list"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
