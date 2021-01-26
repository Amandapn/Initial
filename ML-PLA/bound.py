
import matplotlib.pyplot as plt
import math
import cmath
Dvc = 50
sigma = 0.05
x1 = []
x2 = []
x3 = []
x4 = []
for N in range(3, 1200):
    x1.append(cmath.sqrt((8 / N) * math.log(4 * (math.pow(2 * N, Dvc) + 1) / sigma)))
    x2.append(cmath.sqrt((2 / N) * math.log(2 * N * (math.pow(N, Dvc) + 1))) + cmath.sqrt(
        (2 / N) * math.log(1 / sigma)) + 1 / N)
    x3.append((1 / N) * (1 + cmath.sqrt(N * math.log(6 * (math.pow(2 * N, Dvc) + 1) / sigma) + 1)))
    x4.append((2 + cmath.sqrt((2 * N - 4) * math.log(4 * (math.pow(N, 2 * Dvc) + 1) / sigma) + 4)) / (2 * N - 4))
p1, = plt.plot(range(3, 1200), x1, color='m')
p2, = plt.plot(range(3, 1200), x2, color='b')
p3, = plt.plot(range(3, 1200), x3, color='r')
p4, = plt.plot(range(3, 1200), x4, color='g')
plt.legend([p1, p2, p3, p4], ["Original VC", "Rademacher Penalty", "Parrondo and Van den Broek", "Devroye"], loc='best')
plt.xlabel('N')
plt.ylabel('error')
plt.show()
