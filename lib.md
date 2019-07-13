

---
title: " lib.py: misc utilities"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/lib.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 lib.py: misc utilities


````python
   1. import random
   2. from main import my
   3. from collections.abc import Iterable   
   4. 
   5. 
````

## Misc

### Random numbers

````python
   6. 
   7. r = random.random
   8. any = random.choice
   9. 
````

## Pretty Bring

````python
  10. 
  11. class Pretty:
  12.   def __repr__(i):
  13.     pairs = sorted([(k,v) for k,v in i.__dict__.items() 
  14.                     if k[0] != my.private])
  15.     pre = i.__class__.__name__ + '{'
  16.     quote=lambda z: "'%s'" % z if stringp(z) else str(z)
  17.     return pre + ", ".join(['%s=%s' % (k,quote(v)) for k,v in pairs]) + '}'
  18. 
````

## Meta

### iterp, nump: truth predicates

````python
  19. 
  20. def iterp(x) : return not isinstance(x,str) \
  21.                       and isinstance(x,Iterable)
  22. def nump(x)  : return isinstance(x,(float,int))
  23. 
  24. def stringp(x): return isinstance(x,str)
````

## Math

````python
  25. 
  26. def close(x,y,near=0.01): return y*(1-near) <=x<= y*(1+near)
  27. 
````

## Lists

### Iterate through anything

#### items: over top level

````python
  28. 
  29. def items(x): 
  30.    for y in (x if iterp(x) else [x]): yield y
  31. 
````

#### ritems: recursively, over all levels

````python
  32. def ritems(x): 
  33.   if iterp(x):
  34.     for y in x:
  35.       for z in ritems(y): yield z
  36.   else: yield x
  37. 
````
