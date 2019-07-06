from config import * 
from sym import Sym
from num import Num
from copy import deepcopy as duplicate

Num,[2,3,4]
def chops(lst, q= my.bins, x= lambda z:z,ys=lambda z:[],
          epsilon=None, goals=[],ako=Num):
  "assumes lst is sorted"
  make  = lambda: [(g,ako()) for g in goals]
  update= lambda lst,logs: [log+lst[g] for g,log in logs]
  lst = sorted(lst, key=x)
  n   = len(lst)
  w   = int(n/q)
  out = []
  if epsilon=None:
    epsilion = lst[n*(0.5+my.ncohen)] - lst[n*0.5]
  b4s, nows = stats(), stats()
  for j,item in enumerate(lst):
    update(item, b4s)
    update(item, nows)
    out += [item] 
    if (len(out) >= w and j <= n-w-1 
        and x(item) != x(lst[j+1])
        and x(out[-1]) - x(out[0]) >= epsilon):
      yield out
      out = []
      stats = 
  if out:
    yield out


def  xyStats(lst, x=lambda z:z,
                 ys=lambda z:[]):
  nump = lambda z: instance(z,(float,in))
  what = lambda z: Num() if nump(z) else Sym()
  xstat,ystats = None,None
  for one in lst:
    if x(one) != my.ignore:
      xstat  = xstat  or what(x(one))
      xstat  + x(one)
    goals  = ys(one)
    ystats = ystats or [None]*len(goals)
    for j,goal in enumerate(goals):
      if goal != my,ignore
        ystats[j] = ystats[i] or what(goal)
        ystats[j] + goal
  return xstat,ystats

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
