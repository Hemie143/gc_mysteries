
def isprime(x):
    '''
    if x < 2:
        return False
    else:
        for n in range(2,x):
            if x % n == 0:
               return False
        return True
    '''
    if x < 2:
        return False
    else:
        return all(x % i for i in range(2, x))