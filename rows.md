

---
title: " row.py: a place to store cells"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/rows.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 row.py: a place to store cells

````python
   1. from main import my
   2. from row  import Row
   3. from col  import Col
   4. from memo import memos
   5. from lib  import Pretty
   6. 
   7. @memos
   8. class Rows(Pretty):
   9.   def __init__(i,name=None, headers=[]):
  10.     "build the table, using the text in the headers"
  11.     i.headers = headers
  12.     i.name    = name
  13.     i.all     = [] # stores all the rows
  14.     i.cols    = set([Col(pos=n, txt=txt) 
  15.                      for n,txt in enumerate(headers)])
  16.     for col in i.less: col.w = -1
  17.     for col in i.more: col.w =  1
  18.   def __add__(i,cells):
  19.     "add a row, update the column headers"
  20.     [col + cell for col,cell in zip(i.cols,cells)]
  21.     row = Row(cells)
  22.     i.all += [row]
  23.     return row
  24.   def clone(i):
  25.     "return a new data table that is like me"
  26.     return Table(name=i.name, headers=i.headers)
  27.   def klass0(i):
  28.     for c in i.cols:
  29.       if my.rows.klass in c.txt: return c
  30.   def nums0(i):
  31.     return set(c for c in i.cols if my.rows.nums in c.txt or 
  32.              my.rows.less in c.txt or my.rows.more in c.txt)
  33.   def syms0(i):  return i.cols - i.nums
  34.   def less0(i):  return set(c for c in i.cols if my.rows.less in c.txt)
  35.   def more0(i):  return set(c for c in i.cols if my.rows.more in c.txt)
  36.   def dep0(i):   return i.less | i.more | set([i.klass])
  37.   def indep0(i): return i.cols - i.dep
  38.   def goals0(i): return i.less | i.more 
````
