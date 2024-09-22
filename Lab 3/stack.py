""" CSCI204 Stack lab
Last Modified by: Prof. Fuchsberger, March 2021
"""

from Array import Array

class MyStack:
  """ Implement this Stack ADT using an Array to hold elements.
  """

  def __init__( self ):
    """ Initialize an empty stack.
    Initial capacity should be 2, size should be zero, all items in the array should be None. """
    #TODO
    self._array = Array(2)
    self._size = 0
    

  def is_empty( self ):
    """ Is the stack empty?
    Return:
      True if the stack is empty; False otherwise. """
    #TODO
    return self._size == 0

  def _expand(self):
    """ Stack is full, expand the capacity. """
    new_capacity = self._array.capacity * 2
    new_array = Array(new_capacity)
    for i in range(self._size):
      new_array[i] = self._array.__getitem__(i)  
    self._array = new_array

  def push( self, item ):
    """ Push the item onto the top of the stack. 
    Parameters:
      item; item to add to top of stack.
    Return: None."""
    if self._size == self._array.capacity:
      self._expand()
    self._array.__setitem__(self._size, item)  # Setting element without list indexing
    self._size += 1
    
    # also don't forget to check if array is full and if so call _expand()

  def pop( self ):
    """ Pop the top item off the stack (i.e., remove from stack) and return it. 
    Parameters:
      self, instance of MyStack.
    Return:
      item; item at the top of the stack.
    """
    if self.is_empty():
      return None
    self._size -= 1
    return self._array.__getitem__(self._size)
    #TODO 
  def top( self ):
    """ Return the top item on the stack (does not change the stack). 
    Parameters:
    self, instance of MyStack.
    Return:
    item; item at the top of the stack.
    """
    #TODO
    if self.is_empty():
      return None
    return self._array.__getitem__(self._size - 1)  # Accessing element without list indexing
    

