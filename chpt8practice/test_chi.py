# !usr/bin/python
# Author: Linhe Sun
# for practice 8-16 
# main part
# test if the chi_square.py work well
import chi_square
print(chi_square.compute_chi(120, 300))
chi_square.fit_or_not(chi_square.compute_chi(120, 300))

from chi_square import compute_chi
print(compute_chi(110, 256))

from chi_square import compute_chi as cc
print(cc(110, 256))

import chi_square as cs
print(cs.compute_chi(120, 300))
cs.fit_or_not(cs.compute_chi(120, 300))

from chi_square import *
print(compute_chi(110, 256))
fit_or_not(compute_chi(110, 256))