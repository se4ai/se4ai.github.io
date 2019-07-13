

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
   1. from memo import memos,fresh
   2. from lib  import Pretty
   3. 
   4. @memos
   5. class Row(Pretty):
   6.   id = 0
   7.   def __init__(i,lst):
   8.     i.cells = lst
   9.     i.id = Row.id = Row.id + 1
  10.   @fresh
  11.   def __setitem__(i, k, v): i.cells[k] = v
  12.   def __getitem__(i, k   ): return i.cells[k]
  13.   def doms0(i,rows):
  14.     n = my.someDom
  15.     return sum([ i.dominates( any(rows.all), rows)
  16.                  for _ in range(n) 
  17.               ]) / n
  18.   def dominates(i,j,rows):   
  19.     s1, s2, n = 0, 0, len(rows.goals()) 
  20.     for goal in rows.goals():
  21.       a,b = i[goal.pos], j[goal.pos]
  22.       a,b = goal.norm(a), goal.norm(b)
  23.       s1 += 10**(goal.w * (a-b)/n)
  24.       s2 += 10**(goal.w * (b-a)/n)
  25.     return s1/n < s2/n
  26. 
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
