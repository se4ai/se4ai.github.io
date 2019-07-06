import math
from memo import memo0

class Sym:
  "track symbols seen in a column"
  def __init__(i,inits=[]): 
    i.n,i.most,i.mode,i.bag = 0,0,None,{}
    i.memo = {}
    [i + x for x in inits]
  def spread(i): return i.ent()
  def expect(i): return i.mode
  def __add__(i,x):
    i.n += 1
    new = i.bag[x] = i.bag.get(x,0) + 1
    if new > i.most:
      i.most,i.mode = new,x
    return x
  @memo0
  def ent(i):
    e=0
    for v in i.bag.values():
      p  = v/i.n
      e -= p * math.log(p,2)
    return e
