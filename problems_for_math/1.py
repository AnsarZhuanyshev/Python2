import math
from ssl import SSL_ERROR_WANT_X509_LOOKUP

def isprime(n):
    i,j = 2,0
    if n == 1:
        return False
    else:
        while i*i<=n and j==0:
            if n%i!=0:
                i+=1
            else:
                j+=1
        return True if j==0 else False

primes = []

for i in range(1,151):
    if isprime(i) == True and i%4 == 1:
        primes.append(i)

def sumofsquares(k):
    arr = []
    m = 1
    while m*m<k:
        if math.sqrt(k-m*m) == math.floor(math.sqrt(k-m*m)):
            b = math.sqrt(k-m*m)
            if m<b:
                arr.append(m)
        m+=1
    return sum(arr)

summa = 0
for i in primes:
    print(i,sumofsquares(i))
    summa+=sumofsquares(i)

print(summa)
