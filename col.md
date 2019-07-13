

---
title: " col.py : summarize columns of numbers or symbols"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/col.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 col.py : summarize columns of numbers or symbols

````python
   1. from main import my
   2. from memo import memos, fresh
   3. from lib import nump,items
   4. import math
````

Tables of data have columns. `Col`umns can be `Num`eric
or `Sym`bolic. Some column values may be marked
as unknown (using the character found in `my.ignore`),
Sometimes, we know the number offset (the `pos`)
of the column and the column's name (the `txt`).

`Col`umns can be initialized with an `inits` column.  Internally,
`Col`umns keep a `has` variable which is initially empty. As things
arrive, (if they are not `my.ignore`), then the first thing
that is a symbol or a number triggers the creation of a new `Num` or `Sym` for the `i.has` variable.


````python
   5. class Col(Pretty):
   6.   def __init__(i,inits=[],txt="",pos=0,has=None):
   7.     i.txt,i.pos,i.has = txt,pos,has() if has else None
   8.     i + inits
   9.   def n(i):      return i.has.n        if i.has else 0
  10.   def delta(i):  return i.has.delta()  if i.has else 0
  11.   def expect(i): return i.has.expect() if i.has else 0
  12.   def __add__(i,x):
  13.     for y in items(x): # x could a single thing or list of items
  14.       if y != my.ignore:
  15.         if not i.has: 
  16.           i.has = Num() if nump(y) else Sym()
  17.         i.has + y
  18.   def __sub__(i,x):
  19.     if x != my.ignore and i.has: i.has - x
````


### Num

````python
  20. 
  21. @memos # turns the method sd0 into a property i.sd
  22. class Num(Pretty):
  23.   "Track numbers seen in a column"
  24.   def __init__(i,inits=[]):
  25.     i.n,i.mu,i.m2 = 0,0,0
  26.     i.lo,i.hi     = my.inf, -1*my.inf
  27.     [i + x for x in inits]
  28.   def delta(i) : return i.sd()
  29.   def expect(i): return i.mu
  30.   def sd0(i):
  31.     return 0 if i.n < 2 else (i.m2/(i.n - 1 + 10**-32))**0.5
  32.   @fresh # this method updates state, so  blast the memos
  33.   def __add__(i,x):
  34.     if x < i.lo: i.lo = x
  35.     if x > i.hi: i.hi = x
  36.     i.n  += 1
  37.     d     = x - i.mu
  38.     i.mu += d/i.n
  39.     i.m2 += d*(x - i.mu)
  40.   @fresh # this method updates state, so  blast the memos
  41.   def __sub__(i,x):
  42.     if i.n < 2:
  43.       i.n,i.mu,i.m2 = 0,0,0
  44.     else:
  45.       i.n  -= 1
  46.       d     = x - i.mu
  47.       i.mu -= d/i.n
  48.       i.m2 -= d*(x - i.mu)
  49.   def norm(i,x):
  50.     return (x - i.lo) / (i.hi - i.lo - my.tiny)
````

Note that there is a numerical methods
issue with the `__sub__` method of `Num`: it becomes
inaccurate when the tracked numbers are very small and the sample
size is small (e.g. `i.n` less than 5). So if using
`aNum - x` to walk backwards down a sequence,
have a stopping rule of `i.n` > 5 (say).

### Sym

````python
  51. @memos
  52. class Sym(Pretty):
  53.   "track symbols seen in a column"
  54.   def __init__(i,inits=[]):
  55.     i.n,i.bag = 0,{}
  56.     [i + x for x in inits]
  57.   def delta(i) : return i.ent()
  58.   def expect(i): return i.mode
  59.   @fresh
  60.   def __add__(i,x):
  61.     i.n += 1
  62.     i.bag[x] = i.bag.get(x,0) + 1
  63.   @fresh
  64.   def __sub__(i,x):
  65.     if x in i.bag:
  66.       i.n -= 1
  67.       i.bag[x] -= 1
  68.   def mode0(i):
  69.     most,out = 0,None
  70.     for k,n in i.bag.items():
  71.       if n > most:
  72.         out, most = k,n
  73.     return out
  74.   def ent0(i):
  75.     e=0
  76.     for v in i.bag.values():
  77.       p  = v/i.n
  78.       e -= p * math.log(p,2)
  79.     return e
  80. 
````

## Check Your Comprehension 

- This code uses `__add__` and `__sub__`. What does
  that mean for how items can be added or deleted ?
- `Num` and `Sym` are not sub-classes of `Col`. Why? 
  Hint: `Col` _has_ zero or one `Num` or `Sym`.
- Write down the equation for entropy, standard deviation.
- What is the standard deviation of a list with one item?
- What is the entropy of a list of 10 idenitical items?
- Consider the following  boxes. Intuitively, which is most/least diverse? Check your intution: on an x-y
  plot, lay out box 1,2,3,4,5 on the x-axis and compute their entropy (recorded on the y-axis). Where is
  entropy maximal? Minimal? FYI: log2(1)=0, log2(0.75)=-0.42, log2(0.5)=-1, log2(0.25)=-2.
  - box 1: [apple\*4] 
  - box 2: [apple\*3,orange\*1] 
  - box 3: [apple\*2,orange\*2] 
  - box 4: [apple\*1,orange\*3] 
  - box 5: [orange\*4]
- Match the X to the Y following: X={standard deviation, entropy}  apply to Y={symbolic and numeric}quantities.
- What is the _same_ about standard deviation and entropy?
- What is  _different_ about standard deviation and entropy?
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
