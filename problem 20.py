## Euler 20 (complete)
import math
def sumOfDigits(x):
    res = list(map(int, str(x)))
    sum = 0
    for i in range (0, len(res)):
        sum += res[i]
    return sum
print(sumOfDigits(math.factorial(99)))
