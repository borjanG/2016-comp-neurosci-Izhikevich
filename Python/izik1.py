import numpy as np 
import matplotlib.pyplot as plot 

__author__ = "Borjan Geshkovski & Charlotte Rodriguez"
__usage__ = "CC Neurosciences Computationelles"

def simulate(a, b, c, d, titre, color, I0, I1, start):
	T = 200									# 300 for TC1
	h = 0.5
	N = int(T/h)

	v = [start for i in range(N+1)]
	u = [b*start for i in range(N+1)]
	for t in range(N):
		I = I0 if t < 40 else I1			#100 for TC1
		#For resonator.
		if titre == "Resonator":			
			if t in range(100, 110):		
				I = 2
		v[t+1] = (0.04*v[t]**2+5*v[t]+140-u[t]+I)*h+v[t]
		u[t+1] = (a*(b*v[t]-u[t]))*h+u[t]
		if v[t+1] >= 30:
			v[t] = 30
			v[t+1] = c
			u[t+1] = u[t]+d
	temps = [h*i for i in range(N+1)]
	plot.plot(temps, v, color)
	plot.title(titre)
	# plot.plot(temps, u)
	plot.show()
	#Plan de phase
	# plot.plot(v, u)
	# plot.show() 

# # Modele Regular spiking
# a = 0.02 
# b = 0.2 
# c = -65 
# # d = 2
# d = 8
# simulate(a, b, c, d, "Regular Spiking", "Purple", 0, 10, c)

# # Intrinsically bursting
# a = 0.02
# b = 0.2
# c = -55
# d = 4
# simulate(a, b, c, d, "Intrinsically Bursting", "Green", 0, 10, c)

# # Chattering 
# a = 0.02
# b = 0.2
# c = -50
# d = 2
# simulate(a, b, c, d, "Chattering", "Red", 0, 10, c)

# Fast Spiking
# a = 0.1
# b = 0.2
# c = -65
# d = 2
# simulate(a, b, c, d, "Fast Spiking", "Magenta", 0, 10, c)

# Thalamo-cortical
# a = 0.02
# b = 0.25
# c = -65
# d = 0.05 
# simulate(a, b, c, d, "Thalamo-cortical 1", "Orange", 0, 1, -63)
# simulate(a, b, c, d, "Thalamo-cortical 2", "Cyan", -20, 0, -87)

# Resonator.
a = 0.1
b = 0.25
c = -65
d = 2
simulate(a, b, c, d, "Resonator", "Brown", 0, 0.5, c)

# Low threshold spiking
# a = 0.02
# b = 0.25
# c = -65
# d = 2
# simulate(a, b, c, d, "LTS", "Black",0 , 10, c)