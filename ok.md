
---
title: " ok.py: a simple unit test engine"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/ok.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 ok.py: a simple unit test engine

This unit test engine is strongly inspired by Kent Beck's most
excellent [making making](https://www.youtube.com/watch?v=nIonZ6-4nuU)
video.

## Example usage

Here a demo file that tests the test engine.  Any function wrapped
in `@ok` gets added to a test list.  Then, finally, in `ok()` is
called, all those tests run. And if any crash, then the test engine
just jumps to the next test function.


```python
from ok import ok

@ok
def ok1():
  "This will always fail."
  assert 2==1, "oops"

@ok
def ok2():
  "This will always pass."
  assert 10 == sum([1,2,3,4]), "should not fail"

if __name__ == "__main__": ok()

```

## Useful Features


If a test function contains a documentation string, then that
is printed as part of the test process.

Calling `python3 ok.py` will make this code run all the tests
  in all the  `okXX.py` files in the current directory.

## The Code

````python
   1. import re,traceback,glob
   2. 
   3. def ok(f=None, the=dict(all=[],tries=0,fails=0)):
   4.   if f:
   5.     the["all"] += [f]
   6.   else:
   7.     for f in the["all"]:
   8.       print("\n-----| %s |%s" % (f.__name__,"-"*40))
   9.       if f.__doc__:
  10.         print("# "+ re.sub(r'\n[ \t]*',"\n# ", f.__doc__))
  11.       the["tries"] += 1
  12.       try:
  13.         f()
  14.       except Exception:
  15.         the["fails"] += 1
  16.         print(traceback.format_exc())
  17.       t,f = the["tries"], the["fails"]
  18.       p   = (t-f)/(t+0.0001)
  19.       print(f"# PASS= {t-f} FAIL= {f} %PASS= {p:.0%}")
  20. 
  21. if __name__ == "__main__":
  22.   for f in glob.glob("ok*.py"):
  23.     if not "-" in f:
  24.       m   = re.sub(r'.py',"",f)
  25.       com = "from %s import *" % m
  26.       print("# " + com)
  27.       exec(com)
  28.   ok()  
  29. 
  30. 
````

## Comprehension Exercises

Skim over all the `okXX.py` files to get a sense of how to use this
code/ Write a file `okMyTest.py` that checks if 1+1 equals two.

````python
````
