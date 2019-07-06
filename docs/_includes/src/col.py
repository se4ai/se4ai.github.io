from config import my
from num    import Num
from sym    import Sym

class Col:
  def __init__(i,txt="",pos=0,inits=[]):
    i.txt,i.pos,i.has = txt,pos,None
    [i + x for x in inits]
  def __add__(i,x):
    nump = lambda z: isinstance(z, (int,float))
    if x != my.ignore: 
      if not i.has:
        what  = Num if nump(x) else Sym
        i.has = what()
      return i.has + x
