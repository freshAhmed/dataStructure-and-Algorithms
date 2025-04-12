


class SinglyLinkedList:
 
 class _Node:
  __slots__='_element','_next'
  def __init__(self,e,successor):
   self._element=e
   self._next=successor

 def __init__(self):
  self.header=self._Node(None,None)
  self.tail=self._Node(None,None)
  self.size=0

 def add_first(self,e):
  newnode=self._Node(e,None)
  newnode._next=self.header 
  self.header=newnode
  self.size+=1
 
 def add_last(self,e):
  newnode=self._Node(e,None)
  self.tail._next=newnode
  self.size+=1

 def remove_node(self):
   if self.is_empty():
    raise ValueError('LinkedList is Empty')
   node=self.header
   self.header=node._next
   self.size-=1
   return node._element
 
 def is_empty(self):
  return self.size==0
 
 def __len__(self):
  return self.size
 
 def __iter__(self):
  first=self.first()
  while first is not None and first._element:
   yield first._element
   first=first._next

 def first(self):
  return self.header
 
 def last(self):
  return self.tail
 