

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
   5. 
   6. @ok
   7. def _data():
   8.   rows = auto()
   9.   for row in rows.all:
  10.     print(row.id, row.doms(rows))
  11. 
  12. if __name__ == "__main__": ok()
````
