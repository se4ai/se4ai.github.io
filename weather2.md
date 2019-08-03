

---
title: " weather2.py"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/weather2.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 weather2.py

````python
   1. from data import data
   2. 
   3. def weather2(): return dict(
   4.   about = "albrecht", 
   5.   names = ["outlook", "$temp", 
   6.       "?$humid", "wind", ">play"],
   7.   rows=[
   8.     ["sunny",85,85, "FALSE",1],
   9.     ["sunny",80,90,"TRUE",1],
  10.     ["overcast",83,86,"FALSE",2],
  11.     ["rainy",70,96,"FALSE",2],
  12.     ["rainy",68,80,"FALSE",2],
  13.     ["rainy",65,70,"TRUE",1],
  14.     ["overcast",64,65,"TRUE",2],
  15.     ["sunny",72,95,"FALSE",1],
  16.     ["sunny",69,70,"FALSE",2],
  17.     ["rainy",75,80,"FALSE",2],
  18.     ["sunny",75,70,"TRUE",2],
  19.     ["overcast",72,90,"TRUE",2],
  20.     ["overcast",81,75,"FALSE",2],
  21.     ["rainy",71,91,"TRUE",1]])
````
