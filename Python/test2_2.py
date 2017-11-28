import numpy as np 
import matplotlib.pyplot as plot 
import random

Ne = 80
Ni = 20

re = np.random.rand(Ne, 1)
ri = np.random.rand(Ni, 1)

_a1 = np.array(0.02*np.ones((Ne, 1)))
_a2 = np.array(0.02 + 0.08*ri)
a = np.concatenate((_a1, _a2), axis = 0)

_b1 = np.array(0.2*np.ones((Ne, 1)))
_b2 = np.array(0.25 - 0.05*ri)
b = np.concatenate((_b1, _b2), axis = 0)

_c1 = np.array(-65 + 15*re**2)
_c2 = np.array(-65*np.ones((Ni, 1)))
c = np.concatenate((_c1, _c2), axis = 0)

_d1 = np.array(8-6*re**2)
_d2 = np.array(2*np.ones((Ni, 1)))
d = np.concatenate((_d1, _d2), axis = 0)

_s1 = 0.5*np.random.rand(Ne+Ni, Ne)
_s2 = -np.random.rand(Ne+Ni, Ni)
S = np.concatenate((_s1, _s2), axis = 1)

v = -65*np.ones((Ne+Ni, 1))		#Initial values of v.
u = np.multiply(b, v)			#Initial values of u.
# print(u.shape)
firings = np.array([[], []])	#Spike timings
v1 =list()

tps = 2
fired = 0
for t in range(0, tps):		#Stimulation of 1000 ms
	#Thalamic input
	_i1 = np.array(5*np.random.randn(Ne, 1))
	_i2 = np.array(2*np.random.randn(Ni, 1))
	
	I = np.concatenate((_i1, _i2), axis = 0)

	del fired
	fired = np.nonzero(v >= 30)[0]			#Indices of spikes
	_f1 = firings.copy()
	_f21 = np.array([[t] for elem in fired])
	_f22 = np.array([[elem] for elem in fired])
	_f2 = np.concatenate((_f21, _f22), axis = 1)
	if firings.shape == (2, 0):
		if _f2.shape != (0, ):
			firings = _f2 
	else:
		firings = np.concatenate((_f1, _f2), axis = 0)
	print(u.shape, "1u")
	print(v.shape, "1v")
	print(I.shape, "1I")
	v[fired] = c[fired]
	u[fired] = np.add(u[fired], d[fired])
	# u[fired] = u[fired] + d[fired]
	print(S[:, fired].sum(1), "tester")
	I = np.add(I, S[:, fired].sum(1))
	# I = I + S[:, fired].sum(1)
	print(u.shape, "2u")
	print(v.shape, "2v")
	print(I.shape, "2I")
	v = np.add(v, 0.5*np.add(0.04*np.multiply(v, v), np.add(np.add(5*v+140, -u), I)))
	v = np.add(v, 0.5*np.add(0.04*np.multiply(v, v), np.add(np.add(5*v+140, -u), I)))
	# v = v + 0.5*(0.04*np.multiply(v, v)+5*v+140-u+I)	#Step -> 0.5 ms
	# v = v + 0.5*(0.04*np.multiply(v, v)+5*v+140-u+I)	#For numerical
	u = np.add(u, np.multiply(a, np.add(np.multiply(b, v), -u)))
	print(u.shape, "3u")
	print(v.shape, "3v")
	print(I.shape, "3I")
	# u = u + a*(np.multiply(b, v)-u)					#Stability
	# v1.append(v[0])

# temps=list(range(0,tps))
# # plot.plot(temps[:tps-1],v1[:tps-1])
plot.plot(firings[:, 0], firings[:, 1],  ".")
plot.title("Simple model")

plot.show()
