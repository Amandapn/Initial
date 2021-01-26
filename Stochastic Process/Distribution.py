import numpy as np
from scipy import stats
import pylab as pl

# for i in range(11):
# a = sum(np.random.binomial(10, 0.1, size=2000000) == i) / 2000000
# print(a)

n = 10
p = 0.1
lam = 1.0
k = np.arange(n + 1)
pbino = stats.binom.pmf(k, n, p)
ppois = stats.poisson.pmf(k, lam)
print(pbino)
print(ppois)
pl.stem(k, pbino, basefmt='k-', markerfmt='C0 .', use_line_collection=True)
pl.stem(k, ppois, linefmt='r-', markerfmt='C3.',use_line_collection=True)
pl.margins(0.1)
pl.show()
