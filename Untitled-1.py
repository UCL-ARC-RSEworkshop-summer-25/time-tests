from matplotlib.pyplot import *
from numpy import *
max=2
min=-2
c=2
A=zeros((1240, 1240))
for px in range(1240):
 x0=(px/1240)*(max-min)-2
 for py in range(1240):
  y0=(py/1240)*(max-min)-2
  x=0.0
  y=0.0
  it=0
  while (((x*x)+(y*y))<(c*c)) and it<256:
   xt=(x*x)-(y*y)+x0
   y=2.0*x*y+y0
   x=xt
   it=it+1
  A[px,py]=it
imshow(A)
show()