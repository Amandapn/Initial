from scipy.special import comb
import math

N =14072889
s = 0
#for i in range(11):
#    s = s + comb(2*N, i)
s=math.pow(2*N,10)
m = math.exp(N * 0.0000125)
print(m)
print(80*s)
if m <= 80 * s:
    print('yes')
else:
    print('no')
