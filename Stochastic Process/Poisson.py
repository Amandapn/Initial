import numpy as np
import random
import matplotlib.pyplot as plt
# Poisson process

T = 10000
t = 0
lam = 1
arrival_times = []
for i in range(T):
    t += random.expovariate(lam)
    arrival_times.append(t)
print(arrival_times)
plt.figure()
x = np.linspace(1, 10000, 10000)
print(x)
plt.plot(x, arrival_times)
plt.xlim(0,10000)
plt.ylim(0,10000)
plt.show()
