def is_prime(a):
    if (a == 0) or (a == 1):
        return False
    else:
        for i in range(2, a):
            if a % i == 0:
                return False
    return True
