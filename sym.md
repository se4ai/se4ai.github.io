

### Sym

````python
   1. from memo import memos, fresh
   2. from lib  import *
   3. import math
   4. 
   5. @memos
   6. class Sym(Pretty):
   7.   "track symbols seen in a column"
   8.   def __init__(i,inits=[]):
   9.     i.n,i.bag = 0,{}
  10.     [i + x for x in inits]
  11.   def delta(i) : return i.ent()
  12.   def expect(i): return i.mode
  13.   @fresh
  14.   def __add__(i,x):
  15.     i.n += 1
  16.     i.bag[x] = i.bag.get(x,0) + 1
  17.   @fresh
  18.   def __sub__(i,x):
  19.     if x in i.bag:
  20.       i.n -= 1
  21.       i.bag[x] -= 1
  22.   def mode0(i):
  23.     most,out = 0,None
  24.     for k,n in i.bag.items():
  25.       if n > most:
  26.         out, most = k,n
  27.     return out
  28.   def ent0(i):
  29.     e=0
  30.     for v in i.bag.values():
  31.       p  = v/i.n
  32.       e -= p * math.log(p,2)
  33.     return e
````

## Check Your Comprehension 

- What does the `@memos` class decorator do?
- What does the `@fresh` method decorator do?
- What would happen if the above `__add__` and `__sub__` methods 
  neglected to `@fresh`en?
- This code uses `__add__` and `__sub__`. What does
  that mean for how items can be added or deleted ?
- Write down the equation for entropy.
- What is the entropy of a list of 10 idenitical items?
- Consider the following  boxes. Intuitively, which is most/least diverse? Check your intution: on an x-y
  plot, lay out box 1,2,3,4,5 on the x-axis and compute their entropy (recorded on the y-axis). Where is
  entropy maximal? Minimal? FYI: log2(1)=0, log2(0.75)=-0.42, log2(0.5)=-1, log2(0.25)=-2.
  - box 1: [apple\*4] 
  - box 2: [apple\*3,orange\*1] 
  - box 3: [apple\*2,orange\*2] 
  - box 4: [apple\*1,orange\*3] 
  - box 5: [orange\*4]
- What does the `@memos` class decorator do?
- What does the `@fresh` method decorator do?
- What would happen if the above `__add__` and `__sub__` methods 
  neglected to `@fresh`en?

````python
````
