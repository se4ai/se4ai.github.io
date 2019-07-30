

---
title: " lib.py: misc utilities"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/lib.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 lib.py: misc utilities


````python
   1. import random,re
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
   8. one = random.choice
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
  25. 
  26. def token(x):
  27.   try: return int(x)
  28.   except:
  29.     try: return float(x)
  30.     except:return x
  31.    
````

## Math

````python
  32. 
  33. def close(x,y,near=0.01): return y*(1-near) <=x<= y*(1+near)
  34. 
````

## Strings

````python
  35. 
  36. def s2m(s):
  37.   return [
  38.     [token(cell) for cell in 
  39.        re.sub(r'[ \t]*',"", line).split(",")] 
  40.     for line in s.splitlines()]
  41. 
````

## Lists

### Iterate through anything

#### items: over top level

````python
  42. 
  43. def items(x): 
  44.    for y in (x if iterp(x) else [x]): yield y
  45. 
````

#### ritems: recursively, over all levels

````python
  46. def ritems(x): 
  47.   if iterp(x):
  48.     for y in x:
  49.       for z in ritems(y): yield z
  50.   else: yield x
  51. 
````
