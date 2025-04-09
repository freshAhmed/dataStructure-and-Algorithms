from ExceptionEmpty import Empty


class _DoublyLinkedList:
 class _Node:
  __slots__='_element','_next','_prev'
  def __init__(self,element,nextnode,prevnode):
    self._element=element
    self._next=nextnode
    self._prev=prevnode

 def __init__(self):
  self.header=self._Node(None,None,None)
  self.trailer=self._Node(None,None,None)
  self.header._next=self.trailer
  self.trailer._prev=self.header
  self.size=0

 def is_empty(self):
  return self.size==0
  
 def _insert_between(self,e,predecessor,successor):
  newnode=self._Node(e,successor,predecessor)
  predecessor._next=newnode
  successor._prev=newnode
  self.size+=1
  return newnode
 
 def _delete_node(self,node):
  predecessor=node._prev
  successor=node._next
  predecessor._next=successor
  successor._prev=predecessor
  element=node._element 
  node._element=node._prev=node._next=None
  self.size-=1
  return element
 
 def __len__(self):
  return self.size 

 