from config import * 
from sym import Sym
from num import Num
from copy import deepcopy 

def chops(lst, q= my.bins, 
           getx= lambda z:z,     # for list of numbers
           gety= lambda g,z: z,  # for lst of numbers
           #y= lambda g,z: z[g], # for lst of lists
           epsilon=None, 
           isa=Num,   # to split on symbols, use Sym
           goals=[0], # list of gety's first argument
           ):
  # these 3 functions let an item have 1 to many goals
  def create(): return [(isa(),g) for g in goals]
  def update(ys,item):
    for y,g in ys: 
      val = gety(g,item)
      if val != my.ignore: y + val
  def better(ys0,ys1,ys2):
    for (y0,_),(y1,_),(y2,_) in zip(ys0,ys1,ys2):
      if y0.simpler(y1,y2): return True
  #------
  lst = sorted([z for z in lst if z != my.ignore], key=getx)
  n   = len(lst)
  w   = int(n/q) # a chop must be at least w wide
  if epsilon == None: # set epsilon from value near the median
    epsilon = lst[int(n*(0.5+my.ncohen))] - lst[int(n*0.5)]
  y0, y1, y2 = create(), create(), create()
  nchops, chop = 0, []
  for j,item in enumerate(lst):
    if getx(item) != my.ignore:
      chop += [item] 
      update(y0, item)
      update(y2, item)
      if len(chop) >= w: # enough to chop
       if j <= n-w: # after chop, enough for other chops
        if getx(item) != getx(lst[j+1]):  # dont split same thing
         # does chop divide nums by more then epsilon?
         if getx(chop[-1]) - getx(chop[0]) >= epsilon:
          # is this chop better than that last one?
          if not nchops or better(y0, y1, y2): 
            nchops += 1
            y0 = deepcopy(y2)
            y1 = deepcopy(y2)
            y2 = create()
            yield chop 
            chop = []
  if chop: 
    yield chop

"""
    else:
    while j < most - width - 1:
    j += w
    while j < most - 1 and nth(j) == nth(j+1): j += 1   
    if j<n: 
      out += [nth(j)]
    if len(out) > 1:
      yield out[-2],out[-1]
  return out

nump  = lambda z: isintance(z,(float,int))
  what  = lambda z: Num() if nump(z) else Sym()
  ys    = [what(y(lst[0], z)) for z in ys]


           cohen = my.cohen):   

  if epsilon is None:
    epsilon = nth(most*(0.5+cohen/2)) - nth(n*0.5)
      or nth(j) < out[-1]+epsilon # or this chop is trivial
      """
