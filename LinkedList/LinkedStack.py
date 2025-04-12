

from SinglyLinkedList import SinglyLinkedList


class LinkedStack:
 def __init__(self):
  self._data=SinglyLinkedList()

 def __len__(self):
  return len(self._data)
 
 def push(self,e):
  return self._data.add_first(e)
 
 def pop(self):
  if self.is_empty():
   raise ValueError('LinkedStack is Empty')
  return self._data.remove_node()
 
 def __str__(self):
  return str([i for i in self])
 
 def is_empty(self):
  return len(self)==0

 def __iter__(self):
  for i in self._data:
   if i is not None: 
    yield i






  
if __name__ =='__main__':
 import logging
 logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.DEBUG)
 log=logging.getLogger(__name__)
 linkedstack=LinkedStack()
 linkedstack.push('10')
 linkedstack.push('20')
 linkedstack.push('30')
 log.debug(linkedstack.pop())
 log.debug(linkedstack.pop())
 log.debug(linkedstack.pop())
 log.debug(linkedstack.pop())
 log.debug(linkedstack)

