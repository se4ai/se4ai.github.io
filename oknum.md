

---
title: " oknum.py"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/oknum.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 oknum.py

````python
   1. 
   2. from ok  import ok
   3. from lib import *
   4. from num import Num
   5. 
   6. n=Num()
   7. for x in [1,2,3,4]: n+x
   8. print(n,n.sd)
   9. 
  10. @ok
  11. def _num():
  12.   n= Num()
  13.   for x in [9,2,5,4,12,7,8,11,9,3,7,4,12,5,4,10,9,6,9,4]:
  14.     n + x
  15.   assert close(n.sd,3.0608)
  16.   assert n.mu == 7
````
