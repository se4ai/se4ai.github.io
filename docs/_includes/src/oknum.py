import math,num,ok 

@ok.ok
def _num1():
  n= num.Num([9,2,5,4,12,7,8,11,9,3,7,4,12,5,4,10,9,6,9,4])
  assert math.isclose(n.sd,3.0608,abs_tol=0.001)
  assert n.mu == 7

if __name__ == "__main__": ok.ok()
