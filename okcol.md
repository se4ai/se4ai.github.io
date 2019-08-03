

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
   7. n=Num()
   8. for x in [1,2,3,4]: n+x
   9. print(n,n.sd)
  10. s=Sym()
  11. for x in 'abbcccc': s+x
  12. print(s,s.mode, s.ent)
  13. #dict(n=n.mu,sd=n.sd,lo=n.lo, hi=n.hi))
  14. @ok
  15. def _col1():
  16.   c= Col()
  17.   for x in [9,2,5,4,12,7,8,11,9,3,7,4,12,5,4,10,9,6,9,4]:
  18.     c + x
  19.     print(c.has.sd)
  20.   assert close(c.has.sd,3.0608)
  21.   assert c.has.mu == 7
  22. 
  23. @ok
  24. def _sym1():
  25.   c = Col()
  26.   for x in list('abbcccc'):
  27.     c + x
  28.     print(c.has.ent, c.has.mode)
  29.   assert close(c.has.ent,1.3787836)
  30.   assert c.has.mode == 'c'
  31. 
  32. if __name__ == "__main__": ok()
  33. 
````
