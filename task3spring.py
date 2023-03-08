import my_module
import random

def how_many_primes(NUMBER = 500):
    a = []
    count = 0
    for i in range(NUMBER):
        a.append(random.randint(0, 10**5))
    for i in range(NUMBER):
        if my_module.is_prime(a[i]):
            count += 1
    return count

print(how_many_primes())
