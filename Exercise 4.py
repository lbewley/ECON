# Write a program that prints one realization of the following random device:
# Flip an unbiased coin 10 times
# If 3 consecutive heads occur one or more times within this sequence, pay one dollar
# If not, pay nothing
# Use no import besides from numpy.random import uniform

from numpy.random import uniform

payoff = 0
count = 0

for i in range(10):
    U = uniform()
    count = count + 1 if U < 0.5 else 0
    if count == 3:
        payoff = 1

print(payoff)