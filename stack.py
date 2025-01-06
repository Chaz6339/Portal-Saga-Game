from mylist import Node

class LinkedStack:
    """ Implement this Stack ADT using an linked nodes.
    """

    def __init__(self):
        """ Initialize an empty stack.
        Size should be zero, all items in the LinkedStack should be None. """
        self._size = 0
        self._top = None

    def isEmpty( self ):
        """ Is the stack empty?
        Return:
        True if the stack is empty; False otherwise. """
        if self._size == 0:
            return True
        else:  
            return False

    def push(self, item):
        """ Push the item onto the top of the stack. 
        Parameters:
        item; item to add to top of stack.
        Return: None.
                
        The overall run time of the push method is O(1). This is because all parts of the function are O(1),
        which is possible since this is a linked stack meaning we can use _next and _top to manipulate the pointers
        instead of a for loop to transverse, which would make it O(n). A Creating a new node is an assignment 
        making it O(1). Next, checking if the stack is empty requires and assignment and and if statement, both 
        O(1) in this case. Afterwards. updating _next,  _top, and incrememnting size is just assignment, making 
        it O(1) too. When you add up all these parts it is all constant, which simplifies to O(1).
        """

        node = Node(item)
        if self._size == 0:
            self._top = node
        else:
            node._next = self._top
            self._top = node
        self._size += 1


    def pop(self):
        """ Pop the top item off the stack (i.e., remove from stack) and return it. 
        Parameters:
        self, instance of MyStack.
        Return:
        item; item at the top of the stack.
        """
        if self._size == 0:
            return None
        
        if self._size == 1:
            popped = self._top._data
            self._top = None
        
        else:
            popped = self._top._data
            self._top = self._top._next

        self._size -= 1        
        return popped


    def peek(self):
        """ Return the top item on the stack (does not change the stack). 
        Parameters:
        self, instance of MyStack.
        Return:
        item; item at the top of the stack.
        """
        if self._size > 0:
            return self._top._data
        else:
            return None
        
    def __len__(self):
        """ Return the size of the stack. 
        """
        return self._size

    def __str__(self):
        """ Return a string representation of the stack. 
        """
        if self._size == 0:
            return "empty stack"
        
        else:
            string = "top -->"
            current_node = self._top
            for index in range(self._size):
                string += " " + str(current_node._data)
                current_node = current_node._next

        return string