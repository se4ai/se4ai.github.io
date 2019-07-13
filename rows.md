

---
title: " row.py: a place to store cells"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/rows.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 row.py: a place to store cells

````python
   1. from row  import Row
   2. from memo import memos
   3. from lib  import Pretty
   4. 
   5. @memos
   6. class Rows(Pretty):
   7.   def __init__(i,name=None, headers=[]):
   8.     "build the table, using the text in the headers"
   9.     i.headers= headers
  10.     i.name = name
  11.     i.all  = [] # stores all the rows
  12.     # reason about the headers
  13.     col  = lambda j,s: (Num if my.num in s else Sym)([],s,j)
  14.     i.cols = [col(c,txt) for c,txt in enumerate(headers)]
  15.     for col in i.less: col.w = -1
  16.     for col in i.more: col.w =  1
  17.   def __add__(i,cells):
  18.     "add a row, update the column headers"
  19.     [col + cell for col,cell in zip(i.cols,cells)]
  20.     row = Row(cells)
  21.     i.all += [row]
  22.     return row
  23.   def clone(i):
  24.     "return a new data table that is like me"
  25.     return Table(name=name, headers=i.headers)
  26.   # -- header stuff. Report different headers
  27.   def klass0(i):
  28.     for c in i.cols:
  29.       if my.klass in c.txt: return c
  30.   def nums0(i):
  31.     return set(c for c in i.cols if
  32.      my.num in c.txt or my.less in c.txt or my.more in c.txt)
  33.   def syms0():  return set(i.cols) - i.nums
  34.   def less0(i): return set(c for c in i.cols if my.less in c.txt)
  35.   def more0(i): return set(c for c in i.cols if my.more in c.txt)
  36.   def dep0(i):  return i.less & i.more & set([i.klass])
  37.   def indep0(i):return set(i.cols) - i.dep
  38.   def goals0(i):return i.less & i.more 
  39. 
  40. 
````
