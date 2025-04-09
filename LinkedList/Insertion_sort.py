

def Insertionsort_positionallist(l):
  if len(l)>1:
    '''positionallist based on doublylinkedlist'''
    marke=l.first()
    while marke!=l.last(): 
      pivot=l.after(marke)
      value=pivot.element()
      if value > marke.element():
        marke=pivot
      else:
        walk=marke
        while walk!=l.first() and l.before(walk).element()>value: 
          '''it's going to run from the position of the marke intel it's find a 
            element is less than pivot value and befor it's hit the first node'''  
          walk=l.before(walk)
        l.delete(pivot)
        l.add_before(value,walk)
    return l 

if __name__ == '__main__':
  # test Insertionsort_positionallist
  import logging
  logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
  log=logging.getLogger(__name__)
  from PositionalList import PositionalList
  positionallist=PositionalList()
  positionallist.add_first(50)
  positionallist.add_first(20)
  positionallist.add_first(30)
  positionallist.add_first(10)
  positionallist.add_first(210)
  positionallist.add_first(-120)
  positionallist.add_first(0)
  positionallist=Insertionsort_positionallist(positionallist)
  positionallist.add_first(300)
  log.debug(positionallist)
  positionallist=Insertionsort_positionallist(positionallist)
  log.debug(positionallist)
 
  

