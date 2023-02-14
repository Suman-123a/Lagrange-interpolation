import numpy as np
import matplotlib.pyplot as plt
def lag(x,y,xp):
	cc=[]
	for i in range(len(x)):
		m=1
		for j in range(len(x)):
			if i!=j:
				m=m*(x[i]-x[j])
		c=y[i]/m
		cc.append(c)
	s=0
	for i in range(len(x)):
		n=1
		for j in range(len(x)):
			if i!=j:
				n=n*(xp-x[j])
	
		s=s+cc[i]*n
	return s
x=[5,10,15,20,25,30]
y=[45,105,174,259,364,496]
xp=[5,7,9,11,14,18,22,27,29,30]
zz=[]
for i in range(len(xp)):
	z=lag(x,y,xp[i])
	zz.append(z)
plt.plot(x,y,'o')
plt.plot(xp,zz)
plt.show()
