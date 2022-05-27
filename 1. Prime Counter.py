def countPrimeNumbers(a, b):
    primeCount = 0
    count = 0
    for x in range(a, b):
        for i in range(1, x + 1):
            if x % i == 0:
                count += 1   
        if count == 2:
            primeCount += 1
        count = 0
    return primeCount

print(countPrimeNumbers(-10, 6))