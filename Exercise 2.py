from numpy.random import uniform

def binomial_rv(n, p):
    count = 0
    for i in range(n):
        U = uniform()
        if U < p:
            count = count + 1   # Can use count +=1
    return count

print(binomial_rv(10, 0.5))
