from Favortieslist import Favortieslist
from PositionalList import positionallist



class FavortieslistMTF(Favortieslist):
 

 def _moved_up(self, p):
  if p!=self._data.first():
   self._data.add_first(self._data.delete(p))

 def top(self, k):
  
  if not 1<=k<=len(self):
   raise ValueError('Illegal value for k')

  tmp=positionallist()
  for item in self._data:
    tmp.add_last(item)
  
  for j in range(k):
   highpos=tmp.first()
   walk=tmp.after(highpos)
   while walk is not None :
    if walk.element()._count>highpos.element()._count:
     highpos=walk
    walk=tmp.after(walk)
   yield highpos.element()._value
   tmp.delete(highpos)



