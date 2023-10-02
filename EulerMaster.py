## Euler Master Doc 
import math 
## utilities
def is_prime(n: int) -> bool:
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
def sumOfDigits(x):
    res = list(map(int, str(x)))
    sum = 0
    for i in range (0, len(res)):
        sum += res[i]
    return sum
def number_of_divisors(n):
    if n < 2:
        return 0
    divisors = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors += 2
    if n ** 0.5 == int(n ** 0.5):
        divisors -= 1
    return divisors + 2
## Euler 1 -- Complete
def SumOf3sAnd5s(max: int) -> int:
    total = 0 
    for i in range(1,max+1):
        if i%3==0:
            total+=i
        elif i%5==0:
            total+=i
    return total
## Euler 2 -- Complete
def EvenFibbo(max:int) -> int: 
    arr = [1,1]
    sum = 0 
    i = 0
    while True:
        arr.append(arr[i]+arr[i+1])
        if arr[i]%2==0:
            sum+=arr[i]
        if arr[i+1] >= max:
            break
        i+=1
    print(arr)
    return sum
## Euler 3&4 are lost and that's why this master sheet exists
#
## Euler 5 -- Complete
def SmallestIntDivisableInRange(max: int) -> int:
    ans = 20
    while True:
        for i in range (1,max):
            if (ans%i) != 0:
                break
            if i == max-1:
                return (ans)
        ans+=max
## Euler 6 -- Complete
def SumOfSquaresDiff(x: int) -> int:
    SumOfSq= 0 
    SqOfSums= 0 
    for i in range (1, x+1):
        SumOfSq+=(i**2)
        SqOfSums+=i
    SqOfSums = SqOfSums**2   
    return(SqOfSums-SumOfSq)
## Euler 7 -- Complete
def PrimeFinder(x: int) -> int: 
    i = 0
    allPrimes = []
    while True:
        if is_prime(i):
            allPrimes.append(i)
            if len(allPrimes) == x+1:
                return allPrimes[len(allPrimes)-1]
        i+=1
## Euler 8 -- Complete
def Product3Gen(x: int) -> int: 
    res = list(map(int, str(x)))
    sums = []
    for i in range (0, len(res)-12):
        z = res[i]*res[i+1]*res[i+2]*res[i+3]*res[i+4]*res[i+5]*res[i+6]*res[i+7]*res[i+8]*res[i+9]*res[i+10]*res[i+11]*res[i+12]
        sums.append(z)
    return max(sums)
## Euler 10 - Complete 
def SumOfPrimes(x: int) -> int:
    total = 0 
    for i in range (0, x):
        if is_prime(i):
            total+=i
    return total
## Euler 11 - Incomplete
def Product4LR(x: int):
    res = list(map(int, str(x)))
    sums = []
    for i in range (0, len(res)-12):
        z = res[i]*res[i+1]*res[i+2]*res[i+3]
        sums.append(z)
    return "The sum was" + max(sums)
## Euler 12 - Complete
def genTriNums(x):
    factors = 1
    sum = 0 
    i = 1
    while True:
        sum += i
        print (sum)
        if number_of_divisors(sum) > x:
            return sum 
        i += 1 
## Euler 13 
#
## Euler 14 - Complete 
def Longest_Chain(q):

    arr = []
    length = 0 
    n = 1
    x = 1 
    n = x
    while x<q:
        while True:
            if n%2 == 0:
                n = n/2
                length+=1
            else:
                n = (3*n)+1
                length+=1
            if n == 1:
                arr.append(length)
                length = 0 
                n = 0
                break
        x+=1
        n = x
    return str((arr.index(max(arr)))) + " and the length is " + str(max(arr))
# 
