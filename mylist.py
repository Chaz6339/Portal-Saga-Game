class Node:
    """! The DataStructure.Node class.
    
    This class implements a node that store an object and a link to the next node
    """
    
    def __init__(self, data, next_node  = None) -> None:
        """! The node class initializer.
        
        @param data The input data to be stored in the node.
        
        @param next_node The next node that the current node is pointing to. Default is None.
        """
        # The data that is stored in the node
        self._data = data
        # The next node that the current node is pointing to
        self._next = next_node

    def __str__(self):
        return str(self._data)
    
class MyList:
    """! The LinkedList class

    This class implements a list using nodes to store a sequence of objects
    """

    def __init__(self) -> None:
        """! LinkedList initializer

        This initializer should initialize the head node (`_head`) and the tail node (`_tail`) to `None` and the list size (`_size`) to zero.
        """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self) -> int:
        """! LinkedList class length function

        This returns the current size of the list.

        @rtype: int
        @return: Returns a total number of objects/nodes in the sequence
        """
        return self._size

    def __str__(self) -> str:
        """! LinkedList class str function
        
        This returns a string representation of the list formatted as `[obj at list index 0, obj at list index 1, ..., obj at list index n]` for a list of size n.

        @rtype: str
        @return: Returns a serialized string that describes the list of objects
        """

        if self._size == 0:
            return "empty list"
        string = ""
        current_node = self._head
        for index in range(self._size):
            string += str(current_node._data) + ", "
            current_node = current_node._next

        string = string[:len(string) - 2]
        string = "[" + string + "]"
        return string
    
    def count(self, obj): #need to be able to do for exam
        num = 0
        current_node = self._head
        while current_node != None:
            if current_node._data == obj:
                num += 1
            current_node = current_node._next

        return num
    
    def insert(self, obj, idx = None):
        """! LinkedList class insert
          
        This inserts a new node that stores the input object at the input list index into the list. 
        If the input list index is smaller than 0 or bigger than the list size, it should raise an exception.

        @type obj: Any
        @param obj: an input object

        @type idx: int
        @param idx: the position to insert the input into
        """

        if idx == None:
            idx = self._size


        if idx < 0 or idx > self._size:
            idx = self._size
                
        node = Node(obj)

        # insert at front
        if idx == 0:
            node._next = self._head
            self._head = node
            if self._size == 0:
                self._tail = node

        # insert at back
        elif idx == self._size: 
            self._tail._next = node
            self._tail = node

        # insert in the middle
        else: 
            current_node = self._head
            for index in range(idx - 1):
                current_node = current_node._next
            node._next = current_node._next
            current_node._next = node

        self._size += 1

    def delete(self, idx: int):
        """! LinkedList class delete
          
        This removes the node at the input list index from the list and return the object stored in the deleting node.
        If the input list index is out-of-bound, it should raise an exception.

        @type idx: int
        @param idx: the position at which to remove the node from the list
        
        @rtype: Any
        @return: Returns the object stored in the deleted node.
        """
        if idx < 0 or idx >= self._size or self._size == 0: # O(1)
            return None
        
        # delete at the front
        if idx == 0: # O(1)
            data = self._head._data # O(1)
            self._head = self._head._next # O(1)
            if self._size == 1: # O(1)
                self._tail = None # O(1)

            # Inner if statement: Test: O(1) Body: O(1) = O(1) for all cases
            # Outer if statement: Test (1) Body: O(1+1) = O(2) = O(1) for all cases
            # The maximum in this case is O(1)
            """
            The runtime should be O(1), as it is a delete for a Queue. As 
            you can see in the above, and in the myqueue.py, the function
            is O(1) overall. I only evaluated deleteing at the front, since
            that is how Queues work (first in first out). 
            """
        
        # delete at the back
        elif idx == self._size - 1:
            current_node = self._head
            for index in range(self._size - 2):
                current_node = current_node._next
            data = self._tail._data
            self._tail = current_node
            self._tail._next = None

        # delete at the middle
        else:
            current_node = self._head
            for index in range(idx - 1):
                current_node = current_node._next
            data = current_node._next._data
            current_node._next = current_node._next._next

        self._size -= 1
        return data
    
    def remove(self, obj):
        idx = self.find(obj)
        if idx == -1:
            return
        else:
            self.delete(idx)

    def peek(self, idx: int):
        """! LinkedList class peek
          
        This returns the object stored in the node at the input list index.
        If the input list index is out-of-bound, it should return `None` instead.

        @type idx: int
        @param idx: the position in the list where the object should return

        @rtype: Any
        @return: Returns the object stored in the node at the specified index
        """
        if idx < 0 or idx >= self._size:
            return None
        
        current_node = self._head
        for index in range(idx):
            current_node = current_node._next

        return current_node._data
    

    def find(self, obj):
        count = 0 # O(1)
        current_node = self._head # O(1)
        while current_node != None: # O(n) -> repeats 'n' times
            if current_node._data == obj: # O(1)
                return count #O(1)
            # O(1+1) = O(2) = O(1)
            count += 1 # O(1)
            current_node = current_node._next # O(1)
            # O(1) * 3 = O(3) = O(1)
        # O(1) * O(n) = O(n)
        return -1 # O(1)

    """
    After computing all orders and adding up, we found that O(n) dominates. 
    The method find() should be O(n), as we have to traverse through a list 
    of n size. 
    """    
    
    def __getitem__(self, idx):
        current_node = self._head
        for node in range(idx):
            current_node = current_node._next
        data = current_node._data
        return data


        

