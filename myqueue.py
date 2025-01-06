from mylist import *
    
class LinkedQueue:
    """
    Linked Queue ADT with Linked List Data Structure
    """
    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0
        self._items = MyList()
        
    def enqueue(self, data):
        new_node = Node(data)
        self._items.insert(obj = data, idx = self._size)
        self._back = self._items._tail
        self._front = self._items._head
        self._size += 1

    def dequeue(self):
        if self._size == 0: # O(1)
            return None # O(1)
        
        deleted = self._front # O(1)

        self._items.delete(idx = 0) # Look at mylist.py delete method for index 0 for further analysis
        self._back = self._items._tail # O(1)
        self._front = self._items._head # O(1)
        self._size -= 1 # O(1)

        return deleted._data # O(1)

    def __len__(self):
        return self._size
    
    def __str__(self):
        if self._size == 0:
            return "empty queue"
        
        string = ""

        current_node = self._front
        for index in range(self._size):
            string += str(current_node._data) + " "
            current_node = current_node._next

        string = "front --> " + string + "<-- back"
        return string

    def peek(self):
        if self._size == 0:
            return None
        current_node = self._front

        return current_node._data