

---
title: " col.py : summarize columns of numbers or symbols"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/col.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 col.py : summarize columns of numbers or symbols

````python
   1. from main import my
   2. from lib import nump,items,Pretty
   3. from num import Num
   4. from sym import Sym
````

Tables of data have columns. `Col`umns can be `Num`eric or `Sym`bolic.
Some column values may be marked as unknown (using the character
found in `my.ignore`), Sometimes, we know the number offset (the
`pos`) of the column and the column's name (the `txt`).

`Col`umns can be initialized with an `inits` column.  Internally,
`Col`umns keep a `has` variable which is initially empty. As things
arrive, (if they are not `my.ignore`), then the first thing that
is a symbol or a number triggers the creation of a new `Num` or
`Sym` for the `i.has` variable.


````python
   5. class Col(Pretty):
   6.   def __init__(i,inits=[],txt="",pos=0):
   7.     i.txt, i.pos, i.w, i.has = txt, pos, 1, None
   8.     i + inits
   9.   def n(i):      return i.has.n        if i.has else 0
  10.   def delta(i):  return i.has.delta()  if i.has else 0
  11.   def expect(i): return i.has.expect() if i.has else 0
  12.   def __add__(i,x):
  13.     for y in items(x): # x could a single thing or list of items
  14.       if y != my.data.ignore:
  15.         if not i.has: 
  16.           i.has = Num() if nump(y) else Sym()
  17.         i.has + y
  18.   def __sub__(i,x):
  19.     if x != my.data.ignore and i.has: i.has - x
````

## Check Your Comprehension 

- This code uses `__add__` and `__sub__`. What does
  that mean for how items can be added or deleted ?
- `Num` and `Sym` are not sub-classes of `Col`. Why? 
  Hint: `Col` _has_ zero or one `Num` or `Sym`.
- Match the X to the Y following: X={standard deviation, entropy}  apply to Y={symbolic and numeric}quantities.
- What is the _same_ about standard deviation and entropy?
- What is  _different_ about standard deviation and entropy?

````python
````
