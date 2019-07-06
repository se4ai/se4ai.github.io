import timeit,chops,ok 
import random as r

r.seed(1)
@ok.ok
def _chops1(n=40):
  lst = sorted([int(100*r.random()/20) for _ in range(n)])
  for chop in chops.chops(lst):
     print(len(chop),chop)

@ok.ok
def _chops2(n=20):
  lst = sorted([int(1000*r.random()) for _ in range(n)])
  for chop in chops.chops(lst,q=6):
     print(len(chop),chop)


if __name__ == "__main__": ok.ok()
