import timeit,chops 
from ok import ok
import random as r

r.seed(1)
@ok
def _chops1(n=40):
  lst = sorted([int(100*r.random()/20) for _ in range(n)])
  for chop in chops.chops(lst):
     print(len(chop),chop)

@ok
def _chops2(n=1000):
  lst = sorted([r.random()**2 for _ in range(n)])
  for chop in chops.chops(lst,q=10):
     print(len(chop),chop[0],chop[-1])

@ok
def _chops2(n=100):
  p = lambda z: int(10*z)
  lst  = [p(r.random()*10) for _ in range(n)]
  lst += [p(r.random()*20) for _ in range(n)]
  lst += [p(r.random()*30) for _ in range(n)]
  lst  = sorted(lst)
  print(lst[:int(n*1.5)])
  print("\n ")
  print(lst[int(n*1.5):])
  for chop in chops.chops(lst,q=10,epsilon=50):
     u, v = chop[0],chop[-1]
     print(len(chop),u,v, v-u)

@ok
def _chops3():
  nums= [[85,85],
      [80,90],
      [83,86],
      [70,96],
      [68,80],
      [65,70],
      [64,65],
      [72,95],
      ["?",70],
      [75,80],
      [75,70],
      [72,90],
      [81,75],
      [71,91]]
  col1 = [x[0] for x in nums]
  col2 = [x[1] for x in nums]
  for chop in chops.chops(col2):
    u, v = chop[0],chop[-1]
    print(len(chop),u,v, v-u)
    
  
if __name__ == "__main__": ok()
