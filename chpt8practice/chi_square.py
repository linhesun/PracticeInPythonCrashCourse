# !usr/bin/python
# Author: Linhe Sun
# for practice 8-16 
# function part
# caculating the F2 population chi-square and checking if the segregation fit 3:1.
# Note: df = 1, P 0.05 = 3.84, P 0.01 = 6.63

def compute_chi(num1, num2):
    nums = [num1, num2]
    nbig = max(nums)
    nsmall = min(nums)
    ebig = sum(nums)*3/4
    esmall = sum(nums)/4
    chi_square = (abs(nbig - ebig) - 0.5)**2/ebig + (abs(nsmall - esmall) - 0.5)**2/esmall
    return chi_square

def fit_or_not(num):
    if num < 3.84:
        print("Yes, it fit the 3:1 ratio. You can fine mapping the gene now.")
    else:
        print("No, you can not arrange a fine-mapping.")

