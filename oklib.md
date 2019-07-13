

---
title: " oklib.py"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/oklib.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 oklib.py

````python
   1. 
   2. from ok import ok
   3. from lib import *
   4. 
   5. @ok
   6. def _items():
   7.   assert [5]       == [x for x in items(5)]
   8.   assert [1,2,3,4] == [x for x in items([1,2,3,4])]
   9. 
  10. @ok
  11. def _ritems():
  12.   assert ['a','b'] == [x for x in ritems(dict(a=1,b=2))]
  13.   assert [1,2,3,4] == [x for x in ritems([1,(2,[3]),[4]])]
  14. 
  15. class Fred(Pretty):
  16.   def __init__(i):
  17.     i.a="a"
  18.     i.b=dict(c=1,d=2)
  19.     i.e=100
  20.     i._has=i
  21. 
  22. print(Fred())
  23. if __name__ == "__main__": ok()
````
