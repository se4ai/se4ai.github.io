

---
title: " memo.py"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/memo.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 memo.py

## About

Defines a memo wrapper for methods that caches
memo results in the dictionary `i._memo`. 

## The Code

````python
   1. 
   2. from functools import wraps
   3. 
   4. def memo0(f):
   5.   "Memo index does NOT includes first argument"
   6.   name = f.__name__
   7.   @wraps(f)
   8.   def g(i, *arg, **kw):
   9.    if name not in i._memo:
  10.      i._memo[name] = f(i, *arg, **kw)
  11.    return i._memo[name]
  12.   return g
  13. 
  14. def memo1(f):
  15.   "Memo index includes first argument"
  16.   name = f.__name__
  17.   @wraps(f)
  18.   def g(i, *arg, **kw):
  19.    key=(name,arg[0])
  20.    if key not in i._memo:
  21.      i._memo[key] = f(i, *arg, **kw)
  22.    return i._memo[key]
  23.   return g
  24. 
````

## memos: class decorator

Convert all class methods ending in `0` or `1`' to
properties that call memoed functions. For example
the method `sd0` would be converted into a property `aa`
that calls the function `aa0` memoed using `memo0`.
Also `aa1` would become a property calling a function
memoed via `memo1`.

Also, the decorate adds
`i._memo={}` to the initialization method.

````python
  25. def memos(k):
  26.   setattr(k, "__init__", fresh(getattr(k,"__init__")))
  27.   memoPrim(k,'0',memo0)
  28.   memoPrim(k,'1',memo1)
  29.   return k
  30. 
  31. def memoPrim(k, what='0', decorator=memo0):
  32.   "Turn  methods ending with 'what' into a memoed property"
  33.   for f in dir(k):
  34.     if callable(getattr(k, f)):
  35.       if f[-1] == what:
  36.         setattr(k,f[:-1], property(decorator(getattr(k,f))))
  37. 
  38. def fresh(f):
  39.   "Add `_memo` initialization to the constructor"
  40.   @wraps(f)
  41.   def g(i,*lst,**kw):
  42.     i._memo={}
  43.     f(i,*lst,**kw)
  44.   return g
  45. 
````

## Useful Idiom

The idiom `i._memo={}` resets the memos and forces
a recalculation of all vales. This is recommended
when:

- A class' internal state changes;
- You you want all the memos recalculated.

## Example Usage

See [col](col.md/#Num)

````python
````
