#!/usr/bin/env python3

#汉诺塔
def move(n, a, b, c):
 if n==1 :
  print(a,'-->',c)
  return 1
 x1 = move(n-1, a, c ,b)
 print(a, '-->', c)
 x2 = move(n-1, b, a, c)
 return x1+x2+1;
 
#杨辉三角
def triangles():
 n,L = 1,[]
 while True:
  n,L = n+1, [1 if(i==len(L) or i==0) else L[i-1]+L[i] for i in range(len(L)+1) ]
  yield L
 return
 
#
def normalize(name):
 return name.title()
 