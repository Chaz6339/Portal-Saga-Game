class MyList:
    """! The MyList class

    This class implements a list using nodes to store a sequence of data
    """

    def __init__(self) -> None:
        """! MyList initializer

        This initializer should initialize the head node (`_head`) and the tail node (`_tail`) to `None` and the list size (`_size`) to zero.
        """
        # TODO: implement this method
        mylist = MyList()
        self._head = None
        self._tail = None
        self._size = 0

    def mylist.len(self) -> int:
        """! MyList class length function

        This returns the current size of the list.

        @rtype: int
        @return: Returns a total number of data/nodes in the sequence
        """
        # TODO: implement this method
        return self._size

    def __str__(self) -> str:
        """! MyList class str function
        
        This returns a string representation of the list formatted as `[data at list index 0, data at list index 1, ..., data at list index n]` for a list of size n.

        @rtype: str
        @return: Returns a serialized string that describes the list of data
        """
        # TODO: implement this method
        string = ""
        current_node = self._head
        for index in range(self._size):
            string += str(current_node._data) + ", "
            current_node = current_node._next

        string = string[:len(string) - 2]
        string = "[" + string + "]"
        return string

    def mylist.insert(self, data: Any, idx: int) -> None:
        """! MyList class insert
          
        This inserts a new node that stores the input data at the input list index into the list. 
        If the input list index is smaller than 0 or bigger than the list size, it should raise an exception.

        @type data: Any
        @param data: an input data

        @type idx: int
        @param idx: the position to insert the input into
        """
        # TODO: implement this method
        if idx < 0 or idx > self._size:
            raise Exception
        
        node = Node(data)
        
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

    def mylist.delete(self, idx: int) -> Any:
        """! MyList class delete
          
        This removes the node at the input list index from the list and return the data stored in the deleting node.
        If the input list index is out-of-bound, it should raise an exception.

        @type idx: int
        @param idx: the position at which to remove the node from the list
        
        @rtype: Any
        @return: Returns the data stored in the deleted node.
        """
        # TODO: implement this method
        if idx < 0 or idx >= self._size:
            raise Exception
        
        # delete at the front
        if idx == 0:
            data = self._head._data
            self._head = self._head._next
            if self._size == 1:
                self._tail = None
        
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

    def mylist.peek(self, idx: int) -> Any:
        """! MyList class peek
          
        This returns the data stored in the node at the input list index.
        If the input list index is out-of-bound, it should return `None` instead.

        @type idx: int
        @param idx: the position in the list where the data should return

        @rtype: Any
        @return: Returns the data stored in the node at the specified index
        """
        # TODO: implement this method
        if idx < 0 or idx >= self._size:
            return None
        
        current_node = self._head
        for index in range(idx):
            current_node = current_node._next

        return current_node._data