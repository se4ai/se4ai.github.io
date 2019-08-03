

### Num

````python
   1. from main import my
   2. from memo import memos, fresh
   3. from lib import nump,items,Pretty
   4. 
   5. @memos # turns the method sd0 into a property i.sd
   6. class Num(Pretty):
   7.   "Track numbers seen in a column"
   8.   def __init__(i,inits=[]):
   9.     i.n,i.mu,i.m2 = 0,0,0
  10.     i.lo,i.hi     = my.inf, -1*my.inf
  11.     [i + x for x in inits]
  12.   def delta(i) : return i.sd()
  13.   def expect(i): return i.mu
  14.   def sd0(i):
  15.     return 0 if i.n < 2 else (i.m2/(i.n - 1 + 10**-32))**0.5
  16.   @fresh # this method updates state, so  blast the memos
  17.   def __add__(i,x):
  18.     if x < i.lo: i.lo = x
  19.     if x > i.hi: i.hi = x
  20.     i.n  += 1
  21.     d     = x - i.mu
  22.     i.mu += d/i.n
  23.     i.m2 += d*(x - i.mu)
  24.   @fresh # this method updates state, so  blast the memos
  25.   def __sub__(i,x):
  26.     if i.n < 2:
  27.       i.n,i.mu,i.m2 = 0,0,0
  28.     else:
  29.       i.n  -= 1
  30.       d     = x - i.mu
  31.       i.mu -= d/i.n
  32.       i.m2 -= d*(x - i.mu)
  33.   def norm(i,x):
  34.     return  (x - i.lo) / (i.hi - i.lo - my.tiny)
````

Note that there is a numerical methods
issue with the `__sub__` method of `Num`: it becomes
inaccurate when the tracked numbers are very small and the sample
size is small (e.g. `i.n` less than 5). So if using
`aNum - x` to walk backwards down a sequence,
have a stopping rule of `i.n` > 5 (say).


## Quiz

- What is the standard deviation of a list with one item?
- According to Cohen,
  a _small effect_ (i.e. Of negligible size) is less that 30% of the standard deviation.
  Add a method called `cohen` to `Num` class that returns a _negligible_ amount_ (edit `main.py` to
  define a 
  `negligible` parameter of 30\%). 
  Add a test function to `okcol.py` that uses that `cohen` method
- What does the `@memos` class decorator do?
- What does the `@fresh` method decorator do?
- What would happen if the above `__add__` and `__sub__` methods 
  neglected to `@fresh`en?

````python
````
