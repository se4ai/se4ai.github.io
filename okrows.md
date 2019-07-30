

---
title: " okrows.py"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/okrows.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 okrows.py

````python
   1. from ok   import ok
   2. from lib  import *
   3. from data import data
   4. from auto import auto
   5. from weather2 import weather2
   6. 
   7. @ok
   8. def _data():
   9.   rows = auto()
  10.   lst  = sorted(rows.all,
  11.           key=lambda z:z.doms(rows))
  12.   for row in lst[:5] + lst[-5:]:
  13.     print(row.id, row.doms(rows),
  14.          [ row[g.pos] for g in rows.goals])
  15. 
  16. if __name__ == "__main__": ok()
````
