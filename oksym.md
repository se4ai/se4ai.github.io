

---
title: " oksym.py"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/oksym.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 oksym.py

````python
   1. from ok import ok
   2. from lib import *
   3. from col import Col,Num,Sym
   4. import math
   5. 
   6. s=Sym()
   7. for x in 'abbcccc': s+x
   8. print(s,s.mode, s.ent)
   9. 
  10. @ok
  11. def _sym1():
  12.   s = Sym()
  13.   for x in list('abbcccc'):
  14.     s + x
  15.   assert close(s.ent,1.3787836)
  16.   assert s.mode == 'c'
  17. 
  18. if __name__ == "__main__": ok()
````
