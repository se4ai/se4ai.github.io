

---
title: " row.py: a place to store cells"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/row.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 row.py: a place to store cells

A `row` has `cells` which can be
accessed via `aRow.cells[j]` or
(more conveniently) `aRow[j]`.
A `row` caches a `doms` score
which is an approximate
guess of how often this row has
best goals.

Rows will know how to mutate their cells, soon.

````python
   1. from main import my
   2. from memo import memo0, memos,fresh
   3. from lib  import Pretty
   4. 
   5. @memos
   6. class Row(Pretty):
   7.   id = 0
   8.   def __init__(i,lst):
   9.     i.cells = lst
  10.     i.id = Row.id = Row.id + 1
  11.   @fresh
  12.   def __setitem__(i, k, v): i.cells[k] = v
  13.   def __getitem__(i, k   ): return i.cells[k]
  14.   @memo0
  15.   def doms(i,rows):
  16.     import random
  17.     print("test", random.choice([10,20,30,40]))
  18.     print("any", any(rows.all))
  19.     print("ast", rows.all[0])
  20.     #print("rows", rows)
  21.     n = my.rows.someDom
  22.     return sum([ i.dominates( any(rows.all), rows)
  23.                  for _ in range(n) 
  24.                ]) / n
  25.   def dominates(i,j,rows):   
  26.     print("i",i)
  27.     print("j",j)
  28.     z = 0.00001
  29.     s1, s2, n = z,z,z+len(rows.goals) 
  30.     for goal in rows.goals:
  31.       print("G?",goal.pos)
  32.       a,b = i[goal.pos], j[goal.pos]
  33.       a,b = goal.norm(a), goal.norm(b)
  34.       s1 += 10**(goal.w * (a-b)/n)
  35.       s2 += 10**(goal.w * (b-a)/n)
  36.     return s1/n < s2/n
  37. 
````

## Comprehension Questions

1. Read [A Guide to Python's Magic Methods](https://rszalski.github.io/magicmethods/).  What do the methods `__init__, __getitem__, __setitem__, __repr__` do?
2. Read [memo.py](memo.md). What does the class decorate `@memos` do?
3. In [Num](col.md#num), what does normalization do?
4. This code often crashes if, in `dominates`, the `a,b` values are not normalized.
   Why?
5. Read [On the Value of User Preferences in Search-Based Software
   Engineering](http://bit.ly/2LfLaFP), Section III.c to learn the
   difference between continuous and discrete domination. Then read
   the "%correct" column of Table 8, noting that IBEA uses continuous
   domination while all the other optimizers use discrete domination.
   Based on that table, when is boolean domiantion better than continuous?

````python
````
