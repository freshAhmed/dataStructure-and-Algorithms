

from LinkedList.DoublyLinkedList import _DoublyLinkedList
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
class PositionalList(_DoublyLinkedList):
  class _Position:
    def __init__(self,container,node):
      self.node=node
      self.container=container

    def __eq__(self, other):
     return type(other) is type(self) and other.node is self.node
    
    def __ne__(self, other):
      return not (self == other)
   
    def element(self):
     return self.node._element
  
  def __validate(self,p):
    if not isinstance(p,self._Position):
      raise TypeError('P must be proper Position type')
    if p.container is not self:
      raise ValueError('P does not belong to this container')
    if p.node._next is None:
      raise ValueError('P is not longer valid')
    return p.node
  def _make_position(self,node):
    if node is self.header or node is self.trailer:
     return None
    else:
     return self._Position(self,node)
  
  def first(self):
    return self._make_position(self.header._next)
  
  def last(self):
    return self._make_position(self.trailer._prev)
  
  def befor(self,p):
    node =self.__validate(p)
    return self._make_position(node._prev)
  
  def after (self,p):
    node= self.__validate(p)
    return self._make_position(node._next)
  
  def _insert_between(self, e, predecessor, successor):
    return self._make_position(super()._insert_between(e, predecessor, successor))
  
  def delete(self,p):
    origianl=self.__validate(p)
    return self._delete_node(origianl.node)
  
  def add_befor(self,e,p):
   original=self.__validate(p)
   return self._insert_between(e,original._prev,original)
  
  def add_after(self,e,p):
    original=self.__validate(p)
    return self._insert_between(e,original,original._next)
  
  def add_first(self,e):
    return self._insert_between(e,self.header,self.header._next)
  
  def add_last(self,e):
    return self._insert_between(e,self.trailer._prev,self.trailer)
  
  def __str__(self):
    return str([i for i in self])
  
  def __iter__(self):
    corsur =self.first()
    while corsur is not None:
      yield corsur.element()
      corsur=self.after(corsur)



if __name__ =='__main__':
  # test PositionalList
 log=logging.getLogger(__name__)
  
 positionallist=PositionalList()
 positionallist.add_first(10)
 positionallist.add_first(20)
 positionallist.add_first(30)
 positionallist.add_first(120)
 # [120,30,20,10]
 log.debug([120,30,20,10]==list(positionallist))
 positionallist.add_after(40,positionallist.after(positionallist.after(positionallist.first())))
 # [120,30,20,40,10]
 log.info(positionallist)