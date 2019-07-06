from config import my
from thing  import thing

class Num(Thing):
  "track numbers seen in a column"
  def __init__(i,inits=[]):
    i.n,i.mu,i.sd,i.m2 = 0,0,0,0
    i.lo,i.hi = my.inf, -1*my.inf
    [i + x for x in inits]
  def spread(i): return i.sd
  def expect(i): return i.mu
  def __add__(i,x):
    i.n  += 1
    d     = x - i.mu
    i.mu += d/i.n
    i.m2 += d*(x - i.mu)
    i.sd  = (i.m2/(i.n - 1 + my.tiny))**0.5
    if x < i.lo: i.lo = x
    if x > i.hi: i.hi = x
    return x
