

---
title: " okcol.py"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/okcol.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 okcol.py

````python
   1. 
   2. from ok import ok
   3. from lib import *
   4. from col import Col,Num,Sym
   5. import math
   6. 
   7. @ok
   8. def _col1():
   9.   c= Col()
  10.   for x in [9,2,5,4,12,7,8,11,9,3,7,4,12,5,4,10,9,6,9,4]:
  11.     c + x
  12.     print(c.has.sd)
  13.   assert close(c.has.sd,3.0608)
  14.   assert c.has.mu == 7
  15. 
  16. @ok
  17. def _sym1():
  18.   c = Col()
  19.   for x in list('abbcccc'):
  20.     c + x
  21.     print(c.has.ent, c.has.mode)
  22.   assert close(c.has.ent,1.3787836)
  23.   assert c.has.mode == 'c'
  24. 
  25. if __name__ == "__main__": ok()
````
