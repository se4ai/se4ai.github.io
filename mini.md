
suggestion: 
easier to monitor if stream, not batch
easier to stream if incremental learning
faster to discuss in sample, not show all
easier to explain, control if ranges, not points
look before you leap (reason over sub-sub clusters, not top cluster)

````python
   1. my = o( 
   2.        era=128,
   3.        char= o(ignore="?",
   4.                less  = "<",
   5.                more  = ">"),
   6.        num= o(small= 0.38, #<0.38=small, <1=medium 
   7.               conf = 99,
   8.               p    = 2,
   9.               bins = 10),
  10.        row= o(doms=64),
  11.        cluster= o(m=64, 
  12.                   strange=1 # set to 0 to disable anomaly detection
  13.                   )
  14.       )
  15. 
  16. #----------------------------------------------------------
  17. class Sym(Thing):
  18.   def __init__(i,inits=[], name="",w=1,pos=0): 
  19.     i.w=w; i.pos=pos; i.name=name
  20.     i.n=0; i.d={}; i.most=0;i.mode=None
  21.     [i + x for x in inits]
  22.   def __add__(i,x):
  23.     i.n += 1
  24.     m=i.d[x] = i.d.get(x,0) + 1
  25.     if m >  i.most: i.most,i.mode = m,x
  26.     return x
  27.   def p(i,x):
  28.     return  i.d.get(x,0) / n
  29.   def prep(i,x): return x
  30.   def norm(i,x): return x
  31.   def variety(i):
  32.     e = 0
  33.     for v in i.d.values():
  34.       p  = v/i.n
  35.       e -= p * log(p,2)
  36.     return e
  37.   def dist(i,x,y):
  38.     no = my.char.ignore
  39.     if x==no or y ==no: return 1
  40.     return 0 if x == y else 1
  41. 
  42. class cols(ok):pass
  43. 
  44. @cols
  45. def _sym1():
  46.   s = Sym(list('abbcccc'))
  47.   assert close(s.variety(),1.3787836)
  48.   assert s.mode == 'c'
  49. 
  50. #----------------------------------------------------------
  51. class Num(Thing):
  52.   # some stats thresholds
  53.   z=  ((0,.5),(.25,.5987),(0.5,.6915),(0.75,.7734), (1,.8413),
  54.        (1.25,.8944),(1.5,.9332),(1.75,.9599),(2,.9772),
  55.        (2.25, .9878), (2.5,.9918),(2.75,.997), (3,.9987))
  56.   t95=((1, 6.314),(5,2.015),(10,1.812),(20,1.725),(30,1.697))
  57.   t99=((1,31.821),(5,3.365),(10,2.764),(20,2.528),(30,2.457))
  58. 
  59.   def __init__(i,inits=[],name="",pos=0,w=1):
  60.     i.w=w; i.pos=pos; i.name=name
  61.     i.n,i.mu,i.m2,i.sd = 0,0,0,0
  62.     i.lo =10**32; i.hi = -1*i.lo
  63.     [i + x for x in inits]
  64.   def variety(i): return i.sd
  65.   def __add__(i,x):
  66.     x = i.prep(x)
  67.     if x < i.lo: i.lo = x
  68.     if x > i.hi: i.hi = x
  69.     i.n  += 1
  70.     d     = x - i.mu
  71.     i.mu += d/i.n
  72.     i.m2 += d*(x - i.mu)
  73.     i.sd = (i.m2/(i.n - 0.99999))**0.5
  74.     return x
  75.   def __sub__(i,x):
  76.     if i.n < 2:
  77.       i.n,i.mu,i.m2 = 0,0,0
  78.     else:
  79.       i.n  -= 1
  80.       d     = x - i.mu
  81.       i.mu -= d/i.n
  82.       i.m2 -= d*(x - i.mu)
  83.       i.sd = (i.m2/(i.n - 0.99999))**0.5
  84.   def norm(i,x):
  85.     return  (x - i.lo) / (i.hi - i.lo +0.00000001)
  86.   def dist(i,x,y):
  87.     no = my.char.ignore
  88.     if x==no and y ==no: return 1
  89.     if x=="?":
  90.       y = i.norm(y)
  91.       x = 0 if y>0.5 else 1
  92.     elif y=="?":
  93.       x = i.norm(x)
  94.       y = 0 if x>0.5 else 1
  95.     else:
  96.       x,y=i.norm(x),i.norm(y)
  97.     return (x-y)**my.num.p
  98.   def z(i,x):
  99.     return  (x - i.mu)/(i.sd + 0.000000001)
 100.   def zbin(i,x):
 101.     z = i.z(x)
 102.     p = interpolate(abs(z),Num.z)
 103.     return int((1-p if z < 0 else p) / my.nums.bins)
 104.   def different(i,j):
 105.     return i.hedges(j) or i.ttest(j)
 106.   def ttest(i,j):
 107.     df = min(i.n - 1, j.n - 1) 
 108.     t= interpolate(df,Num.t95 if my.num.conf==95 else Num.t99)
 109.     return abs(i.mu - j.mu)/(i.sd/i.n + j.sd/j.n)**0.5 >= t
 110.   def hedges(i,j):
 111.     num   = (i.n - 1)*i.sd**2 + (j.n - 1)*j.sd**2
 112.     denom = (i.n - 1) + (j.n - 1)
 113.     sp    = (num / denom )**0.5
 114.     delta = abs(i.mu - j.mu) / sp  
 115.     c     = 1 - 3.0 / (4*(i.n + j.n - 2) - 1)
 116.     return delta * c >= my.num.small
 117. 
 118. class Int(Num):
 119.   def prep(i,x): return int(x)
 120. class Float(Num):
 121.   def prep(i,x): return float(x)
 122. 
 123. @cols
 124. def _num1():
 125.   n= Int([9,2,5,4,12,7,8,11,9,3,7,4,12,5,4,10,9,6,9,4])
 126.   assert close(n.sd,3.0608)
 127.   assert n.mu == 7
 128. 
 129. @cols
 130. def _num2():
 131.   c=1
 132.   while c<1.4:
 133.     c+=0.025
 134.     a= [r()**0.5 for _ in range(100)]
 135.     b= [x*c for x in a]
 136.     a= Float(a)
 137.     b= Float(b)
 138.     print("%5.3f %5.3f %5.3f %5.3f %5.3f " % (c,a.mu,b.mu, a.sd,b.sd),
 139.           "hedges %5s ttest %5s both %5s" %(a.hedges(b), a.ttest(b), a.different(b)))
 140. 
 141. #----------------------------------------------------------
 142. class Row(Thing):
 143.   id=0
 144.   def __init__(i,cells) : 
 145.     i._memo={}
 146.     i.cells = cells
 147.     i.id = Row.id = Row.id+1
 148.   def clone(i):
 149.     return Row(i.cells[:])
 150.   def __getitem__(i,k):  return i.cells[k]
 151.   def __setitem__(i,k,v): i.cells[k] =v ; return v
 152.   @memo
 153.   def dominates(i, history):
 154.     n     = my.row.doms
 155.     goals = history.goals()
 156.     return sum([i.dominate(one(history.rows),goals)
 157.                 for _ in range(n)])  / n
 158.   def dominate(i,j,goals):   
 159.     z = 0.00001
 160.     s1, s2, n = z,z,z+len(goals) 
 161.     for goal in goals:
 162.       a,b = i[goal.pos], j[goal.pos]
 163.       a,b = goal.norm(a), goal.norm(b)
 164.       s1 -= 10**(goal.w * (a-b)/n)
 165.       s2 -= 10**(goal.w * (b-a)/n)
 166.     return s1/n < s2/n
 167.   def dist(i,j,history):
 168.     n,d,p = 0.00000001,0,1/my.num.p
 169.     for x,y,h in zip(i.cells,j.cells,history.seen):
 170.       n += 1
 171.       d += h.dist(x,y)
 172.     return d**p/n**p
 173.   def closest(i,rows,history,best=10**32,better=lt):
 174.     out = None
 175.     for j in rows:
 176.       d = i.dist(j,history)
 177.       if better(d, best):
 178.         best,out=d,j
 179.     return out 
 180.   def furthest(i,rows,history):
 181.     return i.closest(rows,history,best=-1,better=gt)
 182. 
 183. #----------------------------------------------------------
 184. class Cluster(Thing):
 185.   def __init__(i, inits=[]): 
 186.     i.rows  = []
 187.     i.dnum=Float()
 188.     i.east,i.west = None,None
 189.     i.left, i.right = None,None
 190.     i.history = history
 191.     i.where
 192.     [i + x for x in inits]
 193.   def clone(i):
 194.    return Cluster(i.history)
 195.   def __add__(i,row):
 196.     if   i.west  is None: 
 197.       i.west=row
 198.     elif i.east is None: 
 199.       i.east=row; c=i.west.dist(i.east)
 200.     else:
 201.       a = i.east.dist(row)
 202.       b = i.west.dist(row)
 203.       d = i.where[row.id] = (a**2 + b**2 - i.c**2)/2*i.c
 204.       i.dnum + d
 205.       if abs(i.dnum.z(d)) > my.cluster.strange: 
 206.         i.rows += [row]
 207.         if len(i.rows) > 2*my.cluster.era:
 208.           i.left  = i.left  or clone()
 209.           i.right = i.right or clone()
 210.           if a < b:
 211.             i.left.add(row)
 212.           else:
 213.             i.right.add(row)
 214.             ## rows are different e in each luster
 215.             ## history is global at the top, pased down
 216.             ## rows dont have history built in
 217.             ## two histoies, global and local
 218. ## only shuffle once at top
 219. ## must remember to add when we start
 220. #----------------------------------------------------------
 221. class History(Thing):
 222.   def __init__(i,names=[],keep=True): 
 223.     i.rows  = []
 224.     i.keep  = keep
 225.     i.names = names
 226.     i.seen  = [None] * len(names)
 227.   def clone(i):
 228.     return History([x.name for x in i.seen])
 229.   def goals(i):
 230.     return [x for x in i.seen if 
 231.             my.char.less in x.name or my.char.more in x.name]
 232.   def __add__(i,row):
 233.     for n,(cell,name) in enumerate(zip(row.cells,i.names)): 
 234.       if cell !=my.char.ignore: 
 235.         watcher = i.seen[n] = i.seen[n] or i.seeing(n,cell,name)
 236.         row[n]  =  watcher + cell
 237.     row = Row(row)
 238.     if i.keep:
 239.       i.rows += [row]
 240.     return row
 241.   def seeing(i,n,x,name):
 242.     try       : x=int(x); what=Int
 243.     except    : 
 244.       try     : x=float(x); what=Float
 245.       except  : what=Sym
 246.     return what(name=name,pos=n,
 247.                 w= -1 if my.char.less in name else 1)
 248. 
 249. def shuffleAndFindPoles(rows):
 250.   hi=len(rows)
 251.   south=b=None
 252.   bx={} 
 253.   c=0
 254.   def update(b,x,south,c):
 255.     tmp = bx[x] = abs(b-x)
 256.     if tmp > c: c,south = tmp,x
 257.     return south,c
 258.   # find south and furthest from south
 259.   for x in range(hi-1,0,-1):
 260.     y=random.randint(0,x)
 261.     if south is None: 
 262.        south = south = rows[y]
 263.        c = bx[south] = 0
 264.     else: 
 265.        south,c=update(south,rows[y],south,c)
 266.     if x==y: continue
 267.     rows[x],rows[y]=rows[y],rows[x]
 268.   south,c=update(south, rows[0],south,c)
 269.   c1= c
 270.   north = south
 271.   for x,b2x in bx.items():
 272.     if c >= 2*b2x:
 273.        tmp= abs(x-north)
 274.        if tmp > c1:
 275.          print(".")
 276.          c1,north = tmp,x
 277.   return c1, c, north,south
 278.        
 279. 
 280. [print(y) for y in  
 281.   sorted(
 282.     [shuffleAndFindPoles(shuffle([0,100]+ [int(r()*100) for _ in range(1000)])) 
 283.      for _ in range(20)])]
 284. 
 285. 
 286. sys.exit()
 287.  
 288. class Place:
 289.   def __init__(i, names):
 290.     i.history= History(names)
 291.     i.c = i.north = i.south = None
 292.     i.distances = Float() 
 293.   def add(i,row,rows):
 294.     if not i.north or not i.south: 
 295.        anything = one(rows)
 296.        i.north  = anything.furthest(rows, i.history)
 297.        i.south  = i.north.furthest(rows,  i.history)
 298.        i.c      = i.south.dist(i.north,   i.history)
 299.     a = i.north.dist(row, i.history)
 300.     b = i.south.dist(row, i.history)
 301.     d = (a**2 + i.c**2 - b**2)/2*i.c
 302.     i.distances + d
 303.     return o(row     = row,
 304.              northern= a<b,
 305.              weird   = abs(i.distances.z(d)) > 1)
 306.   def adds(i,src):
 307.     cache=[]
 308.     for x in src:
 309.       x = x.clone()
 310.       i.history + x
 311.       cache += [x]
 312.       if len(cache) > my.era:
 313.         for row in shuffle(cache):
 314.           yield i.add(row,cache)
 315.         cache = []
 316.     if cache:
 317.       for row in shuffle(cache): 
 318.         yield i.add(row,cache)
 319. 
 320. def data(rows=[], names=[], about=''):
 321.   use  = [n for n,x in enumerate(names) if not my.char.ignore in x]
 322.   cols = lambda lst: [lst[n] for n in use]
 323.   here = Place(cols(names))
 324.   rows = [Row(cols(row)) for row in rows]
 325.   for x in here.adds(rows): 
 326.      tag=""
 327.      if   x.weird and     x.northern:tag="N"
 328.      elif x.weird and not x.northern:tag="S"
 329.      elif not x.weird and x.northern:tag=" "
 330.      else: tag="s"
 331.      print(tag,end="")
 332. 
 333. class stories(ok): pass
 334. 
 335. @stories
 336. def _auto():
 337.   from auto import auto
 338.   from weather2 import weather2
 339.   data(**auto())
---
title: "  for row,history in data(**auto()):"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/mini.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 340.   for row,history in data(**auto()):
---
title: "    print(row.cells)"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/mini.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 341.     print(row.cells)
---
title: "  lst = sorted(history.rows,"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/mini.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 342.   lst = sorted(history.rows,
---
title: "               key=lambda z:z.dominates(history))"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/mini.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 343.                key=lambda z:z.dominates(history))
---
title: "  for row in lst[:5]+lst[-5:]:"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/mini.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 344.   for row in lst[:5]+lst[-5:]:
---
title: "    print(row)"
layout: default
code: true
---

Read the code on [Github](https://github.com/se4ai/code/tree/master/mini.py) <font color=orange><i class="fab fa-github-3x"></i></font>.

 345.     print(row)
 346. ###########################################################
 347. 
 348. if __name__ == "__main__":
 349.   ok.main(sys.argv)
 350. 
````
