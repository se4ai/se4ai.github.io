

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
   6. import sys
   7. 
   8. @memos
   9. class Rows(Pretty):
  10.   def __init__(i,name=None, headers=[]):
  11.     "build the table, using the text in the headers"
  12.     i.headers = headers
  13.     i.name    = name
  14.     i.all     = [] # stores all the rows
  15.     i.cols    = set([Col(pos=n, txt=txt) 
  16.                      for n,txt in enumerate(headers)])
  17.     for col in i.less: col.w = -1
  18.     for col in i.more: col.w =  1
  19.   def __add__(i,cells):
  20.     "add a row, update the column headers"
  21.     for col in i.cols:
  22.       col + cells[col.pos]
  23.     row = Row(cells)
  24.     i.all += [row]
  25.     return row
  26.   def clone(i):
  27.     "return a new data table that is like me"
  28.     return Table(name=i.name, headers=i.headers)
  29.   def klass0(i):
  30.     for c in i.cols:
  31.       if my.rows.klass in c.txt: return c
  32.   def nums0(i):
  33.     return set(c for c in i.cols if my.rows.nums in c.txt or 
  34.              my.rows.less in c.txt or my.rows.more in c.txt)
  35.   def syms0(i):  return i.cols - i.nums
  36.   def less0(i):  return set(c for c in i.cols if my.rows.less in c.txt)
  37.   def more0(i):  return set(c for c in i.cols if my.rows.more in c.txt)
  38.   def dep0(i):   return i.less | i.more | set([i.klass])
  39.   def indep0(i): return i.cols - i.dep
  40.   def goals0(i): return i.less | i.more 
````
