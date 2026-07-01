import matplotlib.pyplot as plt
import numpy as np
from random import choice as c, randint as r

n = 1000000 #no of trials
d = {}
for i in range(n):
  final = 0
  for j in range(100):
    final+=c([-1,1])
  if final in d :
    d[final]+=1
  else:
    d[final]=1

d = dict(sorted(d.items()))
plt.xlabel("final position")
plt.ylabel("trials")
plt.plot(d.keys(),d.values())
plt.show()

n = 1000000 #no of trials
d = {}
for i in range(n):
  final = 0
  for j in range(100):
    a = r(0,2)
    if a<2:
      final+=1
    else:
      final-=1

  if final in d :
    d[final]+=1
  else:
    d[final]=1

d = dict(sorted(d.items()))
plt.xlabel("final position")
plt.ylabel("trials")
plt.plot(d.keys(),d.values())
plt.show()