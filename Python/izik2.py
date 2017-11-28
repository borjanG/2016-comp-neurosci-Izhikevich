import numpy as np
import pylab as py
import matplotlib.pyplot as plot 

__author__ = "Borjan Geshkovski & Charlotte Rodriguez"
__usage__ = "CC Neurosciences Computationelles"

Ne = 800
Ni = 200

re = py.rand(Ne)
ri = py.rand(Ni)

a = np.r_[0.02*np.ones(Ne), 0.02+0.08*ri]
b = np.r_[0.2*np.ones(Ne), 0.25-0.05*ri]
c = np.r_[-65+15*re**2, -65*np.ones(Ni)]
d = np.r_[8-6*re**2, 2*np.ones(Ni)]
S = np.c_[0.5*py.rand(Ne+Ni, Ne), -py.rand(Ne+Ni, Ni)]

v = -65*np.ones(Ne+Ni)			#Initial values of v.
u = b*v 						#Initial values of u.
firings = np.zeros((0,2))

for t in range(1000): 			#Stimulation of 1000 ms
	I = np.r_[5*py.randn(Ne), 2*py.randn(Ni)] #Thalamic input
	fired = py.find(v>=30) 					  #Indices of spikes
	if len(fired) != 0:
		firings = np.vstack((firings, np.c_[t+0*fired, fired]))
		v[fired] = c[fired]
		u[fired] = u[fired] + d[fired]
		I = I + S[:, fired].sum(1)
	v = v+0.5*(0.04*v**2+5*v+140-u+I)
	v = v+0.5*(0.04*v**2+5*v+140-u+I)
	u = u+a*(b*v-u)

plot.plot(firings[:, 0], firings[:, 1],  ".")
plot.title("Izhikevich's simple neuron network model")
plot.show()