



'''
CASE_Study ==>FavoritesList on Postionallist 

the main idea ==> 'is to create song Favoriteslist using PostionalList as data Structure 
so list will maintain for each songs a acess counts variable so each time songs played this variable will incressed 
so the top of the list will have highest count number among the list songs' 


'''
from PositionalList import PositionalList

class Favortieslist:
 class _Item:
   __slots__='_value','_count'
   def __init__(self,e):
     self._value=e
     self._count=0
 def _find_position(self,e):
   walk=self._data.first()
   while walk is not None and walk.element()._value !=e:
     walk=self._data.after(walk)     
   return walk
 def _moved_up(self,p):
   if p!=self._data.first():
     cnt=p.element()._count
     walk=self._data.before(p)
     if cnt >walk.element()._count:
       while walk !=self._data.first() and cnt >self._data.before(walk).element()._count:
         walk=self._data.before(walk)
       self._data.add_before(self._data.delete(p),walk)
 def __init__(self):
   self._data=PositionalList()

 def __len__(self):
   return len(self._data)
 
 def is_empty(self):
   return len(self)==0
 
 def access(self,e):
   p=self._find_position(e)
   if p is None:
     p=self._data.add_last(self._Item(e))
   p.element()._count+=1
   self._moved_up(p)

 def remove(self,e):
   p=self._find_position(e)
   if p is not  None:
     self._data.delete(p)
 def top(self,k):
   if 1<=k<=len(self):
     raise ValueError('Illegal value for k')
   walk=self._data.first()
   for j in range(k):
    if walk is not None:
     item =walk.element()
     yield item._value
     walk=self._data.after(walk)

 def __iter__(self):
   walk=self._data.first()   
   while walk is not None:
     yield walk.element()
     walk=self._data.after(walk)

 def __str__(self):
  return str([{'songname':i._value,'numberplayed':i._count} for i in self])

if __name__ =='__main__':
  import logging 
  logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.DEBUG)
  log=logging.getLogger(__name__)
  favortieslistsongs=Favortieslist()
  favortieslistsongs.access('Low Rider')
  favortieslistsongs.access('Low Rider')
  favortieslistsongs.access('Low Rider')
  favortieslistsongs.access('You Cant Hide from Yourself')
  favortieslistsongs.access('You Cant Hide from Yourself')
  favortieslistsongs.access('You Cant Hide from Yourself')
  
  log.info(list(favortieslistsongs.top(3)))
